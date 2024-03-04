import pygame as pg
from random import randint

HEIGHT_WIN,WIDTH_WIN = 800, 600
WIN = pg.display.set_mode((HEIGHT_WIN, WIDTH_WIN))
pg.display.set_caption("La Bovira!")
#---------------------------------------------------V
#   Constantes:
snake_size=25
snake_color = (153, 153, 153)
move = 5

food_color = (51, 77, 0)
WIN_COLOR = (13, 13, 13)
#---------------------------------------------------V
#   SNAKE MOVMENT
def movimiento(SNAKE, DIRECCION):
        if DIRECCION == "up" and SNAKE.y - move > 0:
            SNAKE.y -= move  
        elif DIRECCION == "down" and SNAKE.y + move < WIDTH_WIN - snake_size:
            SNAKE.y += move  
        elif DIRECCION == "left" and SNAKE.x - move > 0:
            SNAKE.x -= move  
        elif DIRECCION == "right" and SNAKE.x + move < HEIGHT_WIN - snake_size:
            SNAKE.x += move  
    

#---------------------------------------------------V
def draw_win(SNAKE,FOOD):
    WIN.fill(WIN_COLOR)
    pg.draw.rect(WIN, snake_color, SNAKE)
    pg.draw.rect(WIN,food_color,FOOD)
    pg.display.update()

#---------------------------------------------------V
def main():
    SNAKE = pg.rect.Rect(300, 200, snake_size, snake_size)
    DIRECCION = ''
    FOOD = pg.Rect(randint(0, HEIGHT_WIN - snake_size),randint(0, WIDTH_WIN - snake_size) ,snake_size,snake_size)
    clock = pg.time.Clock()
    while True:
        key_pressed = pg.key.get_pressed()
        clock.tick(60)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
# Movimiento
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    DIRECCION = "up"
                elif event.key == pg.K_s:
                    DIRECCION = "down"
                elif event.key == pg.K_a:
                    DIRECCION = "left"
                elif event.key == pg.K_d:
                    DIRECCION = "right"
        if SNAKE.colliderect(FOOD):
            FOOD.y = randint(0, WIDTH_WIN)
            FOOD.x = randint(0, HEIGHT_WIN)
            

        movimiento(SNAKE, DIRECCION)
        draw_win(SNAKE,FOOD)  

main()


