from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
# controler class for mouse and window shape of witch view

class GameShape:
    def __init__(self,walls,index,draw_array):
        self.which_img=index
        self.points_print=walls
        self.draw_array=draw_array
    def display(self):
        self.draw_array(self.points_print,self.which_img)



