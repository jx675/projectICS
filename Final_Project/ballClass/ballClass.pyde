import os
class Ball:
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
    
    def update(self):
        # Update position by adding speed to x and y 
        self.x += self.vx
        self.y += self.vy
        
    #make sure the ball doesn't go outrange
        if self.y>height or self.y<0:
             self.vy=-self.vy

        if self.x > width or self.x <0:
             self.vx=-self.vx        
# Called every re-draw, default 30 times per second
    def display(self):
        self.update()
        stroke(255)
        # Set fill color to white
        fill(255)
        # Draw a circle at position x,y 25 pixels large
        ellipse(self.x,self.y,25,25)

def setup():
    size(720,720)
    background(0)
    stroke(255)
    fill(255)
    ellipse(b.x,b.y,50,50)

b = Ball(360,720,5,5)

def draw():
    background(0)
    if keyCode == UP: #Find the keycode for spacebar to launch the ball initially//alt. find how to do it with mouseClick//alt continue using UP key
        b.display()
