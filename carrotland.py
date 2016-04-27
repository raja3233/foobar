
import math
def answer(vertices):
    #given vertices
    vertices.sort(key = lambda x: x[0])
    x1, y1 = vertices[0]
    x2, y2 = vertices[1]
    x3, y3 = vertices[2]
    #caluclate line equation ax + by + c as [a, b, c]
    line1 = lineEquation(x1, y1, x2, y2)
    line2 = lineEquation(x2, y2, x3, y3)
    line3 = lineEquation(x3, y3, x1, y1)
    count = 0
    if (x3 - x1) < (y3 -y1):
        vertices.sort(key = lambda x: x[0])
        x1, y1 = vertices[0]
        x2, y2 = vertices[1]
        x3, y3 = vertices[2]
        #caluclate line equation ax + by + c as [a, b, c]
        line1 = lineEquation(x1, y1, x2, y2)
        line2 = lineEquation(x2, y2, x3, y3)
        line3 = lineEquation(x3, y3, x1, y1)
        count = 0
        y1_x, y2_x = 0.0, 0.0
        #identify the intersection points y vlaue on the triangles
        #for every  X = p line where x1 < p < x3
        for x in range(x1 + 1, x3):
            if x < x2 :#intersection of X=p and line1,2
                y1_x = -(float(line1[0])/line1[1]) * (x - x1) + y1
            else:#intersection of X=p and line1,2
                y1_x = -(float(line2[0])/line2[1]) * (x - x2) + y2
             #second intersection point is always line 3
            y2_x = -(float(line3[0])/line3[1]) * (x - x3) + y3

            if y1_x < y2_x:
                y1_x = math.floor(y1_x)
                y2_x = math.ceil(y2_x)
            else:
                y1_x = math.ceil(y1_x)
                y2_x = math.floor(y2_x)
            count += abs(y1_x - y2_x) - 1
    else:
        vertices.sort(key = lambda x: x[1])
        x1, y1 = vertices[0]
        x2, y2 = vertices[1]
        x3, y3 = vertices[2]
        #caluclate line equation ax + by + c as [a, b, c]
        line1 = lineEquation(x1, y1, x2, y2)
        line2 = lineEquation(x2, y2, x3, y3)
        line3 = lineEquation(x3, y3, x1, y1)
        count = 0

        for y in range(y1 + 1,  y3):
            if y < y2 :#intersection of X=p and line1,2
                x1_y = -(float(line1[1])/line1[0]) * (y - y1) + x1
            else:#intersection of X=p and line1,2
                x1_y = -(float(line2[1])/line2[0]) * (y - y2) + x2
             #second intersection point is always line 3
            x2_y = -(float(line3[1])/line3[0]) * (y - y3) + x3

            if x1_y < x2_y:
                x1_y = math.floor(x1_y)
                x2_y = math.ceil(x2_y)
            else:
                x1_y = math.ceil(x1_y)
                x2_y = math.floor(x2_y)
            count += abs(x1_y - x2_y) - 1


    return count


def Y_of_intersection(line,x,x1,y1):
    return -(float(line[0])/line[1]) * (x - x1) + y1

def slope(line):
    return -(float(line[0])/line[1])

def lineEquation(x1, y1, x2, y2):
    a = y2 - y1
    b = x1 - x2
    c = (x2 - x1) * y1 - (y2 - y1) * x1
    return a, b, c

print answer([[0,0],[1,8],[4,6]])
print answer([[2, 3], [6, 9], [10, 160]])
print answer([[91207, 89566], [-88690, -83026], [67100, 47194]])