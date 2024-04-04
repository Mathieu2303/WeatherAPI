import pygame 

pygame.init()
background_colour = (234, 212, 252) 
screen = pygame.display.set_mode((300, 300)) 
pygame.display.set_caption('Geeksforgeeks') 
screen.fill(background_colour) 
pygame.display.flip() 
  
x = 50
y = 50
width = 40
height = 60
vel = 5 
  
  
running = True
  
 
while running: 
    pygame.time.delay(100)
   
    for event in pygame.event.get(): 
      
            
        if event.type == pygame.QUIT: 
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    screen.fill(background_colour)
    pygame.draw.rect(screen, (255, 0, 0), (x,y,width,height))
    pygame.display.update()