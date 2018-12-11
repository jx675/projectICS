import os,random
path = os.getcwd()+ '/images/'
class Ball:
    def __init__(self,w,h,x,y,vx,vy):
        self.w = w
        self.h = h
        self.x=x
        self.y=y
        self.vx=vx
        self.img=loadImage(path+"ball.png")
        self.vy=-vy
        self.ballReleased = False
        self.blnMissed = False
        
    def update(self):
        
        #make sure the ball doesn't go outrange// <0 b/c top left is 0,0
        if self.y - (self.h/2) <0:  
             self.vy=-self.vy
    
        #allowing ball to bounce on paddle and then changing direction based on where it bounces
        if self.y  > g.p.yPaddle - (self.h/2)-10  and g.p.xPaddle<self.x<g.p.xPaddle+g.p.wPaddle: #figure out how to make it 'bounce' off surface 
            if self.x < g.p.xPaddle + g.p.wPaddle/2:
                self.vx = -15
            elif self.x > g.p.xPaddle + g.p.wPaddle/2:
                self.vx = 15
            elif self.x == g.p.xPaddle + g.p.wPaddle/2:
                self.vx = 0
            self.vy = -self.vy
            
        #what to do if ball goes below paddle
        if self.y + (self.h/2) > height:
            self.blnMissed = True #deal with this condition
            self.ballReleased = False
            self.x=g.p.xPaddle+(g.p.wPaddle/2-15)
            self.y=g.p.yPaddle-(self.h/2)-10
            self.vy = 0
            self.vx = 0
    
        #make sure ball stays inside width of box
        if self.x + (self.w/2) > width or self.x - (self.w/2) <0:
             self.vx=-self.vx  
             
        #collisions with bricks
        for br in g.br:  
            if br.x<self.x<br.x+br.w and (br.y<self.y<br.y+br.h or self.y == br.y):
                if self.x < br.x + br.w/2:
                    self.vx = -10
                elif self.x >  br.x + br.w/2:
                    self.vx = 10
                elif self.x == br.x + br.w/2:
                    self.vx = 0
                self.vy = -self.vy
                br.numCollisions += 1 
        
        #keep the ball on the platform
        if self.ballReleased == False and g.p.xPaddle<self.x<g.p.xPaddle+g.p.wPaddle and self.y==g.p.yPaddle-(g.bH/2)-10 and (g.p.keyHandler[RIGHT] == True or g.p.keyHandler[LEFT] == True):
            self.x = g.p.xPaddle + g.p.wPaddle/2 -15
            #print(self.vx)

   # Update position by adding speed to x and y 
        self.x += self.vx
        self.y += self.vy
        
# Called every re-draw, default 30 times per second
    def display(self):
        self.update()
        stroke(255)
        # Draw a circle at position x,y 25 pixels large
        image(self.img,self.x,self.y,self.w,self.h)

class Paddle:
    # x_paddle,y_paddle are the cooridinates of the paddle
    def __init__(self,xPaddle,yPaddle,wPaddle,hPaddle,vx_paddle):
        self.xPaddle=xPaddle
        self.yPaddle=yPaddle
        self.wPaddle = wPaddle
        self.hPaddle = hPaddle
        self.vx_paddle=vx_paddle
        self.keyHandler = {LEFT:False, RIGHT:False}
        self.img=loadImage(path+"board.png")
        
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
        image(self.img,self.xPaddle,self.yPaddle,self.wPaddle,self.hPaddle)
        
class Bricks:
    def __init__(self,x,y,w,h,v):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.v = v
        self.numCollisions = 0
        self.imgs = []
        self.unlocked = False
        self.bonus = [] 
        if self.v < 4:
            for i in range(4):
                self.imgs.append(loadImage(path+"/"+str(v+i*4)+".png"))
        elif self.v == 4:
            self.imgs.append(loadImage(path+"/13.png"))
        elif self.v == 5:
            self.imgs.append(loadImage(path+"/14.png"))
        
    def display(self):
        stroke(255)
        if self.v<4:
            if self.numCollisions <= 2:
                image(self.imgs[self.numCollisions],self.x,self.y,self.w,self.h)
            elif self.numCollisions > 2:
                g.br.remove(self)
        elif self.v == 4:
            image(self.imgs[0],self.x,self.y,self.w,self.h)
        elif self.v == 5:
            if self.numCollisions == 0:
                image(self.imgs[0],self.x,self.y,self.w,self.h)
            elif self.numCollisions > 0:
                index = g.br.index(self)
                g.br[index].unlocked = True
                        
class Star:
    def __init__(self,x,y,w,h,vy):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vy = vy
        self.img = loadImage(path+"/star.png")
        
    def update(self):
        self.y += self.vy
        if self.y > g.p.yPaddle - (self.h/2)-10  and g.p.xPaddle<self.x<g.p.xPaddle+g.p.wPaddle:
            for bricks in g.br:
                if bricks.unlocked == True:
                    bricks.bonus = ""
    def display(self):
        self.update()
        image(self.img,self.x,self.y,self.w,self.h)
        

        
