import xlrd
import pygame
from pygame.locals import *
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            



pygame.init()

class Block :
    global taille_case_x
    global taille_case_y
    
    def __init__(self, block_ID): #ajouter type de block
        
        if block_ID == 1 :   
            self.image = pygame.image.load("block.png").convert()
        elif block_ID == 2 :
            self.image = pygame.image.load("water.png").convert()
##        elif block_ID == 1 :
##
##        elif block_ID == 1 :
            
        self.image = pygame.transform.scale(self.image, (taille_case_x, taille_case_y))
        self.position = self.image.get_rect()
        
        
    def moveTo (self, x , y):       
        self.position = self.position.move((x,y))
        
    def place (self):
        main.blit(self.image, self.position)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            

class Player:
    global taille_case_x
    global taille_case_y
    x_vect_actuel = 0
    y_vect_actuel = 0
    
    def __init__(self):
        self.image = pygame.image.load("sprite.jpg") #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
        self.image = pygame.transform.scale(self.image, (taille_case_x, taille_case_y))
        self.position = self.image.get_rect()
        self.position = self.position.move((300, 300))
    def move(self, x_vect, y_vect):
        self.x_vect_actuel = x_vect
        self.y_vect_actuel = y_vect
        

    def afficher(self):
        main.blit(self.image, self.position)
        self.position = self.position.move(self.x_vect_actuel,self.y_vect_actuel)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            





map_file = "C:/Users/Gabril/Desktop/Programme/Python/Game/map.xlsx"


workbook = xlrd.open_workbook(map_file)
sheet = workbook.sheet_by_index(0)

main = pygame.display.set_mode((600,600)) # ou FULLSCREEN  ,RESIZABLE
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
fond = pygame.image.load("bg.jpg").convert()

nbr_case_x = 20
nbr_case_y = 20
taille_case_x = int(width/nbr_case_x)
taille_case_y = int(height/nbr_case_y)




pygame.display.set_caption("Game")
logo = pygame.image.load("sprite.jpg").convert()
pygame.display.set_icon(logo)

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
sprite = pygame.image.load("sprite.jpg") #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
sprite = pygame.transform.scale(sprite, (taille_case_x, taille_case_y))




width, height = pygame.display.Info().current_w, pygame.display.Info().current_h



player = Player()



pygame.display.flip()

pygame.time.Clock().tick(60)
pygame.key.set_repeat(40, 30)

#----------------------Création blocks----------------------------------------------------------------------------------------------------------------------------------------------------------------------            


blocks = []
rang_block_actuel = 0

for row in range(sheet.nrows):  
    for col in range(sheet.ncols):
        if sheet.cell_value(row, col) != 0:
            blocks.append(Block(sheet.cell_value(row, col)
                                ))
            blocks[rang_block_actuel].moveTo(row*taille_case_x, col*taille_case_y)
            rang_block_actuel += 1

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            




#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            
#-------------------------------EVENTS-------------------------------------------------------------------------------------------------------------------------------------------------------------            

continuer = 1
while continuer:
    for event in pygame.event.get():   
        if event.type == QUIT:
            continuer = 0

        if event.type == KEYDOWN:
            if event.key == K_UP :
                player.move(player.x_vect_actuel, -2)
                
##            elif event.key != K_DOWN :
##                player.move(player.x_vect_actuel, 0)
                
            elif event.key == K_DOWN :
                player.move(player.x_vect_actuel, 2)
                

            if event.key == K_LEFT :
                player.move(-2, player.y_vect_actuel)
                
##            elif event.key != K_RIGHT :
##                player.move(0, player.y_vect_actuel)
                
            elif event.key == K_RIGHT :
                player.move(2, player.y_vect_actuel)
                
        if event.type == KEYUP:
            if event.key == K_DOWN or event.key == K_UP :
                player.move(player.x_vect_actuel, 0)
            if event.key == K_RIGHT or event.key == K_LEFT:
                player.move(0, player.y_vect_actuel)

#-------------Affichage-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            

       # if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 100 and event.pos[0] <: #event.pos[0] : abscisse|event.pos[1] : ordonnée | if event.type == MOUSEMOTION and event.buttons[0] == 1:
	

    main.blit(fond,(0,0))
    
    for i in blocks:      

        main.blit(i.image,i.position)
    player.afficher()

    

    pygame.display.flip()  
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            

pygame.quit()
           
	    

