import pygame
from random import randrange
import copy

pygame.init()
screen = pygame.display.set_mode([1920,1080],pygame.FULLSCREEN)
TILE = 10

clock = pygame.time.Clock()

W = 1080//TILE
H = 1920//TILE

count = 0

next_step = []

field=[]

stabil = True

for y in range(W):
    field.append([])
    for x in range(H):
     # field[y].append((randrange(0,2)))
      field[y].append(0)
   
if stabil: 
    for y in range(0,W,3):
        for x in range(0,H,3):
            if x < H-2 and y < W-2:
                field[y][x]=1
                field[y][x+1]=1
                field[y+1][x]=1
                field[y+1][x+1]=1 

print(field)

next_step = copy.deepcopy(field)

start = False

while True:
    while (start == False):
    
        pygame.event.get()
        x, y = pygame.mouse.get_pos()
        print(x, y)

        #Graphic module
        screen.fill((255, 188, 75))
        [[pygame.draw.rect(screen, (72, 47, 10),(x*TILE, y*TILE, TILE, TILE)) for x in range(len(field[y])) if (field[y][x]==1)] for y in range(len(field))]
        [pygame.draw.line(screen, "GRAY", (0, y), (1920, y)) for y in range(0, 1080, 10)]
        [pygame.draw.line(screen, "GRAY", (x, 0), (x, 1080)) for x in range(0, 1920, 10)]
        pygame.display.flip()

        #Logic module

        MOUSEBUTTONDOWN1 = pygame.mouse.get_pressed()[0]
        MOUSEBUTTONDOWN2 = pygame.mouse.get_pressed()[2]
        print(MOUSEBUTTONDOWN1)
    
        if MOUSEBUTTONDOWN1:

           x = (x // TILE)
           y = (y // TILE)
       
           field[y][x] = 1


        if MOUSEBUTTONDOWN2:

           x = (x // TILE)
           y = (y // TILE)
       
           field[y][x] = 0



        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            start = True
        if key[pygame.K_1]:
            for y in range(0,W,3):
                for x in range(0,H,3):
                    if x < H-2 and y < W-2:
                        field[y][x]=1
                        field[y][x+1]=1
                        field[y+1][x]=1
                        field[y+1][x+1]=1 

        if key[pygame.K_0]:
            for y in range(W):
                for x in range(H):
                    field[y][x] = 0

        next_step = copy.deepcopy(field)







    while (start==True):
        #Graphic module
        screen.fill((255, 188, 75))
        [[pygame.draw.rect(screen,(72, 47, 10),(x*TILE,y*TILE,TILE,TILE)) for x in range(len(field[y])) if (field[y][x]==1)] for y in range(len(field))]
        pygame.display.flip()
    
   

        #Logic module
        pygame.event.get()
        count = 0

        field = copy.deepcopy(next_step)
        for y in range(W):
            for x in range(H):
                count = 0   
            

                if x>0:
                    if field[y][x-1] == 1:
                        count+=1
                if x<H-1:
                    if field[y][x+1] == 1:
                        count+=1

                if y>0:
                    if field[y - 1][x]==1:
                        count+=1

                    if x>0:
                        if field[y - 1][x-1]==1:
                            count+=1
                
                    if x<H-1:
                        if field[y - 1][x+1]==1:
                            count+=1
                if y<W-1:
                    if field[y + 1][x]==1:
                        count += 1

                    if x>0:
                        if field[y + 1][x-1]==1:
                            count+=1
                    if x<H-1:
                        if field[y + 1][x+1]==1:
                            count+=1

                if count < 2 or count > 3:
                    next_step[y][x] = 0
                if count == 3:
                    next_step[y][x] = 1
         
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            start = False
            print("fuck")      
                    
        pygame.event.pump()
    
        print('OK!')
        clock.tick(6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
       