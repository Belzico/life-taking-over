import math
import globals
import queue
import random


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

def mapMaker(myMap,matrix):
    i=0
    while i < len(matrix):
        j=0
        while j < len(matrix[i]):
            myMap[i][j]=0

def sumMatrix(myMap,matrix):
    i=0
    while i < len(matrix):
        j=0
        while j < len(matrix[i]):
            myMap[i][j]+=matrix[i][j]

def mulMatrix(matrix,value):
    i=0
    while i < len(matrix):
        j=0
        while j < len(matrix[i]):
            matrix*=value
            
def pathFinder(currentIndividual,foodMatrix,dangerMatrix,mateMatrix,especiesMatrix):
    #mapa para trabajar
    myFixMap=[]    
    #mapa para la matrix de adyacencia
    myMap=[]
    mapMaker(myMap,foodMatrix)
    mapMaker(myFixMap,foodMatrix)
    if currentIndividual.naturalDefenseInd["Inteligencia"]>2:
        sumMatrix(myMap,mulMatrix(foodMatrix,currentIndividual.priorities['hambre']) )
    if currentIndividual.naturalDefenseInd["Inteligencia"]>5:
        sumMatrix(myMap,mulMatrix(dangerMatrix,currentIndividual.priorities['danger']) )
    if currentIndividual.naturalDefenseInd["Inteligencia"]>8:
        sumMatrix(myMap,mulMatrix( mateMatrix,currentIndividual.priorities['mate']))
    if currentIndividual.naturalDefenseInd["Inteligencia"]>11:
        sumMatrix(myMap,mulMatrix(especiesMatrix,currentIndividual.priorities["imanEspecie"]))
        
    destination=bestLocationFinder(myMap)
    adyacencyList=adyacencyMatrizBuilder(myMap)
    
    ucsSmart(myFixMap,adyacencyList,(len(foodMatrix)+1,len(foodMatrix[0])+1),destination,adyacencyList)
    
    
    i=0
    temp=fixRoad(myFixMap,destination,adyacencyList)
    currentPosition=None
    while(currentIndividual.naturalDefenseInd["Velocidad_agua"]>i):
        if  len(temp)>i:
            currentPosition=temp[i]
            currentIndividual.xMundo=currentPosition[0]
            currentIndividual.yMundo=currentPosition[1]
            if chanceToDie(dangerMatrix[currentPosition[0]][currentPosition[1]]):
                currentIndividual.die(globals.allSpecies[currentIndividual.especie])
                return    
         
        i+=1

def chanceToDie(risk,index=10):
    tempInt=random.randint(0,100)
    if tempInt<risk*index:
        return True
    return False

def bestLocationFinder(myMap):
    i=0
    temp=1000000
    result=None
    while i<len(myMap):
        j=0
        while j < len(myMap[i]):
            if temp<myMap[i][j]:
                temp=myMap[i][j]
                result=(i,j)
                
    return result
            
def fixRoad(mapa,destination,adyacencyList):
    road=[]
    road.append(destination)
    distance=mapa[destination[0],destination[1]].distancia
    currentPosition=destination
    while distance>0:
        for i in dir1Row:
            adyacentNode=(currentPosition[0]+dir1Row[i],currentPosition[1]+dir2Col[i])
            if mapa[currentPosition[0]][currentPosition[1]].visitado and mapa[currentPosition[0]][currentPosition[1]].distancia-adyacencyList(adyacentNode[0],adyacentNode[1],currentPosition[0],currentPosition[1])==mapa[adyacentNode[0]][adyacentNode[1]]:
                currentPosition=adyacentNode
                distance-=adyacencyList(adyacentNode[0],adyacentNode[1],currentPosition[0],currentPosition[1])
                road.append(currentPosition)
                break
    
        
    return listInversor(road)

def listInversor(lista):
    result=[]
    i=len(lista)-1
    j=0
    while i>0:
        result[j]=lista[i]        
        
    return result

#dijstra con euristica    
def ucsSmart(mapa,adyacencyList,myPosition,destination):
    myMap=mapZone(mapa)
    myMap[myPosition[0],myPosition[1]]=simpleNode(0,None,False)
    myQueue=queue.PriorityQueue()
    #aqui insertamos euristica
    myQueue.put((calcularDistancia(myPosition[0],myPosition[1],destination[0],destination[1]),myPosition))
    while myQueue.qsize()>0:
        temp=myQueue.get()
        if myMap[temp[1][0],temp[1][1]].visitado:
            continue
        myMap[temp[1][0],temp[1][1]].visitado=True
        if temp[1][0]==destination[0] and temp[1][1]==destination[1]:
            return
        for i in dir1Row:
            adyacentNode=(temp[1][0]+dir1Row[i],temp[1][1]+dir2Col[i])
            #distancia,padre,visto
            if not myMap[adyacentNode[0],adyacentNode[1]].visitado:
                #preguntando si la distancia euristica G es menor x este camino 
                if myMap[adyacentNode[0],adyacentNode[1]].distanciaEuristica> myMap[temp[1][0],temp[1][1]].distancia+calcularDistancia(temp[1][0],temp[1][1],adyacentNode[0],adyacentNode[1]): #adyacencyList[(temp[1][0],temp[1][1],adyacentNode[0],adyacentNode[1])]
                    #actualizando la distancia y la distancia euristica y padre
                    myMap[adyacentNode[0],adyacentNode[1]].distancia=myMap[temp[1][0],temp[1][1]][0]+adyacencyList[(temp[1][0],temp[1][1],adyacentNode[0],adyacentNode[1])]
                    myMap[adyacentNode[0],adyacentNode[1]].distanciaEuristica=myMap[temp[1][0],temp[1][1]].distancia+calcularDistancia(temp[1][0],temp[1][1],adyacentNode[0],adyacentNode[1])
                    myMap[adyacentNode[0],adyacentNode[1]].padre=myMap[temp[1][0],temp[1][1]]
                    #poniendo en la cola con el valor de la distancia euristica G
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
        self.distanciaEuristica=10000000
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