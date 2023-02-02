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

import pygame

# Test d'un code + tentative d'automatisation du calcul de la grille (ça n'a pas très bien marché)
"""
# Grille uniquement pour affichage (ne possède pas de collisions et n'en a pas vraiment besoin si l'on connait les dimension d'un carré)
pygame.init()
debut_grille = (50, 50, 30)
fin_calcul = [(debut_grille[1] + (10 * debut_grille[2])), (debut_grille[0] + (22 * debut_grille[2])), debut_grille[2]]
grid_display=fin_calcul[0]+(debut_grille[0]*4),fin_calcul[1]+(debut_grille[0]*4)
Background = pygame.display.set_mode(grid_display)
pygame.draw.line(Background, (255, 255, 255), (50, 100), (350, 760))
debut_grille = (15, 15, 30)
fin_calcul = [(debut_grille[1] + (10 * debut_grille[2])), (debut_grille[0] + (22 * debut_grille[2])), debut_grille[2]]
print(fin_calcul)
for i in range(debut_grille[0], fin_calcul[1], debut_grille[2]):
    print(i)
    pygame.draw.line(Background, (255, 255, 255), (debut_grille[0], i), (fin_calcul[0], i))
    pygame.draw.line(Background, (255, 255, 255), (i, debut_grille[1]), (i, fin_calcul[1]))
pygame.display.update()

while pygame.event.wait().type != pygame.QUIT:
    pass
"""
Line = [[[0, 0, 0, 0],
         [1, 1, 1, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],

        [[0, 0, 1, 0],  #[1,0] passe a [0,2]
         [0, 0, 1, 0],  #[1,1] passe a [1,2]
         [0, 0, 1, 0],  #[1,2] passe a [2,2]
         [0, 0, 1, 0]], #[1,3] passe a [3,2]

        [[0, 0, 0, 0],  # [0,2] passe a [2,0]
        [0, 0, 0, 0],   # [1,2] passe a [2,1]
        [1, 1, 1, 1],   # [2,2] passe a [2,2]
        [0, 0, 0, 0]],  # [3,2] passe a [2,3]

        [[0, 1, 0, 0],  # [2,0] passe a [0,1]
        [0, 1, 0, 0],   # [2,1] passe a [1,1]
        [0, 1, 0, 0],   # [2,2] passe a [2,1]
        [0, 1, 0, 0]],  # [2,3] passe a [3,1]
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

for i in range(10, 571, 25):
    pygame.draw.line(window, (255, 255, 255), (10, i), (260, i))
    pygame.draw.line(window, (255, 255, 255), (i, 10), (i, 560))
    pygame.draw.rect(window, (0, 255, 255), ((12, 12), (22, 22)), 0)
    pygame.draw.rect(window, (0, 255, 255), ((37, 12), (22, 22)), 0)
    pygame.draw.rect(window, (0, 255, 255), ((62, 12), (22, 22)), 0)
    pygame.draw.rect(window, (0, 255, 255), ((87, 12), (22, 22)), 0)

pygame.display.update()

while pygame.event.wait().type != pygame.QUIT:
    pass
