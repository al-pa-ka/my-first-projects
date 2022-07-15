import pygame
import math

pygame.init()

screen = pygame.display.set_mode([1920,1080])

clock = pygame.time.Clock()

fps = 30

x,y = 10,10

hero2Dproection = [x,y]

num_rays = 1080

FOV = 60 

angle = 0

DIST = 192/math.tan(60*0.017)

ray_x,ray_y = hero2Dproection

p_coef = 3 * DIST * 108

ray_length = 100
left_border = (0,0)
right_border = (0,0)
map =[
    "///1//////",
    "///////1//",
    "///11/1///",
    "//////////",
    "1111111111",
    "1//11/////",
    "1/////////",
    "///////1//",
    "///11/////",
    "1////////1",
    ]
coordinates = []
for num1,string in enumerate(map):
    for num,symbol in enumerate(string):
        if symbol == "1":
            coordinates.append((num*192,num1*108))
        
print(coordinates)
for x,y in coordinates:
    print(x,y)
class Box:
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

ray_x1,ray_y1 = ray_x + ray_length * math.cos(angle), ray_y + ray_length * math.sin(angle)
step = 60/192


while True: 
    #Graphic module
    screen.fill("White")
    pygame.draw.ellipse(screen,'Red',((hero2Dproection),(20,20)),0)
    pygame.draw.line(screen,"Red",(hero2Dproection[0]+10,hero2Dproection[1]+10),(ray_x1,ray_y1),1)
    [pygame.draw.rect(screen,"Blue",(x,y,192,108),0) for x,y in coordinates]
    pygame.draw.line(screen,"Green",(hero2Dproection[0]+10,hero2Dproection[1]+10),(left_border),1)
    pygame.draw.line(screen,"Green",(hero2Dproection[0]+10,hero2Dproection[1]+10),(right_border),1)
    

    

   

    #Logic module
    pygame.event.get()


    key = pygame.key.get_pressed()
    if  key[pygame.K_ESCAPE]:
        break
    if key[pygame.K_d]:
        hero2Dproection[0]+=4
    if key[pygame.K_a]:
        hero2Dproection[0]-=4
    if key[pygame.K_w]:
        hero2Dproection[1]-=4
    if key[pygame.K_s]:
        hero2Dproection[1]+=4
    if key[pygame.K_UP]:
        angle+=7
    if key[pygame.K_DOWN]:
        angle-=7

        
    ray_x,ray_y = hero2Dproection
    
    ray_x1,ray_y1 = ray_x + ray_length * math.cos(angle*0.017), ray_y + ray_length * math.sin(angle*0.017)
    
    left_border  =  (ray_x + ray_length * math.cos((angle - 30)*0.017), ray_y + ray_length * math.sin((angle - 30)*0.017))
    right_border =  (ray_x + ray_length * math.cos((angle + 30)*0.017), ray_y + ray_length * math.sin((angle + 30)*0.017))
    
    counter = 0
    
    count=0
    
    for num_ray in range(192):
        
        faster_x = math.cos((angle - 30 + count)*0.017)
        faster_y = math.sin((angle - 30 + count)*0.017)


        for depth in range(200):
            ray = (ray_x + depth * faster_x,ray_y + depth * faster_y)
            counter+=1
            
            if (ray[0]//192*192,ray[1]//108*108) in coordinates:
                print(ray)
                pygame.draw.line(screen,"Gray",(hero2Dproection[0]+10,hero2Dproection[1]+10),(ray),1)    
                proj_height = min(p_coef / (depth + 0.0001),1080)
                pygame.draw.rect(screen,"Gray",(int(num_ray*(1920/192)),int(590 - proj_height//2),1920/192,int(proj_height)))
                break
                
        count = count + step
            
    clock.tick(fps)
    pygame.display.flip()