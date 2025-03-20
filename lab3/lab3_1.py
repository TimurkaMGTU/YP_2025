import pygame
import sys


pygame.init()


width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Злой Смайлик")


yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)


def draw_angry_smiley():
    
    pygame.draw.circle(screen, yellow, (200, 200), 100)

    
    pygame.draw.circle(screen, red, (160, 170), 16)  
    pygame.draw.circle(screen, red, (240, 170), 16)  

    pygame.draw.circle(screen, black, (163, 170), 5)
    pygame.draw.circle(screen, black, (243, 170), 5)

    pygame.draw.line(screen, black, (140, 140), (180, 160), 10)  
    pygame.draw.line(screen, black, (220, 160), (260, 140), 10)  

    
    pygame.draw.line(screen, black, (150, 260), (260, 260),15)  


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  
    draw_angry_smiley()             

    pygame.display.flip()           
