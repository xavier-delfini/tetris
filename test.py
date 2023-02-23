T_Block = [[0, 6, 0],
           [6, 6, 6],
           [0, 0, 0]]
Line = [[0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]]
"""

grid_array=[]
n=0
while n < 22:
    grid_array.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    n += 1

position=[4,0]
def verif_collision(piece,position,grid):
    i=0
    for c in piece[-1]:
        if (grid[position[1]+(1*i)][(position[0]+1)] > 0  and c >0) or position[1]==20:
            position=[4,0]
        i+=1
    return position

while True:
    position=verif_collision(T_Block,position,grid_array)
    position[1]+=1
""""""
test = [0, 1, 2, 3, 4, 5]



def new_piece(test):
    tost=test
    remove(test)
    print(tost)
    print(test)

def remove(test):
    test.remove(3)
    return test


new_piece(test)
"""

"""
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
            while i < rotation_count:
                new_piece = [[0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]]
                new_piece[0] = [0, piece[2][0], piece[1][0], 0]
                new_piece[1] = [piece[3][1], piece[2][1], piece[1][1], piece[0][1]]
                new_piece[2] = [piece[0][2], piece[2][2], piece[1][2], piece[3][2]]
                new_piece[3] = [0, piece[2][3], piece[1][3], 0]
                piece = new_piece
                i += 1
            if rotation_count < 2:
                rotation_count += 1
            else:
                rotation_count = 1

    return piece, rotation_count


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
            if hitbox == [1,1,1,1]:
                pass
            else:
                if (all(hitbox[0])) or (all(hitbox[1])):
                    hitbox = [1, 1, 1, 1]
                else:
                    hitbox=[[1], [1], [1], [1]]
    return hitbox


print(hitbox_affinate(rotation([Line, 2])[0]))
def draw_pieces(d_piece, position):
    d_piece=hitbox_affinate(d_piece)
    if position is None:
        position = [-1, -1]

    j = position[1]
    for x in d_piece:
        i = position[0]
        try:
            for y in x:
                #width, height = calc_position_grid([i, j])
                if y > 0:
                    print(y)
                    #color = color_selector(y)
                    #pygame.draw.rect(window, color, ((width, height), (22, 22)), 0)
                    #pygame.display.flip()
                i += 1
        except TypeError:
            #width, height =calc_position_grid([i,j])
            if x > 0:
                print(x)
                #color = color_selector(x)
                #pygame.draw.rect(window, color, ((width, height), (22, 22)), 0)
                #pygame.display.flip()
            i += 1
        j += 1
draw_pieces(hitbox_affinate(rotation([Line, 1])[0]),[2,0])"""
#Leaderboard (Pas encore implémenter)
"""
import json
import pygame

pygame.init()
window = pygame.display.set_mode((270, 570))
def fetch_scorelist():
    f = open("score.json", "r")
    json_array = f.read()
    f.close()
    #Si le fichier existe ou est remplie
    try:
        # Retourne un array
        return json.loads(json_array)
    #Si aucuns mots de passe n'est présent dans le fichier password.json
    except json.decoder.JSONDecodeError:
        #Création de l'array
        return []
def leaderboard_fetch():
    font = pygame.font.SysFont("arial", 16)
    score_list=fetch_scorelist()
    score_list.sort(key=lambda score_list:score_list[1], reverse=True)
    leaderboard = score_list[0:10]
    i = 0
    h_font=pygame.font.SysFont("arial", 24)
    leader_text = h_font.render("Leaderboard", True, (255, 255, 255))
    window.blit(leader_text, (55, 50))
    leaderboard_display = []
    for leaderboard_line in leaderboard:
        lead_name = leaderboard_line[0]
        lead_score = str(leaderboard_line[1])
        line = lead_name+"     "+lead_score
        leader_line_display = font.render(line, True, (255, 255, 255))
        window.blit(leader_line_display, (40, 100+40*i))
        leaderboard_display.extend(line)
        i += 1
    pygame.display.flip()
j = 0
leaderboard_fetch()
pygame.display.flip()
while True:
    j+=1"""
import pygame
def grille():#Permet l'affichage de la grille
    i=10
    while i <561:
        if i<261:
            j=i
        pygame.draw.line(window, (255, 255, 255), (10, i), (260, i))
        pygame.draw.line(window, (255, 255, 255), (j, 10), (j, 560))
        i+=25

pygame.init()
window = pygame.display.set_mode((500, 570))
grille()
while True:
    pygame.display.flip()
    for event in pygame.event.get():
        grille()
