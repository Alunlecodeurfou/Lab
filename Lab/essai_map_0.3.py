
import pygame
import time
import random
import math

def creation_map(longueur, largeur):
    map=[]
    for l in range(largeur):
        map.append([])
        for c in range(longueur):
            map[l].append(0)

        map=[[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]]

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

def main_boucle(map, longueur_vision, largeur_vision, taille_bordure, vitesse_character):

    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption("Essai de map")

    longueur, largeur=48*16, 48*16
    longueur_map, largeur_map=len(map), len(map[0])

    if longueur_vision % 2 == 0:
        longueur_vision += 1
    if largeur_vision % 2 == 0:
        largeur_vision += 1

    screen = pygame.display.set_mode((longueur, largeur))
    font = pygame.font.SysFont(None, 24)
    img_fond=pygame.image.load("assets/img_fond.png")
    img_fond=img_fond.convert()
    img_fond=pygame.transform.scale(img_fond, (longueur, largeur))
    img_mur=pygame.image.load("assets/img_mur.png")
    img_mur=img_mur.convert()
    img_mur=pygame.transform.scale(img_mur,(math.floor(longueur/longueur_vision), math.floor(largeur/largeur_vision)))

    longueur_image_character_1, largeur_image_character_1=450, 430
    img_character_1_1=pygame.image.load("assets/character_1_1.png")
    img_character_1_1=img_character_1_1.convert_alpha()
    img_character_1_1=pygame.transform.scale(img_character_1_1,(math.floor(longueur/longueur_vision), math.floor(largeur/largeur_vision)*(1*longueur_image_character_1/largeur_image_character_1)))
    
    img_character_1_2=pygame.image.load("assets/character_1_2.png")
    img_character_1_2=img_character_1_2.convert_alpha()
    img_character_1_2=pygame.transform.scale(img_character_1_2,(math.floor(longueur/longueur_vision), math.floor(largeur/largeur_vision)*(1*longueur_image_character_1/largeur_image_character_1)))


    img_character_1_3=pygame.image.load("assets/character_1_3.png")
    img_character_1_3=img_character_1_3.convert_alpha()
    img_character_1_3=pygame.transform.scale(img_character_1_3,(math.floor(longueur/longueur_vision), math.floor(largeur/largeur_vision)*(1*longueur_image_character_1/largeur_image_character_1)))
    
    img_character_1_4=pygame.image.load("assets/character_1_4.png")
    img_character_1_4=img_character_1_4.convert_alpha()
    img_character_1_4=pygame.transform.scale(img_character_1_4,(math.floor(longueur/longueur_vision), math.floor(largeur/largeur_vision)*(1*longueur_image_character_1/largeur_image_character_1)))

    img_character_1_5=pygame.image.load("assets/character_1_5.png")
    img_character_1_5=img_character_1_5.convert_alpha()
    img_character_1_5=pygame.transform.scale(img_character_1_5,(math.floor(longueur/longueur_vision), math.floor(largeur/largeur_vision)*(1*longueur_image_character_1/largeur_image_character_1)))
            
    img_character_1_6=pygame.image.load("assets/character_1_6.png")
    img_character_1_6=img_character_1_6.convert_alpha()
    img_character_1_6=pygame.transform.scale(img_character_1_6,(math.floor(longueur/longueur_vision), math.floor(largeur/largeur_vision)*(1*longueur_image_character_1/largeur_image_character_1)))

    img_character_1_7=pygame.image.load("assets/character_1_7.png")
    img_character_1_7=img_character_1_7.convert_alpha()
    img_character_1_7=pygame.transform.scale(img_character_1_7,(math.floor(longueur/longueur_vision), math.floor(largeur/largeur_vision)*(1*longueur_image_character_1/largeur_image_character_1)))
    
    img_character_1_8=pygame.image.load("assets/character_1_8.png")
    img_character_1_8=img_character_1_8.convert_alpha()
    img_character_1_8=pygame.transform.scale(img_character_1_8,(math.floor(longueur/longueur_vision), math.floor(largeur/largeur_vision)*(1*longueur_image_character_1/largeur_image_character_1)))
                        
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
    
    x, y=16,11
    old_x, old_y=x, y
    img_character=img_character_1_1
    vitesse_transition=1
    change_frame=0
    liste_changement_frame_right=[img_character_1_1,img_character_1_2,img_character_1_3,img_character_1_4,img_character_1_5,img_character_1_6,img_character_1_7,img_character_1_8]
    liste_changement_frame=liste_changement_frame_right
    liste_changement_frame_left=[]
    for i in range(len(liste_changement_frame_right)):
        liste_changement_frame_left.append(pygame.transform.flip(liste_changement_frame_right[i], True, False))
    ind_changement_frame=0
    
    while running:
        
        clock.tick(vitesse_character)
        
        if ind_changement_frame==len(liste_changement_frame)-1:
            ind_changement_frame=0
        else:
            ind_changement_frame+=1
        img_character=liste_changement_frame[ind_changement_frame]

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        if running==False:
            break
        keys = pygame.key.get_pressed()
        old_x, old_y = x, y

        if keys[pygame.K_RIGHT]:
            x += 1
            liste_changement_frame=liste_changement_frame_right
        elif keys[pygame.K_LEFT]:
            x -= 1
            if liste_changement_frame_left!=[]:
                liste_changement_frame=liste_changement_frame_left
        elif keys[pygame.K_UP]:
            y -= 1
        elif keys[pygame.K_DOWN]:
            y += 1

        
        if x<taille_bordure or x>longueur_map-taille_bordure or y<taille_bordure-1 or y>largeur_map-taille_bordure or map[y-1][x-1]==1:
            x,y=old_x, old_y
        
        screen.blit(img_fond, (0,0))
        for l in range(y-largeur_vision//2-1, y+largeur_vision//2+1):
            for c in range(x-longueur_vision//2-1, x+longueur_vision//2+1,):
                if map[l][c]==1:
                    screen.blit(img_mur, ((c-(x-longueur_vision//2-1))*(longueur/longueur_vision), (l-(y-largeur_vision//2-1))*(largeur/largeur_vision),))
        screen.blit(img_character, (longueur // 2 - img_character.get_width() // 2,largeur // 2 - img_character.get_height() // 2))
        
        pygame.display.flip()

    pygame.quit()

def show_map(map):
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

        for l in range(largeur_map):
            for c in range(longueur_map):
                if map[l][c]==1:
                    screen.blit(img_mur, (c*(math.floor(longueur/longueur_map)), l*(math.floor(largeur/largeur_map))))
        pygame.display.flip()
        time.sleep(1)


longueur_map_miniature, largeur_map_miniature=10, 10
agrandissement_initiation=5
taille_bordure_initiation=10
longueur_vision_intiation, largeur_vision_initiation=15, 15

map=creation_map(longueur_map_miniature, largeur_map_miniature)
map=agrandissment_map(map, agrandissement_initiation)
map=creation_bordure(map, taille_bordure_initiation)
'''show_map(map)'''
main_boucle(map, longueur_vision_intiation, largeur_vision_initiation, taille_bordure_initiation, 12)
