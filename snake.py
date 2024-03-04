import pygame as pg
WIDTH_WIN, HEIGHT_WIN = 400, 600
WIN = pg.display.set_mode((HEIGHT_WIN, WIDTH_WIN))
pg.display.set_caption("La Bovirita!")
#---------------------------------------------------V
#   Variables:
snake_size=20
snake_color = (153, 153, 153)
move = 7

WIN_COLOR = (13, 13, 13)
#---------------------------------------------------V
#   SNAKE MOVMENT
def movimiento(key_pressed, SNAKE):
    if key_pressed[pg.K_w]:
        SNAKE.y -= move  
    elif key_pressed[pg.K_s]:
        SNAKE.y += move  
    elif key_pressed[pg.K_a]:
        SNAKE.x -= move  
    elif key_pressed[pg.K_d]:
        SNAKE.x += move  

#---------------------------------------------------V
def draw_win(SNAKE):
    WIN.fill(WIN_COLOR)
    pg.draw.rect(WIN, snake_color, SNAKE)
    pg.display.update()

#---------------------------------------------------V

def main():

    SNAKE = pg.Rect(300, 200, snake_size, snake_size)
    key_pressed = pg.key.get_pressed()
    clock = pg.time.Clock()
    while True:
        clock.tick(60)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            movimiento(key_pressed, SNAKE)
        draw_win(SNAKE)

main()


