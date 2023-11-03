class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        # Paddle size x y axis
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 485)
        self.x = 0
        self.pausec=0
        self.canvas_width = canvas.winfo_width()
        self.canvas.bind_all("<Left>", self.turn_left)
        self.canvas.bind_all("<Right>", self.turn_right)
        # TODO Pause the game, HINT: something similar as the line above can be done.
        
        

    def draw(self):
        pos = self.canvas.coords(self.id)
        #print(pos)
        if pos[0] + self.x <= 0:
            self.x = 0
        if pos[2] + self.x >= self.canvas_width:
            self.x = 0
        self.canvas.move(self.id, self.x, 0)

    # How fast paddle should move to left or right
    def turn_left(self, event):
        self.x = -3.5

    def turn_right(self, event):
        self.x = 3.5

    def pauser(self,event):
        self.pausec+=1
        if self.pausec==2:
            self.pausec=0
      