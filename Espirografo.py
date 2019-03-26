# Autor: Mario Hernández Cárdenas
# Dibujar figuras con el estilo de un espirógrafo

import pygame
import math
from random import randint

# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# COLORES
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)


# Estructura básica de un programa que usa pygame para dibujar
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
        # colorAleatorio = (randint(0, 255), randint(0, 255), randint(0, 255))
        k = r / R
        for angulo in range(0, 361 * (r // math.gcd(r, R))):
            a = math.radians(angulo)
            x = int(R * ((1 - k) * math.cos(a) + l * k * math.cos(((1 - k) / k) * a)))
            y = int(R * ((1 - k) * math.sin(a) - l * k * math.sin(((1 - k) / k) * a)))
            pygame.draw.circle(ventana, ROJO, (x + ANCHO // 2, ALTO // 2 - y), 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    r = int(input("Teclea un número entero de r: "))
    R = int(input("Teclea un número entero de R: "))
    l = float(input("Teclea el valor de l: "))
    # (1800, 220, .8) Son las medidas que utilicé
    dibujar(r, R, l)


main()
