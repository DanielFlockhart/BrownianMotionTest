import numpy as np
from PIL import Image,ImageDraw
import random,math
import generate as gen
import world
w = 100
h = 100
def main_loop(layers,width,height,generator):
    for layer in range(layers):
        generator.one_pass(10000)
    generator.save_image()
    print("here")
        
if __name__ == "__main__":
    gen = gen.Generator(w,h)
    main_loop(10,w,h,gen)
    wrld = world.worldify(Image.open("output.png","r"))
    image = wrld.clean(w,h)
    gen.set_image(image)
