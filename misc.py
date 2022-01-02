import math
import globals
import queue


dir1Row=[0,-1,-1,-1,0,1,1,1]
dir2Col=[1,1,0,-1,-1,-1,0,1]

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

#dijstra con euristica    
def ucsSmart(mapa,adyacencyList,myPosition,destination):
    myMap=mapZone(mapa)
    myMap[myPosition[0],myPosition[1]]=simpleNode(0,None,False)
    myQueue=queue.PriorityQueue()
    #aqui insertar euristica
    myQueue.put((0,myPosition))
    while myQueue.qsize()>0:
        temp=myQueue.get()
        if myMap[temp[1][0],temp[1][1]].visitado:
            continue
        myMap[temp[1][0],temp[1][1]].visitado=True
        for i in dir1Row:
            adyacentNode=(temp[1][0]+dir1Row[i],temp[1][1]+dir2Col[i])
            #distancia,padre,visto
            if not myMap[adyacentNode[0],adyacentNode[1]].visitado:
                if myMap[adyacentNode[0],adyacentNode[1]].distancia> myMap[temp[1][0],temp[1][1]].distancia+adyacencyList[(temp[1][0],temp[1][1],adyacentNode[0],adyacentNode[1])]:
                    myMap[adyacentNode[0],adyacentNode[1]].distancia=myMap[temp[1][0],temp[1][1]][0]+adyacencyList[(temp[1][0],temp[1][1],adyacentNode[0],adyacentNode[1])]
                    myQueue.put(myMap[temp[1][0],temp[1][1]].distancia+adyacencyList[(temp[1][0],temp[1][1],adyacentNode[0],adyacentNode[1])],(adyacentNode[0],adyacentNode[1]))


def calcularDistancia(self,x1,y1,x2,y2):
    return math.sqrt(abs(x1-x2)+abs(y1-y2)) 

def adyacencyMatrizBuilder(mapa):
    adyacencyList={}
    x=0
    while x < len(mapa):
        y=0
        while y < len(mapa[x]):
            k=0
            while k < len(dir1Row):
                if x+dir1Row[k] >=0 and x+dir1Row[k]< len(mapa) and y+dir2Col[k]>=0 and y+dir2Col[k]<len(mapa[x]):
                    adyacencyList[(x,y,x+dir1Row[k],y+dir2Col[k])]=mapa[x+dir1Row[k]][y+dir2Col[k]]
                k+=1
            y+=1
        x+=1   
    return adyacencyList                        

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

class simpleNode():
    def __init__(self,distancia,padre,visitado):
        self.distancia=distancia
        self.padre=padre
        self.visitado=visitado

class mapZone():
    def __init__(self,myMap):
        i=0
        while i < len(myMap):
            j=0
            while j < len(myMap[i]):
                #distancia=infinita,padre=none,visto=false
                myMap[i][j]=simpleNode(1000000,None,False)

myMap=[[5,3,2,1,0],[0,2,0,1,3],[6,3,0,3,6],[0,1,0,2,0],[1,6,5,2,1]]

test=adyacencyMatrizBuilder(myMap)

print("final test")