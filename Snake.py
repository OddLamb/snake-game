from pygame import K_RIGHT, K_LEFT, K_UP, K_DOWN, KEYDOWN
from math import cos, sin, radians
from random import randint
from Particle import Particle
from macros import *

class Snake:
    def __init__(self):
        self.positions = [(0,0)]
        self.direction = 0
        self.timer = 0
        self.tick = 10
    def reset(self):
        self.positions = [(0,0)]
        self.direction = 0
        self.timer = 0
        self.tick = 10
    def update_pos(self,grid=[],particles=[]):
        for i in range(len(self.positions)):
            if i != (len(self.positions)-1):
                self.positions[i] = (self.positions[i+1][0],self.positions[i+1][1])
            else:
                next_pos = (round(self.positions[i][0]+cos(radians(self.direction*90))),round(self.positions[i][1]+sin(radians(self.direction*90))))
                if next_pos in self.positions:
                    self.reset()
                    break
                else:
                    if next_pos[0] < len(grid) and next_pos[1] < len(grid[0]) and next_pos[0] >= 0 and next_pos[1] >= 0:
                        if grid[next_pos[0]][next_pos[1]] == 1:
                            grid[next_pos[0]][next_pos[1]] = -1
                            grid[randint(0,len(grid)-1)][randint(0,len(grid[0])-1)] = 1
                            for i in range(randint(10,15)):
                                particles.append(Particle("*",45,"red",next_pos[0]*tile_size,next_pos[1]*tile_size,randint(0,360),2,64))
                            self.positions.append(next_pos)
                            self.tick *= .95
                        else:
                            self.positions[i] = next_pos
                    else:
                        p = self.positions[i]
                        if next_pos[0] < 0:
                            p = (len(grid)-1,p[1])
                        elif next_pos[0] > len(grid)-1:
                            p = (0,p[1])

                        if next_pos[1] < 0:
                            p = (p[0],len(grid))
                        elif next_pos[1] > len(grid)-1:
                            p = (p[0],0)
                        self.positions[i] = p 
    def update(self,grid=[],particles=[]):
        if self.timer > 0:
            self.timer-=1
        else:
            self.update_pos(grid,particles)
            self.timer+=self.tick
    def input_ev(self,e):
        if e.type == KEYDOWN:
            next_dir = self.direction
            if e.key == K_RIGHT:
                if next_dir != 2:
                    next_dir = 0
            elif e.key == K_DOWN:
                if next_dir != 3:
                    next_dir = 1
            elif e.key == K_LEFT:
                if next_dir != 0:
                    next_dir = 2
            elif e.key == K_UP:
                if next_dir != 1:
                    next_dir = 3
            if next_dir != self.direction:
                self.direction = next_dir