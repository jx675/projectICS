#Run once at start
def setup(): 
    size(500, 400)
add_library('minim')
import os
path = os.getcwd()
player = Minim(this)


#Variables to keep track of position and speed of ball
Class Ball:
     def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy

     def update(self,):
        self.x += self.vx
        self.y += vy
        
        #make sure the ball doesn't go outrange
        if self.y>h:
            vy=-vy
        elif self.y<0:
            vy=-vy
            
        if x > width or x <0:
            vx=-vx
            

# Called every re-draw, defaul 30 times per second
    def display(self): 
        vx = 5
        vy= 5
        x = 0
        y = 0
        ellipse(x, y, 10, 10)
    #Clear screen to black
    background(0);
    # Set fill color to white
    fill(255);
    # Draw a circle at position x,y, 10 pixels large
    ellipse(x, y, 10, 10);
    # Update position by adding speed

Class Paddle:
    def __init__(self,x,y,w,vx):
        self.x=x
        self.y=y
        self.vx=vx
        
    def display(self): 
   
        if keyCode == RIGHT or key == 'd': 
            x = x + 5;
      # Move paddle right
    
        elif keyCode == LEFT or key == 'a':
      # Move paddle left
            x = x - 5;
      # make sure paddle dont go outside  
        if x> width:
            x= width
        elif x<0:
            x=0
    
        #Clear screen to black
        #background(0);
        # Set fill color to white
        fill(255);
        # draw paddle
        rect(x, y, w+1, 11)
  
def setup():
    size(w,h)
    background(0)
    
def draw():

    textSize(16);
    text("Score", 80, 390);
    textAlign(LEFT);
    text(score, 90, 390);


# def keyPressed():
#     if keyCode == LEFT:
   
#     elif keyCode == RIGHT:
     
#         if g.pause:
#             g.music.play()
#         else:
#             g.music.pause()
        
#         g.pause = not g.pause
    

            
# def keyReleased():
#     if keyCode == LEFT:
#         g.mario.keyHandler[LEFT]=False
#     elif keyCode == RIGHT:
#         g.mario.keyHandler[RIGHT]=False
#     elif keyCode == UP:
#         g.mario.keyHandler[UP]=False
