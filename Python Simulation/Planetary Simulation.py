###############
# Ethan Mayer #
###############
import math
import random
import wx
from visual import*
from visual_common import*
from PIL import Image

# Scene setup
scene.fullscreen = True
scene.show_rendertime = True

# Option variables
showTrail = True
lineType = 'curve'
ret = 10000
moonRet = 100
astRet = 60
inter = 1
moonInter = 1
sunSpeed = 0

# Gravitational
gravConst = 6.67384 * math.pow(10, -11)

# Textures of the planets and the background
print('Setting up Solar System Planet textures...')
ssPlanetTexs = [materials.texture(data = Image.open('sun.jpg'), mapping = 'spherical'),
                materials.texture(data = Image.open('mercury.jpg'), mapping = 'spherical'),
                materials.texture(data = Image.open('venus.jpg'), mapping = 'spherical'),
                materials.texture(data = Image.open('earth.jpg'), mapping = 'spherical'),
                materials.texture(data = Image.open('mars.jpg'), mapping = 'spherical'),
                materials.texture(data = Image.open('jupiter.jpg'), mapping = 'spherical'),
                materials.texture(data = Image.open('saturn.jpg'), mapping = 'spherical'),
                materials.texture(data = Image.open('uranus.jpg'), mapping = 'spherical'),
                materials.texture(data = Image.open('neptune.jpg'), mapping = 'spherical'),
                materials.texture(data = Image.open('pluto.jpg'), mapping = 'spherical')]
print('Done!')

