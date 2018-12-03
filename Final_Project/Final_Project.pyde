# #Run once at start
# add_library('minim')
# import os
# path = os.getcwd()
# #player = Minim(this)

# #Variables to keep track of position and speed of ball
# class Ball:
#     def __init__(self,x,y,vx,vy):
#         self.x=x
#         self.y=y
#         self.vx=vx
#         self.vy=vy
    
#     def update(self):
#         self.x += self.vx
#         self.y += self.vy
        
#         #make sure the ball doesn't go outrange
#         if self.y>height:
#             vy=-vy
#         elif self.y<0:
#             vy=-vy
            
#         if x > width or x <0:
#             vx=-vx        
# # Called every re-draw, default 30 times per second
#     def display(self): 
#       vx = 5
#       vy= 5
#       x = 0
#       y = 0
#       ellipse(x, y, 10, 10)
#       # Set fill color to white
#       fill(255);
#       # Draw a circle at position x,y, 10 pixels large
#       ellipse(x, y, 10, 10);
#       # Update position by adding speed

# class Paddle:
#     # x_paddle,y_paddle are the center cooridinates of the paddle
#     def __init__(self,x_paddle,y_paddle,w_paddle,h_paddle,vx_paddle):
#         self.x_paddle=x_paddle
#         self.y_paddle=y_paddle
#         self.w_paddle = w_paddle
#         self.vx_paddle=vx_paddle
        
#     def display(self): 
#         if keyCode == RIGHT or key == 'd': 
#             x_paddle = x_paddle + 5;
#       # Move paddle right
    
#         elif keyCode == LEFT or key == 'a':
#       # Move paddle left
#             x_paddle = x_paddle - 5;
#        # make sure paddle dont go outside at the edge
#         if x_paddle> width:
#             x_paddle= width
#         elif x_paddle<0:
#             x_paddle=0
    
#         #Clear screen to black
#         #background(0);
#         # Set fill color to white
#         fill(255);
#         # draw paddle
#         rect(x_paddle, y_paddle, w_paddle*2+1, 11)
      
# Class Game:
#   def __init__(self,numBlocks,numRows,numCols,centreX,centreY):
#     self.numBlocks = numBlocks
#     self.numRows = numRows
#     self.numCols = numCols
#     # self.centreX = centreX
#     # self.centreY = centreY #centreX/centreY are the centre points of the playing board 
    
#     #add initialised attributes
#   def blocks():
#       #number_of_rows=random.randint(0,5) #make CSV files for positions of different blocks for different 
#       #numbe_o_cols=random.randint(0,5)

#       for r in range(self.numRows):
#           for c in range(self.numCols):
#               self.blocks.append(Block("block.png",40,40,6,360/8*i,150))
#         # x cooridnates of the brick 

#         #y cooridnates of the brick 
#           y= 40*(i/5)+10

#           if blocks[i]==True:
#               # draw the block
#               rect(x+40,y+0,80,20)
#               # 80 an 20 are width and height of the rectang；e
#           if (mouseX>x and mouseX<(x+80) && mouseY>y && mouseY<(y+20)):
#               #make it disapper 
#               blocks[i]==False;

# def setup():
#     size(w,h)
#     background(0)
#     rectMode(CENTER)
#     height=400
#     width= 500
#     size(500, 400)
    
# def draw():

#     textSize(16);
#     text("Score", 80, 390);
#     textAlign(LEFT);
#     text(score, 90, 390);

# def collides():
#     if x_paddle - w_paddle_half < x < x_paddle + w_paddle_half and y_paddle-h_paddle_half < y < y_paddle + h_paddle_half:
#         vy = -vy
    
# # ball hit the rectangle 
    
#     def keyPressed():
# #     if keyCode == LEFT:
   
# #     elif keyCode == RIGHT:
     
# #         if g.pause:
# #             g.music.play()
# #         else:
# #             g.music.pause()
        
# #         g.pause = not g.pause
    

            
# # def keyReleased():
# #     if keyCode == LEFT:
# #         g.mario.keyHandler[LEFT]=False
# #     elif keyCode == RIGHT:
# #         g.mario.keyHandler[RIGHT]=False
# #     elif keyCode == UP:
# #         g.mario.keyHandler[UP]=False
