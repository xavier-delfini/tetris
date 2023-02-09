# Partie jeu:
# TODO:(Prioritaire 1)Représenter les pièces dans l'array
# TODO:(Prioritaire 2)Fonction vérification de ligne pour savoir si la ligne est complete ou non(Nécessaire d'imprimer les pieces dans l'array)
# TODO:(Non prioritaire)R pour tourner la piece a 90° degrées vers la droite avec la touche flèche haut(Fonction rotation déjà en partie crée mais non implémenter)
# TODO:(Optionnel)Space pour le hard drop (Faire descendre la piece instantanément
# TODO:(Non prioritaire) Donne une couleur a chaque type de pièce
# TODO:(Optionnel)Mettre les paramètres dans un fichier séparer (Temps initial descente piece,intervalle d'augmentation de ce temps,couleurs des pièces,pieces en elle même)
# Partie menu
# TODO:(Non prioritaire)Affichage des prochaines pieces
# TODO:(Non prioritaire)Système de score et leaderboard(Noté 10 meilleurs scores dans un fichier (pas besoin de plus vu que l'on fait un classement type arcade)
# TODO:(Bonus)Menu de sélection de mode de jeu
# TODO:(Bonus)Mode survie
# TODO:(Bonus)Mode course
import pygame
import time
import random

clock = pygame.time.Clock()
n = 0
grid_array = []
while n < 22:
    grid_array.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    n += 1


def hitbox_affinate(piece):
    m = 0
    match len(piece):
        case 3:
            while m < len(piece):

                if piece[m][0] + piece[m][1] + piece[m][2] == 0:
                    piece.pop(m)
                    m = 0
                m += 1

        case 4:
            while m < len(piece):

                if piece[m][0] + piece[m][1] + piece[m][2] + piece[m][3] == 0:
                    piece.pop(m)
                    m = 0
                m += 1
    return piece


def color_selector(piece):
    match piece:
        case 0:  # Blank
            color = (0, 0, 0)
        case 1:  # Line
            color = (0, 240, 240)
        case 2:  # Reverse L
            color = (0, 0, 240)
        case 3:  # L
            color = (240, 160, 0)
        case 4:  # Square
            color = (240, 240, 0)
        case 5:  # Z_BLOCK
            color = (0, 240, 0)
        case 6:  # T_Block
            color = (160, 0, 240)
        case 7:  # S_Block
            color = (240, 0, 0)
        case _:
            exit()
    return color


def draw_array():
    m = 0
    for l in grid_array:
        n = 0
        for b in l:
            color = color_selector(b)
            draw_bloc(color, [m, n])
            n += 1
        m += 1


def draw_bloc(color, position):
    width, height = calc_position_grid(position)
    if color != (0, 0, 0):
        pygame.draw.rect(window, color, ((height, width), (22, 22)), 0)


def draw_pieces(piece, position):
    piece = hitbox_affinate(piece)
    if position is None:
        position = [-1, -1]

    j = position[1]
    for x in piece:
        i = position[0]
        for y in x:
            width, height = calc_position_grid([i, j])
            if y > 0:
                color = color_selector(y)
                pygame.draw.rect(window, color, ((width, height), (22, 22)), 0)
                pygame.display.flip()
            i += 1
        j += 1
    return piece


def calc_position_grid(position):
    calc_width = 12 + (25 * position[0])
    calc_height = 12 + (25 * position[1])
    return calc_width, calc_height


def update_array(piece, pos, grid):
    i = 0
    for x in piece:
        j = 0
        for y in x:
            if y > 0:
                grid[pos[1]+i][pos[0]+j] = piece[i][j]
            j += 1
        i += 1
    return grid


# Définition des pieces(Les array sont carré afin de facilité leur rotation)
Line = [[0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
        ]

Reverse_L = [[2, 0, 0],
             [2, 2, 2],
             [0, 0, 0]]

L = [[0, 0, 3],
     [3, 3, 3],
     [0, 0, 0]]

Square = [[4, 4],
          [4, 4]]

Z_Block = [[5, 5, 0],
           [0, 5, 5],
           [0, 0, 0]]

T_Block = [[0, 6, 0],
           [6, 6, 6],
           [0, 0, 0]]

S_Block = [[0, 7, 7],
           [7, 7, 0],
           [0, 0, 0]]
piece_list = (Line, Reverse_L, L, Square, Z_Block, T_Block, S_Block)
pygame.init()

window = pygame.display.set_mode((270, 570))


def grille():
    for i in range(10, 561, 25):
        pygame.draw.line(window, (255, 255, 255), (10, i), (260, i))
        pygame.draw.line(window, (255, 255, 255), (i, 10), (i, 560))


def verif_collision(piece, position, grid,direction):
    i = len(piece)-1
    for x in piece:
        match direction:
            case "Down":
                j=0
                for y in x:

                    print(position[1] + len(piece))
                    if position[1] + 1 == 23 - len(piece) or (
                            grid[position[1]-i + len(piece)][(position[0] + j)] > 0 and y > 0):
                        return 1
                    j += 1

                i -= 1
            case "Left":
                if grid[position[1] - i + len(piece)][(position[0] + j)] > 0 and y > 0:
                    pass
def rotation(array_piece):
    array_piece[0]=piece
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
        # Line
        case 4:
            i=0
            while i<piece[0]:
                new_piece = [[0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]]
                # TODO:A optimiser aussi
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
                new_piece=piece[0]
                i+=1
    if piece[1]<4:
        piece[1]+=1
    else:
        piece[1]=1

    return new_piece


grille()
draw_array()
pygame.display.update()
piece = random.choice(piece_list)
piece_initial=[0,0]
piece_initial[0]= piece
piece_initial[1]= 1
i = 3
f = 0
pos = [i, f]
fpsClock = pygame.time.Clock()
FPS = 15
start_time = time.time()
while True:
    current_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if current_time - start_time > 0.01:  # déplace la pièce selon le temps donner
        if verif_collision(piece, pos, grid_array,"Down") == 1:
            grid_array=update_array(piece, pos, grid_array)
            piece = random.choice(piece_list)
            piece_initial=[0,0]
            piece_initial[0]= piece
            piece_initial[1]= 1

            pos = [3, 0]
        else:
            pos[1] += 1  # déplacer la pièce vers le bas
        start_time = current_time
        fpsClock.tick(FPS)
    USI = pygame.key.get_pressed()
    if USI[pygame.K_UP]:
        rotation(piece_initial)
    if USI[pygame.K_LEFT] and pos[0] > 0:
        pos[0] -= 1
        print("gauche")
        fpsClock.tick(FPS)
    if USI[pygame.K_RIGHT] and pos[0] < 10 - len(piece[-1]):
        pos[0] += 1
        print("droite")
        fpsClock.tick(FPS)
    window.fill((0, 0, 0))
    grille()
    draw_array()
    piece = draw_pieces(piece, pos)
    fpsClock.tick(FPS)
