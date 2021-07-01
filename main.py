import pygame
#from models import tech_obj_list, persons_list, questions_list
import os
"""Lost Little Holbie pygame script"""

# Window variables
WIDTHB, HEIGHTB = 1200, 800
WIN = pygame.display.set_mode((WIDTHB, HEIGHTB))
pygame.display.set_caption('Lost lil\' holbie')
FPS = 60

# Object variables
Q_X, Q_Y = 150, 150

# BACKGROUND_IMG = pygame.image.load(os.path.join('assets', 'gameboard.PNG'))
# DEREK_Q = pygame.image.load(os.path.join('assets', 'text_derek.PNG'))
BACKGROUND_IMG = pygame.image.load('C:\\Users\Kyle\Documents\HackSprint\\assets\images\gameboard\gameboard.PNG')
DEREK_Q = pygame.transform.scale(pygame.image.load('C:\\Users\Kyle\Documents\HackSprint\\assets\images\\textbox_objs\\text_software.PNG'), (400, 200))

def draw_window():
    """Draws game window"""
    WIN.blit(BACKGROUND_IMG, (0, 0))
    WIN.blit(DEREK_Q, (75, 75))
    pygame.display.update()


def main():
    """Contains game loop"""
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()