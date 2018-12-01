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

     def update(self):
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
    # x_paddle,y_paddle are the center cooridinates of the paddle
    def __init__(self,x_paddle,y_paddle,w_paddle_half,h_paddle_half,vx_paddle):
        self.x_paddle=x_paddle
        self.y_paddle=y_paddle
        self.vx_paddle_half=vx_paddle_half
        
    def display(self): 
        if keyCode == RIGHT or key == 'd': 
            x_paddle = x_paddle + 5;
      # Move paddle right
    
        elif keyCode == LEFT or key == 'a':
      # Move paddle left
            x_paddle = x_paddle - 5;
     
       # make sure paddle dont go outside at the edge
        if x_paddle> width:
            x_paddle= width
        elif x_paddle<0:
            x_paddle=0
    
        #Clear screen to black
        #background(0);
        # Set fill color to white
        fill(255);
        # draw paddle
        rect(x_paddle, y_paddle, w_paddle*2+1, 11)
 
def blocks():
    Number_of_blocks = 20
    
    for i in range(8):
        self.blocks.append(Block(300,300,20,self.g,"star.png",40,40,6,360/8*i,150))
        x = i%100+10
        y= 40*(i/5)+10
        rect(x+40,y+19,80,20)
    
      


def setup():
    size(w,h)
    background(0)
    
    rectMode(CENTER)
    
def draw():

    textSize(16);
    text("Score", 80, 390);
    textAlign(LEFT);
    text(score, 90, 390);

def collides():
    if x_paddle - w_paddle_half < x < x_paddle + w_paddle_half and y_paddle-h_paddle_half < y < y_paddle + h_paddle_half:
        vy = -vy
    
# ball hit the rectangle 
    
    def keyPressed():
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
