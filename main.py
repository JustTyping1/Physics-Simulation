import pygame

pygame.init()

blue = (0, 0, 255)
green = (0, 255, 0)

window = pygame.display.set_mode((300, 300))

pygame.display.set_caption("Physics simulator")
window.fill(blue)
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.draw.rect(window, green, pygame.Rect(30, 30, 60, 60))
                pygame.display.flip()

        if event.type == pygame.QUIT:
            running = False