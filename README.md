# PenaltyCrash

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Jose Venancio
- Henrique Ignacio
- João Pedro
- Ana Ayla

## Descrição do jogo

PenaltyCrash é um jogo de cobrança de pênaltis em que o jogador escolhe uma das 5 posições predefinidas do gol para chutar a bola. O goleiro adversário se move aleatoriamente para tentar defender. O jogador tem 5 cobranças por partida e vence se marcar 3 ou mais gols.

## Objetivo do jogador

Converter o maior número possível de pênaltis em uma série de 5 cobranças, marcando pelo menos 3 gols antes que o goleiro consiga 3 defesas.

## Regras do jogo

- O jogador realiza 5 cobranças por partida.
- Em cada cobrança, escolhe uma das 5 posições (teclas 1 a 5).
- O goleiro escolhe uma posição para defender de forma aleatória.
- Se o jogador chutar na mesma posição que o goleiro defender: **DEFESA**.
- Se o jogador chutar em posição diferente da defendida: **GOL**.
- **Vitória**: marcar 3 ou mais gols ao final das 5 cobranças.
- **Derrota**: marcar 2 ou menos gols.

## Posições de chute

| Tecla | Posição                  |
|-------|--------------------------|
| 1     | Canto superior esquerdo  |
| 2     | Canto superior direito   |
| 3     | Centro                   |
| 4     | Canto inferior esquerdo  |
| 5     | Canto inferior direito   |

## Controles

| Tecla           | Ação                      |
|-----------------|---------------------------|
| 1 a 5           | Selecionar zona de chute  |
| Enter / Espaço  | Confirmar chute / Avançar |
| R               | Reiniciar o jogo          |
| ESC             | Sair do jogo              |

## Sistema de pontuação e ranking

- Cada gol marcado conta como 1 ponto na partida.
- O **recorde** de gols em uma única partida é salvo em `data/recorde.txt`.
- O **ranking** guarda os 5 melhores resultados de todas as partidas em `data/ranking.txt`.
- O ranking é exibido na tela de resultado ao final de cada partida.

## Estrutura do projeto

```
PenaltyCrash/
├── main.py              # Ponto de entrada da aplicação
├── requirements.txt     # Dependências (pygame, pytest)
├── jogar.bat            # Atalho para executar no Windows
├── src/
│   ├── config.py        # Configurações globais (tela, cores, constantes)
│   ├── jogo.py          # Loop principal e máquina de estados
│   ├── telas.py         # Funções de renderização de cada tela
│   ├── funcoes.py       # Regras e lógica do jogo
│   ├── goleiro.py       # Inteligência do goleiro (defesa aleatória)
│   └── dados.py         # Leitura e escrita de recorde e ranking em arquivo
├── assets/
│   ├── imagens/         # Sprites e imagens
│   ├── fontes/          # Fontes tipográficas
│   └── sons/            # Efeitos sonoros
├── data/
│   ├── recorde.txt      # Melhor pontuação registrada
│   └── ranking.txt      # Top 5 melhores partidas
├── tests/
│   └── test_logica.py   # Testes unitários com pytest (18 testes)
└── docs/
    └── proposta.md      # Proposta inicial do projeto
```

## Fases do jogo (máquina de estados)

```
inicio → aguardando → animando → resultado → (próxima cobrança ou fim)
```

- **inicio**: tela de boas-vindas com instruções
- **aguardando**: jogador seleciona a zona de chute (teclas 1–5)
- **animando**: bola e goleiro se movem em direção às zonas escolhidas
- **resultado**: exibe GOL ou DEFENDEU e aguarda ENTER para continuar
- **fim**: tela final com vitória/derrota, placar e ranking

## Estruturas de dados utilizadas

- **Dicionário `estado`**: armazena toda a informação da partida em andamento (fase, gols, defesas, posições, mensagens).
- **Dicionário `ZONAS`**: mapeia cada número de zona (1–5) para suas coordenadas na tela.
- **Lista `ranking`**: mantém os melhores resultados carregados do arquivo e exibidos ao fim da partida.

## Como executar o projeto

**Opção 1 — Pelo script (Windows):**
```
jogar.bat
```

**Opção 2 — Pelo terminal:**
```bash
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

Os testes cobrem:
- Regras de resultado (GOL / DEFESA) para todas as combinações de zonas
- Condições de vitória, derrota e fim de partida
- Lógica do goleiro (sempre escolhe uma zona válida)
- Persistência de recorde e ranking em arquivo
- Funções utilitárias (pontos, vidas, limites de valor)