# Textures for extras (moons, etc.)
print('Setting up Solar System Moon textures...')
ssMoonTexs = [materials.texture(data = Image.open('earthMoon.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('ssMMoon1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('ssMMoon2.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('ssJMoon1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('ssJMoon2.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('ssJMoon3.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('ssJMoon4.png'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical'),
              materials.texture(data = Image.open('asteroid1.jpg'), mapping = 'spherical')]
saturnRingsTex = materials.texture(data = Image.open('saturnRings.jpg'), mapping = 'rectangular')
print('Done!')

# Star variables
numStars = 10000
starRange = math.pow(10, 14)
starRadius = math.pow(10, 11)

# Light variables
lightIntensity = 0.3
lightDistance = 5

# Clears the default scene lighting
scene.lights = []

# Solar system 
ssMasses = [1.9891 * math.pow(10, 30),
            3.3022 * math.pow(10, 23),
            4.8685 * math.pow(10, 24),
            5.9736 * math.pow(10, 24),
            6.4185 * math.pow(10, 23),
            1.8986 * math.pow(10, 27),
            5.6846 * math.pow(10, 26),
            8.6810 * math.pow(10, 25),
            10.243 * math.pow(10, 25),
            1.2500 * math.pow(10, 22)]

ssRadiuses = [695000 * math.pow(10, 3),
                2440 * math.pow(10, 3),
                6052 * math.pow(10, 3),
                6378 * math.pow(10, 3),
                3397 * math.pow(10, 3),
               71492 * math.pow(10, 3),
               60268 * math.pow(10, 3),
               25559 * math.pow(10, 3),
               24766 * math.pow(10, 3),
                1150 * math.pow(10, 3)]

ssDistances = [                                0,
                    5.7894376 * math.pow(10, 10),
                   1.08009663 * math.pow(10, 11),
                   1.49597871 * math.pow(10, 11),
                   2.27388763 * math.pow(10, 11),
                   7.77908928 * math.pow(10, 11),
               1.433147610306 * math.pow(10, 12),
               2.872279117440 * math.pow(10, 12),
                   4.50289591 * math.pow(10, 12),
                   5.90911589 * math.pow(10, 12)]

ssSpeeds = [sunSpeed,
             47362.0,
             35020.0,
             29780.0,
             24077.0,
             13070.0,
              9690.0,
              6800.0,
              5430.0,
              4700.0]

ssSpins = [     2.904 * math.pow(10, -6),
              1.24002 * math.pow(10, -6),
              2.99246 * math.pow(10, -7),
             7.292115 * math.pow(10, -5),
           6.08821804 * math.pow(10, -5),
               1.7585 * math.pow(10, -4),
               1.6378 * math.pow(10, -4),
               1.0124 * math.pow(10, -4),
               1.0834 * math.pow(10, -4),
               1.1386 * math.pow(10, -5)]

ssTilts = [       90,
                7.01,
                3.39,
                   0,
                1.85,
                1.31,
                2.49,
                0.77,
                1.77,
           17.151394]

# Dimensions of Saturn's rings
saturnRingsRadius = 480000 * math.pow(10, 3)
saturnRingsThickness = 10

# Planet spheres for solar system
ssPlanets = []
ssTrailColors = [color.white,
                 (0.5, 0.5, 0.5),
                 color.orange,
                 color.green,
                 color.red,
                 (1, 0, 1),
                 (129.0 / 255.0, 69.0 / 255.0, 19.0 / 255.0),
                 color.blue,
                 color.red,
                 color.white,
                 color.yellow]

print('Generating Solar System Planets...')
for p in range(0,len(ssMasses)):
    # Creates each planet and sets its appropriate trail color
    ssPlanets = ssPlanets + [sphere(pos = vector(ssDistances[p], 0, 0),
                                    velocity = vector(0.0,
                                                      -ssSpeeds[p] * cos(ssTilts[p] * math.pi / 180.0),
                                                      -ssSpeeds[p] * sin(ssTilts[p] * math.pi / 180.0) - ssSpeeds[0]),
                                    radius = ssRadiuses[p],
                                    make_trail = showTrail,
                                    trail_type = lineType,
                                    interval = inter,
                                    retain = ret / 50,
                                    material = ssPlanetTexs[p])]
    # Adjust sun speed, because of doubling
    if p == 0:
        ssPlanets[p].velocity += vector(0, 0, ssSpeeds[0])
        
    ssPlanets[p].trail_object.color = ssTrailColors[p]
print('Done!')

# Light objects for the sun
sunLights = [local_light(color = color.gray(lightIntensity)),
             local_light(color = color.gray(lightIntensity)),
             local_light(color = color.gray(lightIntensity)),
             local_light(color = color.gray(lightIntensity)),
             local_light(color = color.gray(lightIntensity)),
             local_light(color = color.gray(lightIntensity))]
sunLightRelPos = [vector(   ssRadiuses[0] * lightDistance, 0, 0),
                  vector(-(ssRadiuses[0] * lightDistance), 0, 0),
                  vector(0,    ssRadiuses[0] * lightDistance, 0),
                  vector(0, -(ssRadiuses[0] * lightDistance), 0),
                  vector(0, 0,    ssRadiuses[0] * lightDistance),
                  vector(0, 0, -(ssRadiuses[0] * lightDistance))]

# Creates saturns rings
saturnRings = cylinder(pos = vector(ssDistances[6], 0, 0),
                       radius = saturnRingsRadius,
                       length = 0,
                       material = saturnRingsTex)

# Creates the ss moons
ssMoonMasses = [7.341 * math.pow(10, 22),
                1.0659 * math.pow(10, 16),
                1.4762 * math.pow(10, 15),
                8931900 * math.pow(10, 16),
                4800000 * math.pow(10, 16),
                14819000 * math.pow(10, 16),
                10759000 * math.pow(10, 16),
                208 * math.pow(10, 16),
                670 * math.pow(10, 16),
                87 * math.pow(10, 16),
                30 * math.pow(10, 16),
                7.5 * math.pow(10, 16),
                6.3 * math.pow(10, 16),
                13 * math.pow(10, 16),
                3 * math.pow(10, 16),
                0.6 * math.pow(10, 16),
                43 * math.pow(10, 16),
                0.2 * math.pow(10, 16),
                3.6 * math.pow(10, 16),
                0.087 * math.pow(10, 16),
                0.069 * math.pow(10, 16),
                0.021 * math.pow(10, 16),
                0.016 * math.pow(10, 16),
                0.0075 * math.pow(10, 16),
                0.012 * math.pow(10, 16),
                0.019 * math.pow(10, 16),
                0.019 * math.pow(10, 16),
                0.0045 * math.pow(10, 16),
                0.0075 * math.pow(10, 16),
                0.043 * math.pow(10, 16),
                0.009 * math.pow(10, 16),
                0.009 * math.pow(10, 16),
                0.009 * math.pow(10, 16),
                0.0045 * math.pow(10, 16),
                0.0045 * math.pow(10, 16),
                0.0045 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.0045 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.009 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.0045 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.009 * math.pow(10, 16),
                0.0045 * math.pow(10, 16),
                0.009 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.009 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.009 * math.pow(10, 16),
                0.00015 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.00015 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.0015 * math.pow(10, 16),
                0.0015 * math.pow(10, 16)
]

ssMoonRadiuses = [1737.1 * math.pow(10, 3),
                  11.1 * math.pow(10, 3),
                  6.2 * math.pow(10, 3),
                  1818.1 * math.pow(10, 3),
                  1560.7 * math.pow(10, 3),
                  2634.1 * math.pow(10, 3),
                  2408.4 * math.pow(10, 3),
                  83.45 * math.pow(10, 3),
                  67 * math.pow(10, 3),
                  43 * math.pow(10, 3),
                  30 * math.pow(10, 3),
                  19 * math.pow(10, 3),
                  18 * math.pow(10, 3),
                  23 * math.pow(10, 3),
                  14 * math.pow(10, 3),
                  10 * math.pow(10, 3),
                  49.3 * math.pow(10, 3),
                  8.2 * math.pow(10, 3),
                  21.5 * math.pow(10, 3),
                  4.3 * math.pow(10, 3),
                  4 * math.pow(10, 3),
                  2.7 * math.pow(10, 3),
                  2.5 * math.pow(10, 3),
                  1.9 * math.pow(10, 3),
                  2.2 * math.pow(10, 3),
                  2.6 * math.pow(10, 3),
                  2.6 * math.pow(10, 3),
                  1.6 * math.pow(10, 3),
                  1.9 * math.pow(10, 3),
                  3.4 * math.pow(10, 3),
                  2 * math.pow(10, 3),
                  2 * math.pow(10, 3),
                  2 * math.pow(10, 3),
                  1.5 * math.pow(10, 3),
                  1.5 * math.pow(10, 3),
                  1.5 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  1.5 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  2 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  1.5 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  2 * math.pow(10, 3),
                  1.5 * math.pow(10, 3),
                  2 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  2 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  2 * math.pow(10, 3),
                  0.5 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  0.5 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  1 * math.pow(10, 3),
                  1 * math.pow(10, 3)]

ssMoonDistances = [3.84 * math.pow(10, 8),
                   9270 * math.pow(10, 3),
                   23460 * math.pow(10, 3),
                   421800 * math.pow(10, 3),
                   671100 * math.pow(10, 3),
                   1070400 * math.pow(10, 3),
                   1882700 * math.pow(10, 3),
                   181400 * math.pow(10, 3),
                   11461000 * math.pow(10, 3),
                   11741000 * math.pow(10, 3),
                   23624000 * math.pow(10, 3),
                   23939000 * math.pow(10, 3),
                   1117000 * math.pow(10, 3),
                   23404000 * math.pow(10, 3),
                   21276000 * math.pow(10, 3),
                   11165000 * math.pow(10, 3),
                   221900 * math.pow(10, 3),
                   129000 * math.pow(10, 3),
                   128000 * math.pow(10, 3),
                   24103000 * math.pow(10, 3),
                   7284000 * math.pow(10, 3),
                   23493000 * math.pow(10, 3),
                   23280000 * math.pow(10, 3),
                   23100000 * math.pow(10, 3),
                   20858000 * math.pow(10, 3),
                   23483000 * math.pow(10, 3),
                   21060000 * math.pow(10, 3),
                   23196000 * math.pow(10, 3),
                   23155000 * math.pow(10, 3),
                   20908000 * math.pow(10, 3),
                   24046000 * math.pow(10, 3),
                   20939000 * math.pow(10, 3),
                   21131000 * math.pow(10, 3),
                   23229000 * math.pow(10, 3),
                   22865000 * math.pow(10, 3),
                   20797000 * math.pow(10, 3),
                   19304000 * math.pow(10, 3),
                   20720000 * math.pow(10, 3),
                   23487000 * math.pow(10, 3),
                   23217000 * math.pow(10, 3),
                   23004000 * math.pow(10, 3),
                   23577000 * math.pow(10, 3),
                   21035000 * math.pow(10, 3),
                   23980000 * math.pow(10, 3),
                   21164000 * math.pow(10, 3),
                   23355000 * math.pow(10, 3),
                   23288000 * math.pow(10, 3),
                   21069000 * math.pow(10, 3),
                   17058000 * math.pow(10, 3),
                   23328000 * math.pow(10, 3),
                   23809000 * math.pow(10, 3),
                   24543000 * math.pow(10, 3),
                   22983000 * math.pow(10, 3),
                   12570000 * math.pow(10, 3),
                   28455000 * math.pow(10, 3),
                   20224000 * math.pow(10, 3),
                   23933000 * math.pow(10, 3),
                   23498000 * math.pow(10, 3),
                   23388000 * math.pow(10, 3),
                   23044000 * math.pow(10, 3),
                   17833000 * math.pow(10, 3),
                   22630000 * math.pow(10, 3),
                   20956000 * math.pow(10, 3),
                   20426000 * math.pow(10, 3),
                   23535000 * math.pow(10, 3),
                   23566000 * math.pow(10, 3)]

ssMoonSpeeds = [1022,
                2140,
                1350,
                17.33572041 * math.pow(10, 3),
                13.74231753 * math.pow(10, 3),
                10.87946294 * math.pow(10, 3),
                8.203382991 * math.pow(10, 3),
                26.57455364 * math.pow(10, 3),
                3.323798022 * math.pow(10, 3),
                3.298886161 * math.pow(10, 3),
                2.308806777 * math.pow(10, 3),
                2.305359485 * math.pow(10, 3),
                3.293972287 * math.pow(10, 3),
                2.297840533 * math.pow(10, 3),
                2.477488827 * math.pow(10, 3),
                3.377047956 * math.pow(10, 3),
                23.9255162 * math.pow(10, 3),
                31.378470098 * math.pow(10, 3),
                31.51755539 * math.pow(10, 3),
                2.224971234 * math.pow(10, 3),
                4.135131823 * math.pow(10, 3),
                2.384648783 * math.pow(10, 3),
                2.227965935 * math.pow(10, 3),
                2.282330541 * math.pow(10, 3),
                2.457491787 * math.pow(10, 3),
                2.271721132 * math.pow(10, 3),
                2.38598405 * math.pow(10, 3),
                2.294715475 * math.pow(10, 3),
                2.383310925 * math.pow(10, 3),
                2.421465378 * math.pow(10, 3),
                2.318891169 * math.pow(10, 3),
                2.481875254 * math.pow(10, 3),
                2.430043797 * math.pow(10, 3),
                2.219483745 * math.pow(10, 3),
                2.355116428 * math.pow(10, 3),
                2.398501475 * math.pow(10, 3),
                2.520518018 * math.pow(10, 3),
                2.402571736 * math.pow(10, 3),
                2.356817497 * math.pow(10, 3),
                2.234010337 * math.pow(10, 3),
                2.355937945 * math.pow(10, 3),
                2.329695682 * math.pow(10, 3),
                2.478229469 * math.pow(10, 3),
                2.200682464 * math.pow(10, 3),
                2.368193878 * math.pow(10, 3),
                2.356380381 * math.pow(10, 3),
                2.306394958 * math.pow(10, 3),
                2.384931498 * math.pow(10, 3),
                2.732435566 * math.pow(10, 3),
                2.337922735 * math.pow(10, 3),
                2.262532839 * math.pow(10, 3),
                2.17886093 * math.pow(10, 3),
                2.252805637 * math.pow(10, 3),
                3.174893307 * math.pow(10, 3),
                2.244218311 * math.pow(10, 3),
                2.443885916 * math.pow(10, 3),
                2.269571035 * math.pow(10, 3),
                2.360009066 * math.pow(10, 3),
                2.366001306 * math.pow(10, 3),
                2.307897199 * math.pow(10, 3),
                2.634271993 * math.pow(10, 3),
                2.395461784 * math.pow(10, 3),
                2.447601413 * math.pow(10, 3),
                2.415118271 * math.pow(10, 3),
                2.2303925 * math.pow(10, 3),
                2.257729953 * math.pow(10, 3)]

ssMoonSpins = [ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0,
               ssSpins[3] / 27.0]

ssMoonTilts = [5.145,
               26.04,
               27.58,
               2.21,
               2.631,
               2.364,
               2.365,
               2.534,
               32.646,
               31.851,
               143.963,
               155.938,
               29.166,
               167.207,
               153.724,
               29.722,
               3.236,
               2.19,
               2.22,
               142.009,
               47.922,
               152.558,
               167.05,
               169.23,
               149.383,
               167.665,
               149.408,
               165.897,
               167.287,
               146.365,
               153.218,
               149.436,
               153.402,
               167.722,
               151.484,
               145.569,
               146.854,
               144.526,
               156.532,
               167.538,
               167.919,
               154.666,
               151.892,
               162.642,
               153.452,
               166.747,
               166.765,
               156.746,
               58.161,
               166.156,
               142.308,
               139.531,
               164.65,
               29.744,
               155.681,
               148.523,
               149.335,
               167.709,
               167.14,
               165.973,
               144.84,
               143.972,
               152.929,
               149.561,
               166.887,
               151.009]

ssMoonTrailColors = [color.white,
                     (1, 0.4, 0),
                     (1, 0.3, 0),
                     (0.8, 0.8, 0.05),
                     (1, 0.4, 0),
                     (0.9, 0.2, 0),
                     (0.8, 0.1, 0),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5),
                     (0.5, 0.5, 0.5)]

ssMoonPlanetPairs = [3,
                     4, 4,
                     5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                     5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                     5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5  # rip jupiter
                     ]

print('Generating Solar System Moons...')
ssMoons = []
for m in range(0, len(ssMoonMasses)):
    if m <= 6: 
        ssMoons = ssMoons + [sphere(pos = vector(ssDistances[ssMoonPlanetPairs[m]] + ssMoonDistances[m], 0, 0),
                                    velocity = vector(0.0,
                                                      -ssMoonSpeeds[m] * math.cos(ssMoonTilts[m] * math.pi / 180.0)
                                                        - ssSpeeds[ssMoonPlanetPairs[m]] * math.cos(ssTilts[ssMoonPlanetPairs[m]] * math.pi / 180.0),
                                                      -ssMoonSpeeds[m] * math.sin(ssMoonTilts[m] * math.pi / 180.0)
                                                        - ssSpeeds[ssMoonPlanetPairs[m]] * math.sin(ssTilts[ssMoonPlanetPairs[m]] * math.pi / 180.0)
                                                        - ssSpeeds[0]),
                                    radius = ssMoonRadiuses[m],
                                    make_trail = showTrail,
                                    trail_type = lineType,
                                    interval = moonInter,
                                    retain = moonRet,
                                    material = ssMoonTexs[m])]
    else:
        ssMoons = ssMoons + [sphere(pos = vector(ssDistances[ssMoonPlanetPairs[m]] + ssMoonDistances[m], 0, 0),
                                    velocity = vector(0.0,
                                                      -ssMoonSpeeds[m] * math.cos(ssMoonTilts[m] * math.pi / 180.0)
                                                        - ssSpeeds[ssMoonPlanetPairs[m]] * math.cos(ssTilts[ssMoonPlanetPairs[m]] * math.pi / 180.0),
                                                      -ssMoonSpeeds[m] * math.sin(ssMoonTilts[m] * math.pi / 180.0)
                                                        - ssSpeeds[ssMoonPlanetPairs[m]] * math.sin(ssTilts[ssMoonPlanetPairs[m]] * math.pi / 180.0)
                                                        - ssSpeeds[0]),
                                    radius = ssMoonRadiuses[m],
                                    make_trail = showTrail,
                                    trail_type = lineType,
                                    interval = moonInter,
                                    retain = astRet,
                                    material = ssMoonTexs[m])]
        
    ssMoons[m].trail_object.color = ssMoonTrailColors[m]
print('Done!')

# Generates stars at random positions throughout space (unaffected by gravity)
print('Generating Stars...')
for star in range(0, numStars):
    # Generates the random position of the star, and pushes it outwards,
    # out of the planet area
    p = vector(2 * ((starRange * random.random()) - (starRange / 2)),
               2 * ((starRange * random.random()) - (starRange / 2)),
               2 * ((starRange * random.random()) - (starRange / 2)))
    p += starRange * norm(p)
    s = sphere(pos = p,
               velocity = vector(0, 0, 0),
               radius = starRadius,
               material = materials.emissive)
print('Done!')

# Comet for random generation
#cometMass = 5 * math.pow(10, 17)
#comet = sphere(pos = vector(2 * ((ssDistances[5] * random.random()) - (ssDistances[5] / 2)),
#                            2 * ((ssDistances[5] * random.random()) - (ssDistances[5] / 2)),
#                            2 * ((ssDistances[5] * random.random()) - (ssDistances[5] / 2))),
#               velocity = vector(2 * ((ssSpeeds[3] * random.random()) - (ssSpeeds[3] / 2)),
#                                 2 * ((ssSpeeds[3] * random.random()) - (ssSpeeds[3] / 2)),
#                                 2 * ((ssSpeeds[3] * random.random()) - (ssSpeeds[3] / 2))),
#               radius = ssMoonRadiuses[0],
#               make_trail = showTrail,
#               trail_type = lineType,
#               interval = moonInter,
#               retain = moonRet,
#               material = materials.emissive)


# Holds the current net k-forces on each planet and moon (preallocated with zeros).
# K-Forces are the k's found in the RK4 numerical method, in which each k is
# dependent on the current force on the victim, therefore just being
# a rate of change (not a force), contrary to the name. :|
ssPForces = []
ssMForces = []
for p in range(0, len(ssPlanets)):
    ssPForces = ssPForces + [vector(0, 0, 0)]
for m in range(0, len(ssMoons)):
    ssMForces = ssMForces + [vector(0, 0, 0)]

# Creates the controls window
print('Setting up control window...')
cWidth = 650
cHeight = 110
buf = 5
cntrWind = window(title='View Controls',
                  menus = True,
                  width = cWidth, height = cHeight + window.menuheight + window.dheight,
                  style = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
controls = display(window = cntrWind, x = buf, y = buf,
                   width = cWidth - 2 * buf, height = cHeight - 2 * buf)
p = cntrWind.panel
choices = wx.RadioBox(p, label = 'Zoom Choices',
                      size = (cWidth - 2 * buf, 50),
                      choices = ['Sun', 'Merc', 'Ven', 'Ear', 'Moon',
                                 'Mars', 'Jupi', 'Sat', 'Uran',
                                 'Nept', 'Plut'])
wx.StaticText(p, pos = (buf * 2, 50 + 2 * buf),
              size = (cWidth - 2 * buf, 50),
              label = 'Merc = Mercury, Ven = Venus, Ear = Earth, Jupit = Jupiter, Sat = Saturn, Uran = Uranus, Nept = Neptune, Plut = Pluto',
              style = wx.ALIGN_LEFT | wx.ST_NO_AUTORESIZE)
scene.select() # Reselects the original scene so the planets draw to the main window
print('Done!')
print('Running simulation.')


#frameCount = 0 # Frame counter
dt = 1000 # Small span of time delta t (sec)
while true:
    rate(60) # Frames per second
    spinTime = dt
  
    # Spins each planet, and clears their current force from the last frame
    for p in range(0, len(ssPlanets)):
        ssPlanets[p].rotate(angle = ssSpins[p] * spinTime,
                            axis = norm(ssPlanets[p].velocity),
                            origin = ssPlanets[p].pos)
        ssPForces[p] = vector(0, 0, 0)
    
    # Spins each moon
    for m in range(0, len(ssMoons)):
        ssMoons[m].rotate(angle = ssMoonSpins[m] * spinTime,
                          axis = norm(ssMoons[m].velocity),
                          origin = ssMoons[m].pos)

    # Calculate each net k-forces for the planets and moons
    for victimP in range(0, len(ssPlanets) - 1):
        for exertP in range(victimP + 1, len(ssPlanets)):
            ssPForces[victimP] +=  gravConst * ssMasses[exertP] * ssMasses[victimP] * norm(ssPlanets[exertP].pos - ssPlanets[victimP].pos) / mag2(ssPlanets[exertP].pos - ssPlanets[victimP].pos)
            
    for victimP in range(1, len(ssPlanets)):
        for exertP in range(0, victimP):
            ssPForces[victimP] += gravConst * ssMasses[exertP] * ssMasses[victimP] * norm(ssPlanets[exertP].pos - ssPlanets[victimP].pos) / mag2(ssPlanets[exertP].pos - ssPlanets[victimP].pos)            

            
    for m in range(0, len(ssMoons)):
        ssMForces[m] = vector(0, 0, 0)
        for p in range(0, len(ssPlanets)):
            ssMForces[m] += gravConst * ssMasses[p] * ssMoonMasses[m] * norm(ssPlanets[p].pos - ssMoons[m].pos) / mag2(ssPlanets[p].pos - ssMoons[m].pos) 
            ssPForces[p] += gravConst * ssMasses[p] * ssMoonMasses[m] * norm(ssMoons[m].pos - ssPlanets[p].pos) / mag2(ssMoons[m].pos - ssPlanets[p].pos)        


    # Updates each planet's velocity, using Newton's 3rd Law, and assuming constant acceleration
    for p in range(0, len(ssPlanets)):
        ssPlanets[p].velocity += ssPForces[p] * dt / ssMasses[p]
    #    comet.velocity += gravConst * ssMasses[p] * norm(ssPlanets[p].pos - comet.pos) * dt / mag2(ssPlanets[p].pos - comet.pos)
   
    # Updates each moon's velocity, using Newton's 3rd Law, and assuming constant acceleration
    for m in range(0, len(ssMoons)):
        ssMoons[m].velocity += ssMForces[m] * dt / ssMoonMasses[m]
    #    comet.velocity += gravConst * ssMoonMasses[m] * norm(ssMoons[m].pos - comet.pos)  * dt / mag2(ssMoons[m].pos - comet.pos)


    # Updates positions for planets and moons
    for p in range(0, len(ssPlanets)):
        ssPlanets[p].pos += ssPlanets[p].velocity * dt
    for m in range(0, len(ssMoons)):
        ssMoons[m].pos += ssMoons[m].velocity * dt

    # Updates sun's light objects' positions
    for s in range(0, len(sunLights)):
        sunLights[s].pos = ssPlanets[0].pos + sunLightRelPos[s]

    # Updates saturn ring positions
    saturnRings.pos  = ssPlanets[6].pos
    saturnRings.axis = norm(ssPlanets[6].velocity)

    #comet.pos += comet.velocity * dt

    # Sets up the choices for the scene focal (zoom) point,
    # and updates the scene center
    zoomPlanet = choices.GetSelection()
    if zoomPlanet == 4:
        scene.center = ssMoons[0].pos
    else:
        if zoomPlanet > 4:
            zoomPlanet -= 1
        scene.center = ssPlanets[zoomPlanet].pos

    #frameCount += 1
    #if frameCount % 1200 == 0:
        # Generate new position and velocity
    #    comet.pos = vector(2 * ((ssDistances[4] * random.random()) - (ssDistances[4] / 2)),
    #                       0.0,
    #                       0.0)
    #    comet.velocity = vector(0.0,
    #                            2 * ((ssSpeeds[6] * random.random()) - (ssSpeeds[6] / 2)),
    #                            2 * ((ssSpeeds[6] * random.random()) - (ssSpeeds[6] / 2)))

# End of py file #



"""
NOTE: All following lines are comments as temporary holding area
"""

"""
# Calculate each net k-forces for the planets and moons
    for victimP in range(0, len(ssPlanets) - 1):
        for exertP in range(victimP + 1, len(ssPlanets)):
            k1 = gravConst * ssMasses[exertP] * norm(ssPlanets[exertP].pos - ssPlanets[victimP].pos) / mag2(ssPlanets[exertP].pos - ssPlanets[victimP].pos)
            k2 = gravConst * ssMasses[exertP] * norm(ssPlanets[exertP].pos - (ssPlanets[victimP].pos + k1*dt/2)) / mag2(ssPlanets[exertP].pos - (ssPlanets[victimP].pos + k1*dt/2))
            k3 = gravConst * ssMasses[exertP] * norm(ssPlanets[exertP].pos - (ssPlanets[victimP].pos + k2*dt/2)) / mag2(ssPlanets[exertP].pos - (ssPlanets[victimP].pos + k2*dt/2))
            k4 = gravConst * ssMasses[exertP] * norm(ssPlanets[exertP].pos - (ssPlanets[victimP].pos + k3*dt)) / mag2(ssPlanets[exertP].pos - (ssPlanets[victimP].pos + k3*dt))
            ssPForces[victimP] += k1 + (2 * k2) + (2 * k3) + k4
            
    for victimP in range(1, len(ssPlanets)):
        for exertP in range(0, victimP):
            k1 = gravConst * ssMasses[exertP] * norm(ssPlanets[exertP].pos - ssPlanets[victimP].pos) / mag2(ssPlanets[exertP].pos - ssPlanets[victimP].pos)
            k2 = gravConst * ssMasses[exertP] * norm(ssPlanets[exertP].pos - (ssPlanets[victimP].pos + k1*dt/2)) / mag2(ssPlanets[exertP].pos - (ssPlanets[victimP].pos + k1*dt/2))
            k3 = gravConst * ssMasses[exertP] * norm(ssPlanets[exertP].pos - (ssPlanets[victimP].pos + k2*dt/2)) / mag2(ssPlanets[exertP].pos - (ssPlanets[victimP].pos + k2*dt/2))
            k4 = gravConst * ssMasses[exertP] * norm(ssPlanets[exertP].pos - (ssPlanets[victimP].pos + k3*dt)) / mag2(ssPlanets[exertP].pos - (ssPlanets[victimP].pos + k3*dt))
            ssPForces[victimP] += k1 + (2 * k2) + (2 * k3) + k4
            
    for m in range(0, len(ssMoons)):
        ssMForces[m] = vector(0, 0, 0)
        for p in range(0, len(ssPlanets)):
            mk1 = gravConst * ssMasses[p] * norm(ssPlanets[p].pos - ssMoons[m].pos) / mag2(ssPlanets[p].pos - ssMoons[m].pos)
            mk2 = gravConst * ssMasses[p] * norm(ssPlanets[p].pos - (ssMoons[m].pos + mk1*dt/2)) / mag2(ssPlanets[p].pos - (ssMoons[m].pos + mk1*dt/2))
            mk3 = gravConst * ssMasses[p] * norm(ssPlanets[p].pos - (ssMoons[m].pos + mk2*dt/2)) / mag2(ssPlanets[p].pos - (ssMoons[m].pos + mk2*dt/2))
            mk4 = gravConst * ssMasses[p] * norm(ssPlanets[p].pos - (ssMoons[m].pos + mk3*dt)) / mag2(ssPlanets[p].pos - (ssMoons[m].pos + mk3*dt))
            ssMForces[m] += mk1 + (2 * mk2) + (2 * mk3) + mk4
            
            pk1 = gravConst * ssMoonMasses[m] * norm(ssMoons[m].pos - ssPlanets[p].pos) / mag2(ssMoons[m].pos - ssPlanets[p].pos)
            pk2 = gravConst * ssMoonMasses[m] * norm(ssMoons[m].pos - (ssPlanets[p].pos + pk1*dt/2)) / mag2(ssMoons[m].pos - (ssPlanets[p].pos + pk1*dt/2))
            pk3 = gravConst * ssMoonMasses[m] * norm(ssMoons[m].pos - (ssPlanets[p].pos + pk2*dt/2)) / mag2(ssMoons[m].pos - (ssPlanets[p].pos + pk2*dt/2))
            pk4 = gravConst * ssMoonMasses[m] * norm(ssMoons[m].pos - (ssPlanets[p].pos + pk3*dt)) / mag2(ssMoons[m].pos - (ssPlanets[p].pos + pk3*dt))
            ssPForces[p] += pk1 + (2 * pk2) + (2 * pk3) + pk4

    # Updates each planet's velocity, using Newton's 3rd Law, and assuming constant acceleration
    for p in range(0, len(ssPlanets)):
        ssPlanets[p].velocity += ssPForces[p] * dt / 6
    #    comet.velocity += gravConst * ssMasses[p] * norm(ssPlanets[p].pos - comet.pos) * dt / mag2(ssPlanets[p].pos - comet.pos)
   
    # Updates each moon's velocity, using Newton's 3rd Law, and assuming constant acceleration
    for m in range(0, len(ssMoons)):
        ssMoons[m].velocity += ssMForces[m] * dt / 6
    #    comet.velocity += gravConst * ssMoonMasses[m] * norm(ssMoons[m].pos - comet.pos)  * dt / mag2(ssMoons[m].pos - comet.pos)










# Simulates air/fluid resistance
#earth.velocity   -= 0.5 * 0.47 * 100.409 * 1000 * math.pow(10, 8) * norm(earth.velocity) * mag2(earth.velocity) * dt / masses[3]
#mercury.velocity -= 0.5 * 0.47 * 100.409 * 1000 * math.pow(10, 8) * norm(mercury.velocity) * mag2(mercury.velocity) * dt / masses[1]
#venus.velocity   -= 0.5 * 0.47 * 100.409 * 1000 * math.pow(10, 8) * norm(venus.velocity) * mag2(venus.velocity) * dt / masses[2]
#mars.velocity    -= 0.5 * 0.47 * 100.409 * 1000 * math.pow(10, 8) * norm(mars.velocity) * mag2(mars.velocity) * dt / masses[4]
#jupiter.velocity -= 0.5 * 0.47 * 100.409 * 1000 * math.pow(10, 8) * norm(jupiter.velocity) * mag2(jupiter.velocity) * dt / masses[5]
#saturn.velocity  -= 0.5 * 0.47 * 100.409 * 1000 * math.pow(10, 8) * norm(saturn.velocity) * mag2(saturn.velocity) * dt / masses[6]
#uranus.velocity  -= 0.5 * 0.47 * 100.409 * 1000 * math.pow(10, 8) * norm(uranus.velocity) * mag2(uranus.velocity) * dt / masses[7]
#neptune.velocity -= 0.5 * 0.47 * 100.409 * 1000 * math.pow(10, 8) * norm(neptune.velocity) * mag2(neptune.velocity) * dt / masses[8]
#pluto.velocity   -= 0.5 * 0.47 * 100.409 * 1000 * math.pow(10, 8) * norm(pluto.velocity) * mag2(pluto.velocity) * dt / masses[9]
    
s = sphere(pos = vector(-((starRange * random.random()) + starRange),
                            (starRange * random.random()) + starRange,
                            (starRange * random.random()) + starRange),
               velocity = vector(0, 0, 0),
               radius = starRadius,
               material = materials.emissive)
    s = sphere(pos = vector((starRange * random.random()) + starRange,
                            -((starRange * random.random()) + starRange),
                            (starRange * random.random()) + starRange),
               velocity = vector(0, 0, 0),
               radius = starRadius,
               material = materials.emissive)
    s = sphere(pos = vector(-((starRange * random.random()) + starRange),
                            -((starRange * random.random()) + starRange),
                            (starRange * random.random()) + starRange),
               velocity = vector(0, 0, 0),
               radius = starRadius,
               material = materials.emissive)
    s = sphere(pos = vector((starRange * random.random()) + starRange,
                            (starRange * random.random()) + starRange,
                            -((starRange * random.random()) + starRange)),
               velocity = vector(0, 0, 0),
               radius = starRadius,
               material = materials.emissive)
    s = sphere(pos = vector(-((starRange * random.random()) + starRange),
                            (starRange * random.random()) + starRange,
                            -((starRange * random.random()) + starRange)),
               velocity = vector(0, 0, 0),
               radius = starRadius,
               material = materials.emissive)
    s = sphere(pos = vector((starRange * random.random()) + starRange,
                            -((starRange * random.random()) + starRange),
                            -((starRange * random.random()) + starRange)),
               velocity = vector(0, 0, 0),
               radius = starRadius,
               material = materials.emissive)
    s = sphere(pos = vector(-((starRange * random.random()) + starRange),
                            -((starRange * random.random()) + starRange),
                            -((starRange * random.random()) + starRange)),
               velocity = vector(0, 0, 0),
               radius = starRadius,
               material = materials.emissive)
class Planet(object): # Planet class
    # Constructor that takes in mass, radius, distance, speed, spin, inclination, and a texture
    def __init__(self, mass, rad, dist, speed, spin, inclin, texture):
        self.mass = mass
        self.radius = rad
        self.status = sphere(pos = vector(dist * math.cos(inclin * math.pi / 180), dist * math.sin(inclin * math.pi / 180), 0),
                             velocity = vector(0.0, -speed, 0.0),
                             radius = rad,
                             make_trail = True,
                             material = texture)
        self.spin = spin


planets = [Planet(1.9891 * math.pow(10, 30), 695000 * math.pow(10, 3),                                 0,     0.0,      2.904 * math.pow(10, -6),         0,     sunTex),
           Planet(3.3022 * math.pow(10, 23),   2440 * math.pow(10, 3),      5.7894376 * math.pow(10, 10), 47362.0,    1.24002 * math.pow(10, -6),      7.01, mercuryTex),
           Planet(3.3022 * math.pow(10, 23),   6052 * math.pow(10, 3),     1.08009663 * math.pow(10, 11), 35020.0,    2.99246 * math.pow(10, -7),      3.39,   venusTex),
           Planet(3.3022 * math.pow(10, 23),   6378 * math.pow(10, 3),     1.49597871 * math.pow(10, 11), 29780.0,   7.292115 * math.pow(10, -5),         0,   earthTex),
           Planet(3.3022 * math.pow(10, 23),   3397 * math.pow(10, 3),     2.27388763 * math.pow(10, 11), 24077.0, 6.08821804 * math.pow(10, -5),      1.85,    marsTex),
           Planet(3.3022 * math.pow(10, 23),  71492 * math.pow(10, 3),     7.77908928 * math.pow(10, 11), 13070.0,     1.7585 * math.pow(10, -4),      1.31, jupiterTex),
           Planet(3.3022 * math.pow(10, 23),  60268 * math.pow(10, 3), 1.433147610306 * math.pow(10, 12),  9690.0,     1.6378 * math.pow(10, -4),      2.49,  saturnTex),
           Planet(3.3022 * math.pow(10, 23),  25559 * math.pow(10, 3), 2.872279117440 * math.pow(10, 12),  6800.0,     1.0124 * math.pow(10, -4),      0.77,  uranusTex),
           Planet(3.3022 * math.pow(10, 23),  24766 * math.pow(10, 3),     4.50289591 * math.pow(10, 12),  5430.0,     1.0834 * math.pow(10, -4),      1.77, neptuneTex),
           Planet(3.3022 * math.pow(10, 23),   1150 * math.pow(10, 3),     5.90911589 * math.pow(10, 12),  4700.0,     1.1386 * math.pow(10, -5), 17.151394,   plutoTex)]

masses = [1.9891 * math.pow(10, 30), # Sun
          3.3022 * math.pow(10, 23), # Mercury
          4.8685 * math.pow(10, 24), # Venus
          5.9736 * math.pow(10, 24), # Earth
          6.4185 * math.pow(10, 23), # Mars
          1.8986 * math.pow(10, 27), # Jupiter
          5.6846 * math.pow(10, 26), # Saturn
          8.6810 * math.pow(10, 25), # Uranus
          1.0243 * math.pow(10, 26), # Neptune
          1.25   * math.pow(10, 22)] # Pluto
radiuses = [695000 * math.pow(10, 3), # Sun
            2440   * math.pow(10, 3), # Mercury
            6052   * math.pow(10, 3), # Venus
            6378   * math.pow(10, 3), # Earth
            3397   * math.pow(10, 3), # Mars
            71492  * math.pow(10, 3), # Jupiter
            60268  * math.pow(10, 3), # Saturn
            25559  * math.pow(10, 3), # Uranus
            24766  * math.pow(10, 3), # Neptune
            1150   * math.pow(10, 3)] # Pluto

# FOR BALL SIMULATION/REFERENCE
dx = -50
dy = 15
floor = box(pos=(0,0,0), length=100, height=0.5, width=2, color= (1,1,1), material=materials.wood)
floor1 = box(pos=(0,0,-5), length=100, height=0.5, width=2, color= (1,1,1), material=materials.wood)
floor2 = box(pos=(0,0,5), length=100, height=0.5, width=2, color= (1,1,1), material=materials.wood)
floor3 = box(pos=(0,0,-10), length=100, height=0.5, width=2, color= (1,1,1), material=materials.wood)

pball = sphere(pos=(dx,dy,-10), radius=1.5, color=color.red, make_trail=True, material=materials.emissive)
ball = sphere(pos=(dx,dy,0), radius=1, material=earthTex, make_trail=True)
ball2 = sphere(pos=(dx,dy,-5), radius=2, material=sunTex, make_trail=True, color=color.orange)
ball3 = sphere(pos=(dx,dy,5), radius=.5, material=mercuryTex, make_trail=True)

pball.velocity = vector(4,0)
ball.velocity = vector(4,0)
ball2.velocity = vector(4,0)
ball3.velocity = vector(4,0)

gravity = 9.81


# Magnitude of the direction vector between the current planet pair
dirVectMag = math.sqrt((planets[other].status.position.x - planets[curr].status.position.x) ** 2,
                       (planets[other].status.position.y - planets[curr].status.position.y) ** 2,
                       (planets[other].status.position.z - planets[curr].status.position.z) ** 2)

planets[curr].status.velocity.x += gravConst * planets[curr].mass * planets[other].mass * norm(dirVect).x / mag2(dirVect)
planets[curr].status.velocity.y += gravConst * planets[curr].mass * planets[other].mass * norm(dirVect).y / mag2(dirVect)
planets[curr].status.velocity.z += gravConst * planets[curr].mass * planets[other].mass * norm(dirVect).z / mag2(dirVect)

planets[curr].status.pos.x += planets[curr].status.velocity.x * dt
planets[curr].status.pos.y += planets[curr].status.velocity.y * dt
planets[curr].status.pos.z += planets[curr].status.velocity.z * dt

planets[other].status.velocity.x += -gravConst * planets[curr].mass * planets[other].mass * norm(dirVect).x / mag2(dirVect)
planets[other].status.velocity.y += -gravConst * planets[curr].mass * planets[other].mass * norm(dirVect).y / mag2(dirVect)
planets[other].status.velocity.z += -gravConst * planets[curr].mass * planets[other].mass * norm(dirVect).z / mag2(dirVect)

planets[other].status.pos.x += planets[other].status.velocity.x * dt
planets[other].status.pos.y += planets[other].status.velocity.y * dt
planets[other].status.pos.z += planets[other].status.velocity.z * dt

# Loops through each planet pair
    for curr in range(0, 10):
        for other in range(curr + 1, 10):
            # Normalized direction vector between the current planet pair (direction from curr to other)
            dirVect = vector(planets[other].status.pos.x - planets[curr].status.pos.x,
                             planets[other].status.pos.y - planets[curr].status.pos.y,
                             planets[other].status.pos.z - planets[curr].status.pos.z)

            # Updates both planets velocity, using Newton's 3rd Law, and their positions
            sun.velocity += gravConst * masses[0] * masses[1] * norm(dirVect) * dt / mag2(dirVect)
            planets[other].status.velocity += -gravConst * planets[curr].mass * planets[other].mass * norm(dirVect) * dt / mag2(dirVect)

# Updates each planets' velocity, using Newton's 3rd Law
    # Sun
    sun.velocity += gravConst * masses[0] * masses[1] * norm(mercury.pos - sun.pos) * dt / mag2(mercury.pos - sun.pos)
    mercury.velocity += -gravConst * masses[0] * masses[1] * norm(mercury.pos - sun.pos) * dt / mag2(mercury.pos - sun.pos)

    sun.velocity += gravConst * masses[0] * masses[2] * norm(venus.pos - sun.pos) * dt / mag2(venus.pos - sun.pos)
    venus.velocity += -gravConst * masses[0] * masses[2] * norm(venus.pos - sun.pos) * dt / mag2(venus.pos - sun.pos)

    sun.velocity += gravConst * masses[0] * masses[3] * norm(earth.pos - sun.pos) * dt / mag2(earth.pos - sun.pos)
    earth.velocity += -gravConst * masses[0] * masses[3] * norm(earth.pos - sun.pos) * dt / mag2(earth.pos - sun.pos)

    sun.velocity += gravConst * masses[0] * masses[4] * norm(mars.pos - sun.pos) * dt / mag2(mars.pos - sun.pos)
    mars.velocity += -gravConst * masses[0] * masses[4] * norm(mars.pos - sun.pos) * dt / mag2(mars.pos - sun.pos)

    sun.velocity += gravConst * masses[0] * masses[5] * norm(jupiter.pos - sun.pos) * dt / mag2(jupiter.pos - sun.pos)
    jupiter.velocity += -gravConst * masses[0] * masses[5] * norm(jupiter.pos - sun.pos) * dt / mag2(jupiter.pos - sun.pos)

    sun.velocity += gravConst * masses[0] * masses[6] * norm(saturn.pos - sun.pos) * dt / mag2(saturn.pos - sun.pos)
    saturn.velocity += -gravConst * masses[0] * masses[6] * norm(saturn.pos - sun.pos) * dt / mag2(saturn.pos - sun.pos)

    sun.velocity += gravConst * masses[0] * masses[7] * norm(uranus.pos - sun.pos) * dt / mag2(uranus.pos - sun.pos)
    uranus.velocity += -gravConst * masses[0] * masses[7] * norm(uranus.pos - sun.pos) * dt / mag2(uranus.pos - sun.pos)

    sun.velocity += gravConst * masses[0] * masses[8] * norm(neptune.pos - sun.pos) * dt / mag2(neptune.pos - sun.pos)
    neptune.velocity += -gravConst * masses[0] * masses[8] * norm(neptune.pos - sun.pos) * dt / mag2(neptune.pos - sun.pos)

    sun.velocity += gravConst * masses[0] * masses[9] * norm(pluto.pos - sun.pos) * dt / mag2(pluto.pos - sun.pos)
    pluto.velocity += -gravConst * masses[0] * masses[9] * norm(pluto.pos - sun.pos) * dt / mag2(pluto.pos - sun.pos)


    # Mercury
    mercury.velocity += gravConst * masses[1] * masses[2] * norm(venus.pos - mercury.pos) * dt / mag2(venus.pos - mercury.pos)
    venus.velocity += -gravConst * masses[1] * masses[2] * norm(venus.pos - mercury.pos) * dt / mag2(venus.pos - mercury.pos)

    mercury.velocity += gravConst * masses[1] * masses[3] * norm(earth.pos - mercury.pos) * dt / mag2(earth.pos - mercury.pos)
    earth.velocity += -gravConst * masses[1] * masses[3] * norm(earth.pos - mercury.pos) * dt / mag2(earth.pos - mercury.pos)

    mercury.velocity += gravConst * masses[1] * masses[4] * norm(mars.pos - mercury.pos) * dt / mag2(mars.pos - mercury.pos)
    mars.velocity += -gravConst * masses[1] * masses[4] * norm(mars.pos - mercury.pos) * dt / mag2(mars.pos - mercury.pos)

    mercury.velocity += gravConst * masses[1] * masses[5] * norm(jupiter.pos - mercury.pos) * dt / mag2(jupiter.pos - mercury.pos)
    jupiter.velocity += -gravConst * masses[1] * masses[5] * norm(jupiter.pos - mercury.pos) * dt / mag2(jupiter.pos - mercury.pos)

    mercury.velocity += gravConst * masses[1] * masses[6] * norm(saturn.pos - mercury.pos) * dt / mag2(saturn.pos - mercury.pos)
    saturn.velocity += -gravConst * masses[1] * masses[6] * norm(saturn.pos - mercury.pos) * dt / mag2(saturn.pos - mercury.pos)

    mercury.velocity += gravConst * masses[1] * masses[7] * norm(uranus.pos - mercury.pos) * dt / mag2(uranus.pos - mercury.pos)
    uranus.velocity += -gravConst * masses[1] * masses[7] * norm(uranus.pos - mercury.pos) * dt / mag2(uranus.pos - mercury.pos)

    mercury.velocity += gravConst * masses[1] * masses[8] * norm(neptune.pos - mercury.pos) * dt / mag2(neptune.pos - mercury.pos)
    neptune.velocity += -gravConst * masses[1] * masses[8] * norm(neptune.pos - mercury.pos) * dt / mag2(neptune.pos - mercury.pos)

    mercury.velocity += gravConst * masses[1] * masses[9] * norm(pluto.pos - mercury.pos) * dt / mag2(pluto.pos - mercury.pos)
    pluto.velocity += -gravConst * masses[1] * masses[9] * norm(pluto.pos - mercury.pos) * dt / mag2(pluto.pos - mercury.pos)


    # Venus
    venus.velocity += gravConst * masses[2] * masses[3] * norm(earth.pos - venus.pos) * dt / mag2(earth.pos - venus.pos)
    earth.velocity += -gravConst * masses[2] * masses[3] * norm(earth.pos - venus.pos) * dt / mag2(earth.pos - venus.pos)

    venus.velocity += gravConst * masses[2] * masses[4] * norm(mars.pos - venus.pos) * dt / mag2(mars.pos - venus.pos)
    mars.velocity += -gravConst * masses[2] * masses[4] * norm(mars.pos - venus.pos) * dt / mag2(mars.pos - venus.pos)

    venus.velocity += gravConst * masses[2] * masses[5] * norm(jupiter.pos - venus.pos) * dt / mag2(jupiter.pos - venus.pos)
    jupiter.velocity += -gravConst * masses[2] * masses[5] * norm(jupiter.pos - venus.pos) * dt / mag2(jupiter.pos - venus.pos)

    venus.velocity += gravConst * masses[2] * masses[6] * norm(saturn.pos - venus.pos) * dt / mag2(saturn.pos - venus.pos)
    saturn.velocity += -gravConst * masses[2] * masses[6] * norm(saturn.pos - venus.pos) * dt / mag2(saturn.pos - venus.pos)

    venus.velocity += gravConst * masses[2] * masses[7] * norm(uranus.pos - venus.pos) * dt / mag2(uranus.pos - venus.pos)
    uranus.velocity += -gravConst * masses[2] * masses[7] * norm(uranus.pos - venus.pos) * dt / mag2(uranus.pos - venus.pos)

    venus.velocity += gravConst * masses[2] * masses[8] * norm(neptune.pos - venus.pos) * dt / mag2(neptune.pos - venus.pos)
    neptune.velocity += -gravConst * masses[2] * masses[8] * norm(neptune.pos - venus.pos) * dt / mag2(neptune.pos - venus.pos)

    venus.velocity += gravConst * masses[2] * masses[9] * norm(pluto.pos - venus.pos) * dt / mag2(pluto.pos - venus.pos)
    pluto.velocity += -gravConst * masses[2] * masses[9] * norm(pluto.pos - venus.pos) * dt / mag2(pluto.pos - venus.pos)


    # Earth
    earth.velocity += gravConst * masses[3] * masses[4] * norm(mars.pos - earth.pos) * dt / mag2(mars.pos - earth.pos)
    mars.velocity += -gravConst * masses[3] * masses[4] * norm(mars.pos - earth.pos) * dt / mag2(mars.pos - earth.pos)

    earth.velocity += gravConst * masses[3] * masses[5] * norm(jupiter.pos - earth.pos) * dt / mag2(jupiter.pos - earth.pos)
    jupiter.velocity += -gravConst * masses[3] * masses[5] * norm(jupiter.pos - earth.pos) * dt / mag2(jupiter.pos - earth.pos)

    earth.velocity += gravConst * masses[3] * masses[6] * norm(saturn.pos - earth.pos) * dt / mag2(saturn.pos - earth.pos)
    saturn.velocity += -gravConst * masses[3] * masses[6] * norm(saturn.pos - earth.pos) * dt / mag2(saturn.pos - earth.pos)

    earth.velocity += gravConst * masses[3] * masses[7] * norm(uranus.pos - earth.pos) * dt / mag2(uranus.pos - earth.pos)
    uranus.velocity += -gravConst * masses[3] * masses[7] * norm(uranus.pos - earth.pos) * dt / mag2(uranus.pos - earth.pos)

    earth.velocity += gravConst * masses[3] * masses[8] * norm(neptune.pos - earth.pos) * dt / mag2(neptune.pos - earth.pos)
    neptune.velocity += -gravConst * masses[3] * masses[8] * norm(neptune.pos - earth.pos) * dt / mag2(neptune.pos - earth.pos)

    earth.velocity += gravConst * masses[3] * masses[9] * norm(pluto.pos - earth.pos) * dt / mag2(pluto.pos - earth.pos)
    pluto.velocity += -gravConst * masses[3] * masses[9] * norm(pluto.pos - earth.pos) * dt / mag2(pluto.pos - earth.pos)


    # Mars
    mars.velocity += gravConst * masses[4] * masses[5] * norm(jupiter.pos - mars.pos) * dt / mag2(jupiter.pos - mars.pos)
    jupiter.velocity += -gravConst * masses[4] * masses[5] * norm(jupiter.pos - mars.pos) * dt / mag2(jupiter.pos - mars.pos)

    mars.velocity += gravConst * masses[4] * masses[6] * norm(saturn.pos - mars.pos) * dt / mag2(saturn.pos - mars.pos)
    saturn.velocity += -gravConst * masses[4] * masses[6] * norm(saturn.pos - mars.pos) * dt / mag2(saturn.pos - mars.pos)

    mars.velocity += gravConst * masses[4] * masses[7] * norm(uranus.pos - mars.pos) * dt / mag2(uranus.pos - mars.pos)
    uranus.velocity += -gravConst * masses[4] * masses[7] * norm(uranus.pos - mars.pos) * dt / mag2(uranus.pos - mars.pos)

    mars.velocity += gravConst * masses[4] * masses[8] * norm(neptune.pos - mars.pos) * dt / mag2(neptune.pos - mars.pos)
    neptune.velocity += -gravConst * masses[4] * masses[8] * norm(neptune.pos - mars.pos) * dt / mag2(neptune.pos - mars.pos)

    mars.velocity += gravConst * masses[4] * masses[9] * norm(pluto.pos - mars.pos) * dt / mag2(pluto.pos - mars.pos)
    pluto.velocity += -gravConst * masses[4] * masses[9] * norm(pluto.pos - mars.pos) * dt / mag2(pluto.pos - mars.pos)


    # Jupiter
    jupiter.velocity += gravConst * masses[5] * masses[6] * norm(saturn.pos - jupiter.pos) * dt / mag2(saturn.pos - jupiter.pos)
    saturn.velocity += -gravConst * masses[5] * masses[6] * norm(saturn.pos - jupiter.pos) * dt / mag2(saturn.pos - jupiter.pos)

    jupiter.velocity += gravConst * masses[5] * masses[7] * norm(uranus.pos - jupiter.pos) * dt / mag2(uranus.pos - jupiter.pos)
    uranus.velocity += -gravConst * masses[5] * masses[7] * norm(uranus.pos - jupiter.pos) * dt / mag2(uranus.pos - jupiter.pos)

    jupiter.velocity += gravConst * masses[5] * masses[8] * norm(neptune.pos - jupiter.pos) * dt / mag2(neptune.pos - jupiter.pos)
    neptune.velocity += -gravConst * masses[5] * masses[8] * norm(neptune.pos - jupiter.pos) * dt / mag2(neptune.pos - jupiter.pos)

    jupiter.velocity += gravConst * masses[5] * masses[9] * norm(pluto.pos - jupiter.pos) * dt / mag2(pluto.pos - jupiter.pos)
    pluto.velocity += -gravConst * masses[5] * masses[9] * norm(pluto.pos - jupiter.pos) * dt / mag2(pluto.pos - jupiter.pos)


    # Saturn
    saturn.velocity += gravConst * masses[6] * masses[7] * norm(uranus.pos - saturn.pos) * dt / mag2(uranus.pos - saturn.pos)
    uranus.velocity += -gravConst * masses[6] * masses[7] * norm(uranus.pos - saturn.pos) * dt / mag2(uranus.pos - saturn.pos)

    saturn.velocity += gravConst * masses[6] * masses[8] * norm(neptune.pos - saturn.pos) * dt / mag2(neptune.pos - saturn.pos)
    neptune.velocity += -gravConst * masses[6] * masses[8] * norm(neptune.pos - saturn.pos) * dt / mag2(neptune.pos - saturn.pos)

    saturn.velocity += gravConst * masses[6] * masses[9] * norm(pluto.pos - saturn.pos) * dt / mag2(pluto.pos - saturn.pos)
    pluto.velocity += -gravConst * masses[6] * masses[9] * norm(pluto.pos - saturn.pos) * dt / mag2(pluto.pos - saturn.pos)


    # Uranus
    uranus.velocity += gravConst * masses[7] * masses[8] * norm(neptune.pos - uranus.pos) * dt / mag2(neptune.pos - uranus.pos)
    neptune.velocity += -gravConst * masses[7] * masses[8] * norm(neptune.pos - uranus.pos) * dt / mag2(neptune.pos - uranus.pos)

    uranus.velocity += gravConst * masses[7] * masses[9] * norm(pluto.pos - uranus.pos) * dt / mag2(pluto.pos - uranus.pos)
    pluto.velocity += -gravConst * masses[7] * masses[9] * norm(pluto.pos - uranus.pos) * dt / mag2(pluto.pos - uranus.pos)


    # Neptune
    neptune.velocity += gravConst * masses[8] * masses[9] * norm(pluto.pos - neptune.pos) * dt / mag2(pluto.pos - neptune.pos)
    pluto.velocity += -gravConst * masses[8] * masses[9] * norm(pluto.pos - neptune.pos) * dt / mag2(pluto.pos - neptune.pos)


    # Updates positions
    sun.pos += sun.velocity * dt
    mercury.pos += mercury.velocity * dt
    venus.pos += venus.velocity * dt
    earth.pos += earth.velocity * dt
    mars.pos += mars.velocity * dt
    jupiter.pos += jupiter.velocity * dt
    saturn.pos += saturn.velocity * dt
    uranus.pos += uranus.velocity * dt
    neptune.pos += neptune.velocity * dt
    pluto.pos += pluto.velocity * dt


sun = sphere(pos = vector(distances[0] * math.cos(inclinations[0] * math.pi / 180.0), distances[0] * math.sin(inclinations[0] * math.pi / 180), 0),
             velocity = vector(0.0, -speeds[0], 0.0),
             radius = radiuses[0],
             make_trail = True,
             color = color.white,
             material = materials.texture(data=Image.open('sun.jpg'), mapping='spherical'))

mercury = sphere(pos = vector(distances[1] * math.cos(inclinations[1] * math.pi / 180.0), distances[1] * math.sin(inclinations[1] * math.pi / 180), 0),
                 velocity = vector(0.0, -speeds[1], 0.0),
                 radius = radiuses[0],
                 make_trail = True,
                 color = (0.5, 0.5, 0.5),
                 material = materials.texture(data=Image.open('mercury.jpg'), mapping='spherical'))

venus = sphere(pos = vector(distances[2] * math.cos(inclinations[2] * math.pi / 180.0), distances[2] * math.sin(inclinations[2] * math.pi / 180), 0),
               velocity = vector(0.0, -speeds[2], 0.0),
               radius = radiuses[2],
               make_trail = True,
               color = color.orange,
               material = materials.texture(data=Image.open('venus.jpg'), mapping='spherical'))

earth = sphere(pos = vector(distances[3] * math.cos(inclinations[3] * math.pi / 180.0), distances[3] * math.sin(inclinations[3] * math.pi / 180), 0),
               velocity = vector(0.0, -speeds[3], 0.0),
               radius = radiuses[3],
               make_trail = True,
               color = color.green,
               material = materials.texture(data=Image.open('earth.jpg'), mapping='spherical'))

mars = sphere(pos = vector(distances[4] * math.cos(inclinations[4] * math.pi / 180.0), distances[4] * math.sin(inclinations[4] * math.pi / 180), 0),
              velocity = vector(0.0, -speeds[4], 0.0),
              radius = radiuses[4],
              make_trail = True,
              color = color.red,
              material = materials.texture(data=Image.open('mars.jpg'), mapping='spherical'))

jupiter = sphere(pos = vector(distances[5] * math.cos(inclinations[5] * math.pi / 180.0), distances[5] * math.sin(inclinations[5] * math.pi / 180), 0),
                 velocity = vector(0.0, -speeds[5], 0.0),
                 radius = radiuses[5],
                 make_trail = True,
                 color = (1, 0, 1),
                 material = materials.texture(data=Image.open('jupiter.jpg'), mapping='spherical'))

saturn = sphere(pos = vector(distances[6] * math.cos(inclinations[6] * math.pi / 180.0), distances[6] * math.sin(inclinations[6] * math.pi / 180), 0),
                velocity = vector(0.0, -speeds[6], 0.0),
                radius = radiuses[6],
                make_trail = True,
                color = (129 / 255, 69 / 255, 19 / 255),
                material = materials.texture(data=Image.open('saturn.jpg'), mapping='spherical'))

uranus = sphere(pos = vector(distances[7] * math.cos(inclinations[7] * math.pi / 180.0), distances[7] * math.sin(inclinations[7] * math.pi / 180), 0),
                velocity = vector(0.0, -speeds[7], 0.0),
                radius = radiuses[7],
                make_trail = True,
                color = color.blue,
                material = materials.texture(data=Image.open('uranus.jpg'), mapping='spherical'))

neptune = sphere(pos = vector(distances[8] * math.cos(inclinations[8] * math.pi / 180.0), distances[8] * math.sin(inclinations[8] * math.pi / 180), 0),
                 velocity = vector(0.0, -speeds[8], 0.0),
                 radius = radiuses[8],
                 make_trail = True,
                 color = (0.5, 0, 0.5),
                 material = materials.texture(data=Image.open('neptune.jpg'), mapping='spherical'))

pluto = sphere(pos = vector(distances[9] * math.cos(inclinations[9] * math.pi / 180.0), distances[9] * math.sin(inclinations[9] * math.pi / 180), 0),
               velocity = vector(0.0, -speeds[9], 0.0),
               radius = radiuses[9],
               make_trail = True,
               color = color.white,
               material = materials.texture(data=Image.open('pluto.jpg'), mapping='spherical'))

backgroundTex = materials.texture(data = Image.open('earth.jpg'), mapping = 'sign')

# Background sphere
background = box(pos = vector(0, 0, 0),
                    length = radiuses[9] * math.pow(10, 3),
                    height = radiuses[9] * math.pow(10, 3) / 2.0,
                    material = backgroundTex)


# Updates the background
background.pos = -scene.mouse.camera
"""




























