import pygame as pg
pg.font.init()
pg.mixer.init()
from random import randint
#---------------------------------------------------V


HEIGHT_WIN,WIDTH_WIN = 800, 600
WIN = pg.display.set_mode((HEIGHT_WIN, WIDTH_WIN))
pg.display.set_caption("La Viborita!")
#---------------------------------------------------V
#   Constantes:
snake_size=28
snake_color = (153, 153, 153)
move = 7

food_color = (51, 77, 0)
WIN_COLOR = (13, 13, 13)
END_SOUND = pg.mixer.Sound('archivos/end.mp3')
FOOD_SOUND = pg.mixer.Sound('archivos/FOOD.mp3')

#---------------------------------------------------V
#   SNAKE MOVMENT
def movimiento(SNAKE, DIRECCION):
        if DIRECCION == "up":
            SNAKE[0].y -= move  
        elif DIRECCION == "down":
            SNAKE[0].y += move  
        elif DIRECCION == "left":
            SNAKE[0].x -= move  
        elif DIRECCION == "right":
            SNAKE[0].x += move  

# Perder al toar un borde  
def end_move(SNAKE):
    if SNAKE[0].y < 0 or SNAKE[0].y > HEIGHT_WIN - 232:
        END_SOUND.play()
        END()
        main()
    elif SNAKE[0].x < 4 or SNAKE[0].x > WIDTH_WIN + 173:
        END_SOUND.play()
        END()
        main()

# Cartel de que perdiste
def END():  
    LOSE_TXT=pg.font.SysFont("Times New Roman", 100)
    LOSE_RENDER = LOSE_TXT.render("¡PERDISTE!",1, (230, 0, 0))
    WIN.blit(LOSE_RENDER,(WIDTH_WIN//2 - 160, HEIGHT_WIN//2 - 180))
    pg.display.update()
    pg.time.delay(1000)

def comerse_sola(SNAKE): # FALTA TERMINARRRRRRR!!!!!!
    for segment in SNAKE[6:]:
        if SNAKE[0].colliderect(segment):
            pass



#---------------------------------------------------V
def draw_win(SNAKE,FOOD):
    WIN.fill(WIN_COLOR)
    for segment in SNAKE:
        pg.draw.rect(WIN, snake_color, segment)
    pg.draw.rect(WIN,food_color,FOOD)
    pg.display.update()

#---------------------------------------------------V
def main():
    SNAKE = [pg.rect.Rect(300, 200, snake_size, snake_size)]
    DIRECCION = ''
    FOOD = pg.Rect(randint(0, HEIGHT_WIN - snake_size -40), randint(0, WIDTH_WIN - snake_size - 40), snake_size, snake_size)
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
# Coliciones                     
        if SNAKE[0].colliderect(FOOD):
            FOOD_SOUND.play()
            FOOD.y = randint(0, WIDTH_WIN)
            FOOD.x = randint(0, HEIGHT_WIN)
            
            last_segment = SNAKE[-1]
            if DIRECCION == "up":
                SNAKE.append(pg.Rect(last_segment.x, last_segment.y + snake_size, snake_size, snake_size))
            elif DIRECCION == "down":
                SNAKE.append(pg.Rect(last_segment.x, last_segment.y - snake_size, snake_size, snake_size))
            elif DIRECCION == "left":
                SNAKE.append(pg.Rect(last_segment.x + snake_size, last_segment.y, snake_size, snake_size))
            elif DIRECCION == "right":
                SNAKE.append(pg.Rect(last_segment.x - snake_size, last_segment.y, snake_size, snake_size))

        # Actualizar el movimiento de la serpiente
        for i in range(len(SNAKE) - 1, 0, -1):
            SNAKE[i].x = SNAKE[i - 1].x
            SNAKE[i].y = SNAKE[i - 1].y
            

# Funciones            
        movimiento(SNAKE, DIRECCION)
        draw_win(SNAKE,FOOD) 
        end_move(SNAKE) 
        comerse_sola(SNAKE)
        

main()


