from FractalWorld import *

w = FractalWorld(width=1500,height=1000,delay=0) #creates our world, with some arguments for height, width and delay
f = Fractal() #creates a Fractal, which is the same as a turtle in turtleworld.
f.y = -450 # sets the Fractal's y-posistion to -450, which is at the bottom of the canvas.
f.heading = 90 # turns the fractal to face "north" on the screen.

def tree(f,s,d):
  if d == 0:
    pass
  else:
    pd(f)
    fd(f,s,width=d)
    rt(f,40)
    tree(f,s/1.5,d-1)
    lt(f,80)
    tree(f,s/1.5,d-1)
    rt(f,40)
    pu(f)
    fd(f,-s)

tree(f,300,7)
wait_for_user()