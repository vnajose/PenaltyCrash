import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    GOL_RECT,
    ZONAS,
    NOMES_ZONAS,
    RAIO_BOLA,
    BRANCO,
    PRETO,
    CINZA,
    VERDE_CAMPO,
    VERDE_ESCURO,
    AMARELO,
    VERMELHO,
    AZUL,
)


def _texto_centralizado(tela, fonte, texto, cor, centro_x, y):
    """Desenha um texto centralizado horizontalmente em (centro_x, y)."""
    render = fonte.render(texto, True, cor)
    retangulo = render.get_rect(center=(centro_x, y))
    tela.blit(render, retangulo)


def desenhar_campo(tela):
    """Desenha o gramado e a grande área ao fundo."""
    tela.fill(VERDE_CAMPO)
    pygame.draw.rect(tela, VERDE_ESCURO, (0, 0, LARGURA_TELA, 70))
    # Linha da grande área
    pygame.draw.rect(tela, BRANCO, (120, 300, 560, 200), 3)


def desenhar_gol_e_zonas(tela, fonte, zona_selecionada):
    """Desenha a trave do gol e as 5 zonas de chute, destacando a selecionada."""
    x, y, largura, altura = GOL_RECT

    # Trave do gol
    pygame.draw.rect(tela, BRANCO, (x, y, largura, altura), 6)

    # Zonas de chute (alvos numerados)
    for numero, (cx, cy) in ZONAS.items():
        selecionada = numero == zona_selecionada
        cor = AMARELO if selecionada else BRANCO
        raio = 30 if selecionada else 24
        pygame.draw.circle(tela, cor, (cx, cy), raio, 4)
        _texto_centralizado(tela, fonte, str(numero), cor, cx, cy)


def desenhar_goleiro(tela, pos):
    """Desenha o goleiro como um retângulo simples na posição informada."""
    largura, altura = 46, 70
    x = pos[0] - largura // 2
    y = pos[1] - altura // 2
    pygame.draw.rect(tela, AZUL, (x, y, largura, altura), border_radius=8)
    # Cabeça
    pygame.draw.circle(tela, (240, 200, 160), (pos[0], y - 8), 12)


def desenhar_bola(tela, pos):
    """Desenha a bola de futebol na posição informada."""
    pygame.draw.circle(tela, BRANCO, (int(pos[0]), int(pos[1])), RAIO_BOLA)
    pygame.draw.circle(tela, PRETO, (int(pos[0]), int(pos[1])), RAIO_BOLA, 2)


