import pygame # Importar llibreria pygame

# Iniciar Pygame
pygame.init() # Inicia pygame i els seus mòduls (gràfics, so...)

# Configuració de la pantalla
amplada, altura = 800, 670 # Estableixo els valors d'altura i amplada
pantalla = pygame.display.set_mode((amplada, altura)) # Dic que els valors d'altua i amplada siguin la mida de la finestra
pygame.display.set_caption("Carrera de cotxes") # Defineixo el nom de la finestra

# Estableixo colors per a el fons
blanc = (255, 255, 255) # Color blanc
negre = (0, 0, 0) # Color negre
vermell = (255, 0, 0) # Clolor vermell

# Imatge cotxe
cotxe = pygame.image.load("cotxe1.png")  # Utilitzar una imatge pel cotxe (.png en la carpeta del projecte)
cotxe = pygame.transform.scale(cotxe, (96, 216)) # Dimensions del cotxe (per tant, de la imatge)

# Imatge fons
fons = pygame.image.load("fons1.png")  # Canvia "fons.png" pel nom del teu fitxer
fons = pygame.transform.scale(fons, (amplada, altura))  # Ajustar la mida de la imatge a la pantalla

# Paràmetres del jugador
jugador_x = amplada // 2 - 62 # Posició d'amplada del cotxe en començar a jugar
jugador_y = altura - 250 # Posició d'altura del cotxe en començar a jugar
velocitat = 5 # Velocitat de moviment del cotxe

# Límits carretera
marge_esquerre = 50  # Límit esquerra
marge_dret = amplada - 50  # Límit dret 

# Rellotge
rellotge = pygame.time.Clock() # Rellotge per a controlar els FPS

# El bucle del joc
jugant = True # Aquesta variable diu que el joc s'inicia, ja que està en true, si està en false el joc acabarà
while jugant: # Mentre jugant sigui True el joc continuarà executant-se.
    rellotge.tick(60) # Es juga a 40 FPS

    # Per a poder tancar la finestra
    for esdeveniment in pygame.event.get(): # Per a capturar els esdeveniments (tecles, ratolí, tancar finestra...)
        if esdeveniment.type == pygame.QUIT: # Si es detecta QUIT fa el següent:
            jugant = False # S'acaba el joc
    
    # Fotos del joc
    pantalla.blit(fons, (0, 0)) # Posar el fons
    pantalla.blit(cotxe, (jugador_x, jugador_y)) # Posar el cotxe
    
    pygame.display.flip() # Actualitza la pantalla per a ensenyar els canvis


pygame.quit() # Tanca pygame 
