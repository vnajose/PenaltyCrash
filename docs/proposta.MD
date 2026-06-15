# Proposta Inicial do Jogo
 
Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.
 
A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.
 
## 1. Nome provisório do jogo
 
> PenaltyCrash
 
## 2. Integrantes do grupo
 
- Nome 1: Jose Venancio
- Nome 2: Henrique Ignacio
- Nome 3: João Pedro
- Nome 4: Ana Ayla
## 3. Tipo de jogo
 
Tipo escolhido pelo grupo:
 
> Jogo de pênaltis com mecânica de escolha de direção de chute.
 
## 4. Descrição geral do jogo
 
Descrição:
 
> Na tela aparece um campo de futebol com um gol ao fundo, um cobrador e um goleiro. O jogador controla o cobrador e deve escolher uma das 5 posições predefinidas para chutar a bola: canto superior esquerdo, canto superior direito, centro, canto inferior esquerdo ou canto inferior direito. O goleiro se move para defender com base em lógica aleatória. O desafio é tentar enganar o goleiro escolhendo a posição certa antes que ele cubra aquela área.
 
## 5. Objetivo do jogador
 
Objetivo:
 
> Converter o maior número possível de pênaltis em uma série de 5 cobranças, marcando mais gols do que o goleiro consegue defender.
 
## 6. Regras principais
 
Regras do grupo:
 
- Regra 1: O jogador tem 5 cobranças por partida.
- Regra 2: Em cada cobrança, o jogador escolhe uma das 5 posições de chute pressionando as teclas 1 a 5.
- Regra 3: O goleiro escolhe uma posição para defender de forma aleatória.
- Regra 4: Se o jogador chutar na mesma posição que o goleiro defender, o gol é defendido (+1 ponto ao goleiro).
- Regra 5: Se o jogador chutar em posição diferente da defendida pelo goleiro, é gol (+1 ponto ao jogador).
## 7. Condição de vitória
 
Condição de vitória:
 
> O jogador vence se converter 3 ou mais gols ao final das 5 cobranças, ou seja, se marcar mais do que o goleiro defende. Uma tela de vitória é exibida com o placar final.
 
## 8. Condição de derrota ou encerramento
 
Condição de derrota ou encerramento:
 
> O jogo encerra automaticamente após as 5 cobranças. O jogador perde se o goleiro defender 3 ou mais pênaltis, finalizando com uma tela de derrota e a opção de reiniciar.
 
## 9. Elementos previstos no jogo
 
## Jogador ou elemento principal
 
Descrição:
 
> Um cobrador de pênaltis representado por um sprite na tela, controlado pelo jogador via teclado para escolher a direção do chute.
 
## Obstáculos, inimigos ou desafios
 
Descrição:
 
> O goleiro adversário, que se move para uma das 5 posições do gol de forma aleatória a cada cobrança, funcionando como o principal desafio do jogo.
 
## Itens, alvos ou objetos de interação
 
Descrição:
 
> As 5 regiões do gol, visualmente demarcadas na tela, que representam os alvos de chute. A bola de futebol é animada em direção à posição escolhida pelo jogador após a confirmação do chute.
 
## Pontuação, vidas, tempo ou progresso
 
Descrição:
 
> O placar exibido na tela mostra o número de gols do jogador e o número de defesas do goleiro. Não há sistema de vidas; o progresso é medido pelo número de cobranças restantes (de 1 a 5).
 
## 10. Controles previstos
 
Controles do grupo:
 
- Tecla 1: Chutar no canto superior esquerdo
- Tecla 2: Chutar no canto superior direito
- Tecla 3: Chutar no centro
- Tecla 4: Chutar no canto inferior esquerdo
- Tecla 5: Chutar no canto inferior direito
- Enter / Espaço: Confirmar chute e avançar tela
- R: Reiniciar o jogo
- ESC: Sair do jogo
## 11. Organização inicial do código
 
Organização planejada:
 
> - `main.py`: inicia o jogo e chama o loop principal;
> - `src/jogo.py`: contém o loop principal e o controle dos estados do jogo;
> - `src/goleiro.py`: contém a lógica do goleiro (movimentação e defesa);
> - `src/bola.py`: contém a lógica e animação da bola;
> - `src/placar.py`: controla a pontuação e verifica condição de vitória/derrota;
> - `src/config.py`: guarda configurações globais como tamanho da tela, cores e posições;
> - `src/telas.py`: contém as funções para desenhar as telas de início, vitória e derrota.
 
## 12. Recursos externos previstos
 
Recursos previstos:
 
> - Imagens de sprite do jogador, goleiro e bola obtidas de banco de imagens gratuito (ex.: OpenGameArt.org);
> - Imagem de fundo do campo de futebol obtida de banco gratuito;
> - Tutoriais de Pygame utilizados apenas como referência para animações.
 
## 13. Principais dificuldades esperadas
 
Dificuldades previstas:
 
- Dificuldade 1: Implementar as animações da bola e do goleiro de forma fluida e sincronizada com a lógica do jogo.
- Dificuldade 2: Gerenciar os diferentes estados da partida (aguardando entrada, animando chute, exibindo resultado da cobrança, encerrando).
- Dificuldade 3: Desenhar e posicionar corretamente as 5 regiões do gol na tela de forma clara e proporcional.
## 14. Escopo mínimo para a entrega final
 
Escopo mínimo:
 
> A versão mínima do jogo terá uma tela inicial com o nome do jogo, um gol desenhado com as 5 posições de chute visíveis, seleção de posição via teclado (teclas 1 a 5), um goleiro com movimento de defesa visível, detecção correta de gol ou defesa, placar atualizado a cada cobrança, encerramento automático após 5 cobranças e tela de resultado com opção de reiniciar.
 
## 15. Possíveis melhorias, caso haja tempo
 
Melhorias possíveis:
 
- Melhoria 1: Adicionar efeitos sonoros (som de chute, gol e defesa).
- Melhoria 2: Implementar diferentes níveis de dificuldade, com o goleiro cobrindo posições com base no histórico do jogador.
- Melhoria 3: Adicionar animações mais elaboradas para o cobrador e o goleiro (corrida de aproximação, mergulho de defesa).
- Melhoria 4: Criar um sistema de ranking local salvando o recorde de gols em arquivo.
- Melhoria 5: Adicionar modo de disputa de pênaltis entre dois jogadores no mesmo teclado.
