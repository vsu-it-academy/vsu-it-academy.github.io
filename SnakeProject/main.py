from tkinter import Menu
from Game import Game
from Snake import Snake
from Food import Food
from Barrier import Barrier

from Menu import Menu
import Settings as settings

menu = Menu()

game = Game()
snake = Snake(game.green)
food = Food(game.brown, game.screen_width, game.screen_height)
barrier = Barrier(game.black, game.screen_width, game.screen_height)

game.init_and_check_for_errors() 
game.set_surface_and_title()

while True:
    snake.change_to = game.event_loop(snake.change_to)

    snake.validate_direction_and_change()
    
    snake.change_head_position()
   
    game.score, food.food_pos = snake.snake_body_mechanism(game.score, food.food_pos, game.screen_width, game.screen_height)

    game.draw_background('images/bg.jpg')

    snake.draw_snake(game.play_surface, game.white)
    food.draw_food(game.play_surface)
    barrier.draw_barrier(game.play_surface, game.score)
    
    barrier.check_collision(game.game_over, snake.rects)

    snake.check_for_boundaries(game.game_over, game.screen_width, game.screen_height)

    game.show_score()

    start_speed = 8
    level = start_speed + game.score + settings.start_level
    game.refresh_screen(level)