import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Дом с призраком и облаками")

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

    # Белый круг в верхней правой части (луна)
    pygame.draw.circle(screen, WHITE, (width - 100, 100), 50)

# Функция для рисования дома
def draw_house(x, y):
    # Основание дома
    house_width = 400
    house_height = 300
    pygame.draw.rect(screen, GRAY, (x, y, house_width, house_height))

    # Балкон между первым и вторым этажом
    balcony_height = 30
    pygame.draw.rect(screen, DARK_GRAY, (x, y + house_height // 2 - balcony_height // 2, house_width, balcony_height))

    # Окна на первом этаже
    window_width = 80
    window_height = 70
    # Левые коричневые окна
    pygame.draw.rect(screen, BROWN, (x + 20, y + house_height // 2 + 10, window_width, window_height))
    pygame.draw.rect(screen, BROWN, (x + 120, y + house_height // 2 + 10, window_width, window_height))
    # Правое желтое окно
    pygame.draw.rect(screen, YELLOW, (x + house_width - window_width - 20, y + house_height // 2 + 10, window_width, window_height))

    # Окна на втором этаже
    second_floor_window_width = 80
    second_floor_window_height = house_height // 2 - balcony_height // 2 - 10
    for i in range(4):
        pygame.draw.rect(screen, BEIGE, (x + 20 + i * (second_floor_window_width + 20), y + 20, second_floor_window_width, second_floor_window_height))

    # Крыша в виде трапеции
    roof_top_width = 300
    roof_bottom_width = house_width
    roof_height = 100
    roof_points = [
        (x + (house_width - roof_top_width) // 2, y - roof_height),
        (x + (house_width - roof_top_width) // 2 + roof_top_width, y - roof_height),
        (x + house_width, y),
        (x, y)
    ]
    pygame.draw.polygon(screen, BLACK, roof_points)

    # Трубы на крыше
    pipe_width = 20
    pipe_height = 50
    # Три трубы
    pygame.draw.rect(screen, BLACK, (x + 50, y - roof_height - pipe_height, pipe_width, pipe_height))
    pygame.draw.rect(screen, BLACK, (x + house_width // 2 - pipe_width // 2, y - roof_height - pipe_height, pipe_width, pipe_height))
    pygame.draw.rect(screen, BLACK, (x + house_width - 70, y - roof_height - pipe_height, pipe_width, pipe_height))

# Функция для рисования призрака
def draw_ghost(x, y):
    # Тело призрака (форма амебы)
    pygame.draw.ellipse(screen, WHITE, (x, y, 150, 200))  # Основное тело
    pygame.draw.ellipse(screen, WHITE, (x - 30, y + 50, 60, 100))  # Левая "волна"
    pygame.draw.ellipse(screen, WHITE, (x + 120, y + 50, 60, 100))  # Правая "волна"

    # Глаза
    eye_radius = 20
    pupil_radius = 10
    # Левый глаз
    pygame.draw.circle(screen, BLUE, (x + 50, y + 80), eye_radius)
    pygame.draw.circle(screen, BLACK, (x + 50, y + 80), pupil_radius)
    # Правый глаз
    pygame.draw.circle(screen, BLUE, (x + 100, y + 80), eye_radius)
    pygame.draw.circle(screen, BLACK, (x + 100, y + 80), pupil_radius)

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отрисовка фона
    draw_background()

    # Рисование дома (размещён левее)
    draw_house(10, 200)  # Позиция дома (x, y)

    # Рисование призрака
    draw_ghost(500, 300)  # Позиция призрака (x, y)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
