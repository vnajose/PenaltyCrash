import json

TAMANHO_RANKING = 5


def salvar_placar(caminho, gols, nome="Jogador"):
    """Salva o resultado no JSON de placar, atualizando recorde e ranking."""
    placar = carregar_placar(caminho)
    if gols > placar["recorde"]:
        placar["recorde"] = gols
    placar["ranking"].append({"nome": nome, "gols": gols})
    placar["ranking"].sort(key=lambda e: e["gols"], reverse=True)
    placar["ranking"] = placar["ranking"][:TAMANHO_RANKING]
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(placar, arquivo, ensure_ascii=False, indent=2)


def carregar_placar(caminho):
    """Carrega o placar do JSON; migra formato antigo se necessário."""
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        ranking = dados.get("ranking", [])
        if ranking and not isinstance(ranking[0], dict):
            dados["ranking"] = [{"nome": "Jogador", "gols": g} for g in ranking]
        return dados
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