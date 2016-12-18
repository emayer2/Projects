from visual import *
from time import clock, sleep
from random import Random, random



# Stars interacting gravitationally
# Program uses Numeric Python arrays for high speed computations
# Adapted by Lensyl Urbano January 4th, 2006.



class uSwitch:

    def __init__(self, radius=1.0,init_val=0, pos=vector(0,0,0), title="Switch"):

        self.title = title
        self.value = init_val
        

        self.bits = frame(pos=pos)
        self.button = sphere(frame=self.bits, radius = radius, color = self.get_color())
        self.title = label(frame=self.bits, pos=(0,radius*1.2,0),
                           text=self.title, height=10, box=0,
                           xoffset=0, yoffset=0, space = 2)
        self.val_label = label(frame=self.bits, pos=(0,-radius*1.2,0),
                               text=self.get_val(),height=10, box=0, xoffset=0, yoffset=0, space = 2)

        
    def switch(self):
        if self.value == 1:
            self.value = 0
            #self.button.color = color.red
        else:
            self.value = 1
            #self.button.color = color.blue
        self.val_label.text = self.get_val()
        self.button.color = self.get_color()
        #print self.get_val()

    def get_val(self):
        if self.value == 1:
            val = "On"
        else:
            val = "Off"
        return val

    def get_color(self):
        if self.value == 1:
            col = color.red
        else:
            col = color.blue
        return col



win=600
Nstars = 20  # change this to have more or fewer stars
G = 6.7e-11 # Universal gravitational constant

# Typical values
Msun = 2E30
Rsun = 2E9
Rtrail = 2e8

L = 0.5e11

vsun = 0.8*sqrt(G*Msun/Rsun)


print """
Right button drag to rotate view.
Left button drag up or down to move in or out.
Press "s" to pause simulation
Press "g" to restart simulation
"""

origx = 0
origy = 0
w = 704 #+4+4
h = 576 #+24+4
scene.width=w
scene.height=h
scene.x = origx
scene.y = origy

#setting up camera moves lurbano
maxRange = 2*L
minRange = 0.75*L
lastRange = maxRange
startRange = vector(maxRange, maxRange, maxRange)

Rsteps = 200
start_steps = 400


scene = display(title="Stars", width=w, height=h, x = 0, y=0,
                range=startRange, forward=(-1,-1,-1))

scene.range = startRange * (1.0-(0.5))
scene.autocenter = 0

##xaxis = curve(pos=[(0,0,0), (L,0,0)], color=(0.5,0.5,0.5))
##yaxis = curve(pos=[(0,0,0), (0,L,0)], color=(0.5,0.5,0.5))
##zaxis = curve(pos=[(0,0,0), (0,0,L)], color=(0.5,0.5,0.5))

Stars = []
colors = [color.red, color.green, color.blue,
          color.yellow, color.cyan, color.magenta]

poslist = []
plist = []
mlist = []
rlist = []

rv = Random(10)

#print rv



for i in range(Nstars):

    x = -L+2*L*rv.random()
    y = -L+2*L*rv.random()
    z = -L+2*L*rv.random()
    r = Rsun/2+Rsun*rv.random()

    Stars = Stars+[sphere(pos=(x,y,z), radius=r, color=colors[i % 6])]
    #Stars[-1].trail = curve(pos=[Stars[-1].pos], color=colors[i % 6], radius=Rtrail)
    Stars[-1].trail = curve( color=colors[i % 6], radius=Rtrail)
    Stars[-1].alive = 1
    Stars[-1].showtrail = 0
    Stars[-1].vec = 0.0

    mass = Msun*r**3/Rsun**3
    px = mass*(-vsun+2*vsun*rv.random())
    py = mass*(-vsun+2*vsun*rv.random())
    pz = mass*(-vsun+2*vsun*rv.random())
    poslist.append((x,y,z))
    plist.append((px,py,pz))
    mlist.append(mass)
    rlist.append(r)

pos = array(poslist)
p = array(plist)
m = array(mlist)
m.shape = (Nstars,1) # Numeric Python: (1 by Nstars) vs. (Nstars by 1)
radius = array(rlist)

