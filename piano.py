import add
import math

black = center = [0,0,0]
white = [255,255,255]

def keyboard():
    # Base
    add.rectangle3D(center,[0.65,0.1,6],black)
    add.rectangle3D([-0.6,-0.1,0],[1.5,0.1,6],black)
    
    # White keys and non-key space
    x = 0
    y = 0.1
    dimensionsWhite = [0.65,0.1,0.1]
    dimensionsBlack = [0.65,0.1,0.4]
    add.rectangle3D([x,y,2.8],dimensionsBlack,black)
    for i in range(52):
        add.rectangle3D([x,y,2.55-(i*0.1)],dimensionsWhite,white)
    add.rectangle3D([x,y,-2.8],dimensionsBlack,black)

    # Black keys
    dist = 2.6
    x = -0.12
    y = 0.17
    dimensions = [0.43,0.05,0.07]
    for i in range(7):
        add.rectangle3D([x,y,dist-0.1],dimensions,black)
        add.rectangle3D([x,y,dist-0.1*3],dimensions,black)
        add.rectangle3D([x,y,dist-0.1*4],dimensions,black)
        add.rectangle3D([x,y,dist-0.1*6],dimensions,black)
        add.rectangle3D([x,y,dist-0.1*7],dimensions,black)
        dist -= 0.7
    add.rectangle3D([x,y,dist-0.1],dimensions,black)

    # Side walls
    dimensionsWall = [0.65,0.25,0.1]
    add.rectangle3D([0,0.28,2.95],dimensionsWall,black)  # left
    add.rectangle3D([0,0.28,-2.95],dimensionsWall,black) # right
    add.rectangle3D([-0.27,0.7,0],[0.1,0.1,6],black)     # top

def box():
    add.rectangle3D([-1.5,0.35,0],[2.37,0.82,6],black)    # front box
    add.rectangle3D([-3.2,0.35,1],[5.5,0.825,4],black)     # back box
    add.rectangle3D([-3,0.35,-1.2],[0.82,0.80,2.1],black) # small right box
    
    add.cylinder([-6,-0.05,1],[-6,0.75,1],2,100,black)              # big
    add.cylinder([-2.7,-0.05,-2.3],[-2.7,0.745,-2.3],0.71,70,black)  # small

def curvedWall():
    add.rectangle3D([-4,0.35,-0.95],[0.3,0.79,0.07],black)
    add.rectangle3D([-3.7,0.35,-0.82],[0.4,0.77,0.3],black)
    wall = add.layer()

    # Rotate small walls like in a cylinder
    for i in range(32):
        wall = add.rotateY(wall, math.pi/64,[-4,0.35,-1.6])
        add.rectangle3D([-4,0.35,-0.95],[0.3,0.78,0.07],black)
        add.rectangle3D([-3.7,0.35,-0.82],[0.4,0.77,0.3],[0,255,0])
        add.mesh(wall)

def legs():
    thiccLeg = 0.4
    heightCube = 0.25
    heightBall = 0.1
    heightLeg = -2
    detailBall = 5

    # Front left leg
    x = -0.5
    z = 2.5
    add.pyramid([x,0.2,z],thiccLeg,heightLeg,black)
    add.cube([x,-1.7,z],heightCube,black)
    add.sphere([x,-1.9,z],heightBall,detailBall,black)

    # Front right leg
    add.pyramid([x,0.2,-z],thiccLeg,heightLeg,black)
    add.cube([x,-1.7,-z],heightCube,black)
    add.sphere([x,-1.9,-z],heightBall,detailBall,black)

    # Rear leg
    x = -6
    z = 1
    add.pyramid([x,0.2,z],thiccLeg,heightLeg,black)
    add.cube([x,-1.7,z],heightCube,black)
    add.sphere([x,-1.9,z],heightBall,detailBall,black)
    
def pedals():
    # Lyre
    x = -0.5
    y = -0.9
    dimensions = [0.15,1.6,0.15]
    add.rectangle3D([x,y,0.4],dimensions,black)
    add.rectangle3D([x,y,-0.4],dimensions,black)

    # Pedal box
    y = -1.7
    add.rectangle3D([-0.45,y,0],[0.25,0.25,1],black)

    # Pedals
    pedalColor = [27,39,39]
    dimensions = [0.4,0.07,0.15]
    x = -0.3
    add.rectangle3D([x,y,0],dimensions,pedalColor)
    add.rectangle3D([x,y,0.3],dimensions,pedalColor)
    add.rectangle3D([x,y,-0.3],dimensions,pedalColor)

    # Backstay
    x = -0.55
    xFinal = -1.7
    yFinal = 0
    r = 0.03
    detail = 10
    add.cylinder([x,y,0],[xFinal,yFinal,0],r,detail,pedalColor)
    add.cylinder([x,y,0.3],[xFinal,yFinal,0.3],r,detail,pedalColor)
    add.cylinder([x,y,-0.3],[xFinal,yFinal,-0.3],r,detail,pedalColor)

def notes():
    add.rectangle3D([-1,0.8,0],[1,0.05,2],[100,0,0])

    # Paper sheets
    x = -1
    y = 0.8
    dimensions = [0.8,0.06,0.7]
    add.rectangle3D([x,y,-0.37],dimensions,white)
    add.rectangle3D([x,y,0.37],dimensions,white)

    # Black lines (stave)
    dimensions = [0,0.07,0.5]
    dist = -1.3
    for j in range(4):
        for i in range(5):
            add.rectangle3D([dist+(i/50),y,0.37],dimensions,black)
            add.rectangle3D([dist+(i/50),y,-0.37],dimensions,black)
        dist += 0.15

def logoCurve(t):
    x = -0.32
    y = math.cos(t)/60+0.4
    z = t/50
    return [x,y,z]

def logo():
    add.curve(logoCurve,-math.pi*9,math.pi*9,100,50,0.012,[255,215,0],0)

curvedWall()
keyboard()
box()
legs()
pedals()
notes()
logo()

add.off("piano.off")