from cmath import rect
import pygame

pygame.init()

global teal
teal = (2, 245, 208)
global navy
navy = (4, 1, 66)
global dgreen
dgreen = (0, 64, 0)

clock = pygame.time.Clock()

window = pygame.display.set_mode((400, 400))

class Box():
    def __init__(self, x, y):
        mybox = pygame.Rect(x, y, 32, 32)
        self.mybox = mybox
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.colour = teal
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
    def draw(self, window):
        pygame.draw.rect(window, self.colour, self.mybox)
    def update(self):
        self.dx = 0
        self.dy = 0
        if self.left_pressed and not self.right_pressed:
            self.dx = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.dx = self.speed
        if self.up_pressed and not self.down_pressed:
            self.dy = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.dy = self.speed
        
        self.x += self.dx
        self.y += self.dy

        self.mybox = pygame.Rect(self.x, self.y, 32, 32)
    
        

pygame.display.set_caption("Physics simulator")


player = Box(200, 200)

running = True

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False

    window.fill(navy)
    player.draw(window)
    player.update()
    pygame.draw.rect(window, dgreen, pygame.Rect(0, 360, 400, 40))
    pygame.display.flip()
    clock.tick(120)

