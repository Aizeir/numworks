"""
CE SCRIPT N'EST PAS A EXECUTER SUR CALCULATRICE MAIS SOUS PYTHON/PYGAME

molette = changer de bloc
click gauche = placer
clic droit = effacer
tab = reset

BLEU: joueur
VERT: fin
JAUNE: coin
BLANC: bloc

La map est affichée sur la console (print), il faudra ensuite la copier coller dans la liste "levels" en oubliant pas la virgule.
On peut charger un niveau en remplacant "blocks" (attention, vérifier qu'il n'y a pas de virgule après le ']')

ne jouez pas en cours
"""

import pygame as pg
import sys
pg.init()

# Dimensions de la fenêtre et de la grille
TS = 40
MAPW = 16
MAPH = 10
W = TS * MAPW
H = TS * MAPH
screen = pg.display.set_mode((W, H))
pg.display.set_caption("Editeur de niveau")

# Couleurs
BG = (50, 50, 50)
COLORS = {
    0: (150, 150, 150),  # Bloc gris
    1: (200, 200, 50),  # Bloc jaune
    "end": (100, 255, 100),      # Bloc vert
    "player": (50, 150, 255)  # Bloc joueur (bleu)
}

# Variables de l'éditeur
selected_block = 0  # 0 = bloc gris, 1 = bloc vert, "player" = rond bleu

# LE NIVEAU
blocks = [(0, 1, 0), (0, 0, 'player'), (10, 6, 0), (10, 2, 0), (11, -1, 0), (11, -2, 0), (7, 9, 0), (7, 6, 0), (7, 5, 0), (7, 3, 0), (7, 0, 0), (3, 0, 0), (3, 1, 0), (3, 2, 0), (3, 3, 0), (3, 4, 0), (3, 5, 0), (3, 9, 0), (3, 7, 0), (3, 6, 0), (10, 5, 0), (10, 4, 0), (8, 2, 0), (9, 1, 0), (9, 7, 0), (8, 7, 0), (10, 7, 1), (7, 7, 0), (15, 0, 'end'), (12, 5, 0), (12, 4, 0), (12, 3, 0), (12, 2, 0), (12, 1, 0), (12, 0, 0), (14, 0, 0), (14, 1, 0), (14, 2, 0), (14, 9, 0), (14, 5, 0)]

block_types = list(COLORS)  # Types de blocs disponibles
blocks = [block for block in blocks if block[1] < MAPH]

# Fonction pour dessiner un bloc
def draw_block(x, y, code, preview=False):
    color = COLORS[code]
    rect = pg.Rect(x * TS, y * TS, TS, TS)

    if isinstance(code, str):
        center = (x * TS + TS // 2, y * TS + TS // 2)
        radius = TS // 2
        if preview:
            pg.draw.circle(screen, color, center, radius, 2)  # Cercle transparent
        else:
            pg.draw.circle(screen, color, center, radius)  # Cercle plein
    else:
        if preview:
            pg.draw.rect(screen, color, rect, 2)  # Rectangle transparent
        else:
            pg.draw.rect(screen, color, rect)  # Rectangle plein

# Boucle principale
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print([b for b in blocks if b[1] >= 0])
            running = False
        
        elif event.type == pg.KEYDOWN and event.key == pg.K_TAB:
            blocks.clear()


        elif event.type == pg.MOUSEWHEEL:
            # Changer le bloc sélectionné avec la molette
            current_index = block_types.index(selected_block)
            selected_block = block_types[(current_index + event.y) % len(block_types)]

    # Placement
    x, y = pg.mouse.get_pos()
    grid_x, grid_y = x // TS, y // TS

    if pg.mouse.get_pressed()[0] and not (grid_x,grid_y,selected_block) in blocks:
        # Supprimer d'abord tout bloc "player" si un nouveau est ajouté
        if selected_block == "player":
            blocks = [(bx, by, bcode) for bx, by, bcode in blocks if bcode != "player"]
        elif selected_block == "end":
            blocks = [(bx, by, bcode) for bx, by, bcode in blocks if bcode != "end"]
        for block in blocks:
            if block[:2] == (grid_x,grid_y):
                blocks.remove(block)
        blocks.append((grid_x, grid_y, selected_block))
    
    elif pg.mouse.get_pressed()[2]:
        blocks = [(bx, by, bcode) for bx, by, bcode in blocks if not (bx == grid_x and by == grid_y)]


    # Effacer l'écran
    screen.fill(BG)

    # Dessiner les blocs existants
    for x, y, code in blocks:
        draw_block(x, y, code)

    # Prévisualiser le bloc sélectionné
    mouse_x, mouse_y = pg.mouse.get_pos()
    preview_x = mouse_x // TS
    preview_y = mouse_y // TS
    draw_block(preview_x, preview_y, selected_block, preview=True)

    # Mettre à jour l'affichage
    pg.display.flip()

# Quitter pg
pg.quit()
sys.exit()
