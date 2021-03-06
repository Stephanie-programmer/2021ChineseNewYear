import pygame

BULL_BG_COLOR = (0.8471 * 255, 0.22157 * 255, 0.1765 * 255)
LION_BG_COLOR = (0.8471 * 255, 0.1020 * 255, 0.2039 * 255)
SCREEN_SIZE = (int(800 * 1.5), int(450 * 1.5))

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
font = pygame.font.Font('YSHaoShenTi-2.ttf', 100)
FONT_COLOR = (255, 207, 64)

GREETING = u"新春快乐"
GREETING_POS = (SCREEN_SIZE[0] / 2.7, SCREEN_SIZE[1] * 3 / 4)

should_lion_appear = False
lion_image = pygame.image.load("lion_middle.jpg")
lion_image = pygame.transform.scale(lion_image, (lion_image.get_width() // 3, lion_image.get_height() // 3))
LION_POS = ((SCREEN_SIZE[0] - lion_image.get_width()) / 2, (SCREEN_SIZE[1] - lion_image.get_height()) / 8)

bull_l_image = pygame.image.load("bull_left.jpeg")
bull_l_image = pygame.transform.scale(bull_l_image, (bull_l_image.get_width() // 5, bull_l_image.get_height() // 5))
bull_l_pos = (0, (SCREEN_SIZE[1] - bull_l_image.get_height()) / 2)

bull_r_image = pygame.image.load("bull_right.jpg")
bull_r_image = pygame.transform.scale(bull_r_image, (bull_r_image.get_width() // 5, bull_r_image.get_height() // 5))
bull_r_pos = (SCREEN_SIZE[0] - bull_l_image.get_width(), (SCREEN_SIZE[1] - bull_l_image.get_height()) / 2)

# pbg: partial background
pbg_bull_l_image = pygame.image.load("pbg_bull_left.png")
pbg_bull_l_image = pygame.transform.scale(pbg_bull_l_image,
                                          (pbg_bull_l_image.get_width() // 5, pbg_bull_l_image.get_height() // 5))

pbg_bull_r_image = pygame.image.load("pbg_bull_right.png")
pbg_bull_r_image = pygame.transform.scale(pbg_bull_r_image,
                                          (pbg_bull_r_image.get_width() // 5, pbg_bull_r_image.get_height() // 5))
# offset to the left and right side
pbg_bull_offset = 30
pbg_bull_rotate_angle = 0
pbg_bull_rotate_direction = "l"
pbg_bull_l_image_rot = pbg_bull_l_image
pbg_bull_r_image_rot = pbg_bull_r_image

rotation_offset = 20


def draw():
    if should_lion_appear:
        screen.fill(LION_BG_COLOR)
        screen.blit(lion_image, LION_POS)  # draw lion in the middle
        greeting = font.render(GREETING, True, FONT_COLOR)
        screen.blit(greeting, GREETING_POS)
        screen.blit(pbg_bull_l_image_rot, pbg_bull_l_image_rot.get_rect(
            center=pbg_bull_l_image.get_rect(topleft=(pbg_bull_offset,
                                             (SCREEN_SIZE[1] - bull_l_image.get_height()) / 2)).center).topleft)
        screen.blit(pbg_bull_r_image_rot, pbg_bull_r_image_rot.get_rect(
            center=pbg_bull_r_image.get_rect(topleft=(
            SCREEN_SIZE[0] - bull_r_image.get_width() - pbg_bull_offset,
            (SCREEN_SIZE[1] - bull_r_image.get_height()) / 2)).center).topleft)
    else:
        screen.fill(BULL_BG_COLOR)
        screen.blit(bull_l_image, bull_l_pos)
        screen.blit(bull_r_image, bull_r_pos)


def update(t_elaps):
    global bull_r_pos, bull_l_pos, should_lion_appear
    bull_r_pos = (bull_r_pos[0] - t_elaps / 10, bull_r_pos[1])
    bull_l_pos = (bull_l_pos[0] + t_elaps / 10, bull_l_pos[1])
    if bull_r_pos[0] - bull_l_pos[0] < bull_l_image.get_width():
        should_lion_appear = True
    if should_lion_appear:
        global pbg_bull_l_image, pbg_bull_r_image, pbg_bull_rotate_angle, pbg_bull_rotate_direction
        global pbg_bull_l_image_rot, pbg_bull_r_image_rot
        if pbg_bull_rotate_angle > rotation_offset and pbg_bull_rotate_direction == "r":
            pbg_bull_rotate_angle -= t_elaps/15
            pbg_bull_rotate_direction = "l"
        elif pbg_bull_rotate_angle < -1*rotation_offset and pbg_bull_rotate_direction == "l":
            pbg_bull_rotate_angle += t_elaps/15
            pbg_bull_rotate_direction = "r"
        else:
            if pbg_bull_rotate_direction == "r":
                pbg_bull_rotate_angle += t_elaps/15
            else:
                pbg_bull_rotate_angle -= t_elaps/15
        pbg_bull_l_image_rot = pygame.transform.rotate(pbg_bull_l_image, pbg_bull_rotate_angle)
        pbg_bull_r_image_rot = pygame.transform.rotate(pbg_bull_r_image, -1 * pbg_bull_rotate_angle)


running = True
t_pre = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    t_cur = pygame.time.get_ticks()
    update(t_cur - t_pre)
    t_pre = t_cur
    draw()
    pygame.display.update()
