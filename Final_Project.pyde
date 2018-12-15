import os,random, time
add_library('minim')
path = os.getcwd()+ '/images/'
player = Minim(this)
class Ball():
    def __init__(self,w,h,x,y,vx,vy):
        self.w = w
        self.h = h
        self.x=x
        self.y=y
        self.vx=vx
        self.img=loadImage(path+"ball.png")
        self.vy=-vy
        self.ballReleased = False
        self.collide = player.loadFile(path+"/sounds/collide.mp3")
        self.bonusCollisions = 0
        
    def update(self):
        #make sure the ball doesn't go outrange// <0 b/c top left is 0,0
        if self.y - (self.h/2) <0:  
             self.vy=-self.vy
             
        #allowing ball to bounce on paddle and then changing direction based on where it bounces
        if self.y > game[level-1].p.yPaddle - (self.h/2)-10  and game[level-1].p.xPaddle<self.x<game[level-1].p.xPaddle+game[level-1].p.wPaddle: 
            if self.x < game[level-1].p.xPaddle + game[level-1].p.wPaddle/2:
                self.vx = -15
            elif self.x > game[level-1].p.xPaddle + game[level-1].p.wPaddle/2:
                self.vx = 15
            elif self.x == game[level-1].p.xPaddle + game[level-1].p.wPaddle/2:
                self.vx = 0
            self.vy = -self.vy
            
        #what to do if ball goes below paddle
        if self.y + (self.h/2) > height:

            if len(game[level-1].balls) == 1:
                game[level-1].lives -= 1
            #if the user misses a ball with the bonus ball in play, the don't lose a life but the bonus ball disappears
            elif len(game[level-1].balls) > 1:
                del game[level-1].balls[1]
            if game[level-1].lives == 0:
                game[level-1].lose = True
            
            self.ballReleased = False
            self.x=game[level-1].p.xPaddle+(game[level-1].p.wPaddle/2-15)
            self.y=game[level-1].p.yPaddle-(self.h/2)-10
            self.vy = 0
            self.vx = 0
            
        #make sure ball stays inside width of box
        if self.x + (self.w/2) > width or self.x - (self.w/2) <0:
             self.vx=-self.vx  
             
        #collisions with bricks
        for br in game[level-1].br:  
            if br.x<self.x<br.x+br.w and (br.y<self.y<br.y+br.h or self.y == br.y) and (br.unlocked == False):
                if self.x < br.x + br.w/2:
                    self.vx = -10
                elif self.x >  br.x + br.w/2:
                    self.vx = 10
                elif self.x == br.x + br.w/2:
                    self.vx = 0
                self.vy = -self.vy
                
                br.numCollisions += 1
    
                self.collide.rewind()
                self.collide.play() 
                if br.v != 4:
                    game[level-1].score += 10
                if game[level-1].bonusState == "bomb" or game[level-1].bonusState == "star" :
                    self.bonusCollisions += 1
                    if self.bonusCollisions > 8:
                        game[level-1].p.wPaddle = 200
                        game[level-1].p.img=loadImage(path+"board.png")
                        self.bonusCollisions = 0
                        game[level-1].bonusState = "" 
                        
        
            
        #keep the ball on the platform
        if self.ballReleased == False and game[level-1].p.xPaddle<self.x<game[level-1].p.xPaddle+game[level-1].p.wPaddle and self.y==game[level-1].p.yPaddle-(game[level-1].bH/2)-10 and (game[level-1].p.keyHandler[RIGHT] == True or game[level-1].p.keyHandler[LEFT] == True):
            self.x = game[level-1].p.xPaddle + game[level-1].p.wPaddle/2 -15
     

   # Update position by adding speed to x and y 
        self.x += self.vx
        self.y += self.vy
        
    # Called every re-draw, default 30 times per second
    def display(self):
        self.update()
        stroke(255)
        # draw the ball
        image(self.img,self.x,self.y,self.w,self.h)
        #textSize(38)
        #text(str(self.grade),10,10)
 
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
        self.bonus = "" 
        
        if self.v < 4:
            for i in range(4):
                self.imgs.append(loadImage(path+"/"+str(v+i*4)+".png"))
        elif self.v == 4:
            self.imgs.append(loadImage(path+"/13.png"))
        
    def display(self):
        stroke(255)
        if self.v<4:
            
            if self.numCollisions <= 2:
                image(self.imgs[self.numCollisions],self.x,self.y,self.w,self.h)
            elif self.numCollisions > 2:
                #normal bricks are destroyed after 3 collisions
                game[level-1].score += 50
                game[level-1].br.remove(self)
                game[level-1].numBricksDestroyed += 1
                
    
        elif self.v == 4:
            #the unbreakable brick does not change
            image(self.imgs[0],self.x,self.y,self.w,self.h)
        elif self.v == 5:
            #bonus bricks destroyed after one hit and release bonuses
            if self.numCollisions == 0:
                image(self.imgs[0],self.x,self.y,self.w,self.h)
            elif self.numCollisions > 0:
                index = game[level-1].br.index(self)
                game[level-1].br[index].unlocked = True
                if  game[level-1].br[index].bonus.y > game[level-1].p.yPaddle - (self.h/2):
                    game[level-1].br.remove(self)
                    game[level-1].numBricksDestroyed += 1
                    
