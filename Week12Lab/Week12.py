import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 500

fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

font = pygame.font.SysFont('Rockwell', 30)

margin = 50
cpu_score = 0
player_score = 0
fps = 60
winner = 0

bg = (90, 10, 10)
white = (10, 10, 10)

def draw_board():
    screen.fill(bg)
    pygame.draw.line(screen, white, (0,margin), (screen_width, margin))
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))

class paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = Rect(self.x, self.y, 20, 100)
        self.speed = 5

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.top > margin:
            self.rect.move_ip(0, -1 * self.speed)
        if key[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.speed)

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)

class ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ball_rad = 8
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = -4
        self.speed_y = 4
        self.winner = 0
    def move(self):

       if self.rect.top < margin:
           self.speed_y *= -1
       if self.rect.bottom > screen_height:
           self.speed_y *= -1

       if self.rect.left < 0:
           self.winner = 1
       if self.rect.right > screen_width:
           self.winner = -1


       self.rect.x += self.speed_x
       self.rect.y += self.speed_y

       return self.winner

    def draw(self):
        pygame.draw.circle(screen, white, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)


player_paddle = paddle(screen_width - 40, screen_height // 2)
cpu_paddle = paddle(20, screen_height // 2)

pong = ball(screen_width - 60, screen_height // 2 + 50)

run = True
while run:

    fpsClock.tick(fps)

    draw_board()
    draw_text('CPU: ' + str(cpu_score), font, white, 20, 15)
    draw_text('P1: ' + str(player_score), font, white, screen_width -100, 15)

    player_paddle.draw()
    cpu_paddle.draw()

    pong.draw()

    player_paddle.move()

    winner = pong.move()
    print(winner)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

