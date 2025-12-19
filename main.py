import pygame

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Stock Tracker')

header = pygame.font.Font(None, 50)
text = header.render("Stock Tracker", True, (0, 0, 0))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((200, 200, 200))  
    screen.blit(text, (100, 50)) 
    pygame.display.flip()

pygame.quit()
