import pygame
from sys import exit
from random import randint


pygame.init()

bg = pygame.image.load('images/b_spring.png')
screen = pygame.display.set_mode((640,480))

pygame.mixer.music.set_volume(0.15)
bg_music = pygame.mixer.music.load('audios/metamorphosis.wav')
pygame.mixer.music.play(-1)

collision_sound = pygame.mixer.Sound('audios/crunch.wav')
collision_sound.set_volume(0.3)

width = 640
height = 480

x_snake = width // 2
y_snake = height // 2

speed = 5
x_control = speed
y_control = 0

x_apple = randint(40, 600)
y_apple = randint(50, 430)

points = 0

font = pygame.font.SysFont('courier new', 20, True, False)

arena = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake-Butterfly')
pace = pygame.time.Clock()
snake_list = []
inicial_size = 5
gameover = False

def snake_grow(snake_list):
    for XeY in snake_list:
        pygame.draw.rect(arena, (0,0,0), (XeY[0], XeY[1], 20, 20))
    
def restart_game():
    global points, inicial_size, x_snake, y_snake, snake_list, head_list, x_apple, y_apple, gameover
    points = 0
    inicial_size = 5
    x_snake = width // 2
    y_snake = height // 2
    snake_list = []
    head_list = []
    x_apple = randint(40, 600)
    y_apple = randint(50, 430)
    gameover = False

while True:    
    screen.blit(bg, (0, 0))
    pace.tick(20)

    message = f'Pontos: {points}'

    text_points = font.render(message, True, (0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x_control == speed:
                    pass
                else:
                    x_control = -speed
                    y_control = 0
            
            if event.key == pygame.K_RIGHT:
                if x_control == -speed:
                    pass
                else:
                    x_control = speed
                    y_control = 0
                
            if event.key == pygame.K_UP:
                if y_control == speed:
                    pass
                else:
                    x_control = 0
                    y_control = -speed
                    
            if event.key == pygame.K_DOWN:
                if y_control == -speed:
                    pass
                else:
                    x_control = 0
                    y_control = speed

    x_snake = x_snake + x_control
    y_snake = y_snake + y_control

    snake = pygame.draw.rect(arena, (0,255,0), (x_snake, y_snake, 20, 20))
    apple = pygame.draw.circle(arena, (255,0,50), (x_apple, y_apple), 8)

    if snake.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 430)
        points = points + 1
        collision_sound.play()
        inicial_size = inicial_size + 1

    head_list = []
    head_list.append(x_snake)
    head_list.append(y_snake)

    snake_list.append(head_list)

    if snake_list.count(head_list) > 1:
        fonte2 = pygame.font.SysFont('courier new', 20, True, True)
        message = 'Game Over! Pressione R para jogar novamente'
        text_points = fonte2.render(message, True, (0,0,0))
        ret_text = text_points.get_rect()

        gameover = True
        while gameover:
            arena.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        restart_game()

            ret_text.center = (width//2, height//2)
            arena.blit(text_points, ret_text)
            pygame.display.update()

    if x_snake > width:
        x_snake = 0
    if x_snake < 0:
        x_snake = width
    if y_snake < 0:
        y_snake = height
    if y_snake > height:
        y_snake = 0

    if len(snake_list) > inicial_size:
        del snake_list[0]

    snake_grow(snake_list)

    arena.blit(text_points, (500, 20))
    
    pygame.display.update()