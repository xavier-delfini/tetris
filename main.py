#Partie jeu:
#TODO:(Prioritaire 1)Représenter les pièces dans l'array
#TODO:(Prioritaire 2)Fonction vérification de ligne pour savoir si la ligne est complete ou non(Nécessaire d'imprimer les pieces dans l'array)
#TODO:(Non prioritaire)R pour tourner la piece a 90° degrées vers la droite avec la touche flèche haut(Fonction rotation déjà en partie crée mais non implémenter)
#TODO:(Optionnel)Space pour le hard drop (Faire descendre la piece instantanément
#TODO:(Non prioritaire) Donne une couleur a chaque type de pièce
#TODO:(Optionnel)Mettre les paramètres dans un fichier séparer (Temps initial descente piece,intervalle d'augmentation de ce temps,couleurs des pièces,pieces en elle même)
#Partie menu
#TODO:(Non prioritaire)Système de score et leaderboard(Noté 10 meilleurs scores dans un fichier (pas besoin de plus vu que l'on fait un classement type arcade)
#TODO:(Bonus)Menu de sélection de mode de jeu
#TODO:(Bonus)Mode survie
#TODO:(Bonus)Mode course


import pygame
import time

n = 0
grid_array = []
while n < 22:
    grid_array.append([1, 2, 3, 4, 5, 6, 7, 0, 0, 0])
    n += 1

def draw_array():
    m=0
    for l in grid_array:
        n=0
        for b in l:
            match b:
                case 0:
                   color=(0,0,0)
                case 1:#Line
                    color=(0, 240, 240)
                case 2:#Reverse L
                    color=(0, 0, 240)
                case 3:#L
                    color=(240, 160, 0)
                case 4:#Bloc
                    color=(240, 240, 0)
                case 5:#Z_BLOCK
                    color=(0, 240, 0)
                case 6:#T_Block
                    color=(160, 0, 240)
                case 7:#S_Block
                    color=(240, 0, 0)
                case _:
                    exit()
            draw_bloc(color,[m,n])
            n+=1
        m+=1

def draw_bloc(color,position):
    width, height = calc_position_grid(position)
    pygame.draw.rect(window, color, ((height, width), (22, 22)), 0)
def draw_pieces(piece, position):
    if position is None:
        position = [-1, -1]

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
draw_array()
pygame.display.update()

i = 3
f = 4
pos = [i, f]

start_time = time.time()

USI = pygame.key.get_pressed()
while pygame.event.wait().type != pygame.QUIT:
    current_time = time.time()
    draw_array()
    if current_time - start_time > 0.08: # deplace la pièce selon le temps donner
        if pos[1] < 20:
            window.fill((0, 0, 0))
            grille()
            pos[1] += 1 # déplacer la pièce vers le bas
            start_time = current_time
    draw_pieces(Z_Block, pos)
    USI = pygame.key.get_pressed()
    #if USI[pygame.K_UP]
    if USI[pygame.K_LEFT]:
        if pos[0] > 0:
            window.fill((0, 0, 0))
            pos[0] -= 1
            print("gauche")
    if USI[pygame.K_RIGHT]:
        if pos[0] < 7:
            window.fill((0, 0, 0))
            pos[0] += 1
            print("droite")
    grille()
# K_LEFT K_RIGHT K_UP K_DOWN


