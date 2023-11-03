from tkinter import *
from __init__ import *
from ball import Ball
from paddle import Paddle
import time
import random

class Bricks:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(5, 5, 25, 25, fill=color, width=2)


playing = False


def start_game(event):
    global playing
    if playing is False:
        playing = True
        pygame.mixer.music.play()
        file1 = open("highscore.txt","r+")
        highscore = str(file1.read())
        file1.close()
        score.configure(text="Score: 00\n\nHighscore: " + highscore)
        canvas.delete("all")
        BALL_COLOR = ["red"]
        # Search on google for hex colour picker:
        BRICK_COLOR = [
        "#FF6F61",  # A warm red
        "#6B5B95",  # A muted purple
        "#88B04B",  # A fresh green
        "#F7CAC9",  # A soft pink
        "#92A8D1",  # A calm blue
        "#955251",  # A deep wine red
        "#B565A7",  # A medium pink-purple
        "#009B77",  # A medium teal
        "#DD4124",  # A vibrant red-orange
        "#D65076",  # A bright pink
        "#45B8AC",  # A light sea green
        "#EFC050",  # A golden yellow
        "#5B5EA6",  # A royal blue
        "#9B2335",  # A strong red
        "#DFCFBE",  # A neutral beige
        "#55B4B0",  # An aqua blue
        "#E15D44"   # A bright orange-red
        ]
        random.shuffle(BALL_COLOR)
        # Colour of the paddle
        paddle = Paddle(canvas, "#4d55f7")
        bricks = []
        for i in range(0, 5):
            b = []
            for j in range(0, 19):
                random.shuffle(BRICK_COLOR)
                tmp = Bricks(canvas, BRICK_COLOR[0])
                b.append(tmp)
            bricks.append(b)

        for i in range(0, 5):
            for j in range(0, 19):
                canvas.move(bricks[i][j].id, 25 * j, 25 * i)

        ball = Ball(canvas, BALL_COLOR[0], paddle, bricks, score)
        root.update_idletasks()
        root.update()

        time.sleep(1)
        while 1:
            if paddle.pausec !=1:
                try:
                    canvas.delete(m)
                    del m
                except:
                    pass
                if not ball.bottom_hit:
                    ball.draw()
                    paddle.draw()
                    root.update_idletasks()
                    root.update()
                    time.sleep(0.01)
                    if ball.hit==95:
                        # You won message and colour
                        canvas.create_text(250, 250, text="YOU WON !!", fill="yellow", font="Consolas 24 ")
                        root.update_idletasks()
                        root.update()
                        playing = False
                        # Bind keys for when player wins
                        root.bind_all("<Right>", start_game)
                        root.bind_all("<Left>", start_game)
                        break
                else:
                    # Game Over message and colour
                    file1 = open("highscore.txt","r+")
                    highscore = str(file1.read())
                    file1.close()
                    if highscore < str(ball.hit):
                        file1 = open("highscore.txt","w")
                        file1.write(str(ball.hit))
                        file1.close()
                    canvas.create_text(250, 250, text="GAME OVER!!\nYour score was: " + str(ball.hit), fill="red", font="Consolas 24 ")
                    pygame.mixer.music.stop()
                    root.update_idletasks()
                    root.update()
                    playing = False
                    # Bind keys for when game is over
                    root.bind_all("<Right>", start_game)
                    root.bind_all("<Left>", start_game)
                    break
            else:
                try:
                    if m==None:pass
                except:
                    # Pause message and colour
                    m=canvas.create_text(250, 250, text="Paused", fill="blue", font="Consolas 24 ")
                root.update_idletasks()
                root.update()

# Initial text in screen (x,y), and Start Button
root.bind_all("<Return>", start_game)
root.bind_all("<Right>", start_game)
root.bind_all("<Left>", start_game)
canvas.create_text(250, 250, text="Press Enter to start Game!!", fill="red", font="Consolas 18")
root.mainloop()
        