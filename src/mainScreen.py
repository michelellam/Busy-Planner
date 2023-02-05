import pygame
import sys

class main_Screen:
    def __init__(self):
        ##displaying the screen 
        pygame.init()
        pygame.font.init()
        self.width = 400
        self.height = 400
        self.state = "START SCREEN"
        self.size = (self.width, self.height)
        self.resizeable = pygame.RESIZABLE
        self.title = pygame.display.set_caption('Busy Planner')
        # self.screen = pygame.display.set_mode((self.width, self.height), self.resizeable)
        # self.background = pygame.image.load('assets/background.png')

    def mainLoop(self):
        #keep the screen running
        while True:
            if (self.state == "START SCREEN"):
                self.startScreen()

            elif (self.state == "PLANNING SCREEN"):
                self.planningScreen()
                
            # if event.type == pygame.QUIT:
            #     pygame.quit()
            #     sys.exit()
                

            
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         running = False
            # self.screen.blit(self.background, (0,0))
            # pygame.display.update()


    def startScreen(self):
        self.screen = pygame.display.set_mode((self.width, self.height), self.resizeable)
        self.background = pygame.image.load('assets/background.png')
        
        start_button = pygame.image.load('assets/start_button.png')
        start_size = start_button.get_size()
        rect = start_button.get_rect()
        # rect = pygame.draw.rect(self.screen,(0, 0, 255),(400, 0, 475, 600))


        self.screen.blit(start_button, (400, 475))
        
        while self.state == "START SCREEN" :
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN :
                    if mouse[0] > 478 and mouse[0] < 995 and mouse[1] > 403 and mouse[1] < 545:
                        self.state = "PLANNING SCREEN"
                if event.type == pygame.QUIT:
                    sys.exit(0)
            self.screen.blit(self.background, (0,0))
            self.screen.blit(start_button, (475,400))
            pygame.display.flip()

            

    def planningScreen(self):
        self.screen = pygame.display.set_mode((self.width, self.height), self.resizeable)
        self.background = pygame.image.load('assets/planning.png')
        # self.screen = pygame.transform.smoothscale(self.background, self.screen.get_size())


        while self.state == "PLANNING SCREEN":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.background, (0,0))
            pygame.display.flip()
