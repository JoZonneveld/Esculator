from Color import *
import pygame 

def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

class Elevator:
    def __init__(self):
        pass

    def draw_elevator(self, screen, x, y):
        pygame.draw.rect(screen, hover_red, (x, y, 300, 25))

elevator = Elevator()

def program():
    pygame.init()

    width = 1024
    height = 768

    size = (width, height)

    screen = pygame.display.set_mode(size)
    
    while process_events():
        screen.fill(Deep_Sky_Blue)
        elevator.draw_elevator(screen, int(width*0.35), 700)
        pygame.display.flip()