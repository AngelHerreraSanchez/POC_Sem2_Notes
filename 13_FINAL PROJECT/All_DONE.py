import tkinter as tk

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 610
        self.height = 400
        self.bg = "#AAAAFF"
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg=self.bg)        
        self.canvas.pack()
        self.pack()

        self.items = {}
        self.ball = None
        self.paddle = Paddle(self.canvas, self.width / 2, 326)
        self.items[self.paddle.item] = self.paddle

        for x in range(5, self.width - 75, 75):
            self.add_brick(x + 37.5, 50, 2)
            self.add_brick(x + 37.5, 70, 1)
            self.add_brick(x + 37.5, 90, 1)

        self.hud = None
        self.setup_game()
        self.canvas.focus_set()
        self.canvas.bind("<Left>", lambda _: self.paddle.move(-10))
        self.canvas.bind("<Right>", lambda _: self.paddle.move(10))

    def setup_game(self):
        self.add_ball()
        self.update_lives_text()
        self.text = self.draw_text(300, 200, "Press Space to start")
        self.canvas.bind("<space>", lambda _: self.start_game())

    def add_ball(self):
        if self.ball is not None:
            self.ball.delete()
        paddle_coords = self.paddle.get_position()
        x = (paddle_coords[0] + paddle_coords[2]) / 2
        self.ball = Ball(self.canvas, x, 310)
        self.paddle.set_ball(self.ball)

    def add_brick(self, x, y, hits):
        brick = Brick(self.canvas, x, y, hits)
        self.items[brick.item] = brick

    def draw_text(self, x, y, text, size="40"):
        font = ("Helvetica", size)
        return self.canvas.create_text(x, y, text=text, font=font)
    
    def update_lives_text(self):
        text = "Lives: %s" % self.lives
        if self.hud == None:
            self.hud = self.draw_text(50, 20, text, 15)
        else:
            self.canvas.itemconfig(self.hud, text=text)

    def start_game(self):
        self.canvas.unbind("<space>")
        self.canvas.delete(self.text)
        self.paddle.ball = None
        self.game_loop()

    def game_loop(self):
        #YOUDO-36:  call self's check_collisions method
        num_bricks = len(self.canvas.find_withtag("brick"))
        if num_bricks == 0:
            #YOUOD_37:  set self's ball's speed variable to None
            self.draw_text(300, 200, "You win!")
        elif self.ball.get_position()[3] >= self.height:
            self.ball.speed = None
            self.lives -= 1
            if self.lives < 0:
                self.draw_text(300, 200, "Game Over")
            else:
                self.after(1000, self.setup_game)
        else:
            self.ball.update()
            self.after(50, self.game_loop())

    def check_collisions(self):
        #YOUDO_38:  get the ball's coords from self.get_position and store in ball_coords
        items = self.canvas.find_overlapping(*ball_coords)
        objects = [self.items[x] for x in items if x in self.items]
        self.ball.collide(objects)

class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)
    
    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)

class Ball(GameObject):
    def __init__(self, canvas, x, y):  #(x, y) is the center of the ball
        #YOUDO-01: create a radius variable for self and set to 10
        #YOUDO-02: create a direction variable for self and set to [1, -1]
        #This represents the speed of the ball in the x and y direction.  Example:  [xspeed, yspeed]  
        #YOUDO-03:  create a speed variable for self and set to 10
        #YOUDO-04:  create an x1 variable and set to x - self's radius
        #YOUDO-05:  create an y1 variable and set to y - self's radius
        #YOUDO-06:  create an x2 variable and set to x + self's radius
        #YOUDO-07:  create an y2 variable and set to y + self's radius  
        #YOUDO-08:  create a color variable and set to "white"
        item = canvas.create_oval(x1, y1, x2, y2, fill=color)
        super(Ball, self).__init__(canvas, item)

    def update(self):
        #YOUDO-28:  create a coords variable and initialize to self.get_position()
        #YOUDO-29:  create a width variable and initialize to self.canvas.winfo_width()
        if coords[0] <= 0 or coords[2] >= width:
            self.direction[0] *= -1
        if coords[1] <= 0:
            self.direction[1] *= -1
        x = self.direction[0] * self.speed
        y = self.direction[1] * self.speed
        #YOUDO_30:  call the move method for self passing in the appropriate arguments

    def collide(self, game_objects):
        #YOUDO-30:  same logic as YOUDO-28
        #YOUDO-31:  create a variable x for the center of the ball.  so you'll need coords[0] and coords[2] and math midpoint stuff :)
        if len(game_objects) > 1:
            #YOUDO-32:  flip the direction like we did in update for the y direction (index 1)
            pass  #YOUDO-33:  remove this when done
        elif len(game_objects) == 1:
            game_object = game_objects[0]
            #YOUDO-34:  create a coords variable for game_object from get_position like before
            if x > coords[2]:
                self.direction[0] = 1
            elif x < coords[0]:
                self.direction[0] = -1
            else:
                self.direction[1] *= -1 
        
        for game_object in game_objects:
            if(isinstance(game_object, Brick)):
                game_object.hit()

class Paddle(GameObject):
    def __init__(self, canvas, x, y):  #(x, y) is the center of the paddle
        #YOUDO-09:  create a width variable for self and set to 80
        #YOUDO-10:  create a height variable for self and set to 10
        #YOUDO-11:  create a ball variable for self and set to None
        #YOUDO-12:  create an x1 variable and set to x - self's width / 2
        #YOUDO-13:  create an y1 variable and set to y - self's height / 2
        #YOUDO-14:  create an x2 variable and set to x + self's width / 2
        #YOUDO-15:  create an y2 variable and set to y + self's height / 2
        #YOUDO-16:  create a color variable and set to "blue"
        #YOUDO-17:  use create_rectangle on canvas to create an item variable with x1, y1, x2, y2, color
        super(Paddle, self).__init__(canvas, item)
        

    def set_ball(self, ball):
        self.ball = ball

    def move(self, offset):
        coords = self.get_position()
        width = self.canvas.winfo_width()
        x1 = coords[0]
        y1 = coords[1]
        x2 = coords[2]
        y2 = coords[3]
        if x1 + offset >= 0 and x2 + offset <= width:
            super(Paddle, self).move(offset, 0)
        if self.ball is not None:
            self.ball.move(offset, 0)

class Brick(GameObject):
    COLORS = {1 : "#999999", 2 : "#555555", 3 : "#222222"}

    def __init__(self, canvas, x, y, hits):
        #YOUDO-18:  create a width variable for self and initialize to 75
        #YOUDO-19:  create a height variable for self and initialize to 20
        #YOUDO-20:  create a hits variable for self and initialize to hits 
        color = Brick.COLORS[hits]
        #YOUDO-21:  create an x1 variable and set to x - self's width / 2
        #YOUDO-22:  create an y1 variable and set to y - self's height / 2
        #YOUDO-23:  create an x2 variable and set to x + self's width / 2
        #YOUDO-24:  create an y2 variable and set to y + self's height / 2
        #YOUDO-25:  use create_rectangle on canvas to create an item variable with x1, y1, x2, y2, color, tags="brick"        
        super(Brick, self).__init__(canvas, item)

    def hit(self):
        #YOUDO-26:  subtract one from self.hits
        #YOUDO-27:  check if self.hits is equal to 0.  If it is call self.delete().  If not 
        #YOUDO-27-part2:  call self.canvas.itemconfig(self.item, fill=Brick.COLORS[self.hits])
        pass #YOUDO-28:  Remove this pass    

if __name__ == "__main__":    
    root = tk.Tk()
    game = Game(root)
    root.title("BREAKOUT")
    root.mainloop()