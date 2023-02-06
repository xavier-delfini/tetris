import pygame
import time

n = 0
grid_array = []
while n < 22:
    grid_array.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    n += 1


def draw_pieces(piece, position):
    if position is None:
        position = [0, 0]

    j = position[1]
    for x in piece:
        i = position[0]
        for y in x:
            width, height = calc_position_grid([i, j])
            if y == 1:
                pygame.draw.rect(window, (0, 255, 255), ((width, height), (22, 22)), 0)
                pygame.display.flip()
            else:
                pygame.draw.rect(window, (0, 0, 0), ((width, height), (22, 22)), 0)
                pygame.display.flip()
            i += 1
        j += 1


def calc_position_grid(position):
    calc_width = 12 + (25 * position[0])
    calc_height = 12 + (25 * position[1])
    return calc_width, calc_height


# Définition des pieces
Line = [[0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
        ]

Reverse_L = [[1, 0, 0],
             [1, 1, 1],
             [0, 0, 0]]

L = [[0, 0, 1],
     [1, 1, 1],
     [0, 0, 0]]

Square = [[1, 1],
          [1, 1]]

S_Block = [[0, 1, 1],
           [1, 1, 0],
           [0, 0, 0]]

T_Block = [[0, 1, 0],
           [1, 1, 1],
           [0, 0, 0]]

Z_Block = [[1, 1, 0],
           [0, 1, 1],
           [0, 0, 0]]

pygame.init()

window = pygame.display.set_mode((270, 570))

def grille():

    for i in range(10, 561, 25):
       pygame.draw.line(window, (255, 255, 255), (10, i), (260, i))
       pygame.draw.line(window, (255, 255, 255), (i, 10), (i, 560))


grille()

pygame.display.update()

i = 3
f = 4
pos = [i, f]

start_time = time.time()

USI = pygame.key.get_pressed()
while pygame.event.wait().type != pygame.QUIT:
    current_time = time.time()
    if current_time - start_time > 0.08: # deplace la pièce selon le temps donner
        if pos[1] < 20:
            window.fill((0, 0, 0))
            grille()
            pos[1] += 1 # déplacer la pièce vers le bas
            start_time = current_time
    draw_pieces(Z_Block, pos)
    USI = pygame.key.get_pressed()
    if USI[pygame.K_LEFT]:
        if USI[pygame.K_LEFT] and pos[0] > 0:
            window.fill((0, 0, 0))
            grille()
            pos[0] -= 1
            print("gauche")
    if USI[pygame.K_RIGHT]:
        if USI[pygame.K_RIGHT] and pos[0] < 7:
            window.fill((0, 0, 0))
            grille()
            pos[0] += 1
            print("droite")
# K_LEFT K_RIGHT K_UP K_DOWN