class Bonus:
    def __init__(self,x,y,w,h,vy):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vy = vy
    
    def update(self):
        self.y += self.vy
   
    def display(self):
        self.update()
        for bricks in game[level-1].br:
                image(self.img,self.x,self.y,self.w,self.h)
                
class Star(Bonus):
    def __init__(self,x,y,w,h,vy):
        Bonus.__init__(self,x,y,w,h,vy)
        self.img = loadImage(path+"/star.png")
        
    def update(self): 
        self.y += self.vy 
        #if the star is captured
        if self.y > game[level-1].p.yPaddle - (self.h/2)-10 and game[level-1].p.xPaddle<self.x<game[level-1].p.xPaddle+game[level-1].p.wPaddle:
            #if you are currently in a bonus the ball will split
            if game[level-1].bonusState == "star":
                game[level-1].balls.append(Ball(game[level-1].bW,game[level-1].bH,game[level-1].balls[0].x,game[level-1].balls[0].x,-game[level-1].balls[0].vx,game[level-1].balls[0].vy))
            else:
                #if it is the first bonus then the paddle will expand
                game[level-1].bonusState = "star"
                game[level-1].score += 50
                game[level-1].p.wPaddle = 300
                #ensure that the paddle stays within bounds even if it expands at the rightmost edge
                if game[level-1].p.xPaddle + game[level-1].p.wPaddle > width:
                    game[level-1].p.xPaddle -= (game[level-1].p.xPaddle + game[level-1].p.wPaddle) - width
                game[level-1].p.img=loadImage(path+"huge_board.png")
                        
        
class Bomb(Bonus):
    def __init__(self,x,y,w,h,vy):
        Bonus.__init__(self,x,y,w,h,vy)
        self.img = loadImage(path+"/bomb.png")
    
    def update(self): 
        self.y += self.vy 
        if self.y > game[level-1].p.yPaddle - (self.h/2)-10 and game[level-1].p.xPaddle<self.x<game[level-1].p.xPaddle+game[level-1].p.wPaddle:
            #if it the second bomb captured whilst already a smaller brick then game over
            if game[level-1].bonusState == 'bomb':
               game[level-1].lose = True
            else:
                #if it is the first brick then the paddle decreases in size
                game[level-1].bonusState = "bomb"
                game[level-1].score -= 50
                game[level-1].p.wPaddle = 150
                game[level-1].p.img=loadImage(path+"small_board.png")
    
            
