from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy
import pygame
class BallShoter:
    def __init__(self,walls,texture,index):
        self.Walls=walls
        self.Texture=texture
        self.ImageIndex=index
        self.BollShutingStates=False
        self.ShutingPosition=0
        self.BollYStep=1
        self.BollXStep=0
        self.BollXPosition=1
        self.BollYPosition=1
    def PlayerDraw(self,x):
        glBindTexture(GL_TEXTURE_2D, self.Texture[0])
        glBegin(GL_POLYGON)
        glTexCoord(0,0)
        glVertex(x,0)
        glTexCoord(1,0)
        glVertex(x+5,0)
        glTexCoord(1,1)
        glVertex(x+5,5)
        glTexCoord(0,1)
        glVertex(x,5)
        glEnd()
    def BollShutingState(self,x,shutangle,MusicPlayer):
        if self.BollShutingStates==False:
            self.ShutingPosition=x
            self.BollXStep=shutangle
            MusicPlayer()
            self.BollShutingStates=True

    def BollShutingDrawn(self):
        if self.BollShutingStates:
            glBindTexture(GL_TEXTURE_2D, self.Texture[0])
            glBegin(GL_POLYGON)
            glTexCoord(0,0)
            glVertex(self.BollXPosition+self.ShutingPosition,self.BollYPosition)
            glTexCoord(1,0)
            glVertex(self.BollXPosition+self.ShutingPosition+3,self.BollYPosition)
            glTexCoord(1,1)
            glVertex(self.BollXPosition+self.ShutingPosition+3,self.BollYPosition+3)
            glTexCoord(0,1)
            glVertex(self.BollXPosition+self.ShutingPosition,self.BollYPosition+3)
            glEnd()
            return self.BollXPosition+self.ShutingPosition,self.BollYPosition
        else:
            return 0,0

    def RestorPosition(self):
        if self.BollShutingStates:
            self.BollControler()
            self.BollYPosition+=0.7*self.BollYStep
            self.BollXPosition+=0.7*self.BollXStep
    def BollControler(self):
        for i in range(1,self.Walls.shape[0]):

            ############### Down And Up Of Wall Controle #################################
            if (self.BollXPosition+self.ShutingPosition+4 >=self.Walls[i,0]and self.BollXPosition+self.ShutingPosition+4 <=self.Walls[i,1])\
                    or (self.BollXPosition+self.ShutingPosition<=self.Walls[i,1] and self.BollXPosition+self.ShutingPosition>=self.Walls[i,0]):
                if self.BollYPosition+0.5<=self.Walls[i,3] and self.BollYPosition+3>=self.Walls[i,3]:
                    if i==1 or i==3:
                        if self.BollXPosition+self.ShutingPosition>=self.Walls[i,1]-5:
                            pass
                        else:
                            self.BollYStep=1
                    else:
                        self.BollYStep=1
                elif i>=4:
                    pass
                elif self.BollYPosition+3>=self.Walls[i,2] and self.BollYPosition<=self.Walls[i,2]:
                    self.BollYStep=-1
            ############### Right And Left Of Wall Controle #################################
            if self.BollXPosition+self.ShutingPosition+4 >=self.Walls[i,0] and self.BollXPosition+self.ShutingPosition <=self.Walls[i,0]:
                if self.BollYPosition+3>=self.Walls[i,2] and self.BollYPosition<=self.Walls[i,3]:
                    self.BollXStep=-1
            elif self.BollXPosition+self.ShutingPosition <=self.Walls[i,1] and self.BollXPosition+self.ShutingPosition+1 >=self.Walls[i,1]:
                if self.BollYPosition+3>=self.Walls[i,2] and self.BollYPosition<=self.Walls[i,3]:
                    self.BollXStep=1
        ############### Main Walls Controle #################################
        if self.BollXPosition+self.ShutingPosition >=100 or self.BollXPosition+self.ShutingPosition+3 <=0:
            self.BollXStep=-1
            if self.BollXPosition+self.ShutingPosition+3 <=0:
                self.BollXStep=1
        elif self.BollYPosition+4>=100 :
            self.BollYStep=-1
            ###############BollYPosition Under Zero Controle #################################
        if self.BollYPosition+4<=0:
            self.BollYStep=1
            self.BollYPosition=1
            self.BollXPosition=1
            self.BollShutingStates=False
