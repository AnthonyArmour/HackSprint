import pygame
import random
from models import persons_list, tech_obj_list, questions_list
import os
"""Lost Little Holbie pygame script"""
pygame.init()

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
GAME_OVER = pygame.image.load(os.path.join('Assets/images/gameboard', 'closescreen.PNG'))

# Fonts/text
FONT = pygame.font.SysFont('american typewriter', 48)
text = FONT.render('Click anywhere to continue', True, (0,0,0))
textRect = text.get_rect()
textRect.center = (600, 750)

# Misc
START_BUTTON = pygame.Rect(475, 600, 300, 100)
CORRECT_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets/images/textbox_objs', 'text_correct.PNG')),
    (250, 125))
questions_list[0].active = True


# Draws the game window
# screen: determine background
# obj_list: objects to draw
def draw_window(screen, obj_list, total_correct):
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
        if question.correct:
            WIN.blit(CORRECT_IMG, (775, 150))
            WIN.blit(text, textRect)
        WIN.blit(question.image, (75, 75))
        WIN.blit(obj_list[0].active, (75, 400))
        WIN.blit(obj_list[1].active, (450, 400))
        WIN.blit(obj_list[2].active, (825, 400))
    elif screen == "game_over":
        WIN.blit(GAME_OVER, (0, 0))
        score = FONT.render('You Scored: {} / 10'.format(total_correct), True, (0,0,0))
        scoreRect = score.get_rect()
        scoreRect.center = (600, 750)
        WIN.blit(score, scoreRect)
    pygame.display.update()


# Determines currently active question
def get_active_question():
    """Gets active question"""
    for question in questions_list:
        if question.active == True:
            return question


# Determines which objects to display
def blits():
    """Finds obj's to blit"""
    new_list = []
    active = get_active_question()
    temp_person = persons_list.copy()
    temp_tech = tech_obj_list.copy()

    for i, person in enumerate(temp_person):
        if person.name == active.name_id:
            new_list.append(person)
            temp_person.pop(i)
            rand = random.sample(temp_person, 2)
            [new_list.append(i) for i in rand]
            return random.sample(new_list, 3)


    for i, tech in enumerate(temp_tech):
        if tech.name == active.name_id:
            new_list.append(tech)
            temp_tech.pop(i)
            rand = random.sample(temp_tech, 2)
            [new_list.append(i) for i in rand]
            return random.sample(new_list, 3)


# Sets a new active question
# Return: True if new active question set, otherwise False
def set_active():
    """Sets active question"""
    for i in range(len(questions_list)):
        if questions_list[i].active == True:
            questions_list[i].active = False
            if i + 1 < len(questions_list):
                questions_list[i + 1].active = True
                return True
          
    return False


# Sets positions of displayed objects
# obj_list: list of objects to display
def set_pos(obj_list):
    """Sets position of rects"""
    start = 75
    for obj in obj_list:
        obj.pos.x = start
        obj.pos.y = 400
        start += 375


# Resets background colors of objects
# obj_list: list of objects to reset
def reset_colors(obj_list):
    for obj in obj_list:
        obj.active = obj.image_1


# Reacts to clicks, based on currently displayed prompts/questions
# event: click
# screen: background
# obj_list: list of active objects
def clicked(event, screen, obj_list, tries, total_correct):
    """Determines whats clicked and decides actions"""
    if screen == "game_over":
        pygame.quit()
    if screen == "start":
        if START_BUTTON.collidepoint(event.pos):
            return "start_2", None, total_correct
    elif screen == "start_2":
        return "start_3", None, total_correct
    elif screen == "start_3":
        return "instruction", None, total_correct
    elif screen == "instruction":
        obj_list = blits()
        set_pos(obj_list)
        return "background", obj_list, total_correct
    elif screen == "background":
        if get_active_question().correct == True:
            if tries == 1:
                total_correct += 1
            if set_active() == False:
                return "game_over", None, total_correct
            obj_list = blits()
            set_pos(obj_list)
            reset_colors(obj_list)
            return "background", obj_list, total_correct
        else:
            tries += 1
            click_handler(event, get_active_question(), obj_list)

    return screen, obj_list, total_correct


# Handles input - determines if correct or incorrect
# event: click
# question: question object
# obj_list: list of active objects
def click_handler(event, question, obj_list):
    """Determines if correct option clicked or not"""
    for obj in obj_list:
        if obj.pos.collidepoint(event.pos):
            if question.name_id == obj.name:
                obj.active = obj.image_3
                question.correct = True
            else:
                obj.active = obj.image_2


# Game loop
def main():
    """Contains game loop"""
    run = True
    clock = pygame.time.Clock()
    screen = "start"
    obj_list = None
    tries = 0
    total_correct = 0

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    screen, obj_list, total_correct = clicked(event, screen, obj_list, tries, total_correct)

            draw_window(screen, obj_list, total_correct)

    pygame.quit()


if __name__ == '__main__':
    main()