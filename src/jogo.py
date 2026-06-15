import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    TOTAL_COBRANCAS,
    META_VITORIA,
    ZONAS,
    NOMES_ZONAS,
    POS_BOLA_INICIAL,
    VELOCIDADE_BOLA,
    CAMINHO_RECORDE,
    CAMINHO_RANKING,
    CAMINHO_PLACAR,
    FORCA_POR_FRAME,
)

from src.funcoes import determinar_resultado, determinar_resultado_com_forca, jogador_venceu, fim_da_partida
from src.goleiro import escolher_defesa
from src.dados import (
    salvar_recorde, carregar_recorde,
    salvar_ranking, carregar_ranking,
    salvar_placar, carregar_placar,
)
from src.telas import (
    desenhar_campo,
    desenhar_gol_e_zonas,
    desenhar_goleiro,
    desenhar_bola,
    desenhar_hud,
    desenhar_medidor_forca,
    desenhar_tela_inicial,
    desenhar_tela_resultado,
    desenhar_tela_placar,
)

TECLAS_ZONA = {
    pygame.K_1: 1, pygame.K_KP1: 1,
    pygame.K_2: 2, pygame.K_KP2: 2,
    pygame.K_3: 3, pygame.K_KP3: 3,
    pygame.K_4: 4, pygame.K_KP4: 4,
    pygame.K_5: 5, pygame.K_KP5: 5,
}

POS_GOLEIRO_INICIAL = ZONAS[3]


def novo_estado():
    """Cria o dicionário com o estado inicial de uma nova partida."""
    return {
        "fase": "inicio",
        "cobranca": 0,
        "gols": 0,
        "defesas": 0,
        "zona_selecionada": 3,
        "zona_defesa": None,
        "resultado": "",
        "mensagem": "Escolha a zona (1-5) e confirme com ENTER",
        "pos_bola": list(POS_BOLA_INICIAL),
        "pos_goleiro": list(POS_GOLEIRO_INICIAL),
        "forca": 0.0,
        "carregando": False,
    }


def iniciar_cobranca(estado):
    """Confirma o chute: sorteia a defesa e inicia a animação da bola."""
    estado["zona_defesa"] = escolher_defesa(ZONAS)
    estado["pos_bola"] = list(POS_BOLA_INICIAL)
    estado["pos_goleiro"] = list(POS_GOLEIRO_INICIAL)
    estado["fase"] = "animando"
    estado["mensagem"] = ""


def mover_para(pos, alvo, velocidade):
    """Move 'pos' em direção a 'alvo'; retorna True quando chega ao destino."""
    dx = alvo[0] - pos[0]
    dy = alvo[1] - pos[1]
    distancia = (dx ** 2 + dy ** 2) ** 0.5
    if distancia <= velocidade:
        pos[0], pos[1] = alvo[0], alvo[1]
        return True
    pos[0] += velocidade * dx / distancia
    pos[1] += velocidade * dy / distancia
    return False


def atualizar_animacao(estado):
    """Atualiza a posição da bola e do goleiro durante o chute."""
    alvo_bola = ZONAS[estado["zona_selecionada"]]
    alvo_goleiro = ZONAS[estado["zona_defesa"]]

    mover_para(estado["pos_goleiro"], alvo_goleiro, VELOCIDADE_BOLA)
    chegou = mover_para(estado["pos_bola"], alvo_bola, VELOCIDADE_BOLA)

    if chegou:
        finalizar_cobranca(estado)


def finalizar_cobranca(estado):
    """Apura o resultado da cobrança e atualiza o placar."""
    resultado = determinar_resultado_com_forca(
        estado["zona_selecionada"], estado["zona_defesa"], estado["forca"]
    )
    estado["resultado"] = resultado

    if resultado == "GOL":
        estado["gols"] += 1
        estado["mensagem"] = "GOL! Pressione ENTER para continuar"
    elif resultado == "ISOLADO":
        estado["defesas"] += 1
        estado["mensagem"] = "ISOLADO! Chute forte demais! Pressione ENTER para continuar"
    else:
        estado["defesas"] += 1
        estado["mensagem"] = "DEFENDEU! Pressione ENTER para continuar"

    estado["cobranca"] += 1
    estado["fase"] = "resultado"


def avancar_apos_resultado(estado, recorde, ranking):
    """Vai para a próxima cobrança ou encerra a partida após a última."""
    if fim_da_partida(estado["cobranca"], TOTAL_COBRANCAS):
        estado["fase"] = "fim"
        salvar_placar(CAMINHO_PLACAR, estado["gols"])
        dados = carregar_placar(CAMINHO_PLACAR)
        ranking.clear()
        ranking.extend(dados["ranking"])
        return dados["recorde"]

    estado["fase"] = "aguardando"
    estado["zona_defesa"] = None
    estado["resultado"] = ""
    estado["pos_bola"] = list(POS_BOLA_INICIAL)
    estado["pos_goleiro"] = list(POS_GOLEIRO_INICIAL)
    estado["mensagem"] = f"Zona: {NOMES_ZONAS[estado['zona_selecionada']]}"
    estado["forca"] = 0.0
    estado["carregando"] = False
    return recorde


