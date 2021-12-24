def dictMergeSum(dict1, dict2):
    tempdict ={}
    for i in dict1.key():
        tempdict[i] = int(dict1[i])+ int(dict2[i])
        
    return tempdict



class Coordinates:
    X = -1
    Y = -1

    def __init__(self, x, y):
        self.X = x
        self.Y = y



class Element:
    def __init__(self,atmoicValue, name):
        self.AtomicValue = atmoicValue
        self.Name = name