class Game:
    def __init__(self,w,h,bW,bH,level):
        self.w=w
        self.h=h
        self.bW = bW
        self.bH = bH
        self.state = "menu"
        self.p = Paddle(360,684,200,36,10)
        self.balls = []
        self.br = []
        self.numBricks = 0
        self.numBricksDestroyed = 0
        self.numUnbreakableBricks = 0
        self.img=loadImage(path+"background.png")
        self.music = player.loadFile(path+"/sounds/music.mp3")
        self.pause=False
        self.pauseSound = player.loadFile(path+"/sounds/pause.mp3")
        self.score = 0
        self.bonusState = ""
        self.imgLives = loadImage(path+"/lives.png")
        self.lives = 3
        self.win = False
        self.lose = False
        self.level = level

        if self.level == 1:
            self.music.loop()
            #creating the bricks on the screen 
            for i in range(2):
                self.br.append(Bricks(500*i,300*i,150,50,0))
                self.numBricks += 1
            for i in range(2):
                self.br.append(Bricks(200-i*150, 150*i,150,50,1))
                self.numBricks += 1
            for i in range(3):
                self.br.append(Bricks(375+i*100,75*i,150,50,2))
                self.numBricks += 1
            for i in range(3):
                self.br.append(Bricks(550-i*200,150*i,150,50,3))
                self.numBricks += 1
            
            #creating the unbreakable brick
            self.br[8].v = 4
            self.br[8].imgs[0] = loadImage(path+"/13.png")
            self.numUnbreakableBricks += 1     
            
            #creating star bricks in random positions                   
            randBonus = random.randint(0,len(self.br)-1)
            numRandBonus = 0
            while numRandBonus < 2:
                #making sure brick has not already been assigned a bonus and it is not the unbreakable brick
                while self.br[randBonus].v == 4 or self.br[randBonus].bonus != "":
                    randBonus = random.randint(0,len(self.br)-1)
                    
                self.br[randBonus].v = 5
                self.br[randBonus].imgs[0] = loadImage(path+"/14.png")
                self.br[randBonus].bonus = Star(self.br[randBonus].x+(self.br[randBonus].w/2),self.br[randBonus].y+self.br[randBonus].h,30,30,15)
                numRandBonus += 1
        
            #creating bomb bricks in random positions  
            randBonus = random.randint(0,len(self.br)-1)
            numRandBonus = 0
            while numRandBonus < 2:
                #making sure brick has not already been assigned a bonus and it is not the unbreakable brick
                while self.br[randBonus].v == 4 or self.br[randBonus].bonus != "":
                    randBonus = random.randint(0,len(self.br)-1)
                
                self.br[randBonus].v = 5
                self.br[randBonus].imgs[0] = loadImage(path+"/15.png")
                self.br[randBonus].bonus = Bomb(self.br[randBonus].x+(self.br[randBonus].w/2),self.br[randBonus].y+self.br[randBonus].h,40,40,15)
                numRandBonus += 1
        
            #intialising a list with one ball at the beginning of the game
            while len(self.balls) < 1:
                self.balls.append(Ball(self.bW,self.bH,self.p.xPaddle+(self.p.wPaddle/2-15),self.p.yPaddle-(self.bH/2)-10,0,0))
        elif self.level == 2:
            
            self.score = score
            for i in range(3):
                self.br.append(Bricks(180*i,50+90*i,150,50,0))
                self.numBricks += 1
            for i in range(2):
                self.br.append(Bricks(300-i*270,50+125*i,150,50,1))
                self.numBricks += 1
            for i in range(3):
                self.br.append(Bricks(570-i*200,50+100*i,150,50,2))
                self.numBricks += 1
            for i in range(3):
                self.br.append(Bricks(270*i+25,350-50*i,150,50,3))
                self.numBricks += 1
            for i in range(2):
                self.br.append(Bricks(570,170+180*i,150,50,2))
                self.numBricks += 1
            
            #creating the unbreakable brick
            self.br[2].v = 4
            self.br[2].imgs[0] = loadImage(path+"/13.png")
            self.numUnbreakableBricks += 1
                
            #creating star bricks in random positions                   
            randBonus = random.randint(0,len(self.br)-1)
            numRandBonus = 0
            while numRandBonus < 2:
                #making sure brick has not already been assigned a bonus and it is not the unbreakable brick
                while self.br[randBonus].v == 4 or self.br[randBonus].bonus != "":
                    randBonus = random.randint(0,len(self.br)-1)
                        
                self.br[randBonus].v = 5
                self.br[randBonus].imgs[0] = loadImage(path+"/14.png")
                self.br[randBonus].bonus = Star(self.br[randBonus].x+(self.br[randBonus].w/2),self.br[randBonus].y+self.br[randBonus].h,30,30,15)
                numRandBonus += 1
            
            #creating bomb bricks in random positions  
            randBonus = random.randint(0,len(self.br)-1)
            numRandBonus = 0
            while numRandBonus < 2:
                #making sure brick has not already been assigned a bonus and it is not the unbreakable brick
                while self.br[randBonus].v == 4 or self.br[randBonus].bonus != "":
                    randBonus = random.randint(0,len(self.br)-1)
                
                self.br[randBonus].v = 5
                self.br[randBonus].imgs[0] = loadImage(path+"/15.png")
                self.br[randBonus].bonus = Bomb(self.br[randBonus].x+(self.br[randBonus].w/2),self.br[randBonus].y+self.br[randBonus].h,40,40,15)
                numRandBonus += 1
        
            #intialising a list with one ball at the beginning of the game
            while len(self.balls) < 1:
                self.balls.append(Ball(self.bW,self.bH,self.p.xPaddle+(self.p.wPaddle/2-15),self.p.yPaddle-(self.bH/2)-10,0,0))
        
    def display(self):    
        image(self.img,0,0,game[level-1].w,game[level-1].h)
        self.p.display()
        textSize(30)
        text("Score: " + str(game[level-1].score),20,640)
        
        for b in self.balls:
            b.display() 
            
        for bricks in self.br:
            bricks.display()
            
        #displaying the bonus falling 
        for bricks in self.br:
            if bricks.unlocked == True:
                bricks.bonus.display()
        
        for i in range(self.lives):
            image(self.imgLives,20+i*60,550,50,50)
    
        
