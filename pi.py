import pygame


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
    if pi[c_digit] == pi[c_digit-1]:
        off += 70
        print(off)
        print((200+off) % 255, (70+off) % 255, (100+off) % 255)
    else:
        col_off = 0
    pygame.draw.rect(screen, ((200+off) % 255, (70+off) % 255, (100+off) % 255), pad[pi[c_digit]])


screen = pygame.display.set_mode((640, 480))  # Start the screen

GREY = (50, 50, 50)
LIGHT_GREY = (100, 100, 100)

global off
off = 0
pad = board_create()
nos_digits = 200
pi = pi_list(nos_digits)
digit = 150

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

    # Logic goes here

    draw()
    show_pi(digit)
    pygame.display.flip()

pi_print(nos_digits)
pygame.quit()  # Close the window