vcm = sum(p,0)/sum(m) # velocity of center of mass
#print "p=", p
print "vcm, sum(p), sum(m)", vcm, sum(p), sum(m)
p = p-m*vcm # make total initial momentum equal zero

#create control window - lurbano
cwin = display(title="Controls", width=200, height=100,
               x=0, y=h+24)
trail_but = uSwitch(title="Trails")
ride_but = uSwitch(title="Ride", pos=(2.5,0,0))
ride_star = -1

t = 0.0

dt = 1000.0
Nsteps = 0
pos = pos+(p/m)*(dt/2.) # initial half-step
time = clock()
Nhits = 0


#pause before startup
#sleep(15.0)

###scene_rot_period = 5.0 #seconds for a full rotation of scene
##
###rotate scene
##for i in range(360):
##    scene.forward = rotate(scene.forward, angle=pi/180.0, axis=(0,1,0))
##    sleep(5.0/360.0)
##    
##sleep(5.0)

while 1:
    rate(120)

    # Compute all forces on all stars
    try: #numpy
        r = pos-pos[:,newaxis] # all pairs of star-to-star vectors
        for n in range(Nstars):
            r[n,n] = 1e6  # otherwise the self-forces are infinite
        rmag = sqrt(add.reduce(r*r,-1)) # star-to-star scalar distances
        hit = less_equal(rmag,radius+radius[:,newaxis])-identity(Nstars)
        hitlist = sort(nonzero(hit.flat)[0]).tolist() # 1,2 encoded as 1*Nstars+2
        F = G*m*m[:,newaxis]*r/rmag[:,:,newaxis]**3 # all force pairs

    except: # old Numeric
        r = pos-pos[:,NewAxis] # all pairs of star-to-star vectors
        for n in range(Nstars):
            r[n,n] = 1e6  # otherwise the self-forces are infinite
        rmag = sqrt(add.reduce(r*r,-1)) # star-to-star scalar distances
        hit = less_equal(rmag,radius+radius[:,NewAxis])-identity(Nstars)
        hitlist = sort(nonzero(hit.flat)) # 1,2 encoded as 1*Nstars+2
        F = G*m*m[:,NewAxis]*r/rmag[:,:,NewAxis]**3 # all force pairs

    for n in range(Nstars):
        F[n,n] = 0  # no self-forces
    p = p+sum(F,1)*dt

    # Having updated all momenta, now update all positions         
    pos = pos+(p/m)*dt

    # Update positions of display objects; add trail
    for i in range(Nstars):
        Stars[i].vec = Stars[i].pos - pos[i]
        Stars[i].pos = pos[i]
        if (Nsteps % 5 == 0 and
            trail_but.value == 1 and Stars[i].alive == 1) or Stars[i].showtrail == 1:
            Stars[i].trail.append(pos=pos[i])
            Stars[i].trail.visible = 1

    # If any collisions took place, merge those stars
    for ij in hitlist:
        i, j = divmod(ij,Nstars) # decode star pair
        if not Stars[i].visible: continue
        if not Stars[j].visible: continue
        # m[i] is a one-element list, e.g. [6e30]
        # m[i,0] is an ordinary number, e.g. 6e30
        newpos = (pos[i]*m[i,0]+pos[j]*m[j,0])/(m[i,0]+m[j,0])
        newmass = m[i,0]+m[j,0]
        newp = p[i]+p[j]
        newradius = Rsun*((newmass/Msun)**(1./3.))
        iset, jset = i, j
        if radius[j] > radius[i]:
            iset, jset = j, i
        Stars[iset].radius = newradius
        m[iset,0] = newmass
        pos[iset] = newpos
        p[iset] = newp
        Stars[jset].trail.visible = 0
        Stars[jset].visible = 0
        p[jset] = vector(0,0,0)
        m[jset,0] = Msun*1E-30  # give it a tiny mass
        Nhits = Nhits+1
        pos[jset] = (10.*L*Nhits, 0, 0) # put it far away
        Stars[jset].alive = 0
        Stars[jset].showtrail = 0
        if jset == ride_star:
            ride_star = -1
        
    #if Nsteps == 100:
    #    print '%3.1f seconds for %d steps with %d stars' % (clock()-time, Nsteps, Nstars)
    Nsteps = Nsteps+1
    t = t+dt

