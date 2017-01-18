from Color import *
import pygame 

def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

class Elevator:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def draw_elevator(self, screen):
        pygame.draw.rect(screen, red, (self.X, self.Y, 300, 25))
        
    def draw_floor(self,screen, x, y, b, h):
        pygame.draw.rect(screen, green, (x, y, b, h))
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        
            

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.Y -= 1
            print("up")
        elif keys[pygame.K_DOWN]:
            self.Y += 1
            print("down")
        
        
        

elevator = Elevator(300, 700)

def program():
    pygame.init()

    width = 1024
    height = 768

    size = (width, height)

    screen = pygame.display.set_mode(size)
    
    while process_events():
        elevator.update()
        pygame.display.set_caption('Esculator')
        screen.fill(Deep_Sky_Blue)
        elevator.draw_elevator(screen)
        elevator.draw_floor(screen, 650, 125, 50, 600)
        pygame.display.flip()