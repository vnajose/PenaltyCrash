import random


def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def determinar_resultado(zona_chute, zona_defesa):
    """Retorna 'DEFESA' se o goleiro acertou a mesma zona; senão 'GOL'."""
    if zona_chute == zona_defesa:
        return "DEFESA"
    return "GOL"


def determinar_resultado_com_forca(zona_chute, zona_defesa, forca):
    """Determina o resultado levando em conta a força do chute (0.0 a 1.0).

    - Muito forte (> 0.90): 70 % de chance de ISOLADO (bola sai pela linha).
    - Fraco (< 0.25): mesmo que erre a zona, 70 % de chance de DEFESA extra.
    - Normal (0.25 – 0.90): comportamento padrão (goleiro cobre 1 zona).
    """
    if forca > 0.90 and random.random() < 0.70:
        return "ISOLADO"
    if zona_chute == zona_defesa:
        return "DEFESA"
    if forca < 0.25 and random.random() < 0.70:
        return "DEFESA"
    return "GOL"


def jogador_venceu(gols, meta):
    """Indica se o jogador atingiu a meta de gols para vencer."""
    return gols >= meta


def fim_da_partida(cobranca_atual, total_cobrancas):
    """Indica se todas as cobranças da partida já foram realizadas."""
    return cobranca_atual >= total_cobrancas
