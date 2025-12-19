import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Stock tracker')

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()