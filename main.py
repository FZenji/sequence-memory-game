import pygame
pygame.init()  # Start Pygame


def board_create(width=3, height=None):
    if height is None:
        height = width

    box_size = 75
    gap = 10
    boarder_x = (screen.get_width() - (width * (box_size + gap) - gap))/2
    boarder_y = (screen.get_height() - (height * (box_size + gap) - gap))/2

    return [pygame.Rect(boarder_x + (box_size + gap) * i,
                        boarder_y + (box_size + gap) * j,
                        box_size, box_size) for i in range(width) for j in range(height)]
    # for i in range(width):
    #     for j in range(height):
    #         sprites.append(pygame.Rect(boarder_x + (box_size + gap) * i,
    #                                    boarder_y + (box_size + gap) * j,
    #                                    box_size, box_size))


def draw(clicked):
    for i in sprites:
        pygame.draw.rect(screen, LIGHT_GREY, i)
    for j in clicked:
        pygame.draw.rect(screen, (255, 0, 0), j)


screen = pygame.display.set_mode((640, 480))  # Start the screen

GREY = (50, 50, 50)
LIGHT_GREY = (100, 100, 100)

sprites = board_create()
clicked_sprites = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # The user closed the window!
            running = False  # Stop running
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_sprites = [s for s in sprites if s.collidepoint(pygame.mouse.get_pos())]

    # Logic goes here
    draw(clicked_sprites)
    pygame.display.flip()

pygame.quit()  # Close the window