def tratar_eventos(estado, recorde, ranking):
    """Processa os eventos de teclado conforme a fase atual. Retorna (rodando, recorde)."""
    rodando = True
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            continue

        # Soltar ENTER/SPACE em modo aguardando dispara o chute com a força atual.
        if evento.type == pygame.KEYUP:
            if (estado["fase"] == "aguardando"
                    and estado["carregando"]
                    and evento.key in (pygame.K_RETURN, pygame.K_SPACE)):
                estado["carregando"] = False
                iniciar_cobranca(estado)
            continue

        if evento.type != pygame.KEYDOWN:
            continue

        # Tecla ESC: volta ao menu se estiver no placar, senão sai do jogo.
        if evento.key == pygame.K_ESCAPE:
            if estado["fase"] == "placar":
                estado["fase"] = "inicio"
            else:
                rodando = False
            continue
        if evento.key == pygame.K_r:
            estado.clear()
            estado.update(novo_estado())
            continue

        # Teclas específicas de cada fase.
        if estado["fase"] == "placar":
            if evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                estado["fase"] = "inicio"

        elif estado["fase"] == "inicio":
            if evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                estado["fase"] = "aguardando"
                estado["mensagem"] = "Escolha a zona (1-5) e confirme com ENTER"
            elif evento.key == pygame.K_p:
                estado["fase"] = "placar"

        elif estado["fase"] == "aguardando":
            if evento.key in TECLAS_ZONA:
                estado["zona_selecionada"] = TECLAS_ZONA[evento.key]
                estado["mensagem"] = f"Zona: {NOMES_ZONAS[estado['zona_selecionada']]}"
            elif evento.key in (pygame.K_RETURN, pygame.K_SPACE) and not estado["carregando"]:
                estado["carregando"] = True
                estado["forca"] = 0.0

        elif estado["fase"] == "resultado":
            if evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                recorde = avancar_apos_resultado(estado, recorde, ranking)

    return rodando, recorde


def desenhar(tela, fontes, estado, recorde, ranking):
    """Desenha a cena correspondente à fase atual do jogo."""
    fonte_titulo, fonte_texto, fonte_zona = fontes

    if estado["fase"] == "placar":
        desenhar_tela_placar(tela, fonte_titulo, fonte_texto, recorde, ranking)

    elif estado["fase"] == "inicio":
        desenhar_tela_inicial(tela, fonte_titulo, fonte_texto)

    elif estado["fase"] == "fim":
        venceu = jogador_venceu(estado["gols"], META_VITORIA)
        desenhar_tela_resultado(
            tela, fonte_titulo, fonte_texto, venceu, estado["gols"], estado["defesas"], ranking
        )

    else:
        desenhar_campo(tela)
        zona_destacada = estado["zona_selecionada"] if estado["fase"] == "aguardando" else None
        desenhar_gol_e_zonas(tela, fonte_zona, zona_destacada)
        desenhar_goleiro(tela, estado["pos_goleiro"])
        desenhar_bola(tela, estado["pos_bola"])
        desenhar_hud(
            tela, fonte_texto, estado["cobranca"], TOTAL_COBRANCAS,
            estado["gols"], estado["defesas"], estado["mensagem"],
        )

        if estado["fase"] == "aguardando":
            desenhar_medidor_forca(tela, fonte_texto, estado["forca"], estado["carregando"])

    pygame.display.flip()


def executar_jogo():
    """Inicializa o Pygame e executa o loop principal do PenaltyCrash."""
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()

    fontes = (
        pygame.font.SysFont("Arial", 64, bold=True),
        pygame.font.SysFont("Arial", 26),
        pygame.font.SysFont("Arial", 24, bold=True),
    )

    estado = novo_estado()
    dados = carregar_placar(CAMINHO_PLACAR)
    recorde = dados["recorde"]
    ranking = dados["ranking"]
    rodando = True

    while rodando:
        relogio.tick(FPS)

        rodando, recorde = tratar_eventos(estado, recorde, ranking)

        if estado["fase"] == "aguardando" and estado["carregando"]:
            estado["forca"] = min(estado["forca"] + FORCA_POR_FRAME, 1.0)

        if estado["fase"] == "animando":
            atualizar_animacao(estado)

        desenhar(tela, fontes, estado, recorde, ranking)

    pygame.quit()
