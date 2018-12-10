import os
class Ball:
    def __init__(self,w,h,x,y,vx,vy,blnMissed):
        self.w = w
        self.h = h
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=-vy
        
    def update(self):

        #make sure the ball doesn't go outrange// <0 b/c top left is 0,0
        if self.y - (self.h/2) <0:  
             self.vy=-self.vy
             
        #allowing ball to bounce on paddle and then changing direction based on where it bounces
        if self.y > g.p.yPaddle and g.p.xPaddle<self.x<g.p.xPaddle+g.p.wPaddle: #figure out how to make it 'bounce' off surface 
            if self.x < g.p.xPaddle + g.p.wPaddle/2:
                self.vx = -8
            elif self.x > g.p.xPaddle + g.p.wPaddle/2:
                self.vx = 8
            elif self.x == g.p.xPaddle + g.p.wPaddle/2:
                self.vx = 0
            self.vy = -self.vy
          
        #what to do if ball goes below paddle
        if self.y + (self.h/2) > height:
            blnMissed = True #deal with this condition
            self.x=g.p.xPaddle + (g.p.wPaddle/2)
            self.y=g.p.yPaddle
    
        #make sure ball stays inside width of box
        if self.x + (self.w/2) > width or self.x - (self.w/2) <0:
             self.vx=-self.vx  
             
        #collisions with bricks
        for br in g.br:  
            if br.x<self.x<br.x+br.w and (br.y<self.y<br.y+br.h or self.y == br.y):
                br.numCollisions += 1 #FIX THIS.. WHY IS IT COUNTING SO MANY
                print(br.numCollisions)
                if self.x < br.x + br.w/2:
                    self.vx = -8
                elif self.x >  br.x + br.w/2:
                    self.vx = 8
                elif self.x == br.x + br.w/2:
                    self.vx = 0
                self.vy = -self.vy
            
   # Update position by adding speed to x and y 
        self.x += self.vx
        self.y += self.vy
              
# Called every re-draw, default 30 times per second
    def display(self):
        self.update()
        stroke(255)
        # Set fill color to white
        #fill(255)
        # Draw a circle at position x,y 25 pixels large
        ellipse(self.x,self.y,self.w,self.h)

class Paddle:
    # x_paddle,y_paddle are the center cooridinates of the paddle
    def __init__(self,xPaddle,yPaddle,wPaddle,hPaddle,vx_paddle,dir):
        self.xPaddle=xPaddle
        self.yPaddle=yPaddle
        self.wPaddle = wPaddle
        self.hPaddle = hPaddle
        self.vx_paddle=vx_paddle
        self.dir = dir
        self.keyHandler = {LEFT:False, RIGHT:False}
        
    def update(self):
        # Update position by adding speed to x and y and ensure that paddle does not go off screen
        if self.keyHandler[RIGHT] == True and self.xPaddle+self.wPaddle < width:
            self.xPaddle += self.vx_paddle
        elif self.keyHandler[LEFT] ==True and self.xPaddle >0 :
            self.xPaddle -= self.vx_paddle
        
    def display(self):
        self.update() 
        # Set fill color to white
        stroke(255)
        fill(255)
        # draw paddle
        rect(self.xPaddle,self.yPaddle, self.wPaddle,self.hPaddle)
        
class Bricks:
    def __init__(self,x,y,w,h,numBricks):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.numBricks = numBricks
        self.numCollisions = 0 
        self.fRed = 0
        self.fGreen = 0
        self.fBlue = 0
    
    def update(self):
        if self.numCollisions == 0:
            self.Red = 0
            self.fGreen = 255
            self.fBlue = 0
        elif self.numCollisions == 1:
            self.fRed = 255
            self.fGreen = 230
            self.fBlue = 0
        # elif self.numCollisions == 2:
        #     self.fRed = 255
        #     self.fGreen = 0
        #     self.fBlue = 0
        # elif self.numCollisions > 2:
        #     self.brList.remove(self)

    def display(self):
        self.update()
        stroke(255)
        fill(self.fRed,self.fGreen,self.fBlue)
        rect(self.x,self.y,self.w,self.h)
        
class Game:
    def __init__(self,w,h):
        self.w=w
        self.h=h
        #self.state = "menu"
        self.p = Paddle(360,700,200,150,5,1)
        self.balls = []
        self.br = []
        for br in range(2):
            self.br.append(Bricks(360,500,150,50,5))
        
    def display(self):
        
        stroke(255)
        fill(255)
        rect(self.p.xPaddle,self.p.yPaddle,self.p.wPaddle,self.p.hPaddle)
        self.p.display()
        for b in self.balls:
             b.display() 
        for bricks in self.br:
            bricks.display()
        
def setup():
    size(g.w,g.h)
    background(0)
    stroke(255)
    fill(255)
    rect(g.p.xPaddle, g.p.yPaddle,g.p.wPaddle,g.p.hPaddle)
    #ellipse(b.x,b.y,50,50)

g = Game(720,720)

def draw():
    background(0)
    g.display()
   
   
def keyPressed():
    if keyCode == RIGHT:
        g.p.keyHandler[RIGHT] = True
    elif keyCode == LEFT:
        g.p.keyHandler[LEFT] = True
    if keyCode == UP:
        #so that only one ball is released
        # while len(balls) < 1:
        g.balls.append(Ball(25,25,g.p.xPaddle+(g.p.wPaddle/2),(g.p.yPaddle-12.5),1,5,False))
            
        
def keyReleased():
    if keyCode == RIGHT:
        g.p.keyHandler[RIGHT] = False
    elif keyCode == LEFT:
        g.p.keyHandler[LEFT] = False
