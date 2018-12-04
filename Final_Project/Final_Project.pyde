import os
class Ball:
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=-vy
        
    def update(self):
        # Update position by adding speed to x and y 
       
#make sure the ball doesn't go outrange
        if self.y <0 or (self.y>p.yPaddle and p.xPaddle<self.x<p.xPaddle+p.wPaddle):
             self.vy=-self.vy
             
        if self.x > width or self.x<0:
             self.vx=-self.vx  
  
        self.x += self.vx
        self.y += self.vy
              
# Called every re-draw, default 30 times per second
    def display(self):
        self.update()
        stroke(255)
        # Set fill color to white
        fill(255)
        # Draw a circle at position x,y 25 pixels large
        ellipse(self.x,self.y,25,25)

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

def setup():
    size(720,720)
    background(0)
    stroke(255)
    fill(255)
    rect(p.xPaddle, p.yPaddle,p.wPaddle,p.hPaddle)
  #  ellipse(b.x,b.y,50,50)

p = Paddle(360,700,200,150,5,1)

balls = []

def draw():
    background(0)
    p.display()
    for b in balls: #Find the keycode for spacebar to launch the ball initially//alt. find how to do it with mouseClick//alt continue using UP key
        b.display()    
    
def keyPressed():
    if keyCode == RIGHT:
        p.keyHandler[RIGHT] = True
    elif keyCode == LEFT:
        p.keyHandler[LEFT] = True
        
    if keyCode == UP:
        balls.append(Ball(p.xPaddle,p.yPaddle,5,5))
        
def keyReleased():
    if keyCode == RIGHT:
        p.keyHandler[RIGHT] = False
    elif keyCode == LEFT:
        p.keyHandler[LEFT] = False
