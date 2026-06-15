import json

TAMANHO_RANKING = 5


def salvar_placar(caminho, gols):
    """Salva o resultado no JSON de placar, atualizando recorde e ranking."""
    placar = carregar_placar(caminho)
    if gols > placar["recorde"]:
        placar["recorde"] = gols
    placar["ranking"].append(gols)
    placar["ranking"].sort(reverse=True)
    placar["ranking"] = placar["ranking"][:TAMANHO_RANKING]
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(placar, arquivo, ensure_ascii=False, indent=2)


def carregar_placar(caminho):
    """Carrega o placar do JSON; retorna estrutura vazia se não existir."""
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"recorde": 0, "ranking": []}


def salvar_ranking(caminho_arquivo, gols):
    """Adiciona a pontuação ao ranking e mantém os 5 melhores resultados."""
    ranking = carregar_ranking(caminho_arquivo)
    ranking.append(gols)
    ranking.sort(reverse=True)
    ranking = ranking[:TAMANHO_RANKING]
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        for pontuacao in ranking:
            arquivo.write(str(pontuacao) + "\n")


def carregar_ranking(caminho_arquivo):
    """Carrega a lista dos melhores resultados; retorna lista vazia se não existir."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.read().strip().splitlines()
            return [int(linha) for linha in linhas if linha.strip().isdigit()]
    except FileNotFoundError:
        return []


def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0