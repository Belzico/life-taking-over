import globals

def dictMergeSum(dict1, dict2):
    tempdict ={}
    
    #Llenando el dict2 en caso de que sea vacío
    if len(dict2.keys()) == 0:
        for i in dict1.keys():
            dict2[i] = 0
    
    
    for i in dict1.keys():
        tempdict[i] = int(dict1[i])+ int(dict2[i])
        
    return tempdict

def dictMergeSubstract(dict1, dict2):
    tempdict ={}
    
    #Llenando el dict2 en caso de que sea vacío
    if len(dict2.keys()) == 0:
        for i in dict1.keys():
            dict2[i] = 0
    
    for i in dict1.keys():
        tempdict[i] = int(dict1[i])- int(dict2[i])
        
    return tempdict

def dictPromed(dict1, dict2):
    tempdict ={}
    
    
    for i in dict1.keys():
        if (int(dict1[i])+ int(dict2[i]))%2==1:
            tempdict[i] =1+ (int(dict1[i])+ int(dict2[i]))/2
        else:
            tempdict[i] = (int(dict1[i])+ int(dict2[i]))/2
        
    return tempdict

def dieList():
    for item in globals.deadIndividuals:
        if item in globals.worldIndividuals.keys():
            del globals.worldIndividuals[item]
    globals.deadIndividuals=[]

def bornList():
    for item in globals.bornIndividuals:
        globals.worldIndividuals[item[0]]=item[1]
    globals.bornIndividuals=[]

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
