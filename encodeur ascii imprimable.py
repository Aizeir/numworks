import pygame as pg
pg.init()

# palette de couleurs
GRAY3 = (51, 51, 51)  # 333333
BLACK = (25, 31, 34)  # 191f22
GRAY2 = (89, 82, 70)  # 595246
GRAY1 = (128, 118, 101)  # 807665
GRAY0 = (187, 176, 148)  # bbb094
GREEN4 = (47, 68, 67)  # 2f4443
GREEN3 = (59, 94, 88)  # 3b5e58
GREEN2 = (90, 140, 108)  # 5a8c6c
GREEN1 = (139, 180, 141)  # 8bb48d
GREEN0 = (192, 208, 165)  # c0d0a5
WHITE = (247, 239, 199)  # f7efc7
BLUE1 = (161, 205, 176)
BLUE2 = (112, 147, 149)  # 709395
BLUE3 = (74, 120, 123)  # 4a787b
PINK3 = (56, 49, 64)  # 383140
PINK2 = (115, 77, 92)  # 734d5c
PINK1 = (167, 103, 114)  # a76772
PINK0 = (204, 134, 125)  # cc867d
ORANGE0 = (224, 186, 139)  # e0ba8b
ORANGE1 = (195, 130, 82)  # c38252
ORANGE2 = (161, 86, 60)  # a1563c
ORANGE3 = (111, 52, 45)  # 6f342d
ORANGE4 = (68, 39, 31)  # 44271f
COLORS = [GRAY3, BLACK, GRAY2, GRAY1, GRAY0, GREEN4, GREEN3, GREEN2, GREEN1, GREEN0, WHITE, BLUE1, BLUE2, BLUE3, PINK3, PINK2, PINK1, PINK0, ORANGE0, ORANGE1, ORANGE2, ORANGE3, ORANGE4]


# encoder les images (n'est pas a executer dans la calculette)
for name in ("imgs", ...):
    imageset = pg.image.load(name+".png")
    full_data = []
    for X in range(imageset.get_width() // 16):
        image = imageset.subsurface((X*16, 0, 16, imageset.get_height()))
        data = ""
        for y in range(image.get_height()):
            for x in range(16):
                color = image.get_at((x, y))
                if color[3] != 0:
                    col = COLORS.index(color.rgb)
                    pos = y*16+x
                    q, r = pos // 86, pos % 86
                    c = q*23+col
                    data += chr(33+r)+chr(33+c)

        if data: full_data.append(data)
    print(name+" = "+str(full_data))

# pour afficher l'image (dans le code du jeu)
"""
def draw_image(image_x, image_y, offset, img, scale=1):
    for i in range(0, img, 2):
        r, c = ord(img[i])-33, ord(img[i+1])-33
        col,q = c%23, c//23
        pos = q*86+r
        x,y = pos%16, pos//16
        color = COLORS[col]
        fill_rect(image_x-offset[0]+x*scale, image_y-offset[1]+y*scale, scale, scale, color)
"""
