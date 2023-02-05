import pygame
import sys
import json

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

            elif(self.state == "LAST SCREEN"):
                self.lastScreen()
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
        # rect = start_button.get_rect()
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
        self.background = pygame.image.load('assets/planning.png')

        enter_button = pygame.image.load('assets/enterButton3.png')
        enter_size = enter_button.get_size()

        
        self.screen.blit(self.background, (0,0))
        self.screen.blit(enter_button, (400,700))
        pygame.display.flip()

        base_font = pygame.font.Font(None, 32)
        user_text1 = ''
        user_text2 = ''
        user_text3 = ''
        #(x-coords and y coords of the top-left corner, followed by the width and height)
        input_rect1 = pygame.Rect(600,332,400,50)
        input_rect2 = pygame.Rect(512,412,400,50)
        input_rect3 = pygame.Rect(875,600,400, 50)

        rec1 = False
        rec2 = False
        rec3 = False


        # color_active = pygame.Color.r
        # color_passive = pygame.Color.g
        # color = color_passive
        
        # active = False

        while self.state == "PLANNING SCREEN":
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # 493,703 -- 605, 805
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse[0] > 493 and mouse[0] < 703 and mouse[1] > 605 and mouse[1] < 805:
                        self.state = "LAST SCREEN"
                    if input_rect1.collidepoint(event.pos):
                        rec1 = True
                        rec2 = False
                        rec3 = False
                        # active = True
                    if input_rect2.collidepoint(event.pos):
                        rec1 = False
                        rec2 = True
                        rec3 = False
                        # active = True
                    if input_rect3.collidepoint(event.pos):
                        rec1 = False
                        rec2 = False
                        rec3 = True
                    # else:
                    #     active = False
                if rec1 == True:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text1 = user_text1[:-1]
                        else:
                            user_text1 += event.unicode
                if rec2 == True:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text2 = user_text2[:-1]
                        else:
                            user_text2 += event.unicode
                if rec3 == True:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text3 = user_text3[:-1]
                        else:
                            user_text3 += event.unicode
                            
                print(user_text1, user_text2, user_text3)

            # if active:
            #     color = color_active
            # else:
            #     color = color_passive

            pygame.draw.rect(self.screen, (253, 219, 209), input_rect1)
            pygame.draw.rect(self.screen, (253, 219, 209), input_rect2)
            pygame.draw.rect(self.screen, (253, 219, 209), input_rect3)

            if rec1 == True:
                text_surface1 = base_font.render(user_text1, True, (131,115,230))
                self.screen.blit(text_surface1, (600,350))
                input_rect1.w = max(100, text_surface1.get_width()+10)
            
            if rec2 == True:
                text_surface2 = base_font.render(user_text2, True, (131,115,230))
                self.screen.blit(text_surface2, (515,415))
                input_rect2.w = max(100, text_surface2.get_width()+10)

            if rec3 == True:
                text_surface3 = base_font.render(user_text3, True, (131,115,230))
                self.screen.blit(text_surface3, (875,600))
                input_rect3.w = max(100, text_surface3.get_width()+10)

            ##self.text_strings = user_text1 + " , " + user_text2 + " , " + user_text3
            ##print(self.text_strings)

            pygame.display.flip()

    # def saveEvents(events):
    #     fptr = open("etc/events.json" , "w")
    #     json.dump(events, fptr)
    #     fptr.close()

    # def displayEvents(self):
    #     try:
    #         fptr = open("etc/events.json" , "r")
    #         events = json.load(fptr)
    #     except FileNotFoundError:
    #         events = []
    #     fptr.close()
    #     return sorted(events)

    # events = self. displayEvents()
    # events.append(self.text_strings)

    def lastScreen(self):
        self.background = pygame.image.load('assets/thirdscreen.png')
        
        
        while self.state == "LAST SCREEN" :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            self.screen.blit(self.background, (0,0))
            pygame.display.flip()

