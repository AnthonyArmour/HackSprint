import pygame
from models.Logit import logit
import random
from models import persons_list, tech_obj_list, questions_list
import os
"""Lost Little Holbie pygame script"""

# Window variables
WIDTHB, HEIGHTB = 1200, 800
WIN = pygame.display.set_mode((WIDTHB, HEIGHTB))
pygame.display.set_caption('Lost lil\' holbie')
FPS = 60


# Backgrounds
BACKGROUND_IMG = pygame.image.load(os.path.join('Assets/images/gameboard', 'gameboard.PNG'))
START_1 = pygame.image.load(os.path.join('Assets/images/gameboard', 'welcome_1.PNG'))
START_2 = pygame.image.load(os.path.join('Assets/images/gameboard', 'welcome_2.PNG'))
START_3 = pygame.image.load(os.path.join('Assets/images/gameboard', 'welcome_3.PNG'))
INSTRUCTION_IMG = pygame.image.load(os.path.join('Assets/images/gameboard', 'instruction_img.png'))

# Misc
START_BUTTON = pygame.Rect(475, 600, 300, 100)
questions_list[0].active = True


def draw_window(screen, obj_list):
    """Draws game window"""
    if screen == "start":
        WIN.blit(START_1, (0, 0))
    elif screen == "start_2":
        WIN.blit(START_2, (0, 0))
    elif screen == "start_3":
        WIN.blit(START_3, (0, 0))
    elif screen == "instruction":
        WIN.blit(INSTRUCTION_IMG, (0, 0))
    elif screen == "background":
        question = get_active_question()
        WIN.blit(BACKGROUND_IMG, (0, 0))
        WIN.blit(question.image, (75, 75))
        WIN.blit(obj_list[0].active, (75, 400))
        WIN.blit(obj_list[1].active, (450, 400))
        WIN.blit(obj_list[2].active, (825, 400))
    pygame.display.update()


def get_active_question():
    """Gets active question"""
    for question in questions_list:
        if question.active == True:
            return question


def blits():
    """Finds obj's to blit"""
    new_list = []
    active = get_active_question()
    temp_person_list = persons_list.copy()
    temp_tech = tech_obj_list.copy()

    for i, person in enumerate(temp_person_list):
        if person.name == active.name_id:
            logit('correct is ' + str(active.name_id) + ' iteration: ' + str(i))
            new_list.append(person)
            temp_person_list.pop(i)
            new_list.append(random.choice(temp_person_list))
            new_list.append(random.choice(temp_person_list))
            break

    for i, tech in enumerate(temp_tech):
        if tech.name == active.name_id:
            logit('correct is ' + str(active.name_id))
            new_list.append(tech)
            temp_tech.pop(i)
            new_list.append(random.choice(temp_tech))
            new_list.append(random.choice(temp_tech))
            break

    return random.sample(new_list, 3)


def set_active():
    """Sets active question"""
    for i in range(len(questions_list)):
        if questions_list[i].active == True:
            questions_list[i].active = False
            if i + 1 < len(questions_list):
                questions_list[i + 1].active = True
            break


def set_pos(obj_list):
    """Sets position of rects"""
    start = 75
    for obj in obj_list:
        obj.pos.x = start
        obj.pos.y = 400
        start += 375


def reset_colors(obj_list):
    for obj in obj_list:
        obj.active = obj.image_1


def clicked(event, screen, obj_list):
    """Determines whats clicked and decides actions"""
    if screen == "start":
        if START_BUTTON.collidepoint(event.pos):
            return "start_2", None
    elif screen == "start_2":
        return "start_3", None
    elif screen == "start_3":
        return "instruction", None
    elif screen == "instruction":
        obj_list = blits()
        # obj_list, question, next_question = blit_objs()
        set_pos(obj_list)
        return "background", obj_list
    elif screen == "background":
        if get_active_question().correct == True:
            set_active()
            obj_list = blits()
            # for i in range(len(questions_list)):
            #     logit(str(questions_list[i].name_id) + ' ' + str(questions_list[i].active))
            set_pos(obj_list)
            reset_colors(obj_list)
            return "background", obj_list
        else:
            click_handler(event, get_active_question(), obj_list)

    return screen, obj_list


def click_handler(event, question, obj_list):
    """Determines if correct option clicked or not"""
    for obj in obj_list:
        if obj.pos.collidepoint(event.pos):
            if question.name_id == obj.name:
                obj.active = obj.image_3
                question.correct = True
            else:
                obj.active = obj.image_2


def main():
    """Contains game loop"""
    run = True
    clock = pygame.time.Clock()
    screen = "start"
    obj_list = None

    for i in range(len(questions_list)):
        logit(str(questions_list[i].name_id) + ' ' + str(questions_list[i].active))

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    screen, obj_list = clicked(event, screen, obj_list)

            draw_window(screen, obj_list)

    pygame.quit()


if __name__ == '__main__':
    main()