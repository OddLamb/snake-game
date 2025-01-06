import pygame
from random import randint
from Particle import Particle
from Snake import Snake
from macros import *

class Game:
    def __init__(self):
        self.running = True
        self.display = pygame.display.set_mode((640,640))
        self.clock = pygame.time.Clock()
    
        self.grid = []
        for x in range(self.display.get_width()//tile_size):
            self.grid.append([])
            for y in range(self.display.get_height()//tile_size):
                self.grid[x].append(-1)
        self.grid[randint(0,len(self.grid)-1)][randint(0,len(self.grid[0])-1)] = 1

        self.snake = Snake()
        self.particles = []
    def drawGrid(self):
        b = 4
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                for pos in self.snake.positions:
                    if x == pos[0] and y == pos[1]:
                        if self.snake.positions.index(pos) != (len(self.snake.positions)-1):
                            pygame.draw.rect(self.display,(80,255,50),pygame.rect.Rect((x*tile_size)+b,(y*tile_size)+b,tile_size-b,tile_size-b))
                        else:
                            pygame.draw.rect(self.display,(80,255,50),pygame.rect.Rect((x*tile_size)+b,(y*tile_size)+b,tile_size-b,tile_size-b))
                if self.grid[x][y] == 1:
                    pygame.draw.rect(self.display,"red",pygame.rect.Rect((x*tile_size)+b,(y*tile_size)+b,tile_size-b,tile_size-b))
    def drawParticles(self):
        for particle in self.particles:
            if particle.life > 0:
                particle.update(self.display)
            else: 
                self.particles.pop(self.particles.index(particle))
    def drawScreen(self):
        self.display.fill("black")
        self.drawGrid()
        self.drawParticles()
        pygame.display.update()
    def gameLoop(self):
        while self.running:
            self.clock.tick(60)
            pygame.display.set_caption(str(int(self.clock.get_fps())))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False
                self.snake.input_ev(e)
            self.snake.update(self.grid,self.particles)
            self.drawScreen()
if __name__ == "__main__":
    game = Game()
    game.gameLoop()