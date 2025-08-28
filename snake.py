import pygame
import random

# Inicializa o Pygame
pygame.mixer.init()
pygame.init()

# Definindo a nova dimensão da tela (1280x720)
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Definindo cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (35, 130, 10)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Tamanho do bloco da cobrinha
tamanho_bloco = 20
velocidade = 10

# Fonte para escrever os pontos e tempo
fonte = pygame.font.SysFont(None, 30)

# Efeitos sonoros nomeados
# OBS: Certifique-se de que a pasta "SFX/" está no mesmo diretório do arquivo .py
# Caso contrário, você precisará ajustar os caminhos dos arquivos de áudio abaixo.
sons = [
    pygame.mixer.Sound(r"SFX\bite-1.mp3"),
    pygame.mixer.Sound(r"SFX\bite-2.mp3"),
    pygame.mixer.Sound(r"SFX\bite-3.mp3"),
    pygame.mixer.Sound(r"SFX\bite-4.mp3"),
]

# Função para mostrar pontos
def mostrar_pontos(pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, [10, 10])

# Função para mostrar o tempo
def mostrar_timer(segundos):
    texto = fonte.render(f"Tempo: {segundos}s", True, BRANCO)
    largura_texto = texto.get_width()
    tela.blit(texto, [largura - largura_texto - 10, 10])

# Função para gerar uma posição aleatória
def posicao_aleatoria():
    x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
    return x, y

# Função para exibir Game Over
def game_over(pontos):
    fonte_game_over = pygame.font.SysFont(None, 50)
    tela.fill(PRETO)
    texto = fonte_game_over.render("Game Over!", True, VERMELHO)
    tela.blit(texto, [largura // 3, altura // 4])

    texto_pontos = fonte_game_over.render(f"Pontuação: {pontos}", True, BRANCO)
    tela.blit(texto_pontos, [largura // 3, altura // 2])

    pygame.display.update()
    pygame.time.delay(2000)  # Espera 2 segundos antes de fechar

# Função de pausa
def pausar():
    pausado = True
    fonte_pausa = pygame.font.SysFont(None, 50)
    texto_pausa = fonte_pausa.render("Pausado. Pressione uma tecla para continuar.", True, BRANCO)
    tela.blit(texto_pausa, [largura // 4, altura // 2])
    pygame.display.update()

    while pausado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False  # Sai do jogo
            if evento.type == pygame.KEYDOWN:
                if evento.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    pausado = False  # Retorna ao jogo
    return True

# Função principal do jogo
def jogo():
    x, y = largura // 2, altura // 2
    x_mudar = 0
    y_mudar = 0

    corpo_cobra = []
    comprimento = 1
    pontos = 0
    combo_count = 0  # Contador de combo
    velocidade_atual = velocidade

    comida_x, comida_y = posicao_aleatoria()

    clock = pygame.time.Clock()
    rodando = True

    start_ticks = pygame.time.get_ticks()

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x_mudar == 0:
                    x_mudar = -tamanho_bloco
                    y_mudar = 0
                elif evento.key == pygame.K_RIGHT and x_mudar == 0:
                    x_mudar = tamanho_bloco
                    y_mudar = 0
                elif evento.key == pygame.K_UP and y_mudar == 0:
                    y_mudar = -tamanho_bloco
                    x_mudar = 0
                elif evento.key == pygame.K_DOWN and y_mudar == 0:
                    y_mudar = tamanho_bloco
                    x_mudar = 0
                elif evento.key == pygame.K_p:
                    if not pausar():  # Se pressionar 'P', o jogo será encerrado
                        rodando = False
                        continue

        # Atualiza a posição da cobra
        x += x_mudar
        y += y_mudar

        # Teleporte se sair da tela
        if x < 0 or x >= largura or y < 0 or y >= altura:
            game_over(pontos)
            pygame.quit()
            return

        tela.fill(PRETO)
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeca = [x, y]
        corpo_cobra.append(cabeca)

        if len(corpo_cobra) > comprimento:
            del corpo_cobra[0]

        # Alterna as cores da cobra entre verde e azul
        for i, parte in enumerate(corpo_cobra):
            if i % 2 == 0:
                pygame.draw.rect(tela, VERDE, [parte[0], parte[1], tamanho_bloco, tamanho_bloco])
            else:
                pygame.draw.rect(tela, AZUL, [parte[0], parte[1], tamanho_bloco, tamanho_bloco])

        # Exibe os pontos e o tempo
        mostrar_pontos(pontos)
        segundos = (pygame.time.get_ticks() - start_ticks) // 1000
        mostrar_timer(segundos)

        pygame.display.update()

        # Comer comida
        if x == comida_x and y == comida_y:
            comida_x, comida_y = posicao_aleatoria()
            comprimento += 1
            pontos += 1
            combo_count += 1

            # Incrementa a velocidade 5% a cada fruta comida
            velocidade_atual = int(velocidade_atual * 1.05)

            # Adiciona som aleatório
            random.choice(sons).play()

            # Se o jogador comer 3 frutas em sequência, ganha um "combo" (pontos extras)
            if combo_count == 3:
                pontos += 5  # Adiciona pontos extras no combo
                combo_count = 0  # Reseta o contador de combo

        clock.tick(velocidade_atual)

    pygame.quit()

if __name__ == "__main__":
    jogo()


