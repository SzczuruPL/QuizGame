import pygame
import sys

from button import Button
from textinput import TextInput
from banner import Banner
from dualbanner import DualBanner
from gamebanner import GameBanner

pygame.init()

clock = pygame.time.Clock()
timer_event = pygame.USEREVENT + 0
timer_event2 = pygame.USEREVENT + 1
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Kahoot')

font = pygame.font.Font(None, 24)
text_color = (255, 255, 255)

bg_menu = pygame.image.load("images/menu_bg.png")
bg_scoreboard = pygame.image.load("images/scoreboard_bg.png")
logo_img = pygame.image.load("images/logo.png").convert_alpha()

pygame.mixer.music.load("music/lobby.mp3")
pygame.mixer.music.play(-1)

# GLOBAL SETTINGS
music = 1
background = 0
name = ""
scores = []

# MENU ITEMS
menu_btn_img = {
    "normal": pygame.image.load("images/menu_btn.png").convert_alpha(),
    "hover": pygame.image.load("images/menu_btn_hover.png").convert_alpha(),
    "click": pygame.image.load("images/menu_btn_click.png").convert_alpha()
}
menu_inp_img = {
    "normal": pygame.image.load("images/menu_inp.png").convert_alpha(),
    "active": pygame.image.load("images/menu_inp_active.png").convert_alpha()
}

menu_img = {
    2: pygame.image.load("images/menu2.png").convert_alpha(),
    3: pygame.image.load("images/menu3.png").convert_alpha(),
    4: pygame.image.load("images/menu4.png").convert_alpha(),
    5: pygame.image.load("images/menu5.png").convert_alpha()
}

# SCOREBOARD ITEMS
scoreboard_btn_img = {
    "normal": pygame.image.load("images/scoreboard_btn.png").convert_alpha(),
    "hover": pygame.image.load("images/scoreboard_btn_hover.png").convert_alpha(),
    "click": pygame.image.load("images/scoreboard_btn_click.png").convert_alpha()
}

scoreboard_img = {
    0: pygame.image.load("images/scoreboard_band.png").convert_alpha(),
    1: pygame.image.load("images/scoreboard_band2.png").convert_alpha()
}

scoreboard_name_img = pygame.image.load("images/scoreboard_name.png").convert_alpha()

# LEVEL ITEMS
bg_level_img = {
    0: pygame.image.load("images/white_bg.png"),
    1: pygame.image.load("images/classroom_bg.png")
}

level_band_img = {
    "down": pygame.image.load("images/game_down.png"),
    "up": pygame.image.load("images/game_up.png").convert_alpha()
}

level_score_img = pygame.image.load("images/points_board.png").convert_alpha()

get_ready_img = pygame.image.load("images/getready.png").convert_alpha()

question_time_img = pygame.image.load("images/question_time.png").convert_alpha()

question_board_img = {
    "question": pygame.image.load("images/question_board.png").convert_alpha(),
    "answer": pygame.image.load("images/question_board_answer.png")
}

# LEVEL BUTTONS
anwser_bigblue = {
    "normal": pygame.image.load("images/anwser_bigblue.png").convert_alpha(),
    "hover": pygame.image.load("images/anwser_bigblue_hover.png").convert_alpha(),
    "click": pygame.image.load("images/anwser_bigblue_click.png").convert_alpha(),
    "wrong": pygame.image.load("images/anwser_bigblue_wrong.png").convert_alpha(),
    "right": pygame.image.load("images/anwser_bigblue_right.png").convert_alpha()
}

anwser_bigred = {
    "normal": pygame.image.load("images/anwser_bigred.png").convert_alpha(),
    "hover": pygame.image.load("images/anwser_bigred_hover.png").convert_alpha(),
    "click": pygame.image.load("images/anwser_bigred_click.png").convert_alpha(),
    "wrong": pygame.image.load("images/anwser_bigred_wrong.png").convert_alpha(),
    "right": pygame.image.load("images/anwser_bigred_right.png").convert_alpha()
}

