import pygame
from models.Logit import logit
import random
from models import persons_list, tech_obj_list, questions_list
#from models import tech_obj_list, persons_list, questions_list
import os
"""Lost Little Holbie pygame script"""

questions_list[0].active = True
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


def draw_window(screen, obj_list, question):
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
        WIN.blit(question.image, (75, 75))
        WIN.blit(obj_list[0].image_1, (200, 500))
        WIN.blit(obj_list[1].image_1, (500, 500))
        WIN.blit(obj_list[2].image_1, (800, 500))
    pygame.display.update()

def blit_objs():
    temp_persons = persons_list.copy()
    temp_tech_objs = tech_obj_list.copy()
    for x, question in enumerate(questions_list):
        if question.active == True:
            for x, person in enumerate(temp_persons):
                if question.name_id == person.name:
                    logit("should be derek->  " + str(person.name))
                    people = []
                    people.append(person)
                    temp_persons.pop(x)
                    while True:
                        obj = random.choice(temp_persons)
                        if obj not in people:
                            people.append(obj)
                        if len(people) == 3:
                            break
                    return random.sample(people, 3), question
            for x, tech_obj in enumerate(temp_tech_objs):
                if question.name_id == tech_obj.name:
                    tech_objs = []
                    tech_objs.append(tech_obj)
                    temp_tech_objs.pop(x)
                    while True:
                        obj = random.choice(temp_tech_objs)
                        if obj not in tech_objs:
                            tech_objs.append(obj)
                        if len(tech_objs) == 3:
                            break
                    return random.sample(tech_objs, 3), question


def clicked(event, screen, obj_list, question):
    """Determines whats clicked and decides actions"""
    if screen == "start":
        if START_BUTTON.collidepoint(event.pos):
            return "start_2", None, None
    elif screen == "start_2":
        return "start_3", None, None
    elif screen == "start_3":
        return "instruction", None, None
    elif screen == "instruction":
        obj_list, question = blit_objs()
        return "background", obj_list, question
    elif screen == "background":
        if question.correct == True:
            obj_list, question = blit_objs()
            return "background", obj_list, question
    return screen, obj_list, question


def main():
    """Contains game loop"""
    run = True
    clock = pygame.time.Clock()
    screen = "start"
    obj_list = None
    question = None

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    screen, obj_list, question = clicked(event, screen, obj_list, question)

            draw_window(screen, obj_list, question)

    pygame.quit()


if __name__ == '__main__':
    main()