import pygame

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
size = (400, 300)
screen = pygame.display.set_mode(size)

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Définition de la police d'écriture
font = pygame.font.Font(None, 36)

# Définition du texte
text = font.render("Menu de jeux", True, BLACK)

# Définition de la position du texte
text_pos = text.get_rect()
text_pos.centerx = screen.get_rect().centerx
text_pos.centery = 50

# Définition du bouton "Start"
button = pygame.Rect(150, 150, 100, 50)
button_text = font.render("Start", True, WHITE)
button_text_pos = button_text.get_rect()
button_text_pos.centerx = button.centerx
button_text_pos.centery = button.centery

# Boucle principale
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button.collidepoint(mouse_pos):
                print("Le jeu commence !")
                # Ici, on peut lancer le jeu en question

    # Effacement de l'écran
    screen.fill(WHITE)

    # Affichage du texte
    screen.blit(text, text_pos)

    # Affichage du bouton "Start"
    pygame.draw.rect(screen, RED, button)
    screen.blit(button_text, button_text_pos)

    # Rafraîchissement de l'écran
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()