import pygame

#class MainScreen:
pygame.init()
pygame.font.init()
pygame.display.set_caption('Busy Planner')

screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
background = pygame.image.load('src/background.png')
# bgImage = background.get_rect()
# bgImage = pygame.transform.scale(background(screen))
# surface = pygame.display.set_mode((screen))
        

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    pygame.display.update()
  
# quit pygame after closing window
pygame.quit()