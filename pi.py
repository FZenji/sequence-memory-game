import pygame
import time
pygame.font.init()


def calc_pi(limit):  # Generator function
    """
    Prints out the digits of PI
    until it reaches the given limit
    """

    q, r, t, k, n, b = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
        if 4 * q + r - t < n * t:
            # yield digit
            yield n
            # insert period after first digit
            if counter == 0:
                yield '.'
            # end
            if decimal == counter:
                print('')
                break
            counter += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * b
            nn = (q * (7 * k) + 2 + (r * b)) // (t * b)
            q *= k
            t *= b
            b += 2
            k += 1
            n = nn
            r = nr


def pi_print(limit):  # Wrapper function
    # Calls CalcPi with the given limit
    pi_digits = calc_pi(int(limit))

    i = 0

    # Prints the output of calcPi generator function
    # Inserts a newline after every 40th number
    for d in pi_digits:
        print(d, end='')
        i += 1
        if i == 40:
            print("")
            i = 0


def pi_list(limit):
    l_pi = list(calc_pi(limit))
    return l_pi[:1] + l_pi[2:]


def board_create():
    box_size = 75
    gap = 10
    boarder_x = (screen.get_width() - (3 * (box_size + gap) - gap)) / 2
    boarder_y = (screen.get_height() - (4 * (box_size + gap) - gap)) / 2

    board = [pygame.Rect(boarder_x + (box_size + gap),
                         boarder_y + (box_size + gap) * 3,
                         box_size, box_size)]

    board += [pygame.Rect(boarder_x + (box_size + gap) * j,
                          boarder_y + (box_size + gap) * i,
                          box_size, box_size) for i in range(2, -1, -1) for j in range(3)]

    return board


def draw():
    for i in pad:
        pygame.draw.rect(screen, LIGHT_GREY, i)


def show_pi(c_digit):
    global off
    off = 0
    i = c_digit
    recurse = True
    while recurse:
        if pi[i] == pi[i-1]:
            off += 1
            i -= 1
        else:
            recurse = False
    pygame.draw.rect(screen, ((200 + 200 * off) % 255,
                              (70 + 70 * off) % 255,
                              (100 + 100 * off) % 255), pad[pi[c_digit]])
    digits_text = font_big.render("Digit: " + str(digit), False, (200, 30, 100))
    break_text = font_big.render("Break: " + str(brk), False, (200, 30, 100))
    hotkey_p = font_small.render("p = play", False, (200, 30, 100))
    hotkey_b = font_small.render("b = set break", False, (200, 30, 100))
    hotkey_e = font_small.render("e = end", False, (200, 30, 100))
    hotkey_r = font_small.render("r = start", False, (200, 30, 100))
    hotkey_a = font_small.render("a = quick back", False, (200, 30, 100))
    hotkey_d = font_small.render("d = quick advance", False, (200, 30, 100))
    hotkey_al = font_small.render("<- = back", False, (200, 30, 100))
    hotkey_ar = font_small.render("-> = advance", False, (200, 30, 100))
    screen.blit(digits_text, dest=((screen.get_width() // 2) - 73, 20))
    screen.blit(break_text, dest=(20, 20))
    screen.blit(hotkey_p, dest=(screen.get_width() - 180, 20))
    screen.blit(hotkey_b, dest=(screen.get_width() - 180, 40))
    screen.blit(hotkey_e, dest=(screen.get_width() - 180, 60))
    screen.blit(hotkey_r, dest=(screen.get_width() - 180, 80))
    screen.blit(hotkey_a, dest=(screen.get_width() - 180, 100))
    screen.blit(hotkey_d, dest=(screen.get_width() - 180, 120))
    screen.blit(hotkey_al, dest=(screen.get_width() - 180, 140))
    screen.blit(hotkey_ar, dest=(screen.get_width() - 180, 160))


screen = pygame.display.set_mode((640, 480))  # Start the screen
clock = pygame.time.Clock()
font_big = pygame.font.Font(pygame.font.get_default_font(), 36)
font_small = pygame.font.Font(pygame.font.get_default_font(), 18)
FPS = 30

GREY = (50, 50, 50)
LIGHT_GREY = (100, 100, 100)

off = 0
pad = board_create()
nos_digits = 1000
pi = pi_list(nos_digits)
digit = 762
play = False
brk = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # The user closed the window!
            running = False  # Stop running
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if digit + 1 < len(pi):
                    digit += 1
            if event.key == pygame.K_LEFT:
                if digit >= 1:
                    digit -= 1
            if event.key == pygame.K_r:
                digit = 0
            if event.key == pygame.K_e:
                digit = nos_digits
            if event.key == pygame.K_p:
                play = not play
            if event.key == pygame.K_b:
                brk = digit
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        if digit + 1 < len(pi):
            digit += 1
    if keys[pygame.K_a]:
        if digit >= 1:
            digit -= 1

    if play:
        if digit < brk:
            time.sleep(1)
            digit += 1
        else:
            play = not play

    # Logic goes here
    draw()
    show_pi(digit)
    pygame.display.flip()
    screen.fill((0, 0, 0))
    clock.tick(FPS)

pi_print(nos_digits)
pygame.quit()  # Close the window
