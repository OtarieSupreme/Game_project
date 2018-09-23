import xlrd
import pygame
from pygame.locals import *



pygame.init()

#class block :

#def __init__(self): #ajouter type de block


map_file = "C:/Users/Gabril/Desktop/Programme/Python/Game/map.xlsx"


workbook = xlrd.open_workbook(map_file)
sheet = workbook.sheet_by_index(0)

main = pygame.display.set_mode((600,600)) # ou FULLSCREEN  ,RESIZABLE
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
fond = pygame.image.load("bg.jpg").convert()

nbr_case_x = 20
nbr_case_y = 20

taille_case_x = width/nbr_case_x
taille_case_y = height/nbr_case_y



pygame.display.set_caption("Game")
logo = pygame.image.load("sprite.jpg").convert()
pygame.display.set_icon(logo)

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
sprite = pygame.image.load("sprite.jpg") #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent

sprite.set_colorkey((255,255,255))
sprite.convert_alpha()
position_sprite = sprite.get_rect()
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
#spawn_sprite_x = width /2 - sprite.get_width/2
#spawn_sprite_y = height /2 - sprite.get_height/2

#position_sprite = position_sprite.move((spawn_sprite_x, spawn_sprite_y))
position_sprite = position_sprite.move((300, 300))

block = pygame.image.load("block.png").convert()
block = pygame.transform.scale(block, (int(width/nbr_case_x), int(height/nbr_case_y)))



pygame.display.flip()

pygame.time.Clock().tick(60)
pygame.key.set_repeat(40, 30)




continuer = 1
while continuer:
    for event in pygame.event.get():   
        if event.type == QUIT:
            continuer = 0

        if event.type == KEYDOWN:
            if event.key == K_UP :
                position_sprite = position_sprite.move(0,-3)

            if event.key == K_DOWN :
                position_sprite = position_sprite.move(0,3)

            if event.key == K_RIGHT :
                position_sprite = position_sprite.move(3,0)
            if event.key == K_LEFT :
                position_sprite = position_sprite.move(-3,0)

    
    for row in range(sheet.nrows):
        
        for col in range(sheet.ncols):
            if sheet.cell_value(row, col) == 1:
                main.blit(block,(taille_case_x*row,taille_case_y*col))
                pygame.display.flip() 
                


       # if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 100 and event.pos[0] <: #event.pos[0] : abscisse|event.pos[1] : ordonnée | if event.type == MOUSEMOTION and event.buttons[0] == 1:
	

         

    main.blit(fond,(0,0))
    main.blit(sprite, position_sprite)
    pygame.display.flip()  
        
pygame.quit()
            
	    

