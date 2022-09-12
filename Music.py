import pygame as pg
class Music: ##### music Class #########
    def __init__(self):
        pg.init()
    def MainGlobalMusic(self):
        pg.mixer.music.load("Black-Death.wav")
        pg.mixer.music.play(-1)
    def BallCrashSpiderMusic(self):
        pg.mixer.Sound("Shot.wav").play()
    def BallInitShot(self):
        pg.mixer.Sound("laser.wav").play()
