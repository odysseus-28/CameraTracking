from random import *
import array as arr
import numpy as np


def pointGen():
    x = randint(0, 100)
    y = randint(0, 100)
    return x, y


def distance(firstPoint, secondPoint):
    deltaY = (firstPoint[1] - secondPoint[1]) ** 2
    deltaX = (firstPoint[0] - secondPoint[0]) ** 2
    totDelta = deltaY + deltaX
    return totDelta ** 0.5


def printer(distances):
    for i in range(0, len(distances) -1):
        for j in range(0, len(distances[i]) -1):
            print(distances[i][j])


def main():
    points = []
    distances = []
    no_of_points = 4

    points.append((0,0)) # origin(camera location), is point 0
    for i in range(0, no_of_points):
        points.append(pointGen())

    points_ref = points
    for i in range(0, no_of_points):
        point_i = []
        for j in range(0, no_of_points):
            point_i.append(distance(points[i],points[j]))
        #print(f"point_i: {point_i}")
        distances.append(point_i)

    printer(distances)
    print(f"the points are: {points}")
    print(f"the distances are: {distances}")


if __name__ == "__main__":
    main()
