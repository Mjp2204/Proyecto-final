import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
screen_width = 800
screen_height = 600

# Crear la ventana del juego
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Movimiento de Imagen")

# Cargar la imagen
background = pygame.image.load('imagenes/carretera.jpeg')

# Posición inicial de la imagen
background_y = 0

# Velocidad de movimiento
speed = 10

# Reloj para controlar la velocidad de fotogramas
clock = pygame.time.Clock()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mover la imagen hacia abajo
    background_y += speed
    if background_y > screen_height:
        background_y = 0

    # Dibujar la imagen en la pantalla
    screen.fill((0, 0, 0))  # Limpiar la pantalla
    screen.blit(background, (0, background_y))
    
    
    screen.blit(background, (0, background_y - screen_height))

    # Actualizar la pantalla
    pygame.display.flip()

    # velocidad de fotogramas
    clock.tick(60)


pygame.quit()
sys.exit()