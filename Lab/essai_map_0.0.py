import pygame
import time
import random
import math

def creation_map():
    map=[]
    for l in range(10):
        map.append([])
        for c in range(10):
            map[l].append(0)

    map=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    return(map)

def agrandissment_map(map, agrandissement):
    map_agrandie = []

    for l in range(len(map) * agrandissement):
        map_agrandie.append([0] * (len(map[0]) * agrandissement))

    for l in range(len(map)):
        for c in range(len(map[0])):
            val = map[l][c]
            for i in range(agrandissement):
                for j in range(agrandissement):
                    map_agrandie[l * agrandissement + i][c * agrandissement + j] = val

    return map_agrandie

def creation_bordure(map, taille):
    new_map=[]
    for l in range(len(map)+2*taille):
        new_map.append([])
        for c in range(len(map[0])+2*taille):
            new_map[l].append(1)
    for l in range(len(map)):
        for c in range(len(map[0])):
            new_map[l+taille][c+taille]=map[l][c]
    return new_map
def main_boucle(map):
    pygame.init()
    pygame.display.set_caption("Essai de map")

    longueur, largeur=48*16, 48*16
    longueur_map, largeur_map=len(map), len(map[0])

    screen = pygame.display.set_mode((longueur, largeur))
    font = pygame.font.SysFont(None, 24)
    img_fond=pygame.image.load("assets/img_fond.png")
    img_fond=img_fond.convert()
    img_fond=pygame.transform.scale(img_fond, (longueur, largeur))
    img_mur=pygame.image.load("assets/img_mur.png")
    img_mur=img_mur.convert()
    img_mur=pygame.transform.scale(img_mur,(math.floor(longueur/longueur_map), math.floor(largeur/largeur_map)))

    screen.blit(img_fond, (0,0))

    WHITE = (255,255,255)
    GREEN = (0,255,0)
    RED = (255,0,0)
    BLUE = (0,0,255)
    BLACK = (0,0,0)
    FUCHSIA = (255, 0, 255)
    GRAY = (128, 128, 128)
    LIME = (0, 128, 0)
    MAROON = (128, 0, 0)
    NAVYBLUE = (0, 0, 128)
    OLIVE = (128, 128, 0)
    PURPLE = (128, 0, 128)
    TEAL = (0,128,128)
    ROUGE_FONCE=(139, 0, 0)

    running=True

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for l in range(longueur_map):
            for c in range(largeur_map):
                if map[l][c]==1:
                    screen.blit(img_mur, (c*(math.floor(longueur/longueur_map)), l*(math.floor(largeur/largeur_map))))
        pygame.display.flip()
        time.sleep(1)


map=creation_map()
map=creation_bordure(map,2)
map=agrandissment_map(map, 2)
print(len(map), len(map[0]))
'''for l in map:
    print(l)'''
main_boucle(map)