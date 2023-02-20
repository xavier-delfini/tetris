# Partie jeu:
# TODO:(Optionnel)Space pour le hard drop (Faire descendre la piece instantanément
# TODO:(Prioritaire 1)Faire les collision pour le déplacement en diagonales
# TODO:(Optionnel)Mettre les paramètres dans un fichier séparer (Temps initial descente piece,intervalle d'augmentation de ce temps,couleurs des pièces,pieces en elle même)
# Partie menu
# TODO:(Optionnel)Affichage des prochaines pieces
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
score=0
def check_for_lines(grid_array):
    def is_complete(line):
        return all(x > 0 for x in line)
    count=0
    i=0
    for line in grid_array:
        if is_complete(line):
            del grid_array[i]
            grid_array.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            count +=1
        i+=1
    match count:
        case 1:
            score = 1
        case 2:
            score = 3
        case 3:
            score = 5
        case 4:
            score = 8
        case _:
            score = 0
    return grid_array,score


def hitbox_affinate(hitbox):
    m = 0
    match len(hitbox):
        case 1: pass
        case 2:
            pass
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
            pass
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
    d_piece = hitbox_affinate(d_piece)
    j = position[1]
    i = position[0]
    for x in d_piece:
        if isinstance(x, int):#Si la piece ne fait qu'une seul ligne
            width, height = calc_position_grid([i, j])
            color = color_selector(x)
            pygame.draw.rect(window, color, ((width, height), (22, 22)), 0)
            pygame.display.flip()
            i += 1
        else:
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


def verif_collision(piece, position, grid, direction="Rotation"):
    i = len(piece) - 1
    for x in piece:
        j = 0
        match direction:
            case "Down":

                for y in x:
                    if position[1] + 1 == 23 - len(piece) or (
                            grid[position[1] - i + len(piece)][(position[0] + j)] > 0 and y > 0):
                        return 1
                    j += 1

                i -= 1
            case "Left":
                for y in x:
                    if grid[position[1] - i + len(piece)][(position[0] + j-1)] > 0 and y > 0:
                        return 1
                    j += 1
            case "Right":
                for y in x:
                    if grid[position[1] - i + len(piece)][(position[0] + j+1)] > 0 and y > 0:
                        return 1
                    j += 1
            case "diag_left":
                if position[1] + 1 == 23 - len(piece):
                    for y in x:
                        if grid[position[1]+1 - i + len(piece)][(position[0] + j - 1)] > 0 and y > 0:
                            return 1
                        j += 1
            case "diag_right":
                if position[1] + 1 == 23 - len(piece):
                    for y in x:
                        if grid[position[1]+1 - i + len(piece)][(position[0] + j + 1)] > 0 and y > 0:
                            return 1
                        j += 1
            case "Rotation":
                print("a")




def rotation(array_piece):
    piece = array_piece[0]
    rotation_count = array_piece[1]
    i = 0
    match len(piece):
        case 1: piece = [[1], [1], [1], [1]]
        # L reverseL,S_Block,Z_block
        case 3:
            while i < rotation_count:
                new_piece = [[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]]
                new_piece[0] = [piece[2][0], piece[1][0], piece[0][0]]
                new_piece[1] = [piece[2][1], piece[1][1], piece[0][1]]
                new_piece[2] = [piece[2][2], piece[1][2], piece[0][2]]
                piece = new_piece
                i += 1
            if rotation_count < 4:
                rotation_count += 1
            else:
                rotation_count = 1
        # Line
        case 4:
            piece=[
                [1, 1, 1, 1]
             ]

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
piece, initial_piece = next_piece()
fpsClock = pygame.time.Clock()
start_time = time.time()
while True:
    USI = pygame.key.get_pressed()
    current_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if current_time - start_time > array_actualisation:  # déplace la pièce selon le temps donner
        if verif_collision(piece, pos, grid_array, "Down"):
            #if verif_collision(piece,pos, grid_array,"diag_left"):
                #pos[0]+=1
            #elif verif_collision(piece,pos, grid_array,"diag_right"):
                #pos[0]-=1


            if pos[1]==0:#Condition fin de partie (les pieces posées ont atteint le haut de la grille
                font = pygame.font.SysFont("arial", 24)
                img = font.render('Game Over', True, (255, 255, 255))
                window.fill((0, 0, 0))
                window.blit(img, (63, 270))
                pygame.display.flip()
                time.sleep(10)
                pygame.quit()
            else:
                grid_array = update_array(piece, pos, grid_array)
                piece, initial_piece = next_piece()
                pos = copy.copy(pos_initial)
        else: #Aucune pièce n'est présente a la case en dessous
            pos[1] += 1  # déplace la pièce vers le bas
        start_time = current_time
        fpsClock.tick(FPS)

    if USI[pygame.K_UP]:
        piece, initial_piece[1] = rotation(initial_piece)
        if initial_piece[0] == [[1, 1, 1, 1]]:
            initial_piece[0] = [[1], [1], [1], [1]]
        elif initial_piece[0] == [[1], [1], [1], [1]]:
            initial_piece[0] = [[1, 1, 1, 1]]
        start_time = current_time
        pygame.display.flip()
        fpsClock.tick(FPS)
    if USI[pygame.K_LEFT] and pos[0] > 0:
        if verif_collision(piece, pos, grid_array, "Left") != 1:
            pos[0] -= 1
            fpsClock.tick(FPS)
    if USI[pygame.K_RIGHT] and pos[0] < 10 - len(piece[-1]):
        if verif_collision(piece, pos, grid_array, "Right") != 1:
            pos[0] += 1
            fpsClock.tick(FPS)
    grid_array, count = check_for_lines(grid_array)
    score = count + score
    print(score)
    window.fill((0, 0, 0))
    grille()
    draw_array()
    draw_pieces(piece, pos)
    fpsClock.tick(FPS)