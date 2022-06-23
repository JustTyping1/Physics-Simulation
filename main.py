import pygame

blue = (0, 0, 255)

window = pygame.display.set_mode((300, 300))

pygame.display.set_caption("Physics simulator")
window.fill(blue)
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():      
        if event.type == pygame.QUIT:
            running = False