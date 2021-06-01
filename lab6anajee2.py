# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:07:32 2018

@author: Predecessor
"""
import random
import csv
import matplotlib.pyplot as plt

def plot_data(name, xnum, ynum):
    xnumList = []
    ynumList = []
    fileref = open('iris.csv')
    fileref = csv.reader(fileref)
    for i in fileref:
        if len(i) > 0:
            xnumList.append(i[xnum])
            ynumList.append(i[ynum])
        else:
            break
    plt.plot(xnumList)
    plt.plot(ynumList)
    plt.ylabel("SepalWidthCm")
    plt.xlabel("SepalLengthCm")
    plt.title("Sepal Width vs. Speal Length")
    plt.show()
    

    
def plot_random(fname, x, y, n):
    fileref = open('iris.csv')
    fileref = csv.reader(fileref)
    randnum = 0
    while (randnum < 50):
        for i in fileref:
            minx = int(min(x))
            miny = int(min(y))
            n = random.uniform(minx, miny)
            randnum += 1
    plt.plot(n)

    
    
    
    
plot_data("iris.csv", 1, 2)
plot_random("iris.csv", 2, 4, 1)
    
    
