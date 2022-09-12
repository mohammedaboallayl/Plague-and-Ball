from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import pygame
# controler class for mouse and window shape of witch view


class InteringShape:
    def __init__(self,index,draw_array):
        self.which_img=index
        self.draw_array=draw_array
        self.points_print=np.array([[0,100,0,100],
                                    [40,60,60,70],
                                    [40,60,30,40]])


    def display(self):

        self.draw_array(self.points_print,self.which_img)
        return [47,63,47,34],["Play","Exit"]
