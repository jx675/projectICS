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
        if self.y > p.yPaddle and p.xPaddle<self.x<p.xPaddle+p.wPaddle: #figure out how to make it 'bounce' off surface 
            if self.x < p.xPaddle + p.wPaddle/2:
                self.vx = -8
            elif self.x >  p.xPaddle + p.wPaddle/2:
                self.vx = 8
            elif self.x == p.xPaddle + p.wPaddle/2:
                self.vx = 0
            self.vy = -self.vy
          
        #what to do if ball goes below paddle
        if self.y + (self.h/2) > height:
            blnMissed = True #deal with this condition
            self.x=p.xPaddle + (p.wPaddle/2)
            self.y=p.yPaddle
    
       #make sure ball stays inside width of box
        if self.x + (self.w/2) > width or self.x - (self.w/2) <0:
             self.vx=-self.vx  
             
          #collisions with bricks   
        if self.y + (self.h/2) < br.y + (br.h) and br.x<self.x<br.x+br.w:
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
    def __init__(self,x,y,w,h,colour,numBricks):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.colour = colour
        self.numBricks = numBricks
    
            
    def display(self):
        #self.update()
        stroke(255)
        fill(0,255,0)
        rect(self.x,self.y,self.w,self.h)
        
    
    

def setup():
    size(720,720)
    background(0)
    stroke(255)
    fill(255)
    rect(p.xPaddle, p.yPaddle,p.wPaddle,p.hPaddle)
    #ellipse(b.x,b.y,50,50)

p = Paddle(360,700,200,150,5,1)
br = Bricks(360,100,150,50,255,5)

balls = []

def draw():
    background(0)
    p.display()
    for b in balls: #Find the keycode for spacebar to launch the ball initially//alt. find how to do it with mouseClick//alt continue using UP key
        b.display()  
    br.display()
    
def keyPressed():
    if keyCode == RIGHT:
        p.keyHandler[RIGHT] = True
    elif keyCode == LEFT:
        p.keyHandler[LEFT] = True
        
    if keyCode == UP:
        #so that only one ball is released
        while len(balls) < 1:
            balls.append(Ball(25,25,p.xPaddle+(p.wPaddle/2),p.yPaddle,1,5,False))
            
        
def keyReleased():
    if keyCode == RIGHT:
        p.keyHandler[RIGHT] = False
    elif keyCode == LEFT:
        p.keyHandler[LEFT] = False
