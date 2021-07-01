import pygame
from models.Logit import logit
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

BACKGROUND_IMG = pygame.image.load(os.path.join('Assets/images/gameboard', 'gameboard.PNG'))
START_1 = pygame.image.load(os.path.join('Assets/images/gameboard', 'welcome_1.PNG'))
START_2 = pygame.image.load(os.path.join('Assets/images/gameboard', 'welcome_2.PNG'))
START_3 = pygame.image.load(os.path.join('Assets/images/gameboard', 'welcome_3.PNG'))
INSTRUCTION_IMG = pygame.image.load(os.path.join('Assets/images/gameboard', 'welcome_3.PNG'))

# instruction = pygame.image.load(os.path.join('Assets/images/textbox_objs', 'text_instruct.PNG'))

DEREK_Q = pygame.image.load(os.path.join('Assets/images/textbox_objs', 'text_derek.PNG'))
# BACKGROUND_IMG = pygame.image.load('/Users/anthonyarmour/VS_Code_Folders/HackSprint/assets/images/gameboard/gameboard.PNG')
# DEREK_Q = pygame.transform.scale(pygame.image.load('/Users/anthonyarmour/VS_Code_Folders/HackSprint/assets/images/textbox_objs/text_derek.PNG'), (400, 200))



# PRAC = pygame.transform.scale(pygame.image.load(os.path.join('Assets/images/textbox_objs', 'text_derek.PNG')), (300, 100))
START_BUTTON = pygame.Rect(475, 600, 300, 100)


def draw_window(screen):
    """Draws game window"""
    if screen == "start":
        WIN.blit(START_1, (0, 0))
    elif screen == "start_2":
        WIN.blit(START_2, (0, 0))
    elif screen == "start_3":
        WIN.blit(START_3, (0, 0))
    elif screen == "instruction":
        WIN.blit(START_1, (0, 0))
    elif screen == "background":
        WIN.blit(BACKGROUND_IMG, (0, 0))
        WIN.blit(DEREK_Q, (75, 75))
    pygame.display.update()

def clicked(event, screen):
    """Determines whats clicked and decides actions"""
    if screen == "start":
        if START_BUTTON.collidepoint(event.pos):
            return "start_2"
    elif screen == "start_2":
        return "start_3"
    elif screen == "start_3":
        return "instruction"
    elif screen == "instruction":
        return "background"
    return screen


def main():
    """Contains game loop"""
    run = True
    clock = pygame.time.Clock()
    screen = "start"

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    screen = clicked(event, screen)

            draw_window(screen)

    pygame.quit()


if __name__ == '__main__':
    main()