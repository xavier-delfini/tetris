# TODO:Aide a la disposition des pieces ("Surement"mettre dans un array)https://static.wikia.nocookie.net/tetrisconcept/images/3/3d/SRS-pieces.png/revision/latest?cb=20060626173148
# TODO:Taille d'une grille de tetris
#   Hauteur: 22
#   Largueur: 10
# TODO:Possibilité de tourner les pieces(indépendant du reset de la grille)
# TODO:Fonction actualisation de la grille + descente de la piece (Optionnel: Augmenter cette vitesse avec le temps pour augmenter la difficulté)
#   Faire aussi une fonction en cas de lignes (Les lignes au dessus de la ligne complété doivent être décaler de x lignes complété
# TODO:Spawn location : https://tetris.fandom.com/wiki/Spawn_Location (Indiquer au minimum la piece qui va suivre(peut aller jusqu'a 5 sur certaines versions de Tetris)
# TODO:Système de score
#   Single: 1 point
#   Double: 3 points
#   Triple: 5 points
#   Tetris: 8 points
# TODO:Bonus ajouter la musique de tetris (pygame mixer)

import pygame

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


def rotation(piece):
    match len(piece):
        # Square
        case 2:
            new_piece = piece
        # L reverseL,S_Block,Z_block
        case 3:
            new_piece = [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]
            # TODO:A optimiser
            new_piece[0][0] = piece[2][0]
            new_piece[0][1] = piece[1][0]
            new_piece[0][2] = piece[0][0]
            new_piece[1][0] = piece[2][1]
            new_piece[1][1] = piece[1][1]
            new_piece[1][2] = piece[0][1]
            new_piece[2][0] = piece[2][2]
            new_piece[2][1] = piece[1][2]
            new_piece[2][2] = piece[0][2]
            return new_piece
        # Line
        case 4:
            new_piece = [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]
            # TODO:A obtimiser aussi
            new_piece[0][1] = piece[2][0]
            new_piece[0][2] = piece[1][0]
            new_piece[1][0] = piece[3][1]
            new_piece[1][1] = piece[2][1]
            new_piece[1][2] = piece[1][1]
            new_piece[1][3] = piece[0][1]
            new_piece[2][0] = piece[0][2]
            new_piece[2][1] = piece[2][2]
            new_piece[2][2] = piece[1][2]
            new_piece[2][3] = piece[3][2]
            new_piece[3][1] = piece[2][3]
            new_piece[3][2] = piece[1][3]
            print(new_piece[0])
            print(new_piece[1])
            print(new_piece[2])
            print(new_piece[3])
            print("")
            return new_piece


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

# Impression de la grille a partir d'une boucle dessinant des lignes horizontales et verticales
for i in range(10, 561, 25):
    pygame.draw.line(window, (255, 255, 255), (10, i), (260, i))
    pygame.draw.line(window, (255, 255, 255), (i, 10), (i, 560))
pygame.display.update()
pos = [3, 4]

USI = pygame.key.get_pressed()
while pygame.event.wait().type != pygame.QUIT:
    draw_pieces(Z_Block, pos)
    USI = pygame.key.get_pressed()
    if USI[pygame.K_LEFT]:
        pos[0] -= 1
        print("gauche")
    pass

# K_LEFT K_RIGHT K_UP K_DOWN
