import pygame
pygame.init()  # Start Pygame

screen = pygame.display.set_mode((640, 480))  # Start the screen
sprites = []
GREY = (50, 50, 50)


def draw(width=3, height=None):
    box_size = 20
    boarder = 0
    gap = 5

    if height is None:
        height = width
    for i in range(width):
        for j in range(height):
            pygame.draw.rect(screen, GREY, (boarder + (box_size + gap)*i,
                                            boarder + (box_size + gap)*j,
                                            box_size, box_size))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # The user closed the window!
            running = False  # Stop running
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_sprites = [s for s in sprites if s.rect.collidepoint(pygame.mouse.get_pos())]
    # Logic goes here
    draw(3)
    pygame.display.flip()

pygame.quit()  # Close the window
