import pygame
import math
import cmath
import sys



flag = True

HEIGHT, WIDTH = 1000, 1000

z=25

pygame.init()
screen = pygame.display.set_mode((HEIGHT,WIDTH))
fps = 60
graph = []
serifs = []
x = -500

peredv_x = 500

print(pygame.font.get_fonts())
f1 = pygame.font.SysFont('arial',10)
print(f1)

while True:
    
    
    

    screen.fill("WHITE")
    pygame.draw.line(screen,"BLACK",(500,1000),(500,0),1)
    pygame.draw.line(screen,"BLACK",(0,500),(1000,500))
    
    
    while x < 501:
        flag_1 = False
        try:
            y = math.sin(x) + math.sin(x**2)
        except :
            x_graph,y_graph = x*z + 500, 'stop'
            graph.append((x_graph,y_graph))
            x=round(x+0.01,2)
            pass
        else:
            x_graph = x*z + peredv_x
            y_graph = -(y*z) + 500
            graph.append((x_graph,y_graph))
            x=round( x + 0.1,2)
                                                
    if flag:
        print (graph)
        flag = False
        

    
    for count in range (len(graph)-1):
            if count%10==0:
                pygame.draw.line(screen,"BLACK",(graph[count][0],502),(graph[count][0],498),2) #горизонтальные насечки
                pygame.draw.line(screen,"BLACK",(498,graph[count][0]),(502,graph[count][0]),2)
                if ((graph[count][0]-500)/z) !=0:
                    text  = f1.render(f'{(graph[count][0]-500)/z}',True,"BLACK")
                    screen.blit(text,(graph[count][0],510))
                    text2 = f1.render(f'{-((graph[count][0]-500)/z)}',True,"BLACK")
                    screen.blit(text2,(510,graph[count][0]-6))

                else:
                    text3 = f1.render(f'{((graph[count][0]-500)/z)}',True,"BLACK")
                    screen.blit(text3,(503,510))

            if graph[count][1] == 'stop' or (graph[count + 1][1] == 'stop'):
             continue

            else:      
                pygame.draw.aaline(screen,"RED",graph[count],graph[count+1])
             
                
                

               
    
        
    graph =[]
    x=-500
        
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit()
    
    key = pygame.key.get_pressed()
    
    if  key[pygame.K_w] and z<100:
        z+=0.5
    if  key[pygame.K_s] and z>1:
        z-=0.5
    if  key[pygame.K_d]:
        peredv_x -= 10
    if  key[pygame.K_a]:
        peredv_x += 10
    clock = pygame.time.Clock()
    clock.tick(fps)

    pygame.display.flip()