anwser_blue = {
    "normal": pygame.image.load("images/anwser_blue.png").convert_alpha(),
    "hover": pygame.image.load("images/anwser_blue_hover.png").convert_alpha(),
    "click": pygame.image.load("images/anwser_blue_click.png").convert_alpha(),
    "wrong": pygame.image.load("images/anwser_blue_wrong.png").convert_alpha(),
    "right": pygame.image.load("images/anwser_blue_right.png").convert_alpha()
}

anwser_red = {
    "normal": pygame.image.load("images/anwser_red.png").convert_alpha(),
    "hover": pygame.image.load("images/anwser_red_hover.png").convert_alpha(),
    "click": pygame.image.load("images/anwser_red_click.png").convert_alpha(),
    "wrong": pygame.image.load("images/anwser_red_wrong.png").convert_alpha(),
    "right": pygame.image.load("images/anwser_red_right.png").convert_alpha()
}

anwser_yellow = {
    "normal": pygame.image.load("images/anwser_yellow.png").convert_alpha(),
    "hover": pygame.image.load("images/anwser_yellow_hover.png").convert_alpha(),
    "click": pygame.image.load("images/anwser_yellow_click.png").convert_alpha(),
    "wrong": pygame.image.load("images/anwser_yellow_wrong.png").convert_alpha(),
    "right": pygame.image.load("images/anwser_yellow_right.png").convert_alpha()
}

anwser_green = {
    "normal": pygame.image.load("images/anwser_green.png").convert_alpha(),
    "hover": pygame.image.load("images/anwser_green_hover.png").convert_alpha(),
    "click": pygame.image.load("images/anwser_green_click.png").convert_alpha(),
    "wrong": pygame.image.load("images/anwser_green_wrong.png").convert_alpha(),
    "right": pygame.image.load("images/anwser_green_right.png").convert_alpha()
}

check_img = {
    "good": pygame.image.load("images/good.png").convert_alpha(),
    "bad": pygame.image.load("images/bad.png").convert_alpha()
}

# QUIZ STUFF
quiz_geo = [
    ["Co jest stolicą Albanii?", ["Valetta", "Tirana", "Pristina", "Podgorica"], [1]],
    ["Które pasmo górskie jest w Europie?", ["Alpy", "Andy", "Góry Skaliste", "Pireneje"], [0, 3]],
    ["Czy Szwajcaria jest w strefie Schengen?", ["Tak", "Nie"], [0]],
    ["Czy Barcelona jest stolicą?", ["Tak", "Nie"], [1]],
    ["Gdzie mieszka papież?", ["Rzym", "Watykan", "San Marino", "Wenecja"], [1]],
]

quiz_math = [
    ["Ile wynosi pierwiastek kwadratowy z 81?", ["7", "9", "8", "11"], [1]],
    ["Jakie działanie da wynik 21?", ["3*7", "4*2", "6*9", "7*3"], [0, 3]],
    ["Czy można dzielić przez 0?", ["Tak", "Nie"], [1]],
    ["Która z poniższych liczb jest pierwsza?", ["25", "29", "33", "37"], [1, 3]],
    ["Które z poniższych działań jest równoważne 2 * 3 + 4?", ["6 + 4", "2 + 12", "2 * (3 + 4)", "6 * 4"], [2]],
    ["Który z poniższych ułamków jest największy?", ["3/4", "5/8", "7/12", "2/3"], [0]],
    ["Ile wynosi obwód prostokąta o bokach długości 8 cm i 12 cm?", ["34cm", "32cm"], [1]]
]

quiz_cs = [
    ["Jakim typem pamięci jest pamięć RAM?", ["Operacyjną", "Wewnętrzną", "Masową", "Zewnętrzną"], [0, 1]],
    ["Czym jest Python?", ["Rodzajem węża", "Systemem operacyjnym", "Językiem programowania", "Przeglądarką"], [2]],
    ["Czy język Python jest interpretowany?", ["Tak", "Nie"], [0]],
    ["Co to jest algorytm?", ["Część komputera", "Instrukcje operacyjne", "Język programowania", "Zestaw kroków"], [1, 3]],
    ["Czy instrukcja parzenia kawy jest algorytmem?", ["Tak", "Nie"], [0]],
    ["Jakie jest zadanie chmury obliczeniowej?", ["Przechowywanie danych", "Ochrona przed wirusami"], [0]]
]

