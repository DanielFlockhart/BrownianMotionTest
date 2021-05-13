from PIL import Image
import numpy as np
class worldify:
    def __init__(self,img):
        self.image = img
        self.pixels = []
    def clean(self,w,h):
        self.pixels = list(self.image.getdata())
        self.pixels = np.array(self.pixels).reshape(-1,w,3).tolist()
        for y in range(1,len(self.pixels)-1):
            for x in range(1,len(self.pixels[y])-1):
                if(self.pixels[y][x] != self.pixels[y][x+1] and
                   self.pixels[y][x] != self.pixels[y][x-1] and
                   self.pixels[y][x] != self.pixels[y+1][x] and
                   self.pixels[y][x] != self.pixels[y-1][x]):
                    self.pixels[y][x] = self.pixels[y][x+1]
                    
        return self.pixels
