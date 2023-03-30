from pygame import *

win_width = 970
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption('Ping pong game')
background = transform.scale(image.load('tbl.png'), (win_width, win_height))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player1.update_l()
        player2.update_r()

        player1.reset()
        player2.reset()


    display.update()
