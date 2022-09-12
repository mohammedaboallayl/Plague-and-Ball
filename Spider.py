from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from MainShape import GameShape
from InteringShape import InteringShape
from BallShoter import BallShoter
from numpy.random import randint,choice
from numpy import sin,abs
import pygame
 ################## spider means Plauge #####################
class Spider:
    def __init__(self,walls,x,texture,index):
        self.texture=texture
        self.ImageIndex=index
        self.Walls=walls
        self.SpiserState=0
        self.jump=[-0.2,0.2]
        self.jumpwhich=0
        self.SpiderXPosition=x
        self.SpiderYPosition=100
        self.SpiderXStep=0
        self.SpiderYStep=-1
    def SpiderDraw(self):
        glBindTexture(GL_TEXTURE_2D, self.texture[self.ImageIndex])
        glBegin(GL_POLYGON)
        glTexCoord(0,0)
        glVertex(self.SpiderXPosition,self.SpiderYPosition)
        glTexCoord(1,0)
        glVertex(self.SpiderXPosition+3,self.SpiderYPosition)
        glTexCoord(1,1)
        glVertex(self.SpiderXPosition+3,self.SpiderYPosition+3)
        glTexCoord(0,1)
        glVertex(self.SpiderXPosition,self.SpiderYPosition+3)
        glEnd()
        if self.SpiserState==1:
            return 1
        elif self.SpiderYPosition+3<=0:
            return 2
        else:
            return 0
    def InitPositionJump(self,ballxp,ballyp): ################### main func That call drawing func and simple jump in shaps #################
        if (glutGet(GLUT_ELAPSED_TIME)/1000)%0.2<=0.01:
            self.SpiderYPosition=self.SpiderYPosition+self.jump[self.jumpwhich]
            if self.jumpwhich==0:
                self.jumpwhich=1
            else:
                self.jumpwhich=0
        self.SpiderMotionControle()
        self.BallSpiderCheck(ballxp,ballyp)
    def BallSpiderCheck(self,x,y): ######################## check if ball Killed the Plague ###########################
        if (x<self.SpiderXPosition+3 and x>self.SpiderXPosition) or (x+3>self.SpiderXPosition and x+3<self.SpiderXPosition+3):
            if (y+3<self.SpiderYPosition+3 and y+3>self.SpiderYPosition)or (y>self.SpiderYPosition and y<self.SpiderYPosition+3):
                self.SpiserState=1

    def SpiderMotionControle(self):###################### spider Motion Controle #############
        if (glutGet(GLUT_ELAPSED_TIME)/1000)%0.7<=0.01:
            self.SpiderYPosition+=self.SpiderYStep
            self.SpiderXPosition+=self.SpiderXStep
            if (self.SpiderYPosition >=85  or self.SpiderYPosition+3 <=45):
                self.SpiderXStep=choice([1,-1])
                self.SpiderYStep=choice([0,-1])
            else:
                self.SpiderXStep=0
                self.SpiderYStep=choice([0,-1])
            for i in range(1,self.Walls.shape[0],1):
                ####################### Up controle ######################################
                if (self.SpiderXPosition+3 >=self.Walls[i,0]and self.SpiderXPosition+3 <=self.Walls[i,1])or\
                        (self.SpiderXPosition<=self.Walls[i,1] and self.SpiderXPosition>=self.Walls[i,0]):
                    if self.SpiderYPosition-1<=self.Walls[i,3] and self.SpiderYPosition+1>=self.Walls[i,3]:
                        if i>=self.Walls.shape[0]-2:
                            self.SpiderXStep=1
                        elif i<=self.Walls.shape[0]-2:
                            self.SpiderXStep=-1
                        self.SpiderYStep=0
                ####################### Right And Left ######################################
                # elif i<= self.Walls.shape[0]-2 :
                #     if (self.SpiderYPosition+3 >=self.Walls[i,2]and self.SpiderYPosition+3 <=self.Walls[i,3])or (self.SpiderYPosition<=self.Walls[i,3] and self.SpiderYPosition>=self.Walls[i,2]):
                #         self.SpiderXStep=0
                #         self.SpiderYStep=choice([0,-1])
            if self.SpiderXPosition+3>=100:
                self.SpiderXStep=0
                self.SpiderYStep=-1
            elif self.SpiderXPosition<=0:
                self.SpiderXStep=0
                self.SpiderYStep=-1
