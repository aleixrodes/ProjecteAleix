import pygame 

# Per a iniciar Pygame
pygame.init()

# Per a configurar la pantalla del joc
amplada, altura = 600, 650 # Estableixo els valors d'altura i amplada
pantalla = pygame.display.set_mode((amplada, altura)) # Dic que els valors d'altua i amplada siguin la mida de la finestra
pygame.display.set_caption("Carrera de cotxes") # Defineixo el nom de la finestra

# Estableixo colors per a el fons
blanc = (255, 255, 255) # Color blanc
negre = (0, 0, 0) # Color negre

# El bucle del joc
jugando = True # Aquesta varible diu que el joc s'inicia ja que esta en true, si esta en false el joc acabara
while jugando:    
    # Per a poder tencar la finestra
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
    
    # Per a el fons d'el joc
    pantalla.fill(blanc)
    

pygame.quit()
