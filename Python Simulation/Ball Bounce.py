import math
from visual import*
import Image
dx=-50
dy=15

#Green comment block was originally user input for drop position, etc.,
#but was commented out, just not deleted.
"""
dx=-20
dy=input("please input the drop y position....recommand 10 or higher")

w=input("if you know the bounce height press '1', if you dont press '2' :")
if w==1:
    bh=input("enter the 1st bounce height")
    res=sqrt(bh/dy)##the equation for resitution
else:
    res=.89
  
else :
    print("try the balls we know!" )
    type1=input("press '1' for b-ball, '2' for tennis ball")
    if type1==1:#b ball
        res=0.83#restitution
    elif type1==2:#t ball
        res=0.72
    else:           #no friction ball. no restitution
        res=1
"""

im = Image.open('tennisball.jpg') 
tex = materials.texture(data=im, mapping='spherical')

im2 = Image.open('BasketballColor.jpg')  
tex2 = materials.texture(data=im2, mapping='spherical')

im3 = Image.open('golfball.jpg')  
tex3 = materials.texture(data=im3, mapping='spherical')


floor = box(pos=(0,0,0), length=100, height=0.5, width=2, color= (1,1,1), material=materials.wood) #width=5, #edit
floor1 = box(pos=(0,0,-5), length=100, height=0.5, width=2, color= (1,1,1), material=materials.wood)
floor2 = box(pos=(0,0,5), length=100, height=0.5, width=2, color= (1,1,1), material=materials.wood)
floor3 = box(pos=(0,0,-10), length=100, height=0.5, width=2, color= (1,1,1), material=materials.wood)

pball = sphere(pos=(dx,dy,-10), radius=1.5, color=color.red, make_trail=True, material=materials.emissive) #edit
ball = sphere(pos=(dx,dy,0), radius=1, material=tex, make_trail=True, color=color.green)
ball2 = sphere(pos=(dx,dy,-5), radius=2, material=tex2, make_trail=True, color=color.orange) #the starting point of the ball .. add z value to make it 3d
ball3 = sphere(pos=(dx,dy,5), radius=.5, material=tex3, make_trail=True)

pball.velocity = vector(4,0)
ball.velocity = vector(4,0)
ball2.velocity = vector(4,0)
ball3.velocity = vector(4,0)#(4,0,0) for 3d motion

gravity = 9.81


dt = 0.01 #delta time frame of the ball
while true:

    rate(100) #rate of speed
    
    pball.pos = pball.pos + pball.velocity*dt   #ball.pos += velocity*dt
    ball.pos = ball.pos + ball.velocity*dt      #ball.pos += velocity*dt
    ball2.pos = ball2.pos + ball2.velocity*dt   #ball.pos += velocity*dt
    ball3.pos = ball3.pos + ball3.velocity*dt   #ball.pos += velocity*dt
    
    if pball.y < .5:
        pball.velocity.y = abs(pball.velocity.y)
    else:
        pball.velocity.y = pball.velocity.y - gravity*dt

    if ball.y < .5:
        ball.velocity.y = abs(ball.velocity.y*0.905)
    else:
        ball.velocity.y = ball.velocity.y - gravity*dt
        
    if ball2.y < .5:
        ball2.velocity.y = abs(ball2.velocity.y*0.79)
    else:
        ball2.velocity.y = ball2.velocity.y - gravity*dt
        
    if ball3.y < .5:
        ball3.velocity.y = abs(ball3.velocity.y*0.78)
    else:
        ball3.velocity.y = ball3.velocity.y - gravity*dt
"""NOTE:
        All lines are original, except for the if-else statements, which are edited, unless otherwise stated.
"""
