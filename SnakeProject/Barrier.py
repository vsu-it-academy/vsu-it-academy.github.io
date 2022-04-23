import pygame
import random

class Barrier():
    def __init__(self, barrier_color, screen_width, screen_height):
        """Инит препятствий"""
        self.barrier_color = barrier_color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rects = []

    def draw_barrier(self, play_surface, score):
        """Отображение препятствий"""
        # Постоянное препятсвие
        barrier_rect = pygame.draw.rect(play_surface, self.barrier_color, pygame.Rect(0, 0, 30, 40))
        self.rects.append(barrier_rect)

        # Уровневое препятствие
        if score==1:
            # препятствие уровня 1
            self.rects.clear()
            
            barrier_rect = pygame.draw.rect(play_surface, self.barrier_color, pygame.Rect(20, 50, 10, 40))
            self.rects.append(barrier_rect)
            
            barrier_rect = pygame.draw.rect(play_surface, self.barrier_color, pygame.Rect(100, 100, 40, 40))
            self.rects.append(barrier_rect)


    def check_collision(self, game_over, snake_rects):
        """Проверка пересечения с препятствием"""
        for barrier_rect in self.rects:
            check = barrier_rect.collidelist(snake_rects)
            if check == True:
                game_over()