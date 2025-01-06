from math import cos, sin, radians
from pygame import font
font.init()
class Particle:
    def __init__(self,_text="text",_life=60,_col="white",_x=0,_y=0,_dir=0,_spd=2,_size=32):
        self.text = _text
        self.life = _life
        self.col = _col
        self.x, self.y = _x,_y
        self.dir = _dir
        self.spd = _spd
        self.font = font.SysFont("comic sans",_size)
    def update(self,display):
        if self.life > 0:
            self.x+=cos(radians(self.dir))*self.spd
            self.y+=sin(radians(self.dir))*self.spd

            text = self.font.render(self.text,True,self.col)
            display.blit(text,(self.x,self.y))
            self.life-=1