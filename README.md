# PenaltyCrash

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Jose Venancio
- Henrique Ignacio
- João Pedro
- Ana Ayla

## Descrição do jogo

PenaltyCrash é um jogo de cobrança de pênaltis em que o jogador digita seu nome, escolhe uma das 5 zonas do gol para chutar e controla a força do chute segurando ENTER. O goleiro se move aleatoriamente para tentar defender. O jogador tem 5 cobranças por partida e vence se marcar 3 ou mais gols.

## Como executar

**Windows — dois cliques:**
```
jogar.bat
```

**Terminal:**
```bash
pip install -r requirements.txt
python main.py
```

## Controles

| Tecla | Ação |
|---|---|
| 1 a 5 | Selecionar zona de chute |
| Segurar ENTER / ESPAÇO | Carregar a força do chute |
| Soltar ENTER / ESPAÇO | Disparar o chute |
| P | Ver placar (na tela inicial) |
| R | Reiniciar o jogo |
| ESC | Voltar ao menu / Sair |

## Posições de chute

| Tecla | Posição |
|---|---|
| 1 | Canto superior esquerdo |
| 2 | Canto superior direito |
| 3 | Centro |
| 4 | Canto inferior esquerdo |
| 5 | Canto inferior direito |

## Regras e lógica de força

- O jogador realiza **5 cobranças** por partida.
- Em cada cobrança, escolhe uma zona (1–5) e segura ENTER para carregar a força.
- O goleiro escolhe uma zona para defender de forma aleatória.

| Força | Efeito |
|---|---|
| Fraca (< 25%) | 70% de chance de DEFESA mesmo o goleiro indo para o lado errado |
| Normal (25–90%) | Resultado depende apenas da zona: GOL ou DEFESA |
| Muito forte (> 90%) | 70% de chance de ISOLADO — bola sai pela linha de fundo |

- **Vitória**: marcar 3 ou mais gols ao final das 5 cobranças.
- **Derrota**: marcar 2 ou menos gols.

## Fluxo de telas (máquina de estados)

```
inicio → nome → aguardando → animando → resultado → (próxima cobrança ou fim)
                    ↑                                         |
                    └─────────────────────────────────────────┘
```

| Estado | Descrição |
|---|---|
| `inicio` | Menu principal com instruções |
| `nome` | Input do nome do jogador (até 16 caracteres) |
| `aguardando` | Jogador escolhe zona e carrega a força |
| `animando` | Bola e goleiro se movem; medidor congelado mostrando força usada |
| `resultado` | Exibe GOL / DEFENDEU / ISOLADO; aguarda ENTER para continuar |
| `fim` | Tela final com vitória ou derrota e top 5 |
| `placar` | Placar geral acessível pela tecla P no menu |

## Sistema de placar

- O **recorde** de gols em uma única partida é salvo automaticamente.
- O **ranking** guarda as 5 melhores partidas com nome do jogador e quantidade de gols.
- Tudo é persistido em `data/placar.json`.
- O placar é acessível pela tecla **P** no menu inicial e é exibido na tela de resultado ao fim de cada partida.

Formato do arquivo:
```json
{
  "recorde": 4,
  "ranking": [
    { "nome": "Jose", "gols": 4 },
    { "nome": "Ana",  "gols": 3 }
  ]
}
```

## Estrutura do projeto

```
PenaltyCrash/
├── main.py               # Ponto de entrada da aplicação
├── requirements.txt      # Dependências (pygame, pytest)
├── jogar.bat             # Atalho para executar no Windows
├── src/
│   ├── config.py         # Constantes globais (tela, cores, zonas, caminhos)
│   ├── jogo.py           # Loop principal e máquina de estados
│   ├── telas.py          # Funções de renderização de cada tela
│   ├── funcoes.py        # Regras de resultado e lógica de força
│   ├── goleiro.py        # Defesa aleatória do goleiro
│   ├── dados.py          # Leitura e escrita de placar.json
│   └── sprites.py        # Utilitário de corte de spritesheet BMP
├── assets/
│   ├── imagens/          # Sprites e imagens (spritesheet.bmp)
│   ├── fontes/           # Fontes tipográficas
│   └── sons/             # Efeitos sonoros
├── data/
│   └── placar.json       # Recorde e top 5 com nomes (criado automaticamente)
├── tests/
│   └── test_logica.py    # Testes unitários com pytest
└── docs/
    └── proposta.md       # Proposta inicial do projeto
```

## Estruturas de dados principais

- **`estado` (dict)**: centraliza toda a informação da partida em andamento — fase, gols, defesas, força, posições da bola e do goleiro, nome do jogador, resultado pré-calculado e alvos de animação.
- **`ZONAS` (dict)**: mapeia cada número de zona (1–5) para suas coordenadas `(x, y)` na tela.
- **`ranking` (list of dict)**: lista de até 5 entradas `{"nome": str, "gols": int}`, ordenada do maior para o menor.

## Como executar os testes

```bash
python -m pytest
```

Os testes cobrem funções utilitárias de `funcoes.py` (pontos, vidas, limite de valor).

## Dependências

| Pacote | Uso |
|---|---|
| `pygame` | Janela, eventos, renderização e sons |
| `pytest` | Testes unitários |