##    #center on largest object
##    maxr = 0.0
##    bigstar = 0
##    ct = 0
##    for i in radius:
##        if i > maxr:
##            maxr = i
##            bigstar = ct
##        ct += 1
##    scene.center = Stars[bigstar].pos
    
##    if (Nsteps % 810 == 0):
##        print Nsteps
##        Nsteps = 0
##        #scene.range = startRange * (1.0-(0.5*Nsteps/810.))
##        l_go = 0
##        while l_go == 0:
##            if scene.kb.keys: # is there an event waiting to be processed?
##                s = scene.kb.getkey() # obtain keyboard information
##                if s == "g":
##                    print s
##                    l_go = 1
##        #sleep(2.0)
##        print "go"

    #adjust scene
    #rotate scene
    #scene.forward = rotate(scene.forward, angle=(360.0/810.0)*pi/180.0, axis=(0,1,0))
    #zoom in
    #if (Nsteps > 810 and Nsteps <= 1620):  #Scene 2
    #if (Nsteps > 1620 and Nsteps <= 2430):  #scene 3
##    if Nsteps == 1621:  #scene 3
##        #scene.range = startRange * (1.0-(0.5))
##        ##  SHOW TRAILS
##        Stars[136].showtrail = 1
##        Stars[83].showtrail = 1
##        Stars[122].showtrail = 1
##        ##  ROTATE
##        #scene.forward = rotate(scene.forward, angle=(360.0/810.0)*pi/180.0, axis=(0,1,0))
##        ##  RIDE
##        ride_but.value = 1
##        ride_star = 83
        
        
##    #ZOOM IN
##    if scene.range.x > minRange and Nsteps > start_steps:
##        nRange = maxRange - (Nsteps-start_steps)*(maxRange-minRange)/float(Rsteps) 
##        #print nRange
##        scene.range = (nRange, nRange, nRange)
##        #print scene.range

    l_go = 0
    key = "g"
    while l_go == 0:
##        if (Nsteps % 810 <> 0):
##            l_go = 1
            
        if scene.kb.keys: # is there an event waiting to be processed?
            s = scene.kb.getkey() # obtain keyboard information
            if s == "g":
                #print s
                #l_go = 1
                key = "g"
            if s == "s":
                #l_go = 0
                key = "s"

        if key == "g":
            l_go = 1
        else:
            l_go = 0

        if cwin.mouse.events:
            m1 = cwin.mouse.getevent() # obtain drag or drop event
            if m1.pick == trail_but.button and m1.release:
                trail_but.switch()
                if trail_but.value == 0:
                    for i in range(Nstars):
                        Stars[i].trail.visible = 0 #pos = Stars[i].trails.pos * 0.0
                        Stars[i].trail.pos=[]
                        
            if m1.pick == ride_but.button and m1.release:
                ride_but.switch()
                if ride_but.value == 0:
                    scene.forward = vector(-1,-1,-1)
                    scene.range = lastRange
                    ride_star = -1
                    
                    
        if scene.mouse.events:
            m1 = scene.mouse.getevent()
            nct = 0
            for i in range(len(Stars)):
                if m1.pick == Stars[i] and m1.release:
                    print "Star ="
                    print i
                    if Stars[i].showtrail == 1:
                        Stars[i].showtrail = 0
                        Stars[i].trail.visible = 0
                        Stars[i].trail.pos=[]
                    else:
                        Stars[i].showtrail = 1

                    if ride_but.value == 1:
                        ride_star = nct
                nct += 1

        if ride_but.value == 1 and ride_star <> -1:
            scene.forward = -(Stars[ride_star].pos - scene.center)
            lastRange = scene.range
            scene.range = 1.1 *mag(Stars[ride_star].pos)


