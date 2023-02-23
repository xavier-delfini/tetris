# ----Paramètres globaux-----
# Position initial des pièces
pos_initial = [3, 0]

# Nombre d'image par seconde du jeu(Défaut 15) (une trop haute valeur peut provoquer un clignotement de la pièce
# et une accélération de la vitesse de déplacement latéral de la piece)
FPS = 15

# Peut aussi être défini manuellement(Défaut 0.20)
array_actualisation = 0.20

# Peut aussi être défini en fonction des FPS (déconseiller pour un jeu comme tetris)
# array_actualisation=1/FPS

# Pièces
Line = [
    [1, 1, 1, 1]
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

# Liste des pièces a utiliser
piece_list = (Line,Reverse_L, L, Square, Z_Block, T_Block, S_Block)
#

# Couleurs a utiliser pour chaque pièces
def color_selector(color_code):
    match color_code:
        case 0:  # No piece
            color = (0, 0, 0)
        case 1:  # Line
            color = (0, 240, 240)
        case 2:  # Reverse_L
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


#Longueur maximal du nom du joueur
name_max_lenth=15

#Score en fonction du nombre de lignes effectué
oneline_points = 1
twolines_points = 3
threelines_points = 5
tetris_points = 8