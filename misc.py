import random

#class Coordinates:
#    X = -1
#   Y = -1
#
#    def __init__(self, x, y):
#        self.X = x
#        self.Y = y

from random import randint


class Element:
    def __init__(self,atmoicValue, name):
        self.AtomicValue = atmoicValue
        self.Name = name

def randCord(xmin,xmax,ymin,ymax):
    x = randint(xmin,xmax)
    y = randint(ymin,ymax)
    return (x,y)