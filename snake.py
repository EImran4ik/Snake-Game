import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (0, 255, 0)
RED = (255, 0, 0)

# Размер экрана
WIDTH, HEIGHT = 600, 400

# Размер блока и скорость змейки
BLOCK_SIZE = 20
SNAKE_SPEED = 15

# Инициализация экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простая змейка")

# Инициализация часов
clock = pygame.time.Clock()

# Инициализация начальных координат и направления змейки
snake = [{'x': WIDTH // 2, 'y': HEIGHT // 2}]
snake_dir = {'x': 0, 'y': 0}

# Инициализация координат яблока
apple = {'x': round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE,
         'y': round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_dir['x'] == 0:
                snake_dir = {'x': -BLOCK_SIZE, 'y': 0}
            elif event.key == pygame.K_RIGHT and snake_dir['x'] == 0:
                snake_dir = {'x': BLOCK_SIZE, 'y': 0}
            elif event.key == pygame.K_UP and snake_dir['y'] == 0:
                snake_dir = {'x': 0, 'y': -BLOCK_SIZE}
            elif event.key == pygame.K_DOWN and snake_dir['y'] == 0:
                snake_dir = {'x': 0, 'y': BLOCK_SIZE}

    # Изменение координат змейки
    new_head = {'x': snake[0]['x'] + snake_dir['x'], 'y': snake[0]['y'] + snake_dir['y']}
    snake.insert(0, new_head)

    # Проверка на столкновение с границами экрана
    if new_head['x'] >= WIDTH or new_head['x'] < 0 or new_head['y'] >= HEIGHT or new_head['y'] < 0:
        pygame.quit()
        quit()

    # Проверка на съедание яблока
    if new_head['x'] == apple['x'] and new_head['y'] == apple['y']:
        apple = {'x': round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE,
                 'y': round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE}
    else:
        snake.pop()

    # Очистка экрана
    screen.fill(BLACK)

    # Отрисовка яблока
    pygame.draw.rect(screen, RED, [apple['x'], apple['y'], BLOCK_SIZE, BLOCK_SIZE])

    # Отрисовка змейки
    for segment in snake:
        pygame.draw.rect(screen, WHITE, [segment['x'], segment['y'], BLOCK_SIZE, BLOCK_SIZE])

    # Обновление экрана
    pygame.display.update()

    # Ограничение скорости
    clock.tick(SNAKE_SPEED)
