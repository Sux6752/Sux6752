# import pygame module in this program 
import pygame

colour = [[255, 0, 255], [255, 0, 0], [255, 255, 0], [0, 255, 0], [0, 0, 255]]
  
# activate the pygame library .  
# initiate pygame and give permission  
# to use pygame's functionality.  
pygame.init()
  
# create the display surface object  
# of specific dimension..e(500, 500).  
win = pygame.display.set_mode((1200, 600))
  
# set the pygame window name 
pygame.display.set_caption("Проект <<pygame>>")
  
# object current co-ordinates

x_rs = 0

x_r = 550
y_r = 550

x_p = 625
y_p = 700
  
# dimensions of the object 
width = 150
height = 20
  
# velocity / speed of movement
vel = 10
# V = 3
V_y_p = 3
V_x_p = 3
V_x_x_p = (V_y_p, V_x_p)
  
# Indicates pygame is running
run = True
  
# infinite loop 
while run:
    # creates time delay of 10ms 
    pygame.time.delay(15)
      
    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get():
          
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT:
              
            # it will make exit the while loop 
            run = False
    # stores keys pressed 
    keys = pygame.key.get_pressed()
      
    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x_r>50:
          
        # decrement in x co-ordinate
        x_r -= vel
          
    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x_r<1150-width:
          
        # increment in x co-ordinate
        x_r += vel
         
    # if left arrow key is pressed   
#     if keys[pygame.K_UP] and y>0:
#           
#         # decrement in y co-ordinate
#         y -= vel
#           
#     # if left arrow key is pressed   
#     if keys[pygame.K_DOWN] and y<500-height:
#         # increment in y co-ordinate
#         y += vel
         
              
    # completely fill the surface object  
    # with black colour  
    win.fill((0, 0, 0))
      
    # drawing object on screen which is rectangle here 
    rect = pygame.draw.rect(win, (255, 255, 255), (x_r, y_r, width, height))
    point = pygame.draw.rect(win, (255, 255, 255), (x_p, y_p, 7,7))
    move = x_rs
    d = 1
    for i in range (1, 46):
        pygame.draw.rect(win, (colour[0]), (move, 0, 25,25))
        move+=27 + d
    move = x_rs
    for i in range (1, 46):
        pygame.draw.rect(win, (colour[1]), (move, 27, 25,25))
        move+=27 + d
    move = x_rs
    for i in range (1, 46):
        pygame.draw.rect(win, (colour[2]), (move, 54, 25,25))
        move+=27 + d
    move = x_rs
    for i in range (1, 46):
        pygame.draw.rect(win, (colour[3]), (move, 81, 25,25))
        move+=27 + d
    move = x_rs
    for i in range (1, 46):
        pygame.draw.rect(win, (colour[4]), (move, 108, 25,25))
        move+=27 + d
        
        
    if rect.colliderect(point):
        V_x_p=-V_x_p
        V_y_p=-V_y_p
        
    y_p -= V_y_p;
    x_p -= 2 * V_x_p;
    if y_p < 0:
        V_y_p = -V_y_p;
    if x_p < 0 or x_p > 1200:
        V_x_p = -V_x_p
    
    if x_p < rect.center[0] and rect.colliderect(point):
        V_x_p = V_x_p
    if x_p > rect.center[1] and rect.colliderect(point):
        V_y_p = V_y_p

    
      
    # it refreshes the window
    pygame.display.update() 
  
# closes the pygame window 
pygame.quit()