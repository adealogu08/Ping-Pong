from pygame import *

win_width = 970
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption('Ping pong game')
background = transform.scale(image.load('pp2.png'), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

player1 = Player('padle3.png', 80, 500 - 60, 7)
player2 = Player('padle4.png', 700, 500 - 400, 5)
ball = Player('ppball.png', 1, 500 - 10, 1)

font.init()
font = font.Font(None, 37)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

finish = False
FPS = 60
clock = time.Clock()

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player1.update_l()
        player2.update_r()
        ball.update()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game = True

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game = True

        player1.reset()
        player2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
