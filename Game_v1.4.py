import xlrd
import pygame
from pygame.locals import *
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            



pygame.init()

class Block :
    global taille_case_x
    global taille_case_y
    
    def __init__(self, block_ID): #ajouter type de block
        block_ID = int(block_ID)
        self.image = pygame.image.load(data.cell_value( block_ID + 1, 1)).convert()
        self.image = pygame.transform.scale(self.image, (taille_case_x, taille_case_y))
        self.position = self.image.get_rect()
        
        
    def moveTo (self, x , y):       
        self.position = self.position.move((x*taille_case_x,y*taille_case_y))
        
    def place (self):
        main.blit(self.image, self.position)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            

class Player:
    global taille_case_x
    global taille_case_y
    global width, height
    global nbr_case_x ,nbr_case_y 
    x_vect_actuel = 0
    y_vect_actuel = 0

    
    def __init__(self):

        self.image = pygame.image.load("sprite.jpg")
        
##        self.image.set_alpha(255)
##        self.image.set_colorkey((255,255,255))
##        pygame.Surface.convert_alpha(self.image)
        self.image = pygame.transform.scale(self.image, (taille_case_x, taille_case_y))
        self.position = self.image.get_rect()
        self.position = self.position.move((300, 300))
        x = self.position.centerx
        y = self.position.centery
        xgrid = int((x/width)*nbr_case_x)
        ygrid = int((x/height)*nbr_case_y)
        self.x = 0
        self.y = 0
        self.xgrid = 0
        self.ygrid = 0
        
    def move(self, x_vect, y_vect):



##        if (map_array[player.ygrid - 1][player.xgrid] ==0 or y_vect >0)and (map_array[player.ygrid + 1][player.xgrid] ==0 or y_vect <0):
##            self.y_vect_actuel = y_vect    
##        else :
##            self.y_vect_actuel =0
##
##        if (map_array[player.ygrid][player.xgrid-1] ==0 or x_vect >0)and (map_array[player.ygrid][player.xgrid + 1] ==0 or x_vect <0):
##            self.x_vect_actuel = x_vect    
##        else :
##            self.x_vect_actuel =0
#------------------------------------Test-----------------------------------------------------------------------------------------------------------------
        self.y_vect_actuel =y_vect
        self.x_vect_actuel =x_vect
        for i in blocks:

            
            if self.y_vect_actuel !=0:
                if (abs(self.position.centerx - i.position.centerx) > taille_case_x-1) or(self.position.top> i.position.bottom) or (self.position.bottom < i.position.top):
                    self.y_vect_actuel = y_vect
                elif (abs(self.position.top - i.position.bottom) < 2 and y_vect >0 )or(abs(self.position.bottom - i.position.top) < 4 and y_vect <0):
                    self.y_vect_actuel = y_vect
                else :
                    self.y_vect_actuel =0
            if self.x_vect_actuel !=0:
                if (abs(self.position.centery - i.position.centery) > taille_case_y-1) or(self.position.left > i.position.right) or (self.position.right < i.position.left):
                    self.x_vect_actuel = x_vect

                elif (abs(self.position.right - i.position.left) < 2 and x_vect < 0 )or(abs(self.position.left - i.position.right) < 4 and x_vect >0):
                    self.x_vect_actuel = x_vect

                else :
                    self.x_vect_actuel =0

        


#-----------------------------------------------------------------------------------------------------------------------------------------------------

            
        self.position = self.position.move(self.x_vect_actuel,self.y_vect_actuel)
        
        self.x = self.position.centerx
        self.y = self.position.centery
        self.xgrid = int((self.x/width)*nbr_case_x)      
        self.ygrid = int((self.y/height)*nbr_case_y)             

    def afficher(self):
        main.blit(self.image, self.position)
           
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            





map_file = "map.xlsx"
data_file = "data.xlsx"

workbook_data = xlrd.open_workbook(data_file)
data = workbook_data.sheet_by_index(0)

workbook = xlrd.open_workbook(map_file)
sheet = workbook.sheet_by_index(0)

main = pygame.display.set_mode((600,600)) # ou FULLSCREEN  ,RESIZABLE
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
fond = pygame.image.load("bg.jpg").convert()

nbr_case_x = 20
nbr_case_y = 20
taille_case_x = width//nbr_case_x
taille_case_y = height//nbr_case_y




pygame.display.set_caption("Game")
logo = pygame.image.load("sprite.jpg").convert()
pygame.display.set_icon(logo)

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
sprite = pygame.image.load("sprite.jpg") #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
sprite = pygame.transform.scale(sprite, (taille_case_x, taille_case_y))




width, height = pygame.display.Info().current_w, pygame.display.Info().current_h



player = Player()



pygame.display.flip()

#pygame.time.Clock().tick(60)
pygame.key.set_repeat(40, 30)

#----------------------Création blocks----------------------------------------------------------------------------------------------------------------------------------------------------------------------            

line_array = []
map_array = [] 
blocks = []
rang_block_actuel = 0

for row in range(sheet.nrows):  
    for step_row in range(sheet.ncols):
        if sheet.cell_value(step_row, row) != 0:
            blocks.append(Block(sheet.cell_value(step_row, row)))
            blocks[rang_block_actuel].moveTo(row, step_row)
            rang_block_actuel += 1
            
        line_array.append(int(sheet.cell_value(row, step_row)))
        
    map_array.append(line_array)
    line_array = []
                              

        
        


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            


##############################################-##--BOUCLE--##-######################################################################################################################

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            
#-------------------------------EVENTS-------------------------------------------------------------------------------------------------------------------------------------------------------------            
speed = 10
continuer = 1
while continuer:
    for event in pygame.event.get():   
        if event.type == QUIT:
            continuer = 0

        if event.type == KEYDOWN:
##            print(player.xgrid)
##            print(player.ygrid)
            
            if event.key == K_UP :
                player.move(player.x_vect_actuel, -speed)
                
##            elif event.key != K_DOWN :
##                player.move(player.x_vect_actuel, 0)
                
            elif event.key == K_DOWN :
                player.move(player.x_vect_actuel, speed)
                

            if event.key == K_LEFT :
                player.move(-speed, player.y_vect_actuel)
                
##            elif event.key != K_RIGHT :
##                player.move(0, player.y_vect_actuel)
                
            elif event.key == K_RIGHT :
                player.move(speed, player.y_vect_actuel)
                
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
           
	    

