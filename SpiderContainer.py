from Spider import Spider
from numpy.random import randint
class Container:
    def __init__(self,walls,texture,index,addednewlist,MusicPlayer):
        self.texture=texture
        self.MusicPlayer=MusicPlayer
        self.ImageIndex=index
        self.Walls=walls
        self.Life=3
        self.Score=0
        self.SpiderNumper=10
        self.AddedNewSpiderNumber=addednewlist
        self.SpiderList=[]
        self.SpiderNumperState=True
    def InitSpiderList(self): ################ contoling and redrawing spider lists ###########
        if self.SpiderNumperState:
            for i in range(self.SpiderNumper+self.AddedNewSpiderNumber):
                if len(self.SpiderList)<self.SpiderNumper+self.AddedNewSpiderNumber:
                    self.SpiderList.append(Spider(self.Walls,randint(0,96),self.texture,self.ImageIndex))
                elif self.SpiderList[i]==None:
                    self.SpiderList[i]=Spider(self.Walls,randint(0,96),self.texture,self.ImageIndex)
            self.SpiderNumperState=False
        elif self.SpiderList.count(None)>self.SpiderNumper/3:
            self.SpiderNumperState=True

    def Draw(self,ballxpos,ballypos):
        self.InitSpiderList()
        for i in range(self.SpiderNumper+self.AddedNewSpiderNumber):
            if self.SpiderList[i] != None:
                self.SpiderList[i].InitPositionJump(ballxpos,ballypos)
                if self.SpiderList[i].SpiderDraw()==1:
                    self.MusicPlayer.BallCrashSpiderMusic()
                    self.SpiderList[i]=None
                    self.Score+=1
                elif self.SpiderList[i].SpiderDraw()==2:
                    self.SpiderList[i]=None
                    self.Life-=1
        return [10,90,80,85],["SCORE = "+str(self.Score),"LIFE = "+str(self.Life)],self.Score,self.Life



