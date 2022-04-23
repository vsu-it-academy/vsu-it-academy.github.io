from asyncio import events
from platform import python_branch
import pygame
import sys
import time

import Settings as settings

class Game():
    def __init__(self):
        # задаем размеры экрана
        self.screen_width = 720
        self.screen_height = 460

        # необходимые цвета
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.brown = pygame.Color(165, 42, 42)

        # Frame per second controller
        # будет задавать количество кадров в секунду
        self.fps_controller = pygame.time.Clock()

        # переменная для оторбражения результата
        # (сколько еды съели)
        self.score = 0

    def init_and_check_for_errors(self):
        """Начальная функция для инициализации и
           проверки как запустится pygame"""
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print('Игра запущена')

    def set_surface_and_title(self):
        """Задаем surface(поверхность поверх которой будет все рисоваться)
        и устанавливаем загаловок окна"""
        self.play_surface = pygame.display.set_mode((
            self.screen_width, self.screen_height))
        pygame.display.set_caption('Игра змейка')

    def event_loop(self, change_to):
        """Функция для отслеживания нажатий клавиш игроком"""

        # запускаем цикл по ивентам
        for event in pygame.event.get():
            # если двинули мышью
            if event.type == pygame.MOUSEMOTION:
                x,y = event.pos # позиция относительно левого верхнего угла окна
                w, h = pygame.display.get_surface().get_size() # определим ширину и высоту экрана
                w = w//2 #получим кооринату центра по одной оси
                h = h//2 #получим кооринату центра по другой оси
                # определим сторону движения
                if y > h:
                    change_to = "DOWN"
                elif y < h:
                    change_to = "UP"

            # если нажали клавишу
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = "DOWN"
                elif event.key == pygame.K_SPACE:
                    self.pause()
                # нажали escape
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        return change_to

    def refresh_screen(self, speed):
        """обновляем экран и задаем фпс"""
        pygame.display.flip()
        self.fps_controller.tick(speed)

    def show_score(self, choice=1):
        """Отображение результата"""
        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render(
            'Очки: {0}'.format(self.score), True, self.black)
        s_rect = s_surf.get_rect()
        # дефолтный случай отображаем результат слева сверху
        if choice == 1:
            s_rect.midtop = (80, 10)
        # при game_overe отображаем результат по центру
        # под надписью game over
        else:
            s_rect.midtop = (360, 120)
        # рисуем прямоугольник поверх surface
        self.play_surface.blit(s_surf, s_rect)

    def pause(self):
        go_font = pygame.font.SysFont('monaco', 72)
        go_surf = go_font.render('Пауза', True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        self.play_surface.blit(go_surf, go_rect)
        self.show_score(self.score)
        pygame.display.flip()

        is_pause = True # пока True - будет пауза
        while is_pause:
            for event in pygame.event.get():
            # если нажали клавишу
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: # проверяем что нажали на пробел
                        is_pause = False # снимаем с паузы
                        break # выходим из цикла
    
    def game_over(self):
        """Функция для вывода надписи Game Over и результатов
        в случае завершения игры и выход из игры"""
        go_font = pygame.font.SysFont('monaco', 72)
        go_surf = go_font.render('Вы проиграли '+settings.name_player, True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        self.play_surface.blit(go_surf, go_rect)
        self.show_score(0)
        pygame.display.flip()

        f = open("score.txt","a", encoding="utf-8")
        f.write("\nОчки: " + str(self.score))
        f.close()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    def draw_background(self, path):
        bg = pygame.image.load(path)
        bg_rect = bg.get_rect(bottomright=( self.screen_width,  self.screen_height))
        self.play_surface.blit(bg, bg_rect)
