import pygame
import random
import time
pygame.init()  # Start Pygame


def board_create(width=3, height=None):
    if height is None:
        height = width

    box_size = 75
    gap = 10
    boarder_x = (screen.get_width() - (width * (box_size + gap) - gap))/2
    boarder_y = (screen.get_height() - (height * (box_size + gap) - gap))/2

    board = [pygame.Rect(boarder_x + (box_size + gap) * i,
                         boarder_y + (box_size + gap) * j,
                         box_size, box_size) for i in range(height) for j in range(width)]

    sprite2num = {tuple(s): n for n, s in enumerate(board)}
    num2sprite = {n: s for n, s in enumerate(board)}

    return board, sprite2num, num2sprite


def draw(clicked):
    for i in sprites:
        pygame.draw.rect(screen, LIGHT_GREY, i)
    for j in clicked:
        pygame.draw.rect(screen, GREY, j)


def show_pattern():
    new = True
    while new:
        pattern.append(random.randint(0, 8))
        try:
            if pattern[-1] != pattern[-2]:
                new = False
        except IndexError:
            pass
    for i in pattern:
        draw([])
        pygame.draw.rect(screen, (255, 0, 0), sprites[i])
        pygame.display.flip()
        time.sleep(0.5)
    #print(pattern)


screen = pygame.display.set_mode((640, 480))  # Start the screen

GREY = (50, 50, 50)
LIGHT_GREY = (100, 100, 100)

sprites, sprite_to_number, number_to_sprite = board_create()
clicked_sprites = []
clicked_order = []
pattern = []
round_done = True
round_counter = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # The user closed the window!
            running = False  # Stop running
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_sprites = [s for s in sprites if s.collidepoint(pygame.mouse.get_pos())]
            if len(clicked_sprites) != 0:
                clicked_order.append(sprite_to_number[tuple(clicked_sprites[0])])

    # Logic goes here
    draw(clicked_sprites)
    #print(clicked_order)
    if round_done:
        show_pattern()
        clicked_sprites = []
        clicked_order = []
        round_done = False

    if clicked_order == pattern[:len(clicked_order)+1]:
        time.sleep(0.5)
        round_counter += 1
        round_done = True

    if clicked_order != pattern[:len(clicked_order)]:
        running = False

    if len(clicked_order) >= len(pattern):
        clicked_order = clicked_order[:len(clicked_order)]
    pygame.display.flip()

print(round_counter)
print(clicked_order)
print(pattern)
pygame.quit()  # Close the window