imgin1=loadImage(path+"Instruction1.png")
imgin2=loadImage(path+"Instruction2.png")
img=loadImage(path+"background.png") 
img2=loadImage(path+"pause.png")  


level = 1
game = []
score = 0
def setup():
    size(720, 720)
    for g in range(1,3):
        game.append(Game(720,720,25,25,g)) 
    

def draw():
    global level,score
    global img, img2, imgin1, imgin2
    
    if level == 2 and game[level-1].state != "play":
        game[level-1].state = "play"
    
    if game[level-1].state == "menu":
       # background(0)
        image(img,0,0,game[level-1].w,game[level-1].h)
        textSize(50)
        text("Brick Breaker",game[level-1].w//3-50, game[level-1].h//3-40)
        textSize(36)
        text("Play Game",game[level-1].w//2.8, game[level-1].h//2.8+40)
        text("Instruction", game[level-1].w//2.8, game[level-1].h//2.8+140)  
        if game[level-1].w//2.8 < mouseX < game[level-1].w//2.8 + 220 and game[level-1].h//2.8 < mouseY < game[level-1].h//2.8+50:
            fill(255,0,0)
            text("Play Game",game[level-1].w//2.8, game[level-1].h//2.8+40)
            fill(255)
        elif game[level-1].w//2.8 < mouseX < game[level-1].w//2.8 + 220 and game[level-1].h//2.8+100 < mouseY < game[level-1].h//2.8+150:
            fill(255,0,0)    
            text("Instructions", game[level-1].w//2.8, game[level-1].h//2.8+140)    
            fill(255)
    
    elif game[level-1].state == "instruction2":
        image(imgin2,0,0,game[level-1].w,game[level-1].h)
        text("Menu",game[level-1].w//4, game[level-1].h//3+400)
        text("Previous Page",game[level-1].w-300, game[level-1].h//3+400)
        
        if  game[level-1].w//4-50 < mouseX < game[level-1].w//4+100 and game[level-1].h//3+350 < mouseY < game[level-1].h//3+450:
            fill(255,0,0) 
            textSize(40)
            text("Menu",game[level-1].w//4, game[level-1].h//3+400)
            fill(255)
            
        if  game[level-1].w-350 < mouseX < game[level-1].w-100 and game[level-1].h//3+350 < mouseY < game[level-1].h//3+500:
            fill(255,0,0) 
            textSize(40)
            text("Previous Page",game[level-1].w-300, game[level-1].h//3+400)
            fill(255)    
    elif game[level-1].state == "instruction":
        #background(0)
        image(imgin1,0,0,game[level-1].w,game[level-1].h)
        text("Next Page",game[level-1].w-300, game[level-1].h//3+400)
        text("Menu",game[level-1].w//4, game[level-1].h//3+400)
        if  game[level-1].w//4-50 < mouseX < game[level-1].w//4+100 and game[level-1].h//3+350 < mouseY < game[level-1].h//3+450:
            fill(255,0,0) 
            textSize(40)
            text("Menu",game[level-1].w//4, game[level-1].h//3+400)
            fill(255)
           # text("Next Page",game[level-1].w-300, game[level-1].h//3+400)
        if  game[level-1].w-350 < mouseX < game[level-1].w-100 and game[level-1].h//3+350 < mouseY < game[level-1].h//3+500:
            fill(255,0,0) 
            textSize(40)
            text("Next Page",game[level-1].w-300, game[level-1].h//3+400)
            fill(255)
                    
    elif game[level-1].state == "play":
        if game[level-1].pause == False:

            background(255)
            game[level-1].display()
        else:
      
            fill(255,0,0)
            image(img2,300,300,182,137)
        
    if game[level-1].numBricksDestroyed == game[level-1].numBricks - game[level-1].numUnbreakableBricks:
        if level == 1:
            game[level].score = game[level-1].score
            game[level].lives = game[level-1].lives
            game[level].music.pause()
            level += 1
        
        elif level == 2:
            game[level-1].win = True
        
    
        
    if game[level-1].lose == True:
        image(loadImage(path+"/gameover.png"),720/4,720/4)
        textSize(40)
        text("Retry",game[level-1].w/2.3, game[level-1].h-100)
        if  game[level-1].w/2.3-100 < mouseX < game[level-1].w/2.3+100 and game[level-1].h-180 < mouseY < game[level-1].h-80:
            fill(255,0,0) 
            textSize(40)
            text("Retry",game[level-1].w/2.3, game[level-1].h-100)
            fill(255)
        
        for ball in game[level-1].balls:
            ball.ballReleased = True
            ball.vy = 0
            ball.vx = 0
        game[level-1].p.vx_paddle = 0
        
    if game[level-1].win == True:
        image(loadImage(path+"/win.gif"),720/4,720/4)
        textSize(40)
        for ball in game[level-1].balls:
            ball.ballReleased = True
            ball.vy = 0
            ball.vx = 0
        game[level-1].p.vx_paddle = 0
        
def mouseClicked():
    #Page Menu
    if game[level-1].state == "menu" and game[level-1].w//2.8 < mouseX < game[level-1].w//2.8 + 220 and game[level-1].h//2.8 < mouseY < game[level-1].h//2.8+50:
        game[level-1].state="play"
    elif game[level-1].state == "menu" and game[level-1].w//2.8 < mouseX < game[level-1].w//2.8 + 220 and game[level-1].h//2.8+100 < mouseY < game[level-1].h//2.8+150:
        game[level-1].state="instruction"
     
    #Page Instruction
    elif game[level-1].state == "instruction" and game[level-1].w//4-50 < mouseX < game[level-1].w//4+100 and game[level-1].h//3+350 < mouseY < game[level-1].h//3+450:
        game[level-1].state="menu"
    elif game[level-1].state == "instruction" and game[level-1].w-350 < mouseX < game[level-1].w-100 and game[level-1].h//3+350 < mouseY < game[level-1].h//3+500:
        game[level-1].state="instruction2"

     
    #Page Instruction2   
    elif game[level-1].state == "instruction2" and game[level-1].w-350 < mouseX < game[level-1].w-100 and game[level-1].h//3+350 < mouseY < game[level-1].h//3+500:
        game[level-1].state="instruction"
    elif game[level-1].state == "instruction2" and game[level-1].w//2.5-100 < mouseX < game[level-1].w//2.5+100 and game[level-1].h//3+350 < mouseY < game[level-1].h//3+450:
        game[level-1].state="menu"
        
    elif game[level-1].state == "play" and game[level-1].lose == True and game[level-1].w/2.3-100 < mouseX < game[level-1].w/2.3+100 and game[level-1].h-180 < mouseY < game[level-1].h-80:
        game[level-1].__init__(720,720,25,25,level)
        game[level-1].music.pause()
       
 
def keyPressed():
    if keyCode == RIGHT:
        game[level-1].p.keyHandler[RIGHT] = True
    elif keyCode == LEFT:
        game[level-1].p.keyHandler[LEFT] = True
    elif keyCode == UP:
        for balls in game[level-1].balls: 
            if balls.ballReleased == False:
                for ball in game[level-1].balls: 
                    ball.vx = 0.0001 
                    ball.vy = -15
                    ball.ballReleased = True
    elif keyCode == 80:
   
        game[level-1].pauseSound.rewind()
        game[level-1].pauseSound.play()
        
        if game[level-1].pause:
            game[level-1].music.play()
        else:
            game[level-1].music.pause()
        
        game[level-1].pause = not game[level-1].pause

def keyReleased():
    if keyCode == RIGHT:
        game[level-1].p.keyHandler[RIGHT] = False
    elif keyCode == LEFT:
        game[level-1].p.keyHandler[LEFT] = False
