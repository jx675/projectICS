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
        rect(self.xPaddle, self.yPaddle, self.wPaddle,self.hPaddle)
    
def setup():
    size(720,720)
    background(0)
    stroke(255)
    fill(255)
    rect(p.xPaddle, p.yPaddle,p.wPaddle,p.hPaddle)

p = Paddle(360,700,200,150,5,1)

def draw():
    background(0)
    p.display()
    
def keyPressed():
    if keyCode == RIGHT:
        p.keyHandler[RIGHT] = True
    elif keyCode == LEFT:
        p.keyHandler[LEFT] = True
        
def keyReleased():
    if keyCode == RIGHT:
        p.keyHandler[RIGHT] = False
    elif keyCode == LEFT:
        p.keyHandler[LEFT] = False
