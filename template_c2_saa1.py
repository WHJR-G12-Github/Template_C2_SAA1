import pygame
pygame.init()
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Shooting Spaceship")
background_image = pygame.image.load("bg2.jpg").convert()
screen.blit(background_image,[0,0])
BLUE=(0,0,255)
player=pygame.Rect(200,200,30,30)
pygame.draw.rect(screen,BLUE,player)
WHITE=(255,255,255)
enemy=pygame.Rect(100,100,30,30)
pygame.draw.rect(screen,WHITE,enemy)
# Assign the value '5' to 'xvel'
xvel=
# Assign the value '5' to 'yvel'
yvel=
# Game loop
while True:
    # Code to close the game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # Inside the loop - Start coding here
    # Incrementing 'enemy.x' with 'xvel'
    enemy.x=enemy.x + xvel
    # Incrementing 'enemy.y' with 'yvel'
    enemy.y=enemy.y + yvel
    # Checking for condition 1 or condition 2
    if enemy.x < -250 or enemy.x > 650:
        xvel = -1*xvel  
    # Checking for condition 1 or condition 2
    if enemy.y < -250 or enemy.y > 850:
        yvel = -1*yvel  
    
    # Adding the background image and drawing the rectangles
    screen.blit(background_image,[0,0])
    pygame.draw.rect(screen,BLUE,player)
    pygame.draw.rect(screen,WHITE,enemy)
    
    # Updating the screen display
    pygame.display.update()
    
    # Setting the maximum number of frames
    pygame.time.Clock().tick(30)

    

 
