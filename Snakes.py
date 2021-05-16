import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
darkred = (232,32,32)
green = (17,255,0)
blue = (0,0,200)
red = (255,0,0)

# Creating window
screen_width = 1200
screen_height = 700
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snake game by Abhishek")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 99)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(blue)
        text_screen("Welcome to Snakes", white, 300, 300)
        text_screen("Press Space Bar To Play", white, 220, 380)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, 1150)
    food_y = random.randint(20, 680)
    score = 0
    init_velocity = 5
    snake_size = 30
    foodsize = 15
    fps = 60
    while not exit_game:
        if game_over:
            gameWindow.fill(blue)
            text_screen("Game Over !", red, 400, 250)
            text_screen("Press Enter To Continue", white, 200, 350)
            text_screen(f"Your highscore is {score}", green, 250, 450)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score +=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<20:
                score +=10
                food_x = random.randint(20, 1150)
                food_y = random.randint(20, 680)
                snk_length +=5

            gameWindow.fill(blue)
            text_screen("Score: " + str(score), white, 5, 5)
            pygame.draw.circle(gameWindow, green, [food_x, food_y,], foodsize)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            plot_snake(gameWindow, darkred, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
