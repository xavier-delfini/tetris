# Partie jeu:
# TODO:(Prioritaire 2)Fonction vérification de ligne pour savoir si la ligne est complete ou non(Nécessaire d'imprimer les pieces dans l'array)
# TODO:(Optionnel)Space pour le hard drop (Faire descendre la piece instantanément
# TODO:(Prioritaire 1)Faire les collision pour le déplacement a gauche ou a droite
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
import copy
from parameters import *
clock = pygame.time.Clock()
n = 0
grid_array = []
while n < 22:
    grid_array.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    n += 1


def hitbox_affinate(hitbox):
    m = 0
    match len(hitbox[m]):
        case 3:
            while m < len(hitbox):
                try:
                    if hitbox[m][0] + hitbox[m][1] + hitbox[m][2] == 0:
                        hitbox.pop(m)
                        m = 0

                    elif hitbox[0][m] + hitbox[1][m] + hitbox[2][m] == 0:
                        del hitbox[0][m], hitbox[1][m], hitbox[2][m]
                        m = 0
                except IndexError:
                    pass
                m += 1

        case 4:
            while m < len(hitbox):
                try:
                    if hitbox[0][m]+ hitbox[1][m] + hitbox[2][m] + hitbox[3][m] == 0:
                        del hitbox[0][m], hitbox[1][m], hitbox[2][m], hitbox[3][m]
                        m = 0
                except IndexError:
                    pass
                try:
                    if hitbox[m][0] + hitbox[m][1] + hitbox[m][2] + hitbox[m][3] == 0:
                        hitbox.pop(m)
                        m = 0
                except IndexError:
                    pass



                m += 1
    return hitbox


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


def draw_pieces(d_piece, position):
    hitbox_affinate(d_piece)
    if position is None:
        position = [-1, -1]

    j = position[1]
    for x in d_piece:
        i = position[0]
        for y in x:
            width, height = calc_position_grid([i, j])
            if y > 0:
                color = color_selector(y)
                pygame.draw.rect(window, color, ((width, height), (22, 22)), 0)
                pygame.display.flip()
            i += 1
        j += 1


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


def grille():
    for i in range(10, 561, 25):
        pygame.draw.line(window, (255, 255, 255), (10, i), (260, i))
        pygame.draw.line(window, (255, 255, 255), (i, 10), (i, 560))


def verif_collision(piece, position, grid,direction):
    i = len(piece)-1
    for x in piece:
        j=0
        match direction:
            case "Down":

                for y in x:
                    if position[1] + 1 == 23 - len(piece) or (
                            grid[position[1]-i + len(piece)][(position[0] + j)] > 0 and y > 0):
                        return 1
                    j += 1

                i -= 1
            case "Left":
                for y in x:
                    if grid[position[1] - i  + len(piece)][(position[0] + j)] > 0 and y > 0:


                        pass


def rotation(array_piece):
    piece = array_piece[0]
    rotation_count = array_piece[1]
    i = 0
    match len(piece[0]):
        # L reverseL,S_Block,Z_block
        case 3:
            while i < rotation_count:
                new_piece = [[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]]
                new_piece[0]=[piece[2][0],piece[1][0],piece[0][0]]
                new_piece[1]=[piece[2][1],piece[1][1],piece[0][1]]
                new_piece[2]=[piece[2][2],piece[1][2],piece[0][2]]
                piece = new_piece
                i += 1
            if rotation_count < 4:
                rotation_count += 1
            else:
                rotation_count = 1
        # Line
        case 4:
            while i<rotation_count:
                new_piece = [[0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]]
                new_piece[0]=[0,piece[2][0],piece[1][0],0]
                new_piece[1]=[piece[3][1],piece[2][1],piece[1][1],piece[0][1]]
                new_piece[2]=[piece[0][2],piece[2][2],piece[1][2], piece[3][2]]
                new_piece[3]=[0,piece[2][3],piece[1][3],0]
                piece = new_piece
                i += 1
            if rotation_count < 2:
                rotation_count += 1
            else:
                rotation_count = 1

    return piece, rotation_count

def next_piece():
    random_piece = random.choice(piece_list)
    initial_piece = [random_piece, 1]
    piece = copy.copy(random_piece)
    return piece, initial_piece

pos = copy.copy(pos_initial)
pygame.init()
window = pygame.display.set_mode((270, 570))
grille()
draw_array()
piece, initial_piece=next_piece()
fpsClock = pygame.time.Clock()
start_time = time.time()
while True:
    current_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if current_time - start_time > array_actualisation:  # déplace la pièce selon le temps donner
        if verif_collision(piece, pos, grid_array,"Down") == 1:
            grid_array = update_array(piece, pos, grid_array)
            piece, initial_piece = next_piece()
            pos = copy.copy(pos_initial)
        else:
            pos[1] += 1  # déplacer la pièce vers le bas
        start_time = current_time
        fpsClock.tick(FPS)
    USI = pygame.key.get_pressed()
    if USI[pygame.K_r]:
        piece,initial_piece[1]=rotation(initial_piece)
        start_time = current_time
        fpsClock.tick(FPS)
    if USI[pygame.K_LEFT] and pos[0] > 0:
        pos[0] -= 1
        fpsClock.tick(FPS)
    if USI[pygame.K_RIGHT] and pos[0] < 10 - len(piece[-1]):
        pos[0] += 1
        fpsClock.tick(FPS)
    window.fill((0, 0, 0))
    grille()
    draw_array()
    draw_pieces(piece, pos)
    fpsClock.tick(FPS)