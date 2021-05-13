import numpy as np
from PIL import Image,ImageDraw
import random,math
import generate as gen
import world
w = 5
h = 5
def main_loop(layers,width,height,generator):
    for layer in range(layers):
        generator.one_pass(100)
    generator.save_image()
        
if __name__ == "__main__":
    gen = gen.Generator(w,h)
    main_loop(10,w,h,gen)
    wrld = world.worldify(Image.open("output.png","r"))
    image = wrld.clean(w,h)
    gen.set_image(image)