quizzes = [quiz_geo, quiz_math, quiz_cs]


def scores_save():
    global scores

    for i, quiz_scores in enumerate(scores):
        file_name = f"scores_{i+1}.dat"
        with open(file_name, 'w') as file:
            for user, score in quiz_scores:
                file.write(f"{user}:{score}\n")


def scores_load():
    global scores

    for i in range(3):
        file_name = f"scores_{i+1}.dat"

        try:
            with open(file_name, 'r') as file:
                quiz_scores = []
                for line in file:
                    line = line.strip()
                    if line:
                        user, score = line.split(':')
                        quiz_scores.append((user, int(score)))
                scores.append(quiz_scores)
        except FileNotFoundError:
            with open(file_name, 'w'):
                pass
            scores.append([])

    print(scores)


def score_add(quiz_index, score):
    global scores
    global name

    print(scores)
    quiz_scores = scores[quiz_index]
    for i, (player, points) in enumerate(quiz_scores):
        if player == name:
            if score > points:
                quiz_scores[i] = (name, score)
            return
    quiz_scores.append((name, score))


def scores_total():
    global scores

    total_scores = {}
    for quiz_scores in scores:
        for user, score in quiz_scores:
            if user in total_scores:
                total_scores[user] += score
            else:
                total_scores[user] = score
    return total_scores


def name_menu():
    global name

    scores_load()

    name_inp = TextInput(368, 394, menu_inp_img, "Wpisz swój nick")
    accept_but = Button(368, 452, menu_btn_img, "Zatwierdź")

    while True:
        screen.blit(bg_menu, (0, 0))

        screen.blit(logo_img, (412, 294))
        screen.blit(menu_img[2], (352, 378))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            name_inp.handle_event(event)
            name = name_inp.get_text()

            if accept_but.handle_event(event):
                if name != "Wpisz swój nick" and name != "":
                    main_menu()

        name_inp.draw(screen)
        accept_but.draw(screen)
        pygame.display.flip()


def main_menu():
    start_but = Button(368, 394, menu_btn_img, "Start")
    results_but = Button(368, 452, menu_btn_img, "Wyniki")
    settings_but = Button(368, 510, menu_btn_img, "Ustawienia")
    quit_but = Button(368, 568, menu_btn_img, "Wyjdź")

    while True:
        screen.blit(bg_menu, (0, 0))

        screen.blit(logo_img, (412, 294))
        screen.blit(menu_img[4], (352, 378))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if start_but.handle_event(event):
                start_menu()

            if results_but.handle_event(event):
                scoreboard_menu()

            if settings_but.handle_event(event):
                settings_menu()

            if quit_but.handle_event(event):
                pygame.quit()
                sys.exit()

        start_but.draw(screen)
        results_but.draw(screen)
        settings_but.draw(screen)
        quit_but.draw(screen)
        pygame.display.flip()


def start_menu():
    geography_but = Button(368, 394, menu_btn_img, "Geografia")
    math_but = Button(368, 452, menu_btn_img, "Matematyka")
    cs_but = Button(368, 510, menu_btn_img, "Informatyka")
    back_but = Button(368, 568, menu_btn_img, "Wróć")

    while True:
        screen.blit(bg_menu, (0, 0))

        screen.blit(logo_img, (412, 294))
        screen.blit(menu_img[4], (352, 378))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if geography_but.handle_event(event):
                game_hold(0)

            if math_but.handle_event(event):
                game_hold(1)

            if cs_but.handle_event(event):
                game_hold(2)

            if back_but.handle_event(event):
                main_menu()

        geography_but.draw(screen)
        math_but.draw(screen)
        cs_but.draw(screen)
        back_but.draw(screen)
        pygame.display.flip()


