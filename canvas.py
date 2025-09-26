import pygame
from globals import SCREEN_SIZE, FPS

class Canvas: 
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption("Canvas")
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock() 
        self.running = True
    def run(self): 
        while(self.running):
            self.handle_eventsl()
            self.update()
            self.render()
    def handle_eventsl(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    def update(self): 
        pass
    def render(self):
        self.screen.fill((0, 0, 0)) 
        pygame.display.flip() 
        self.clock.tick(FPS)