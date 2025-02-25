# Explicació del Joc 
 

**Objectiu** 

Has de controlar un cotxe i esquivar els obstacles que cauen des de dalt. A mesura que passa el temps, els obstacles es mouen més ràpidament i apareixen amb més freqüència. El joc acaba si el cotxe xoca amb un obstacle. 
 

**Controls** 

← Moure a l'esquerra 
→ Moure a la dreta 
↑ Moure cap amunt 
↓ Moure cap avall 
 

**Funcionament** 

- El cotxe es mou dins d’uns límits perquè no surti de la carretera. 
- Els obstacles apareixen en posicions aleatòries i es desplacen cap avall. 
- Amb el temps, el joc es torna més difícil: els obstacles es mouen més ràpidament i apareixen més sovint. 
- Si el cotxe toca un obstacle, has perdut.


**Documentació addicional**

He utilitzat les següents llibreries:
- Pygame: Per gestionar gràfics, esdeveniments i la finestra del joc.
- Random: Per generar posicions aleatòries dels obstacles.

Configuració de la pantalla:
- Amb pygame he definit la mida (800x670).
- Faig servir blit() per renderitzar les imatges.
- flip() actualitza la pantalla perquè els canvis siguin visibles.
- He limitat el joc a 60 FPS amb Clock.tick(60).

**Paràmetres del joc:**

- Velocitat del cotxe: velocitat = 7
- Dimensions del cotxe: cotxe = pygame.transform.scale(cotxe, (96, 216))
- Velocitat dels obstacles: velocitat_obstacles = 5
- Dimensions dels obstacles: twingo = pygame.transform.scale(twingo, (80, 160))
- Freqüència dels obstacles: freqencia_obstacles = 70