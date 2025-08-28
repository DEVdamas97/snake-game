# Jogo da Cobrinha (Snake Game) com Python e Pygame

Este é um projeto clássico do **Jogo da Cobrinha** desenvolvido do zero em Python, utilizando as bibliotecas [Pygame](https://www.pygame.org/) e [Random](https://docs.python.org/3/library/random.html).

---

## Sobre o Projeto

O objetivo foi criar um jogo interativo onde o jogador controla uma cobra que cresce ao comer frutas geradas aleatoriamente na tela, evitando colidir com as bordas. O projeto explora conceitos importantes de lógica de programação, manipulação de eventos, controle de tempo e integração de multimídia.

---

## Funcionalidades

- Cobra representada como uma lista de coordenadas (x, y) que simula o corpo e movimentação;
- Geração aleatória da comida dentro dos limites da tela;
- Controle da direção com teclado (setas), incluindo sistema de pausa (tecla `P`);
- Sistema de pontuação em tempo real, com bônus (combo) a cada 3 frutas consecutivas;
- Detecção de colisão com as bordas da tela (game over);
- Alternância de cores nos segmentos da cobra (verde e verde claro);
- Game loop fluido com atualização contínua e resposta imediata;
- Efeitos sonoros aleatórios ao comer frutas, para melhorar a experiência;
- Cronômetro integrado mostrando o tempo total da partida.

---

## Pré-requisitos

- Python 3.x instalado: https://www.python.org/downloads/
- Biblioteca Pygame instalada:

```bash
pip install pygame