def scoreboard_menu():
    general_but = Button(368, 394, menu_btn_img, "Ogólne")
    math_but = Button(368, 510, menu_btn_img, "Matematyka")
    cs_but = Button(368, 568, menu_btn_img, "Informatyka")
    geography_but = Button(368, 452, menu_btn_img, "Geografia")
    back_but = Button(368, 626, menu_btn_img, "Wróć")

    while True:
        screen.blit(bg_menu, (0, 0))

        screen.blit(logo_img, (412, 294))
        screen.blit(menu_img[5], (352, 378))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if geography_but.handle_event(event):
                scoreboard(1, 0)

            if math_but.handle_event(event):
                scoreboard(2, 0)

            if cs_but.handle_event(event):
                scoreboard(3, 0)

            if general_but.handle_event(event):
                scoreboard(0, 0)

            if back_but.handle_event(event):
                main_menu()

        geography_but.draw(screen)
        math_but.draw(screen)
        cs_but.draw(screen)
        general_but.draw(screen)
        back_but.draw(screen)
        pygame.display.flip()


def settings_menu():
    global music

    music_text = {
        0: "Muzyka",
        1: "> Muzyka <"
    }

    background_but = Button(368, 394, menu_btn_img, "Tło")
    music_but = Button(368, 452, menu_btn_img, music_text[music])
    back_but = Button(368, 510, menu_btn_img, "Wróć")

    while True:
        screen.blit(bg_menu, (0, 0))

        screen.blit(logo_img, (412, 294))
        screen.blit(menu_img[3], (352, 378))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if background_but.handle_event(event):
                background_menu()

            if music_but.handle_event(event):
                if music:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1)
                music = not music
                music_but.set_text(music_text[music])

            if back_but.handle_event(event):
                main_menu()

        background_but.draw(screen)
        music_but.draw(screen)
        back_but.draw(screen)
        pygame.display.flip()


def background_menu():
    global background

    white_text = {
        0: "> Białe <",
        1: "Białe"
    }

    classroom_text = {
        0: "Klasa",
        1: "> Klasa <"
    }

    white_but = Button(368, 394, menu_btn_img, white_text[background])
    classroom_but = Button(368, 452, menu_btn_img, classroom_text[background])
    back_but = Button(368, 510, menu_btn_img, "Wróć")

    while True:
        screen.blit(bg_menu, (0, 0))

        screen.blit(logo_img, (412, 294))
        screen.blit(menu_img[3], (352, 378))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if white_but.handle_event(event):
                background = 0
                white_but.set_text(white_text[background])
                classroom_but.set_text(classroom_text[background])

            if classroom_but.handle_event(event):
                background = 1
                white_but.set_text(white_text[background])
                classroom_but.set_text(classroom_text[background])

            if back_but.handle_event(event):
                settings_menu()

        white_but.draw(screen)
        classroom_but.draw(screen)
        back_but.draw(screen)
        pygame.display.flip()


