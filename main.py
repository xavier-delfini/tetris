import copy
import json
import pygame
import random
import time

from parameters import *
clock = pygame.time.Clock()
def tetris():
    def check_for_lines(grid_array):
        #Vérifie si une ligne n'est pas complete et si c'est le cas l'enlève et en rajoute une nouvelle a la position 0
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
                score = oneline_points
            case 2:
                score = twolines_points
            case 3:
                score = threelines_points
            case 4:
                score = tetris_points
            case _:
                score = 0
        return grid_array,score


    def hitbox_affinate(hitbox):
        #Enlève la lignes de 0 de certaines pièces
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
        #Affiche les pièces déjà posées
        m = 0
        for l in grid_array:
            n = 0
            for b in l:
                color = color_selector(b)
                draw_bloc(color, [m, n])
                n += 1
            m += 1


    def draw_bloc(color, position):
        #Affiche le bloc a la position demandé
        width, height = calc_position_grid(position)
        if color != (0, 0, 0):
            pygame.draw.rect(window, color, ((height, width), (22, 22)), 0)


    def draw_pieces(d_piece, position):
        #Affiche la pièce actuellement utilisé (n'est pas encore inclu dans l'array car non posé)
        d_piece = hitbox_affinate(d_piece)
        j = position[1]
        i = position[0]
        for x in d_piece:
            if isinstance(x, int):#Si la piece ne fait qu'une seule ligne
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
        #Caclul la position d'un carré sur la grille et retourne ces coordonnée par rapport a la position dans l'array
        calc_width = 12 + (25 * position[0])
        calc_height = 12 + (25 * position[1])
        return calc_width, calc_height


    def update_array(piece, pos, grid):
        #Permet de mettre la pièces posé dans l'array
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
        #Permet l'affichage de la grille
        i=10
        while i <561:
            if i<261:
                j=i
            pygame.draw.line(window, (255, 255, 255), (10, i), (260, i))
            pygame.draw.line(window, (255, 255, 255), (j, 10), (j, 560))
            i+=25


    def verif_collision(piece, position, grid, direction="Rotation"):
        #Vérification pour vérifier si la pièces peut aller dans la direction que l'utilisateur demande
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
        # Change le sens de la pièce en fonction de 2 paramètres piece qui est la pièce obtenue via la fonction next_piece (version non affinée de la hitbox)
        # et rotation_count qui est le nombre de fois que l'on souhaite faire tourner la pièce(si la pièce n'a jamais été tourné ce chiffre est a 1
        #et peut aller jusqu'a 4, si l'on réappelle cette fonction alors que ce nombre est de 4 alors celui ci repassera a 1
        #Exception: La barre(Line) n'a pas le même fonctionnement puisqu'elle n'a que 2 états (Horizontal,vertical), et n'a donc pas
        #besoin d'être tourné 4 fois
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
        #Récupération de la piéces suivante lorsque la précedente est posé
        random_piece = random.choice(piece_list)
        initial_piece = [random_piece, 1]
        piece = copy.copy(random_piece)
        return piece, initial_piece
    def store_score(score):
        #écriture par-dessus la liste de score existante pour rajouter notre nouveau score
        score_list = fetch_scorelist()
        score_list.extend([score])
        json_array = json.dumps(score_list)
        f = open("score.json", "w")
        f.write(json_array)
        f.close()

    def game_over(final_score):
        #Permet l'affichage de l'écran de game_over, l'entrée du nom du joueur, et appel la fonction store_score avec la touche entrée
        font = pygame.font.SysFont("arial", 24)
        str_score = copy.copy(str(final_score))
        player_name = ""
        while True:
            USI = pygame.key.get_pressed()
            over = font.render('Game Over', True, (255, 255, 255))
            displayed_score = font.render(str_score, True, (255, 255, 255))
            enter_name = font.render('Entrer votre nom', True, (255, 255, 255))
            display_name = font.render(player_name, True, (255, 255, 255))

            window.fill((0, 0, 0))

            window.blit(over, (120, 270))
            window.blit(displayed_score, (175, 295))
            window.blit(enter_name, (90, 320))
            window.blit(display_name, (90, 345))

            pygame.display.flip()
            fpsClock.tick(FPS)
            if USI[pygame.K_RETURN]:  # Touche entrée
                if len(player_name) < name_max_lenth:
                    player_name = player_name[:-1]  # Suppréssion du caractère \n qui apparait à cause de la touche entrée
                store_score([player_name, score])
                return
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # Si une touche est préssé
                    if event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]  # Suppréssion du dernier caractère si la touche retour arrière est préssée
                    elif len(player_name) < name_max_lenth:  # On souhaite un nom ne faisant pas plus de caractèresque le paramètre name_max_lenth(Situé dans le fichier parameters)
                        player_name += event.unicode

    pos = copy.copy(pos_initial)
    pygame.init()
    window = pygame.display.set_mode((370, 570))
    grille()
    n = 0
    grid_array = []
    while n < 22:
        grid_array.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        n += 1
    draw_array()
    piece, initial_piece = next_piece()
    score = 0
    fpsClock = pygame.time.Clock()
    start_time = time.time()
    while True:
        USI = pygame.key.get_pressed()
        current_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Retour au menu si la croix de la fênetre est préssé
                return
        if current_time - start_time > array_actualisation:  # déplace la pièce selon le temps donné
            if verif_collision(piece, pos, grid_array, "Down"):

                if pos[1] == 0:#Condition fin de partie (les pieces posées ont atteint le haut de la grille
                    game_over(score)
                    return
                else:#Le jeu continue
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
        window.fill((0, 0, 0))
        grille()
        font = pygame.font.SysFont("Arial", 20)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        window.blit(score_text, (280, 500))
        draw_array()
        draw_pieces(piece, pos)
        fpsClock.tick(FPS)
