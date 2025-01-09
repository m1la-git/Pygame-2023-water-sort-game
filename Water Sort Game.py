from copy import deepcopy
import random
import pygame


class Clock:
    def __init__(self, x, y, screen):
        self.screen = screen
        self.image = pygame.image.load('images/clock.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xx = x

    def update(self):
        self.xx += 0.05
        self.rect.x = self.xx
        self.screen.blit(self.image, self.rect)

    def check_collision(self, rect):
        return self.rect.colliderect(rect)


def generate_start():
    t_num = random.randint(10, 14)
    t_colors = []
    available_colors = []
    for i in range(t_num):
        t_colors.append([])
        if i < t_num - 2:
            for j in range(4):
                available_colors.append(i)
    for i in range(t_num - 2):
        for j in range(4):
            color = random.choice(available_colors)
            t_colors[i].append(color)
            available_colors.remove(color)
    return t_num, t_colors


def draw_tubes(tubes_num, tube_cols):
    t_boxes = []
    if tubes_num % 2 == 0:
        tubes_per_row = tubes_num // 2
        offset = False
    else:
        tubes_per_row = tubes_num // 2 + 1
        offset = True
    spacing = WIDTH / tubes_per_row
    for i in range(tubes_per_row):
        for j in range(len(tube_cols[i])):
            pygame.draw.rect(screen, colors[tube_cols[i][j]], [20 + spacing * i, 220 - (50 * j), 65, 50], 0, 3)
        box = pygame.draw.rect(screen, '#9c89b8', [20 + spacing * i, 70, 65, 200], 5, 0)
        if select_rect == i:
            pygame.draw.rect(screen, '#80ed99', [20 + spacing * i, 70, 65, 200], 3, 0)
        t_boxes.append(box)
    if offset:
        for i in range(tubes_per_row - 1):
            for j in range(len(tube_cols[i + tubes_per_row])):
                pygame.draw.rect(screen, colors[tube_cols[i + tubes_per_row][j]],
                                 [(spacing * 0.5) + 20 + spacing * i, 470 - (50 * j), 65, 50], 0, 3)
            box = pygame.draw.rect(screen, '#9c89b8', [(spacing * 0.5) + 20 + spacing * i, 320, 65, 200], 5, 0)
            if select_rect == i + tubes_per_row:
                pygame.draw.rect(screen, '#80ed99', [(spacing * 0.5) + 20 + spacing * i, 320, 65, 200], 3, 0)
            t_boxes.append(box)
    else:
        for i in range(tubes_per_row):
            for j in range(len(tube_cols[i + tubes_per_row])):
                pygame.draw.rect(screen, colors[tube_cols[i + tubes_per_row][j]], [5 + spacing * i,
                                                                                   450 - (50 * j), 65, 50], 0, 3)
            box = pygame.draw.rect(screen, '#9c89b8', [5 + spacing * i, 300, 65, 200], 5, 0)
            if select_rect == i + tubes_per_row:
                pygame.draw.rect(screen, '#80ed99', [5 + spacing * i, 300, 65, 200], 3, 0)
            t_boxes.append(box)
    return t_boxes


def calc_move(colors, selected_rect, destination, steps):
    chain = True
    color_on_top = 100
    length = 1
    color_to_move = 100
    if len(colors[selected_rect]) > 0:
        color_to_move = colors[selected_rect][-1]
        for i in range(1, len(colors[selected_rect])):
            if chain:
                if colors[selected_rect][-1 - i] == color_to_move:
                    length += 1
                else:
                    chain = False
    if 4 > len(colors[destination]):
        if len(colors[destination]) == 0:
            color_on_top = color_to_move
        else:
            color_on_top = colors[destination][-1]
    if color_on_top == color_to_move and selected_rect != destination:
        water_sound.play()
        steps += 1
        for i in range(length):
            if len(colors[destination]) < 4:
                if len(colors[selected_rect]) > 0:
                    colors[destination].append(color_on_top)
                    colors[selected_rect].pop(-1)
    return colors, steps


def check_victory(colors):
    won = True
    for i in range(len(colors)):
        if len(colors[i]) > 0:
            if len(colors[i]) != 4:
                won = False
            else:
                main_color = colors[i][-1]
                for j in range(len(colors[i])):
                    if colors[i][j] != main_color:
                        won = False
    return won


pygame.init()

WIDTH = 700
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Water Sort Game')
font = pygame.font.Font('fonts/font.otf', 40)
victory_font = pygame.font.Font('fonts/font.otf', 70)
timer = pygame.time.Clock()
colors = ['#283618', '#ff006e', '#8338ec', '#1d3557', '#e63946', '#6d6875', '#590d22', '#e76f51',
          '#00b4d8', '#76c893', '#ffb703', '#000814']
t_colors = []
init_colors = []

bg = pygame.transform.scale(pygame.image.load('images/bg.jpeg'), (1000, HEIGHT))
bg_x1 = 0
bg_x2 = -1000
clock = Clock(0, 530, screen)
end_img = pygame.transform.scale(pygame.image.load('images/end.png'), (50, 50))
end_rect = end_img.get_rect()
end_rect.x, end_rect.y = 630, 530

pygame.mixer.music.load('sounds/bg.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=-1)

water_sound = pygame.mixer.Sound('sounds/water.wav')
over_sound = pygame.mixer.Sound('sounds/over.wav')

tubes = 10
new_game = True
selected = False
tube_rects = []
select_rect = 100
win = False
win_sound = True
run = True
steps = 0
lose = False
while run:
    bg_x1 += 0.4
    if bg_x1 > 1000:
        bg_x1 = bg_x1 - 1000
    bg_x2 = bg_x1 - 1000
    screen.blit(bg, (bg_x1, 0))
    screen.blit(bg, (bg_x2, 0))
    timer.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                t_colors = deepcopy(init_colors)
            elif event.key == pygame.K_RETURN:
                new_game = True
                steps = 0
                if win or lose:
                    win = False
                    lose = False
                    clock = Clock(10, 530, screen)
                    pygame.mixer.music.play(loops=-1)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not selected:
                for item in range(len(tube_rects)):
                    if tube_rects[item].collidepoint(event.pos):
                        selected = True
                        select_rect = item
            else:
                for item in range(len(tube_rects)):
                    if tube_rects[item].collidepoint(event.pos):
                        dest_rect = item
                        t_colors, steps = calc_move(t_colors, select_rect, dest_rect, steps)
                        selected = False
                        select_rect = 100
    if win or lose:
        pygame.mixer.music.stop()
        if win_sound:
            over_sound.play()
            win_sound = False
        if win:
            text = 'You Won in ' + str(steps) + ' steps!'
        else:
            text = 'Time is up! You lost :('
        screen.blit(victory_font.render(text, True, '#001d3d'), (100, 200))
        screen.blit(victory_font.render('Press Enter', True, '#001d3d'), (100, 300))
    else:
        clock.update()
        screen.blit(end_img, end_rect)
        restart_text = font.render('Space-Restart, Enter-New Board!', True, '#001d3d')
        screen.blit(restart_text, (10, 10))
        screen.blit(font.render(str(steps) + ' steps', True, '#001d3d'), (600, 10))
        if new_game:
            tubes, t_colors = generate_start()
            init_colors = deepcopy(t_colors)
            new_game = False
        else:
            tube_rects = draw_tubes(tubes, t_colors)
        win = check_victory(t_colors)
        win_sound = win
        if not win and clock.check_collision(end_rect):
            lose = True
            win_sound = True
    pygame.display.flip()
pygame.quit()