def desenhar_hud(tela, fonte, cobranca, total, gols, defesas, mensagem, offset_y=0):
    """Mostra o placar, a cobrança atual e a mensagem de status."""
    placar = f"Gols: {gols}    Defesas: {defesas}"
    tela.blit(fonte.render(placar, True, BRANCO), (20, 510 + offset_y))

    progresso = f"Cobranca: {min(cobranca + 1, total)} / {total}"
    render = fonte.render(progresso, True, BRANCO)
    tela.blit(render, (LARGURA_TELA - render.get_width() - 20, 510 + offset_y))

    if mensagem:
        _texto_centralizado(tela, fonte, mensagem, AMARELO, LARGURA_TELA // 2, 555 + offset_y)


def desenhar_medidor_forca(tela, fonte, forca, carregando, animando=False):
    """Desenha a barra de força do chute estilo FIFA."""
    barra_x = 200
    barra_y = 487
    barra_largura = 400
    barra_altura = 16

    # Fundo escuro da barra
    pygame.draw.rect(tela, PRETO, (barra_x - 2, barra_y - 2, barra_largura + 4, barra_altura + 4))
    pygame.draw.rect(tela, (50, 50, 50), (barra_x, barra_y, barra_largura, barra_altura))

    # Preenchimento colorido conforme o nível
    fill_width = int(barra_largura * forca)
    if fill_width > 0:
        if forca < 0.60:
            cor_barra = (50, 210, 50)    # verde — zona segura
        elif forca < 0.80:
            cor_barra = (240, 200, 40)   # amarelo — zona de atenção
        else:
            cor_barra = (220, 55, 40)    # vermelho — zona de perigo
        pygame.draw.rect(tela, cor_barra, (barra_x, barra_y, fill_width, barra_altura))

    # Linha de perigo a 90 % (isolamento)
    perigo_x = barra_x + int(barra_largura * 0.90)
    pygame.draw.line(tela, BRANCO, (perigo_x, barra_y - 3), (perigo_x, barra_y + barra_altura + 3), 2)

    # Rótulos laterais
    tela.blit(fonte.render("FRACO", True, CINZA), (barra_x - 68, barra_y - 2))
    tela.blit(fonte.render("FORTE", True, CINZA), (barra_x + barra_largura + 6, barra_y - 2))

    # Instrução abaixo da barra
    if animando:
        instrucao = ""
        cor_instrucao = BRANCO
    elif carregando:
        instrucao = "Solte para chutar!"
        cor_instrucao = AMARELO
    else:
        instrucao = "Segure ENTER para carregar a forca"
        cor_instrucao = BRANCO
    if instrucao:
        _texto_centralizado(tela, fonte, instrucao, cor_instrucao, LARGURA_TELA // 2, barra_y + barra_altura + 14)


def desenhar_tela_nome(tela, fonte_titulo, fonte_texto, nome_atual):
    """Tela de input do nome do jogador antes da partida."""
    tela.fill(VERDE_ESCURO)

    _texto_centralizado(tela, fonte_titulo, "Quem vai jogar?", AMARELO, LARGURA_TELA // 2, 140)
    pygame.draw.line(tela, AMARELO, (150, 200), (650, 200), 2)

    caixa = pygame.Rect(200, 250, 400, 56)
    pygame.draw.rect(tela, (25, 25, 25), caixa)
    pygame.draw.rect(tela, BRANCO, caixa, 2)

    cursor = "|" if (pygame.time.get_ticks() // 500) % 2 == 0 else " "
    _texto_centralizado(tela, fonte_titulo, nome_atual + cursor, BRANCO, LARGURA_TELA // 2, caixa.centery)

    _texto_centralizado(
        tela, fonte_texto,
        "Digite seu nome e pressione ENTER para jogar",
        CINZA, LARGURA_TELA // 2, 340,
    )
    _texto_centralizado(tela, fonte_texto, "ESC  —  Voltar ao menu", CINZA, LARGURA_TELA // 2, ALTURA_TELA - 55)


def desenhar_tela_inicial(tela, fonte_titulo, fonte_texto):
    """Tela de abertura com o nome do jogo e as instruções."""
    tela.fill(VERDE_CAMPO)
    _texto_centralizado(tela, fonte_titulo, "PenaltyCrash", BRANCO, LARGURA_TELA // 2, 140)

    instrucoes = [
        "Escolha onde chutar com as teclas 1 a 5:",
        "1 e 2 = cantos superiores | 3 = centro | 4 e 5 = cantos inferiores",
        "ENTER / ESPACO: confirmar o chute",
        "R: reiniciar    ESC: sair",
        "",
        "Pressione ENTER para comecar",
        "Pressione P para ver o placar",
    ]
    y = 250
    for linha in instrucoes:
        _texto_centralizado(tela, fonte_texto, linha, BRANCO, LARGURA_TELA // 2, y)
        y += 40


def desenhar_tela_placar(tela, fonte_titulo, fonte_texto, recorde, ranking):
    """Tela de placar com o recorde e o top 5 de melhores partidas."""
    tela.fill(VERDE_ESCURO)
    _texto_centralizado(tela, fonte_titulo, "PLACAR GERAL", AMARELO, LARGURA_TELA // 2, 80)

    recorde_texto = f"Recorde: {recorde} gol{'s' if recorde != 1 else ''}"
    _texto_centralizado(tela, fonte_texto, recorde_texto, BRANCO, LARGURA_TELA // 2, 175)

    pygame.draw.line(tela, BRANCO, (150, 205), (650, 205), 1)

    _texto_centralizado(tela, fonte_texto, "TOP 5 MELHORES PARTIDAS:", AMARELO, LARGURA_TELA // 2, 235)

    if ranking:
        for posicao, entrada in enumerate(ranking, start=1):
            nome = entrada["nome"] if isinstance(entrada, dict) else "Jogador"
            gols = entrada["gols"] if isinstance(entrada, dict) else entrada
            linha = f"{posicao}.  {nome}  —  {gols} gol{'s' if gols != 1 else ''}"
            _texto_centralizado(tela, fonte_texto, linha, BRANCO, LARGURA_TELA // 2, 235 + posicao * 45)
    else:
        _texto_centralizado(
            tela, fonte_texto, "Nenhuma partida registrada ainda.",
            CINZA, LARGURA_TELA // 2, 310,
        )

    _texto_centralizado(
        tela, fonte_texto, "ESC / ENTER: voltar ao menu",
        BRANCO, LARGURA_TELA // 2, 540,
    )


def desenhar_tela_resultado(tela, fonte_titulo, fonte_texto, venceu, gols, defesas, ranking=None):
    """Tela final de vitória ou derrota com o placar, ranking e opção de reinício."""
    tela.fill(VERDE_ESCURO)

    if venceu:
        titulo = "VITORIA!"
        cor = AMARELO
    else:
        titulo = "DERROTA"
        cor = VERMELHO

    _texto_centralizado(tela, fonte_titulo, titulo, cor, LARGURA_TELA // 2, 110)
    _texto_centralizado(
        tela, fonte_texto, f"Placar final  -  Gols: {gols}   Defesas: {defesas}",
        BRANCO, LARGURA_TELA // 2, 200,
    )

    if ranking:
        _texto_centralizado(tela, fonte_texto, "TOP 5 PARTIDAS:", AMARELO, LARGURA_TELA // 2, 255)
        for posicao, entrada in enumerate(ranking, start=1):
            nome = entrada["nome"] if isinstance(entrada, dict) else "Jogador"
            gols = entrada["gols"] if isinstance(entrada, dict) else entrada
            linha = f"{posicao}.  {nome}  —  {gols} gol{'s' if gols != 1 else ''}"
            _texto_centralizado(tela, fonte_texto, linha, BRANCO, LARGURA_TELA // 2, 255 + posicao * 35)

    _texto_centralizado(
        tela, fonte_texto, "R: jogar de novo      ESC: sair",
        BRANCO, LARGURA_TELA // 2, 490,
    )
