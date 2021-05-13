import numpy as np
from PIL import Image,ImageDraw
import random,math


class Generator:
    def __init__(self,WIDTH,HEIGHT):
        self.im = Image.new('RGB', (WIDTH, HEIGHT), (0,0,255))
        self.draw = ImageDraw.Draw(self.im)
        self.w = WIDTH
        self.h = HEIGHT
    def sample(self,mean,sd):
        return np.random.normal(mean,sd,1000)
    
    def one_pass(self,steps):
        x = random.randint(0,self.w)
        y = random.randint(0,self.h)
        for z in range(steps):
            self.draw.point([int(x), int(y)], (0,255,0))
            x+=random.choice(self.sample(0,0.5))
            y+=random.choice(self.sample(0,0.5))
    def save_image(self):
        self.im.save(f'output.png', 'PNG')
    def set_image(self,pixels):
        self.im = Image.new('RGB', (self.w, self.h), (0,0,255))
        self.draw = ImageDraw.Draw(self.im)
        for y in range(self.h):
            for x in range(self.w):
                self.draw.point([x,y], (pixels[y][x][0],pixels[y][x][1],pixels[y][x][2]))
    