def fetch_scorelist():
    #Récupération de la liste des scores
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
    #Affichage des meilleurs scores
    screen = pygame.display.set_mode((400, 650))
    while True:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("arial", 16)
        score_list = fetch_scorelist()
        score_list.sort(key=lambda score_list: score_list[1], reverse=True)
        leaderboard = score_list[0:10]
        i = 0
        h_font = pygame.font.SysFont("arial", 24)
        leader_text = h_font.render("Leaderboard", True, (255, 255, 255))
        screen.blit(leader_text, (140, 50))
        leaderboard_display = []

        for leaderboard_line in leaderboard:
            lead_name = leaderboard_line[0]
            lead_score = str(leaderboard_line[1])
            line = lead_name + "     " + lead_score
            leader_line_display = font.render(line, True, (255, 255, 255))
            screen.blit(leader_line_display, (40, 120 + 40 * i))
            leaderboard_display.extend(line)
            i += 1

        button_back = pygame.Rect(150, 150, 100, 50)
        button_back.centery = 600
        button_text = font.render("Retour", True, (255, 255, 255))
        button_text_pos = button_text.get_rect()
        button_text_pos.centerx = button_back.centerx
        button_text_pos.centery = button_back.centery
        pygame.draw.rect(screen, (255, 0, 0), button_back)
        screen.blit(button_text, button_text_pos)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button_back.collidepoint(mouse_pos):
                    return

pygame.init()

done = False

while not done:
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Tetris')
    BLACK = (0, 0, 0)
    background_image = pygame.image.load("background_image.jpg").convert()

    font = pygame.font.Font(None, 50)

    text = font.render("Tetris", True, (255, 0, 0))

    text_pos_play = text.get_rect()
    text_pos_play.centerx = screen.get_rect().centerx
    text_pos_play.centery = 20

    button_lead = pygame.Rect(150, 150, 250, 50)
    button_text_lead = font.render("Leaderboard", True, (255, 255, 255))
    button_lead.centerx = 200
    button_lead.centery = 180
    button_text_leadpos = button_text_lead.get_rect()
    button_text_leadpos.centerx = button_lead.centerx
    button_text_leadpos.centery = button_lead.centery

    button_play = pygame.Rect(150, 150, 100, 50)
    button_play.centery = 100
    button_text = font.render("Start", True, (255, 255, 255))
    button_text_pos = button_text.get_rect()
    button_text_pos.centerx = button_play.centerx
    button_text_pos.centery = button_play.centery
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button_lead.collidepoint(mouse_pos):
                leaderboard_fetch()
            if button_play.collidepoint(mouse_pos):
                tetris()

    screen.fill((255, 255, 255))
    screen.blit(background_image, [0, 0])

    screen.blit(text, text_pos_play)

    pygame.draw.rect(screen, (255, 0, 0), button_play)
    screen.blit(button_text, button_text_pos)
    pygame.draw.rect(screen, (255, 0, 0), button_lead)
    screen.blit(button_text_lead,button_text_leadpos)

    pygame.display.flip()



pygame.quit()