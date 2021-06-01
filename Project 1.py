# Created By: Abdullah Najeeb
# Date: 10/14/2019
'''


import random

def encryption(S, n):
    S.lower()
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    newString = ''
    for x in S:
        if x == ' ':
            newString+= ' '
            continue
        index = alphabet.find(x)
        index += n
        if index >= 26:
            index = 0 + index % 26
        newString += alphabet[index]
    newString += str(n)
    return newString

def decryption(W):
    count = 0
    for x in range(len(W)):
        if W[x].isdigit():
            var = W[x:]
            break
        count += 1
    var = int(var)
    var =- var
    string = W[0:count]
    decrypt = encryption(string, var)
    return decrypt[0:count]

def main():
    print(encryption('hello world', 1))
    print(decryption('ebiil tloia23'))
    randomSeed()

def randomSeed():
    random.seed(10)

    #Generate Random Number First Time
    var = random.randint(1, 27)
    first = encryption('hello world', var)
    print(first)
    print(decryption(first))

    #Generate Random Number Second Time
    randVar = random.randint(1, 27)
    second = encryption('computer science', randVar)
    print(second)
    print(decryption(second))

    #Generate Random Number Third Time
    randNum = random.randint(1, 27)
    third = encryption('abdullah najeeb', randNum)
    print(third)
    print(decryption(third))



main()

'''

import turtle

t = turtle.Turtle()


def drawRectangle(t, length, width, x, y, color, pensize, heading):
    """ t is a Turtle object.  """
    t.pensize(pensize)
    t.setheading(heading)
    t.penup()
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.back(.5 * length)
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.end_fill()
    t.setheading(0)
    t.pensize()
    t.setheading()


drawRectangle(t, 50, -50, 75, 15, "green", 45, 2)
drawRectangle(t, 0, 0, 30, 75, "orange", 0, 10)
drawRectangle(t, 100, 100, 25, 25, "purple", 75, 5)
turtle.done()
