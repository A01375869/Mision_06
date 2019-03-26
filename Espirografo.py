# Autor: Mario Hernández Cárdenas
# Dibujar figuras con el estilo de un espirógrafo

import pygame
import math
from random import randint

# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)


# Estructura básica de un programa que usa pygame para dibujar
def dibujarCirculo(ventana, r, R, l):
    for angulo in range(0, (360 * (r // math.gcd(r, R)))):
        a = math.radians(angulo)
        k = r / R
        formulaX = R * (((1 - k) * math.cos(a)) + (l * k * math.cos(((1 - k) / k) * a)))
        formulaY = R * (((1 - k) * math.sin(a)) + (l * k * math.sin(((1 - k) / k) * a)))
        x = int(formulaX)
        y = int(formulaY)
        colorAleatorio = (randint(0, 255), randint(0, 255), randint(0, 255))
        pygame.draw.circle(ventana, ROJO, (x + ANCHO // 2, ALTO // 2 - y), 1)


def dibujar(r, R, l):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        dibujarCirculo(ventana, r, R, l)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    dibujar(1, 220, 1)


main()
