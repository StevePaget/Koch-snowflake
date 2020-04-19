from pygame_functions import *
import math

screenSize(900,900)
setAutoUpdate(False)

def calculateThirdPoint(p1, p2, length):
    thisSlope = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    newslope = thisSlope+math.pi/3
    newx = p1[0]+math.cos(newslope)*length
    newy = p1[1]+math.sin(newslope)*length
    return (newx, newy)

def onscreen(point):
    return 0<= point[0] <= 900 and 0<= point[1] <= 900

def drawkoch(cornerPos, size, colour):
    p1 = cornerPos
    p2 = (p1[0]+math.cos(math.pi/3)*size, p1[1]-math.sin(math.pi/3)*size)
    p3 = (p1[0]-math.cos(math.pi/3)*size, p1[1]-math.sin(math.pi/3)*size)
    lines = [(p1,p2), [p2,p3], [p3,p1]]
    split = True
    while split:
        split=False
        for x in range(len(lines)):
            line = lines.pop(0)
            if not (onscreen(line[0]) or onscreen(line[1])):
                continue
            length = math.sqrt((line[1][1]-line[0][1])**2 + (line[1][0]-line[0][0])**2)
            if length > 10:
                split = True
                # find the 2 break points
                stepx = (line[1][0] - line[0][0])/3 # a third of the x distance
                stepy = (line[1][1] - line[0][1])/3 # a third of the y distance
                b1 = (line[0][0]+stepx, line[0][1]+stepy)
                b2 = (line[0][0]+stepx*2, line[0][1]+stepy*2)
                lines.append((line[0],b1))
                b3 = calculateThirdPoint(b1,b2,length/3)
                lines.append((b1, b3))
                lines.append((b3, b2))
                lines.append((b2, line[1]))
            else:
                lines.append(line)
            
    clearShapes()
    for line in lines:
        drawLine(*line[0], *line[1], colour)
    updateDisplay()

for x in range(10,1000,40):
    drawkoch((450,750), x, "white")
    tick(20)
while True:
    for x in range(1000,3000,40):
        drawkoch((450,750), x, "white")
        tick(20)

endWait()