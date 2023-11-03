from __init__ import *
import random

class Ball:
    def __init__(self, canvas, color, paddle, bricks, score):
        self.bricks = bricks
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.bottom_hit = False
        # Points to start with at beginning of game
        self.hit = 0   
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color, width=1)
        self.canvas.move(self.id, 230, 461)
        start = [8, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
        random.shuffle(start)
        #print(start)
        self.x = start[0]
        self.y = -start[0]
        self.canvas.move(self.id, self.x, self.y)
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()
        

    def brick_hit(self, pos):
        for brick_line in self.bricks:
            for brick in brick_line:
                brick_pos = self.canvas.coords(brick.id)
                #print(brick_pos)
                try:
                    if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
                        if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                            canvas.bell()
                            # Points gained per brick hit.
                            self.hit += 25
                            file1 = open("highscore.txt","r+")
                            highscore = str(file1.read())
                            file1.close()
                            self.score.configure(text="Score: " + str(self.hit) + "\n\nHighscore: " + highscore)
                            self.canvas.delete(brick.id)
                            return True
                except:
                    continue
        return False
    
        
    def paddle_hit(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                #print("paddle hit")
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        #print(pos)
        start = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
        random.shuffle(start)
        if self.brick_hit(pos):
            self.y = start[0]
        if pos[1] <= 0:
            self.y = start[0]
        if pos[3] >= self.canvas_height:
            self.bottom_hit = True
        if pos[0] <= 0:
            self.x = start[0]
        if pos[2] >= self.canvas_width:
            self.x = -start[0]
        if self.paddle_hit(pos):
            self.y = -start[0]