# Creator: Abdullah Najeeb
# Due: 12/6/2019

import math


class Triangle(object):

    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By
        self.Cx = Cx
        self.Cy = Cy
        self.AB = self.distance(Ax, Ay, Bx, By)
        self.BC = self.distance(Bx, By, Cx, Cy)
        self.CA = self.distance(Cx, Cy, Ax, Ay)

    def __str__(self):
        return "Triangle(A" + '(' + str(self.Ax) + ',' + str(self.Ay) + ')' + ', B' + '(' + str(self.Bx) + ',' + str(
            self.By) + ')' + ', C' + '(' + str(self.Cx) + ',' + str(self.Cy) + ')' + ')'

    def distance(self, l, m, n, o):
        return math.sqrt((l - n) ** 2 + (m - o) ** 2)

    def perimeter(self):
        return self.AB + self.BC + self.CA

    def area(self):
        perimeter = self.perimeter() / 2.0
        return (perimeter * (perimeter - self.AB) * (perimeter - self.BC) * (perimeter - self.CA)) ** 0.5

    def longestSide(self):
        return max(self.AB, self.BC, self.CA)

    def classifyBySideLength(self):
        if (self.AB == self.BC) and (self.BC == self.CA):
            return 'Equilateral Triangle'
        elif (self.AB == self.BC) or (self.BC == self.CA) or (self.AB == self.CA):
            return 'Isosceles Triangle'
        else:
            return 'Scalene Triangle'

    def isRightTriangle(self):
        if self.longestSide() != self.AB and self.BC:
            if self.CA ** 2 == (self.AB ** 2) + (self.BC ** 2):
                return True
        if self.longestSide() != self.BC and self.CA:
            if self.AB ** 2 == (self.BC ** 2) + (self.CA ** 2):
                return True
        if self.longestSide() != self.CA and self.AB:
            if self.BC ** 2 == (self.CA ** 2) + (self.AB ** 2):
                return True

        return False

    def centroid(self):
        return ((self.Ax + self.Bx + self.Cx) / 3.0, (self.Ay + self.By + self.Cy) / 3.0)


def main():
    filename = open("TriangleOutput.txt", "w")

    T1 = Triangle(0, 0, 3, 0, 0, 4)
    perimeter1 = T1.perimeter()
    area1 = T1.area()
    longside1 = T1.longestSide()
    classification1 = T1.classifyBySideLength()
    righttriangle1 = T1.isRightTriangle()
    centroid1 = T1.centroid()

    T2 = Triangle(5, 30, 27, 43, 18, 8)
    perimeter2 = T2.perimeter()
    area2 = T2.area()
    longside2 = T2.longestSide()
    classification2 = T2.classifyBySideLength()
    righttriangle2 = T2.isRightTriangle()
    centroid2 = T2.centroid()

    filename.write(str(T1))
    filename.write('\n' + 'Area: {}'.format(area1))
    filename.write('\n' + 'Perimeter: {}'.format(perimeter1))
    filename.write('\n' + 'LongestSide: {}'.format(longside1))
    filename.write('\n' + 'ClassifyBySideLength: {}'.format(classification1))
    filename.write('\n' + 'IsRightTriangle: {}'.format(righttriangle1))
    filename.write('\n' + 'Centroid: {}'.format(centroid1))

    filename.write('\n' + '\n')

    filename.write(str(T2))
    filename.write('\n' + 'Area: {}'.format(area2))
    filename.write('\n' + 'Perimeter: {}'.format(perimeter2))
    filename.write('\n' + 'LongestSide: {}'.format(longside2))
    filename.write('\n' + 'ClassifyBySideLength: {}'.format(classification2))
    filename.write('\n' + 'IsRightTriangle: {}'.format(righttriangle2))
    filename.write('\n' + 'Centroid: {}'.format(centroid2))

    filename.close()


main()
