import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Дома и призраки")

# Цвета
LIGHT_GRAY = (200, 200, 200)  # Светло-серый
BLACK = (0, 0, 0)  # Черный
WHITE = (255, 255, 255)  # Белый
GRAY = (128, 128, 128)  # Серый
DARK_GRAY = (64, 64, 64)  # Темно-серый
YELLOW = (255, 255, 0)  # Желтый
BROWN = (139, 69, 19)  # Коричневый
BEIGE = (245, 245, 220)  # Бежевый
BLUE = (0, 0, 255)  # Голубой
LIGHT_GRAY_GHOST = (180, 180, 180, 128)  # Светло-серый для призрака (с прозрачностью)

# Функция для рисования фона
def draw_background():
    # Верхняя половина светло-серого цвета
    screen.fill(LIGHT_GRAY, (0, 0, width, height // 2))
    # Нижняя половина черного цвета
    screen.fill(BLACK, (0, height // 2, width, height // 2))

    # Облака (овалы темно-серого и серого цветов)
    pygame.draw.ellipse(screen, DARK_GRAY, (100, 50, 200, 80))  # Темно-серое облако
    pygame.draw.ellipse(screen, GRAY, (400, 80, 250, 90))      # Серое облако
    pygame.draw.ellipse(screen, DARK_GRAY, (600, 40, 150, 70))  # Темно-серое облако

    # Луна (белый круг за облаками)
    pygame.draw.circle(screen, WHITE, (width - 100, 100), 50)

# Функция для рисования дома
def draw_house(x, y, scale=1.0):
    house_width = int(400 * scale)
    house_height = int(300 * scale)
    balcony_height = int(20 * scale)
    window_width = int(80 * scale)
    window_height = int(100 * scale)
    second_floor_window_width = int(80 * scale)
    second_floor_window_height = int((house_height // 2 - balcony_height // 2 - 10) * scale)
    roof_top_width = int(300 * scale)
    roof_height = int(100 * scale)
    pipe_width = int(20 * scale)
    pipe_height = int(50 * scale)

    # Основание дома
    pygame.draw.rect(screen, GRAY, (x, y, house_width, house_height))

    # Балкон между первым и вторым этажом
    pygame.draw.rect(screen, DARK_GRAY, (x, y + house_height // 2 - balcony_height // 2, house_width, balcony_height))

    # Перила на балконе
    railing_height = int(10 * scale)
    pygame.draw.rect(screen, BLACK, (x, y + house_height // 2 - balcony_height // 2 - railing_height, house_width, railing_height))

    # Окна на первом этаже
    pygame.draw.rect(screen, BROWN, (x + int(20 * scale), y + house_height // 2 + int(10 * scale), window_width, window_height))
    pygame.draw.rect(screen, BROWN, (x + int(120 * scale), y + house_height // 2 + int(10 * scale), window_width, window_height))
    pygame.draw.rect(screen, YELLOW, (x + house_width - window_width - int(20 * scale), y + house_height // 2 + int(10 * scale), window_width, window_height))

    # Окна на втором этаже
    for i in range(4):
        pygame.draw.rect(screen, BEIGE, (x + int(20 * scale) + i * (second_floor_window_width + int(20 * scale)), y + int(20 * scale), second_floor_window_width, second_floor_window_height))

    # Крыша в виде трапеции
    roof_points = [
        (x + (house_width - roof_top_width) // 2, y - roof_height),
        (x + (house_width - roof_top_width) // 2 + roof_top_width, y - roof_height),
        (x + house_width, y),
        (x, y)
    ]
    pygame.draw.polygon(screen, BLACK, roof_points)

    # Трубы на крыше
    pygame.draw.rect(screen, BLACK, (x + int(30 * scale), y - roof_height - pipe_height - int(20 * scale), pipe_width + int(10 * scale), pipe_height + int(20 * scale)))
    pygame.draw.rect(screen, BLACK, (x + house_width // 2 - pipe_width // 2, y - roof_height - pipe_height, pipe_width, pipe_height))
    pygame.draw.rect(screen, BLACK, (x + house_width - int(70 * scale), y - roof_height - pipe_height, pipe_width, pipe_height))

# Функция для рисования призрака
def draw_ghost(x, y, scale=1.0):
    ghost_surface = pygame.Surface((int(150 * scale), int(200 * scale)), pygame.SRCALPHA)
    ghost_surface.fill((0, 0, 0, 0))  # Прозрачный фон

    # Тело призрака (форма плаща)
    pygame.draw.ellipse(ghost_surface, (*LIGHT_GRAY_GHOST[:3], 128), (0, 0, int(150 * scale), int(200 * scale)))
    # "Волны" плаща
    pygame.draw.ellipse(ghost_surface, (*LIGHT_GRAY_GHOST[:3], 128), (int(-30 * scale), int(150 * scale), int(60 * scale), int(80 * scale)))
    pygame.draw.ellipse(ghost_surface, (*LIGHT_GRAY_GHOST[:3], 128), (int(120 * scale), int(150 * scale), int(60 * scale), int(80 * scale)))

    # Глаза
    eye_radius = int(15 * scale)
    pupil_radius = int(7 * scale)
    pygame.draw.circle(ghost_surface, BLUE, (int(50 * scale), int(80 * scale)), eye_radius)
    pygame.draw.circle(ghost_surface, BLACK, (int(50 * scale), int(80 * scale)), pupil_radius)
    pygame.draw.circle(ghost_surface, BLUE, (int(100 * scale), int(80 * scale)), eye_radius)
    pygame.draw.circle(ghost_surface, BLACK, (int(100 * scale), int(80 * scale)), pupil_radius)

    screen.blit(ghost_surface, (x, y))

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отрисовка фона
    draw_background()

    # Рисование трёх домов
    draw_house(10, 300, 0.6)  
    draw_house(260, 270, 0.5)  
    draw_house(560, 200, 0.6)  

    # Рисование шести призраков
    draw_ghost(500, 430, 0.5)  # Призрак 1
    draw_ghost(200, 350, 0.4)  # Призрак 2
    draw_ghost(700, 290, 0.3)  # Призрак 3
    draw_ghost(550, 500, 0.6)  # Призрак 4
    draw_ghost(350, 450, 0.5)  # Призрак 5
    draw_ghost(150, 400, 0.4)  # Призрак 6

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
