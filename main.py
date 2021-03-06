import sys
import pygame
import math
import tkinter as tk

def run():
    window = tk.Tk()

    def getval():
        global values
        values = [gravityslider.get(), frictionslider.get(), speedslider.get()]

    window.title("Control Panel!")

    val1 = tk.Label(text = "Gravity")
    val1.pack()
    global gravityslider
    gravityslider = tk.Scale( from_ = 0, to_ = 30, orient = tk.HORIZONTAL)
    gravityslider.pack()

    val2 = tk.Label(text = "Speed")
    val2.pack()
    global speedslider
    speedslider = tk.Scale(window, from_ = 0, to_ = 10, orient = tk.HORIZONTAL)
    speedslider.pack()

    val3 = tk.Label(text = "Friction")
    val3.pack()
    global frictionslider
    frictionslider = tk.Scale(window, from_ = 0, to_ = 10, orient = tk.HORIZONTAL)
    frictionslider.pack()

    donebutton = tk.Button( text = "Apply", command=getval)
    donebutton.pack()

    window.mainloop()

run()

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
        self.down_pressed = True
        self.mousefollow = False
        self.gravity = values[0]
        self.speed = values[2]
        self.terminalvel = 798.8
        self.friction = values[1]
    def draw(self, window):
        pygame.draw.rect(window, self.colour, self.mybox)
    def update(self):
        if self.friction >= self.speed:
            self.friction = self.speed
        self.dx = 0
        self.dy = 0
        if self.left_pressed and not self.right_pressed:
            self.dx = -self.speed + self.friction
        if self.right_pressed and not self.left_pressed:
            self.dx = self.speed - self.friction
        if self.up_pressed and not self.down_pressed:
            self.dy = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.dy = self.gravity
        
        self.x += self.dx
        self.y += self.dy

        if self.y <= 0:
            self.y = 0
        if self.x <= 0:
            self.x = 0
        if self.x >= 368:
            self.x = 368
        if self.y >= 328:
            self.y = 328
        elif self.y <= 328:
            if self.dy < self.terminalvel:
                self.dy += self.gravity
            self.down_pressed = True


        self.mybox = pygame.Rect(self.x, self.y, 32, 32)
    def restart(self):
        self.x = 200
        self.y = 200
    def drag(self):
        if self.mousefollow == True:
            self.x = pygame.mouse.get_pos()[0]
            self.y = pygame.mouse.get_pos()[1]
        else:
            pass

              

pygame.display.set_caption("Physics simulator")


player = Box(200, 200)

running = True

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
            if event.key == pygame.K_r:
                player.restart()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= player.x and pygame.mouse.get_pos()[0] <= (player.x + 32) and pygame.mouse.get_pos()[1] >= player.y and pygame.mouse.get_pos()[0] <= (player.x + 32):
                player.mousefollow = True
            else:
                pass
        if event.type == pygame.MOUSEBUTTONUP:
            player.mousefollow = False  

    window.fill(navy)
    player.draw(window)
    player.update()
    player.drag()
    pygame.draw.rect(window, dgreen, pygame.Rect(0, 360, 400, 40))
    pygame.display.flip()
    clock.tick(120)