class Game:
    def __init__(self,w,h,bW,bH,numBricks):
        self.w=w
        self.h=h
        self.bW = bW
        self.bH = bH
        self.state = "menu"
        self.p = Paddle(360,684,200,36,10)
        self.balls = []
        self.br = []
        self.numBricks = numBricks
        self.img=loadImage(path+"background.png")
            
        for i in range(2):
            self.br.append(Bricks(500*i,300*i,150,50,0))
        
        for i in range(2):
            self.br.append(Bricks(200-i*150, 150*i,150,50,1))
            
        for i in range(3):
            self.br.append(Bricks(375+i*100,75*i,150,50,2))
        
        for i in range(3):
            self.br.append(Bricks(550-i*200,150*i,150,50,3))
            
        self.br[8].v = 4
        self.br[8].imgs[0] = loadImage(path+"/13.png")     
                           
        randBonus = 8
        numRandBonus = 0
        while numRandBonus != 2:
            while randBonus == 8:
                randBonus = random.randint(0,len(self.br)-1)
            self.br[randBonus].v = 5
            self.br[randBonus].imgs[0] = loadImage(path+"/14.png")
            self.br[randBonus].bonus.append(Star(self.br[randBonus].x+self.br[randBonus].x/2,self.br[randBonus].y+self.br[randBonus].h,30,30,15))
            randBonus = 8
            numRandBonus += 1
        while len(self.balls) < 1:
            self.balls.append(Ball(bW,bH,self.p.xPaddle+(self.p.wPaddle/2-15),self.p.yPaddle-(bH/2)-10,0,0))
            
    def display(self):    
        image(self.img,0,0,g.w,g.h)
        #rect(self.p.xPaddle,self.p.yPaddle,self.p.wPaddle,self.p.hPaddle)
        self.p.display()
        for b in self.balls:
            b.display() 
        for bricks in self.br:
            bricks.display()
        for bricks in self.br:
            if bricks.unlocked == True:
                for bonus in bricks.bonus:
                    bonus.display()
        
img=loadImage(path+"background.png")  
def setup():
    size(g.w,g.h)

g = Game(720,720,25,25,4)

def draw():
    global img
    if g.state == "menu":
       # background(0)
        image(img,0,0,g.w,g.h)
        textSize(50)
        text("Brick Breaker",g.w//3-50, g.h//3-40)
        textSize(36)
        text("Play Game",g.w//2.8, g.h//2.8+40)
        text("Instructions", g.w//2.8, g.h//2.8+140)  
        if g.w//2.8 < mouseX < g.w//2.8 + 220 and g.h//2.8 < mouseY < g.h//2.8+50:
            fill(255,0,0)
            text("Play Game",g.w//2.8, g.h//2.8+40)
            fill(255)
        elif g.w//2.8 < mouseX < g.w//2.8 + 220 and g.h//2.8+100 < mouseY < g.h//2.8+150:
            fill(255,0,0)    
            text("Instructions", g.w//2.8, g.h//2.8+140)    
            fill(255)
    elif g.state == "play":
        background(255)
        g.display()
        #print("game1")
    elif g.state == "instruction":
        #background(0)
        image(img,0,0,g.w,g.h)
        textSize(50)
        text("BrickBreaker Instruction",g.w//5-50, g.h//3-40)
        textSize(30)
        text("1)Use Up key to shoot",g.w//5-100, g.h//3+20)
        text("2)Use left and right key to move the paddle",g.w//5-100, g.h//3+60)
        text("3)Your goal is to eliminate all possible bricks!",g.w//5-100, g.h//3+100)
        text("4)Avoid bombs and try to catch stars!",g.w//5-100, g.h//3+140)
        textSize(50)
        text("Return",g.w//5-100, g.h//3+240)
        
def mouseClicked():
    if g.state == "menu" and g.w//2.8 < mouseX < g.w//2.8 + 220 and g.h//2.8 < mouseY < g.h//2.8+50:
        g.state="play"
    if g.state == "menu" and g.w//2.8 < mouseX < g.w//2.8 + 220 and g.h//2.8+100 < mouseY < g.h//2.8+150:
        g.state="instruction"
    if g.state == "instruction" and g.w//5-150 < mouseX < g.w//5 + 100 and g.h//3+200 < mouseY < g.h//3+280:
        g.state="menu"
        print("menu")
 
def keyPressed():
    if keyCode == RIGHT:
        g.p.keyHandler[RIGHT] = True
    elif keyCode == LEFT:
        g.p.keyHandler[LEFT] = True
    if keyCode == UP:
        for balls in g.balls: 
            if balls.ballReleased == False:
                for ball in g.balls: 
                    ball.vx = 0.0001 
                    ball.vy = -15
                    ball.ballReleased = True

def keyReleased():
    if keyCode == RIGHT:
        g.p.keyHandler[RIGHT] = False
    elif keyCode == LEFT:
        g.p.keyHandler[LEFT] = False
