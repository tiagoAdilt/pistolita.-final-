import pygame
import random

# Inicializar pygame
pygame.init()

#Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

#Dimensiones de la pantalla
ANCHURA = 800
ALTURA = 600

#Configuración de pantalla
pantalla = pygame.display.set_mode((ANCHURA, ALTURA))
pygame.display.set_caption('Pistola vs Naves - Pixeles')

#Reloj
reloj = pygame.time.Clock()

# Funciones del juego
def mostrar_puntaje(puntaje):
    fuente = pygame.font.SysFont(None, 35)
    texto = fuente.render("Puntaje: " + str(puntaje), True, BLANCO)
    pantalla.blit(texto, [10, 10])

def dibujar_pistola(x, y):
    pygame.draw.rect(pantalla, VERDE, [x, y, 40, 20])

def dibujar_bala(x, y):
    pygame.draw.rect(pantalla, ROJO, [x, y, 5, 10])

def dibujar_nave(x, y):
    pygame.draw.rect(pantalla, BLANCO, [x, y, 40, 20])

def bucle_juego():
    game_over = False

    # Posición inicial de la pistola
    x_pistola = ANCHURA / 2
    y_pistola = ALTURA - 50
    x_cambio = 0

    # Lista de naves
    naves = []
    for i in range(5):
        naves.append([random.randint(0, ANCHURA - 40), random.randint(-150, -50)])

    # Lista de balas
    balas = []

    # Puntaje inicial
    puntaje = 0

    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_cambio = -5
                if evento.key == pygame.K_RIGHT:
                    x_cambio = 5
                if evento.key == pygame.K_SPACE:
                    balas.append([x_pistola + 17, y_pistola - 10])
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    x_cambio = 0

        x_pistola += x_cambio
        if x_pistola < 0:
            x_pistola = 0
        elif x_pistola > ANCHURA - 40:
            x_pistola = ANCHURA - 40

        # Mover las balas
        for b in balas:
            b[1] -= 10
            if b[1] < 0:
                balas.remove(b)

        # Mover las naves
        for n in naves:
            n[1] += 5
            if n[1] > ALTURA:
                n[0] = random.randint(0, ANCHURA - 40)
                n[1] = random.randint(-150, -50)
            for b in balas:
                if n[0] < b[0] < n[0] + 40 and n[1] < b[1] < n[1] + 20:
                    balas.remove(b)
                    n[0] = random.randint(0, ANCHURA - 40)
                    n[1] = random.randint(-150, -50)
                    puntaje += 1

        # Dibujar todo
        pantalla.fill(NEGRO)
        dibujar_pistola(x_pistola, y_pistola)
        for n in naves:
            dibujar_nave(n[0], n[1])
        for b in balas:
            dibujar_bala(b[0], b[1])
        mostrar_puntaje(puntaje)

        pygame.display.update()
        reloj.tick(30)

    pygame.quit()
    quit()



bucle_juego()