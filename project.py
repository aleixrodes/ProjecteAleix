import pygame # Importar llibreria pygame
import random # Importar llibreria random

# Iniciar Pygame
pygame.init() # Inicia pygame i els seus mòduls (gràfics, so...)

# Configuració de la pantalla
amplada, altura = 800, 670 # Estableixo els valors d'altura i amplada
pantalla = pygame.display.set_mode((amplada, altura)) # Dic que els valors d'altua i amplada siguin la mida de la finestra
pygame.display.set_caption("Carrera de cotxes") # Defineixo el nom de la finestra

# Estableixo colors per a el fons
blanc = (255, 255, 255) # Color blanc
negre = (0, 0, 0) # Color negre

# Font per al temporitzador
font = pygame.font.Font(None, 45)  # Font i mida de la lletra

# Imatge cotxe
cotxe = pygame.image.load("cotxe1.png")  # Utilitzar l'imatge cotxe2.png pel cotxe (.png en la carpeta del projecte)
cotxe = pygame.transform.scale(cotxe, (96, 216)) # Dimensions del cotxe (per tant, de la imatge)

# Imatge fons
fons = pygame.image.load("fons1.png")  # Utilitza l'imatge fons1.png per el fons (.png en la carpeta del projecte)
fons = pygame.transform.scale(fons, (amplada, altura))  # Ajustar la mida de la imatge a la pantalla

# Imatge twingo
twingo = pygame.image.load("twingo.png")  # Utilitzar l'imatge twingo.png pel cotxe (.png en la carpeta del projecte)
twingo = pygame.transform.scale(twingo, (80, 160)) # Dimensions del cotxe (per tant, de la imatge)

# Paràmetres del jugador
jugador_x = amplada // 2 - 62 # Posició d'amplada del cotxe en començar a jugar
jugador_y = altura - 250 # Posició d'altura del cotxe en començar a jugar
velocitat = 7.5 # Velocitat de moviment del cotxe

# Límits carretera
marge_esquerre = 50  # Límit esquerra
marge_dret = amplada - 50  # Límit dret 
marge_superior = 100  # Límit superior
marge_inferior = altura - 216  # Límit inferior

# Obstacles
obstacles = []  # Llista per a guardar els obstacles
velocitat_obstacles = 5  # Velocitat inicial dels obstacles
freqencia_obstacles = 75  # Freqüència inicial d'aparició d'obstacles
amplada_obs, altura_obs = 80, 160  # Dimensions dels obstacles

def crear_obstacle(): # Funció per a crear obstacles
    x = random.randint(0, amplada - amplada_obs) # Que l'objecte és crei en una posició horitzontal aleatòria
    y = -altura_obs # Que l'objecte és crei a sobre la pantalla
    obstacles.append((x, y)) # Crear obstacles com a rectangles

# Rellotge
rellotge = pygame.time.Clock() # Rellotge per a controlar els FPS
temps_joc = 0  # Comptador de temps de joc

# El bucle del joc
jugant = True # Aquesta variable diu que el joc s'inicia, ja que està en true, si està en false el joc acabarà
while jugant: # Mentre jugant sigui True el joc continuarà executant-se.
    rellotge.tick(60) # Es juga a 60 FPS
    temps_joc += 1  # Incrementar el comptador de temps

 # Augmentar dificultat amb el temps
    if temps_joc % 600 == 0:  # Cada 10 segons (60 FPS * 10 segons)
        velocitat_obstacles += 0.5  # Augmenta la velocitat dels obstacles
        freqencia_obstacles = max(10, freqencia_obstacles - 4)  # Augmenta la freqüència d'aparició

    # Per a poder tancar la finestra
    for esdeveniment in pygame.event.get(): # Per a capturar els esdeveniments (tecles, ratolí, tancar finestra...)
        if esdeveniment.type == pygame.QUIT: # Si es detecta QUIT fa el següent:
            jugant = False # S'acaba el joc
    
    # Moviment del jugador
    tecla = pygame.key.get_pressed() # Detecta les tecles
    if tecla[pygame.K_LEFT] and jugador_x > marge_esquerre: # Si es detecta aquesta tecla fa el següent:
        jugador_x -= velocitat # Es mou a l'esquerra (velocitat negativa en x)
    if tecla[pygame.K_RIGHT] and jugador_x < marge_dret -106: # Si es detecta aquesta tecla fa el següent:
        jugador_x += velocitat # Es mou a la dreta (velocitat positiva en x)
    if tecla[pygame.K_UP] and jugador_y > marge_superior:  # Si es detecta aquesta tecla fa el següent:
        jugador_y -= velocitat # Es mou cap a amunt (velocitat positiva en y)
    if tecla[pygame.K_DOWN] and jugador_y < marge_inferior:  # Si es detecta aquesta tecla fa el següent:
        jugador_y += velocitat # Es mou cap a abaix (velocitat negativa en y)
    
    # Crear obstacles
    if random.randint(1, 75) == 1:  # Probabilitat d'aparèixer un obstacle
        crear_obstacle() # Genera l'obstacle
    
    obstacles = [(x, y + velocitat_obstacles) for x, y in obstacles]  # Moure obstacles
    
    # Col·lisions
    for x, y in obstacles: # Selecciona tots els obstacles
        if pygame.Rect(x, y, amplada_obs, altura_obs).colliderect(pygame.Rect(jugador_x, jugador_y, 96, 216)):# Comprova si el cotxe i un obstacle es toquen
            print("Game Over. Has fet:" , temps_joc , "punts" ) # Si és cert es mostrarà aquest text
            jugant = False # Acaba el joc
    
    # Eliminar obstacles
    obstacles = [(x, y) for x, y in obstacles if y < altura] # Elimina el obstacles de fora la pantalla
    
    # Fotos del joc
    pantalla.blit(fons, (0, 0)) # Posar el fons
    pantalla.blit(cotxe, (jugador_x, jugador_y)) # Posar el cotxe
    
    # Personalitzar obstacles
    for x, y in obstacles:  # Selecciona els obstacles
        pantalla.blit(twingo, (x, y))  # Dibuixar el Twingo amb les coordenades correctes

    # Dibuixar el temps a la pantalla amb contorn negre
    temps_text = font.render(f"Temps: {temps_joc // 60}s", True, blanc)  # Crear el text
    contorn_text = font.render(f"Temps: {temps_joc // 60}s", True, negre)  # Crear el contorn negre
    pantalla.blit(contorn_text, (13, 13))  # Dibuixar el contorn lleugerament desplaçat
    pantalla.blit(temps_text, (10, 10))  # Dibuixar el text

    pygame.display.flip() # Actualitza la pantalla per a ensenyar els canvis

pygame.quit() # Tanca pygame