def scoreboard(n, ref):
    global scores

    button_strings = {
        0: "Wróć",
        1: "Dalej"
    }

    scoreboard_strings = {
        0: "Wyniki ogólne",
        1: "Wyniki: Geografia",
        2: "Wyniki: Matematyka",
        3: "Wyniki: Informatyka"
    }

    scorebanners_strings = {
        0: "main",
        1: "bottom"
    }

    scorebanners = []

    back_but = Button(950, 16, scoreboard_btn_img, button_strings[ref])
    back_but.set_color((0, 0, 0))
    name_ban = Banner(237, 16, scoreboard_name_img, scoreboard_strings[n])

    if n != 0:
        quiz_scores = scores[n - 1]
    else:
        quiz_scores = scores_total()

    if isinstance(quiz_scores, dict):
        quiz_scores_list = [(user, score) for user, score in quiz_scores.items()]
    else:
        quiz_scores_list = quiz_scores

    sorted_scores = sorted(quiz_scores_list, key=lambda x: x[1], reverse=True)
    top_scores = sorted_scores[:5]
    for i, (user, score) in enumerate(top_scores):
        scorebanners.append(DualBanner(55, 278 + (76 * i), scoreboard_img[int(i != 0)], str(user), str(score)))

    if scorebanners:
        scorebanners[0].set_color((0, 0, 0))

    while True:
        screen.blit(bg_scoreboard, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if back_but.handle_event(event):
                if ref == 0:
                    scoreboard_menu()
                else:
                    main_menu()

        name_ban.draw(screen)
        back_but.draw(screen)
        for i, (user, score) in enumerate(top_scores):
            scorebanners[i].draw(screen)
        pygame.display.flip()


def game_hold(ref):
    global background
    global name

    score = 0
    qnumber = len(quizzes[ref])

    pygame.time.set_timer(timer_event, 5000)
    pygame.time.set_timer(timer_event2, 20)

    game_ban = GameBanner(level_band_img, level_score_img, 0, qnumber, name, score)

    i = 0

    while True:
        screen.blit(bg_level_img[background], (0, 0))

        screen.blit(get_ready_img, (238, 288))

        game_ban.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == timer_event:
                n = 0
                game_question(n, ref, score)
            elif event.type == timer_event2:
                szerokosc_paska = int((i / 250) * 1024)
                pygame.draw.rect(screen, (138, 43, 226), (0, 650, szerokosc_paska, 30))
                pygame.display.flip()
                pygame.time.delay(int(1000 / 50))
                i = i + 1

        pygame.display.flip()


def game_question(n, ref, score):
    global background
    global name

    qnumber = len(quizzes[ref])

    game_ban = GameBanner(level_band_img, level_score_img, n, qnumber, name, score)

    question_ban = Banner(0, 303, question_board_img["question"], quizzes[ref][n][0])

    pygame.time.set_timer(timer_event, 5000)
    pygame.time.set_timer(timer_event2, 20)

    i = 0

    while True:
        screen.blit(bg_level_img[background], (0, 0))

        question_ban.draw(screen)
        game_ban.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == timer_event:
                game_answer(n, ref, score)
            elif event.type == timer_event2:
                szerokosc_paska = int((i / 250) * 1024)
                pygame.draw.rect(screen, (138, 43, 226), (0, 650, szerokosc_paska, 30))
                pygame.display.flip()
                pygame.time.delay(int(1000 / 50))
                i = i + 1

        pygame.display.flip()


def game_answer(n, ref, score):
    global background
    global name

    qtime = 30
    qnumber = len(quizzes[ref])

    game_ban = GameBanner(level_band_img, level_score_img, n, qnumber, name, score)

    qtime_ban = Banner(24, 140, question_time_img, str(qtime))
    qtime_ban.set_color((255, 255, 255))
    qtime_ban.set_fontsize(48)

    question_ban = Banner(153, 120, question_board_img["answer"], quizzes[ref][n][0])

    if len(quizzes[ref][n][1]) == 4:
        blue_but = Button(37, 384, anwser_blue, quizzes[ref][n][1][0])
        blue_but.set_fontsize(32)
        red_but = Button(535, 384, anwser_red, quizzes[ref][n][1][1])
        red_but.set_fontsize(32)
        yellow_but = Button(37, 545, anwser_yellow, quizzes[ref][n][1][2])
        yellow_but.set_fontsize(32)
        green_but = Button(535, 545, anwser_green, quizzes[ref][n][1][3])
        green_but.set_fontsize(32)
    else:
        bigblue_but = Button(37, 384, anwser_bigblue, quizzes[ref][n][1][0])
        bigblue_but.set_fontsize(32)
        bigred_but = Button(535, 384, anwser_bigred, quizzes[ref][n][1][1])
        bigred_but.set_fontsize(32)

    pygame.time.set_timer(timer_event, 30000)
    pygame.time.set_timer(timer_event2, 1000)

    while True:
        screen.blit(bg_level_img[background], (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == timer_event2:
                qtime = qtime-1
                qtime_ban.set_text(str(qtime))
                qtime_ban.draw(screen)

            elif event.type == timer_event:
                game_check(n, ref, score, -2, 0)

            if len(quizzes[ref][n][1]) == 4:
                if blue_but.handle_event(event):
                    game_check(n, ref, score, 0, qtime)

                if red_but.handle_event(event):
                    game_check(n, ref, score, 1, qtime)

                if yellow_but.handle_event(event):
                    game_check(n, ref, score, 2, qtime)

                if green_but.handle_event(event):
                    game_check(n, ref, score, 3, qtime)
            else:
                if bigblue_but.handle_event(event):
                    game_check(n, ref, score, 0, qtime)

                if bigred_but.handle_event(event):
                    game_check(n, ref, score, 1, qtime)

        qtime_ban.draw(screen)
        question_ban.draw(screen)

        if len(quizzes[ref][n][1]) == 4:
            blue_but.draw(screen)
            red_but.draw(screen)
            yellow_but.draw(screen)
            green_but.draw(screen)
        else:
            bigblue_but.draw(screen)
            bigred_but.draw(screen)

        game_ban.draw(screen)
        pygame.display.flip()


def game_check(n, ref, score, a_id, qtime):
    global background
    global name

    is_correct = False
    score_curr = 0
    qnumber = len(quizzes[ref])
    t = ["wrong", "right"]

    w = quizzes[ref][n][2]

    if len(w) == 1:
        w.append(-1)

    if a_id == w[0] or a_id == w[1]:
        score_curr = int((1 - (((30 - qtime) / 30) / 2)) * 1000)
        score = score + score_curr
        is_correct = True

    game_ban = GameBanner(level_band_img, level_score_img, n, qnumber, name, score)

    if len(quizzes[ref][n][1]) == 4:
        blue_but = Banner(37, 384, anwser_blue[t[(0 == w[0] or 0 == w[1])]], quizzes[ref][n][1][0])
        blue_but.set_color((255, 255, 255))
        blue_but.set_fontsize(32)
        red_but = Banner(535, 384, anwser_red[t[(1 == w[0] or 1 == w[1])]], quizzes[ref][n][1][1])
        red_but.set_color((255, 255, 255))
        red_but.set_fontsize(32)
        yellow_but = Banner(37, 545, anwser_yellow[t[(2 == w[0] or 2 == w[1])]], quizzes[ref][n][1][2])
        yellow_but.set_color((255, 255, 255))
        yellow_but.set_fontsize(32)
        green_but = Banner(535, 545, anwser_green[t[(3 == w[0] or 3 == w[1])]], quizzes[ref][n][1][3])
        green_but.set_color((255, 255, 255))
        green_but.set_fontsize(32)
    else:
        bigblue_but = Banner(37, 384, anwser_bigblue[t[(0 == w[0] or 0 == w[1])]], quizzes[ref][n][1][0])
        bigblue_but.set_fontsize(32)
        bigblue_but.set_color((255, 255, 255))
        bigred_but = Banner(535, 384, anwser_bigred[t[(1 == w[0] or 1 == w[1])]], quizzes[ref][n][1][1])
        bigred_but.set_fontsize(32)
        bigred_but.set_color((255, 255, 255))

    score_curr_ban = Banner(431, 330, level_score_img, "+ " + str(score_curr))
    score_curr_ban.set_color((255, 255, 255))

    pygame.time.set_timer(timer_event, 5000)

    while True:
        screen.blit(bg_level_img[background], (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == timer_event:
                if n < (qnumber - 1):
                    game_question(n + 1, ref, score)
                else:
                    score_add(ref, score)
                    scores_save()
                    scoreboard(ref + 1, 1)

        if len(quizzes[ref][n][1]) == 4:
            blue_but.draw(screen)
            red_but.draw(screen)
            yellow_but.draw(screen)
            green_but.draw(screen)
        else:
            bigblue_but.draw(screen)
            bigred_but.draw(screen)

        if is_correct:
            screen.blit(check_img["good"], (340, 61))
        else:
            screen.blit(check_img["bad"], (300, 61))

        game_ban.draw(screen)
        score_curr_ban.draw(screen)
        pygame.display.flip()


name_menu()
