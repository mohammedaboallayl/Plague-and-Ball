from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from MainShape import GameShape
from InteringShape import InteringShape
from BallShoter import BallShoter
from SpiderContainer import Container
import pygame
from numpy import array,random
from Music import Music
# controler class for mouse and window shape of witch view
################## spider means Plauge #####################
class Display():
    def __init__(self):
        self.which_shape=0 #there is 4 shaps this define which
        self.PlayerPosition=0 # define where is point X
        self.images_list=["ANTI_PLAGUE.png","PLAGUE.png","Plague_Mask.jpg","Plague_Mask.jpg","Black_Death1.jpg","Exit.tif","play.tif"] #images
        self.texture=0 # for Texture array
        self.Score=0 #player score
        self.Life=3 #player life
        self.Stage2Colled=False #we use to reinit InteringPoints array for drawing and controle
        self.SpiderNewNum=0 # change Plague numpers
        self.TextPosition,self.Text=[10,90,80,90],["SCORE = 0","LIFE = 0"] # Score and life draw
        self.MainShapeImageRanke=[4,2,2,2,2,2] #mainshape image rank for binding
        self.InsiderImageRanke=[4,6,5] #Insider image rank for binding
        self.MusicPlayer=Music() #Music class controler
        self.InteringPoints=array([[0,100,0,100],# drawing points
                                   [9,30,65,75],
                                   [45,60,45,55],
                                   [70,95,50,60],
                                   [20,30,75,85],
                                   [78,95,60,70]])
    def init_clases(self):#init classes with wanted data
        self.GameShape=GameShape(self.InteringPoints,self.MainShapeImageRanke,self.draw_array)
        self.InteringShape=InteringShape(self.InsiderImageRanke,self.draw_array)
        self.BallShoter=BallShoter(self.InteringPoints,self.texture,0)
        self.Container=Container(self.InteringPoints,self.texture,1,self.SpiderNewNum,self.MusicPlayer)
    def Stage2Data(self): # restoring new drawing points array
        if self.which_shape==2:
            self.InteringShape=array([[0,100,0,100],
                                     [15,20,45,85],
                                     [45,54,45,85],
                                     [70,75,45,85]])
        elif self.which_shape==3:
            self.InteringShape=array([[0,100,0,100],
                                     [15,25,60,85],
                                     [45,60,45,60],
                                     [80,85,45,85]])
        self.BallShoter.Walls=self.GameShape.points_print=self.InteringShape
        for i in range(len(self.Container.SpiderList)):
            if self.Container.SpiderList[i] !=None:
                self.Container.SpiderList[i].Walls=self.BallShoter.Walls
        self.Container.Walls=self.BallShoter.Walls
        self.Stage2Colled=False
    def draw_text(self,string, x, y): #draw text
        glLineWidth(3)
        glColor(1, 0, 0)  # WHITE COLOR
        glPushMatrix()
        glTranslate(x, y, 0)
        glScale(0.03, 0.03, 1)
        string = string.encode()
        for c in string:
            glutStrokeCharacter(GLUT_STROKE_ROMAN, c)
        glPopMatrix()
    def draw_array(self,points_print,which_img): # used to draw array_points
        for i in range(points_print.shape[0]):
            glBindTexture(GL_TEXTURE_2D, self.texture[which_img[i]])
            glBegin(GL_POLYGON)
            for j in range(points_print.shape[1]-2):
                if j==1:
                    glTexCoord(j,j)
                    glVertex(points_print[i,j],points_print[i,j+2])
                    glTexCoord(j,0)
                    glVertex(points_print[i,j],points_print[i,j+1])
                else:
                    glTexCoord(0,0)
                    glVertex(points_print[i,j],points_print[i,j+2])
                    glTexCoord(0,1)
                    glVertex(points_print[i,j],points_print[i,j+3])
            glEnd()
    def init_window(self): #init the window of drawing
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0,100,0,100,-1,1)
        glMatrixMode(GL_MODELVIEW)
    def MainInint(self): #to init window image binding and loading
        self.init_window()
        self.MusicPlayer.MainGlobalMusic()
        self.init_images()
        self.init_clases()
    def init_images(self): #images generations and loading
          # Generate 5 textures
        glEnable(GL_TEXTURE_2D)
        self.texture = glGenTextures(7)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        for i in range(len(self.images_list)):
            imgload = pygame.image.load(self.images_list[i])
            img = pygame.image.tostring(imgload, "RGBA", 1) # 0) # Serializing the image to a string
            width = imgload.get_width()
            height = imgload.get_height()
            glBindTexture(GL_TEXTURE_2D, self.texture[i])
            glTexParameter(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
            glTexParameter(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
            glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) # GL_CLAMP)
            glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    def MainDisplay(self): #drawing func
        if self.Score>=30 and not self.Stage2Colled:
            self.which_shape=2
            self.Stage2Colled=True
        if self.Score>=50 and  self.Stage2Colled:
            self.which_shape=3
            self.Stage2Colled=True
        if self.which_shape==0:
            self.InteringShape.display()
            self.draw_text("Click s for strate Shot ",5,75)
            self.draw_text("Click  a for right shot",5,70)
            self.draw_text("Click d for left shot",5,65)
            glColor(1,1,1)
        elif self.which_shape==1:
            self.GameShape.display()
            for i in range(len(self.Text)):
                self.draw_text(self.Text[i],self.TextPosition[2*i],self.TextPosition[2*i+1])
            glColor(1, 1, 1)
            self.BallXP,self.BallYP=self.BallShoter.BollShutingDrawn()
            self.TextPosition,self.Text,self.Score,self.Life=self.Container.Draw(self.BallXP,self.BallYP)
            self.BallShoter.RestorPosition()
            self.BallShoter.PlayerDraw(self.PlayerPosition)
        else:
            if self.Stage2Colled:
                self.Stage2Data()
            self.GameShape.display()
            for i in range(len(self.Text)):
                self.draw_text(self.Text[i],self.TextPosition[2*i],self.TextPosition[2*i+1])
            glColor(1, 1, 1)
            self.BallXP,self.BallYP=self.BallShoter.BollShutingDrawn()
            self.TextPosition,self.Text,self.Score,self.Life=self.Container.Draw(self.BallXP,self.BallYP)
            self.BallShoter.RestorPosition()
            self.BallShoter.PlayerDraw(self.PlayerPosition)
        #glFlush()
        if self.Life<=0:
            glutDestroyWindow(1)
        glutSwapBuffers()

    def SpiderNumControle(self): #change spider number
        self.Container.AddedNewSpiderNumber +=1
        self.Container.SpiderNumperState=True

######################## mouse keybord func ###############################
    def Mouse(self,x,y):
        self.PlayerPosition=((x/glutGet(GLUT_WINDOW_WIDTH))*100)-3
    def KeyBord(self,key,x,y):
        if self.which_shape==0:
            return 0
        if key==b"s":
            self.BallShoter.BollShutingState(self.PlayerPosition,0,self.MusicPlayer.BallInitShot)
        elif key==b"a":
            self.BallShoter.BollShutingState(self.PlayerPosition,1,self.MusicPlayer.BallInitShot)
        elif key==b"d":
            self.BallShoter.BollShutingState(self.PlayerPosition,-1,self.MusicPlayer.BallInitShot)
    def Click(self,Button,status,x,y):
        x=(x/glutGet(GLUT_WINDOW_WIDTH))*100
        y=(y/glutGet(GLUT_WINDOW_HEIGHT))*100
        if self.which_shape==1:
            x,y=0,0
        if x>=40 and x<=60:
            if y<=70 and y>= 50:
                glutDestroyWindow(1)
            elif y<=40 and y>=30:
                self.which_shape=1
            else:
                pass


m=Display()
def Timer(v):
    m.MainDisplay()
    if ((glutGet(GLUT_ELAPSED_TIME)/1000)%5<=0.01 and m.Score>10) and m.Container.AddedNewSpiderNumber<=15:
        m.SpiderNumControle()
    glutTimerFunc(5,Timer,100)
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
    glutInitWindowSize(800,700)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"spider_game")
    m.MainInint()
    #print(np.random.choice([1,-1]))
    glutMouseFunc(m.Click)
    glutKeyboardFunc(m.KeyBord)
    glutPassiveMotionFunc(m.Mouse)
    glutDisplayFunc(m.MainDisplay)
    glutTimerFunc(0,Timer,0)
    glutMainLoop()

if __name__=="__main__":
    main()
