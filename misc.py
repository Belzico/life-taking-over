from audioop import reverse
from dis import dis
import math
import globals
import queue
import random
from ArbolEvolutivo.arbolEvolutivo import Arbol_Evo


dir1Row=[0,-1,-1,-1, 0, 1,1,1]
dir2Col=[1,1,  0,-1,-1,-1,0,1]

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

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
        myMap.append([])
        j=0
        while j < len(matrix[i]):
            if matrix[i][j]==globals.voidValue:
                myMap[i].append(globals.voidValue)    
            else:
                myMap[i].append(0)
            j+=1
        i+=1
def sumMatrix(myMap,matrix):
    i=0
    while i < len(matrix):
        j=0
        while j < len(matrix[i]):
            myMap[i][j]+=matrix[i][j]
            j+=1
        i+=1
        
def mulMatrix(matrix,value):
    i=0
    while i < len(matrix):
        j=0
        while j < len(matrix[i]):
            if matrix[i][j]!=globals.voidValue: 
                matrix[i][j]*=value
            j+=1
        i+=1    
    return matrix
            
            
def pathFinder(currentIndividual,mapa):
    
    previusX,previusY=currentIndividual.xMundo,currentIndividual.yMundo
    #mapa para trabajar
    myFixMap=[]    
    #mapa para la matrix de adyacencia
    myMap=[]
    foodMatrix=mapa["Comida"]
    dangerMatrix=mapa["Peligro"]
    mateMatrix=mapa["Pareja"]
    especiesMatrix=mapa["Especie"]
    deathMatrix=mapa["Peligro Real"]
    
    
    mapMaker(myMap,mapa["Tile"])
    mapMaker(myFixMap,mapa["Tile"])
    
    
    if currentIndividual.naturalDefenseInd["Inteligencia"]>=2:
        sumMatrix(myMap,mulMatrix(foodMatrix,currentIndividual.priorities['hambre']) )
    if currentIndividual.naturalDefenseInd["Inteligencia"]>5:
        sumMatrix(myMap,mulMatrix(dangerMatrix,currentIndividual.priorities['danger']) )
    if currentIndividual.naturalDefenseInd["Inteligencia"]>8:
        sumMatrix(myMap,mulMatrix( mateMatrix,currentIndividual.priorities['mate']))
    if currentIndividual.naturalDefenseInd["Inteligencia"]>11:
        sumMatrix(myMap,mulMatrix(especiesMatrix,currentIndividual.priorities["imanEspecie"]))
        
    destination=bestLocationFinder(myMap)
    adyacencyList=adyacencyMatrizBuilder(myMap)
    
    myPosition=(int((len(foodMatrix)-1)/2),int((len(foodMatrix)-1)/2))
    
    
    
    road= ucsSmart(myFixMap,adyacencyList,myPosition,destination)
    

    i=1
    temp=fixRoad(road,destination,myPosition)
    currentPosition=None
    lastPosition=temp[0]
    
    #caso en que no se mueve
    if currentIndividual.naturalDefenseInd["Velocidad_agua"]<=i:
        if chanceToDie(deathMatrix[currentPosition[0]][currentPosition[1]]):
                globals.worldMap.udpdateIndividual(currentIndividual,previusX,previusY)
                print("Yo "+currentIndividual.name+" me movi hacia "+str(currentIndividual.xMundo) +","+str(currentIndividual.yMundo)+"")
                currentIndividual.die("Moving")
                #actualizando las zonas de estancia de la especie
                currentIndividual.especie.dataDicc["Zone"][globals.worldMap.Tiles[currentIndividual.xMundo][currentIndividual.yMundo].Zone.ZoneType]+=1
                return False    
        
        
    while(currentIndividual.naturalDefenseInd["Velocidad_agua"]>i):
        if  len(temp)>i:
            currentPosition=temp[i]
            currentIndividual.xMundo+=currentPosition[0] - lastPosition[0] 
            currentIndividual.yMundo+=currentPosition[1] - lastPosition[1] 
            
            #actualizando las zonas de estancia de la especie
            currentIndividual.especie.dataDicc["Zone"][globals.worldMap.Tiles[currentIndividual.xMundo][currentIndividual.yMundo].Zone.ZoneType]+=1
            
            if chanceToDie(deathMatrix[currentPosition[0]][currentPosition[1]]):
                globals.worldMap.udpdateIndividual(currentIndividual,previusX,previusY)
                print("Yo "+currentIndividual.name+" me movi hacia "+str(currentIndividual.xMundo) +","+str(currentIndividual.yMundo)+"")
                currentIndividual.die("Moving")
                return False    

            previusX,previusY=currentIndividual.xMundo,currentIndividual.yMundo
            lastPosition=currentPosition                
        i+=1
    return True




def chanceToDie(risk):
    chanceToDie=secondPercent(risk,globals.MaxDangerinTile)*globals.killerModifier 
    tempInt=random.randint(0,100)
    if tempInt<chanceToDie:
        return True
    return False



def bestLocationFinder(myMap):
    i=0
    temp=globals.voidValue
    result=None
    while i<len(myMap):
        j=0
        while j < len(myMap[i]):
            if temp>myMap[i][j] and myMap[i][j]!=globals.voidValue:
                temp=myMap[i][j]
                result=(i,j)
            j+=1
        i+=1        
    return result

#revisar que no se salga de los indices de la matrix
def indexChecker(tup,size):
    for i in range(len(tup)):
        if int(tup[i])<0 or int(tup[i])>=int(size):
            return False
    return True

def fixRoad(mapa,destination,origin):
    road=[]
    road.append(destination)
    currentPosition=destination
    if  abs(destination[0]-origin[0])>1 and abs(destination[1]-origin[1])>1:
        print('a')
    
    while mapa[currentPosition[0]][currentPosition[1]].padre!=None:
        road.append(mapa[currentPosition[0]][currentPosition[1]].padre)
        currentPosition=mapa[currentPosition[0]][currentPosition[1]].padre
    return listInversor(road)

def listInversor(lista):
    result=[]
    i=len(lista)-1
    while i>=0:
        result.append(lista[i])
        i-=1
    return result

#dijstra con euristica    
def ucsSmart(mapa,adyacencyList,myPosition,destination):
    myMap=mapZone(mapa)
    x1=myPosition[0]
    y1=myPosition[1]
    myMap[x1][y1]=simpleNode(0,None,False)
    
    myQueue=queue.PriorityQueue()
    
    #aqui insertamos euristica
    myQueue.put((calcularDistancia(myPosition[0],myPosition[1],destination[0],destination[1]),myPosition))
    while myQueue.qsize()>0:
        temp=myQueue.get()

        if myMap[temp[1][0]][temp[1][1]].visitado:
            continue
        myMap[temp[1][0]][temp[1][1]].visitado=True
        if temp[1][0]==destination[0] and temp[1][1]==destination[1]:
            break
        i=0
        while i < len(dir1Row):
            adyacentNode=(temp[1][0]+dir1Row[i],temp[1][1]+dir2Col[i])
            #revisando q no este visitado y q sea una posicion valida
            valid=indexChecker(adyacentNode,len(mapa))
            
            if valid  and not myMap[adyacentNode[0]][adyacentNode[1]].visitado  and mapa[adyacentNode[0]][adyacentNode[1]]!=globals.voidValue:
                #preguntando si la distancia euristica G es menor x este camino 
                if  myMap[adyacentNode[0]][adyacentNode[1]].distanciaEuristica> myMap[temp[1][0]][temp[1][1]].distancia+calcularDistancia(temp[1][0],temp[1][1],adyacentNode[0],adyacentNode[1]): #adyacencyList[(temp[1][0],temp[1][1],adyacentNode[0],adyacentNode[1])]
                    #actualizando la distancia y la distancia euristica y padre
                    myMap[adyacentNode[0]][adyacentNode[1]].distancia=myMap[temp[1][0]][temp[1][1]].distancia+adyacencyList[(temp[1][0],temp[1][1],adyacentNode[0],adyacentNode[1])]
                    myMap[adyacentNode[0]][adyacentNode[1]].distanciaEuristica=myMap[temp[1][0]][temp[1][1]].distancia+calcularDistancia(destination[0],destination[1],adyacentNode[0],adyacentNode[1])+adyacencyList[(temp[1][0],temp[1][1],adyacentNode[0],adyacentNode[1])]
                    myMap[adyacentNode[0]][adyacentNode[1]].padre=(temp[1][0],temp[1][1])
                    #poniendo en la cola con el valor de la distancia euristica G
                    myQueue.put((myMap[adyacentNode[0]][adyacentNode[1]].distanciaEuristica,(adyacentNode[0],adyacentNode[1])))

            i+=1
    return myMap
    

def calcularDistancia(x1,y1,x2,y2):
    temp =math.sqrt(pow(abs(x1-x2),2)+pow(abs(y1-y2),2))
    return temp

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
        self.distanciaEuristica=globals.voidValue
        self.padre=padre
        self.visitado=visitado

def mapZone(myMap):
    newMap=[]
    i=0
    while i < len(myMap):
        j=0
        newMap.append([])
        while j < len(myMap[i]):
            #distancia=infinita,padre=none,visto=false
            newMap[i].append(simpleNode(globals.voidValue,None,False))
            j+=1
        i+=1

    return newMap
                


    ##################################################combate##########################################
    
    #tipos de accion se recibe una accion de lucha y una cantidad de pasos para escapar
    #1-caminar hacia alguna casilla 
    #2-atacar con golpe normal que hace daño normal
    #3-atacar con ataque debil, este tiene mas chance de critico
    #4-atacar a bajar velocidad (bajo daño bajo critico alto chance de lenteo)
    #dir= countPredictionsFirst,countPredictionsSecond,moves,atacks,debuffs,mapa,firstIndividualPos,SecondIndividualPos,firstIndividualVit,SecondIndividualVit 
def combatTurnPredator(predator,prey,battleLogPredator,battleLogPrey,myMap,whosPredicting,iteration):
    #(value,tuple) tuple is a tuple with las position and which attack
    fullResult=None
    result4=None
    result1=None
    result2=None
    result3=None
    

    

    
    posX=battleLogPredator["xPosition"]
    posY=battleLogPredator["yPosition"]
    enemyPosX=battleLogPrey["xPosition"]
    enemyPosY=battleLogPrey["yPosition"]
    
    
    fastResult=None
    if battleLogPrey["life"]<=0:
        fastResult=(1000000,(posX,posY,battleLogPrey["action"]))
        return fastResult
    if battleLogPredator["life"]<=0:
        fastResult=(-1000000,(posX,posY,battleLogPrey["action"]))
        return fastResult
        
    if checkBorderEscape((battleLogPrey["xPosition"],battleLogPrey["yPosition"]),myMap):
        fastResult=(-5000,(enemyPosX,enemyPosY,battleLogPrey["action"]))
        return fastResult
    
    value=euristicaHunt(battleLogPredator,battleLogPrey,myMap)
    
    if iteration<0:
        action=battleLogPrey["action"]
        return (value,(posX,posY,action))
    
        
    moves=battleLogPredator["movements"]-battleLogPredator["debuffSlow"]
    if moves > 0:
        
        reacheableList=reacheablePos(battleLogPredator,battleLogPrey,myMap,0)
        iCount=globals.tempPredictions
        for item in reacheableList:
            
            if iCount==0:
                break
            
            iCount-=1
            
            newDiccPredator=copyBattleLog(battleLogPredator)
            newDiccPrey=copyBattleLog(battleLogPrey)
            newDiccPredator["xPosition"]=item[1]
            newDiccPredator["yPosition"]=item[2]
            
            tempresult=combatTurnPrey(predator,prey,newDiccPredator,newDiccPrey,myMap,whosPredicting,iteration-1)
            if tempresult==None:continue
            if result4==None:
                result4=tempresult
            if whosPredicting == 0:
                if result4[0]>tempresult[0]:
                    result4=tempresult
            else:
                if result4[0]<tempresult[0]:
                    result4=tempresult
            result4=(result4[0],(posX,posY,battleLogPredator["action"]))
        
                        
    if battleLogPredator["action"]==None and hitRange((posX,posY),(battleLogPrey["xPosition"],battleLogPrey["yPosition"])):
        newDiccPredator1=copyBattleLog(battleLogPredator)
        newDiccPrey1=copyBattleLog(battleLogPrey)
        newDiccPredator1["action"]="normalHit"
        standarAttack(predator,prey,newDiccPredator1,(2,1,1))
        result1=combatTurnPrey(predator,prey,newDiccPredator1,newDiccPrey1,myMap,whosPredicting,iteration-1)
        result1=(result1[0],(posX,posY,"normalHit"))
        
        newDiccPredator2=copyBattleLog(battleLogPredator)
        newDiccPrey2=copyBattleLog(battleLogPrey)
        newDiccPredator2["action"]="critHit"
        standarAttack(predator,prey,newDiccPredator2,(1,2,1))
        result2=combatTurnPrey(predator,prey,newDiccPredator2,newDiccPrey2,myMap,whosPredicting,iteration-1)
        result2=(result2[0],(posX,posY,"critHit"))
        
        newDiccPredator3=copyBattleLog(battleLogPredator)
        newDiccPrey3=copyBattleLog(battleLogPrey)
        newDiccPredator3["action"]="slowHit"
        standarAttack(predator,prey,newDiccPredator1,(1,1,2))
        result3=combatTurnPrey(predator,prey,newDiccPredator3,newDiccPrey3,myMap,whosPredicting,iteration-1)
        result3=(result3[0],(posX,posY,"slowHit"))
        

    if whosPredicting==0:
        fullResult=bestResultMax([result1,result2,result3,result4])
    else:
        fullResult=bestResultMin([result1,result2,result3,result4])
        
    return fullResult
    
        
        


def combatTurnPrey(predator,prey,battleLogPredator,battleLogPrey,myMap,whosPredicting,iteration):
    #(value,tuple) tuple is a tuple with las position and which attack
    fullResult=None
    result4=None
    result1=None
    result2=None
    result3=None
    
    posX=battleLogPrey["xPosition"]
    posY=battleLogPrey["yPosition"]
    enemyPosX=battleLogPredator["xPosition"]
    enemyPosY=battleLogPredator["yPosition"]
    
    if battleLogPredator["life"]<=0: return (1000000,(posX,posY,battleLogPredator["action"]))
    if battleLogPrey["life"]<=0: return (-1000000,(posX,posY,battleLogPredator["action"]))
    if checkBorderEscape((battleLogPrey["xPosition"],battleLogPrey["yPosition"]),myMap): return (5000,(enemyPosX,enemyPosY,battleLogPredator["action"]))
    
    value=euristicaHuir(battleLogPrey,battleLogPredator,myMap)
    
    
    if iteration<0:
        action=battleLogPredator["action"]
        return (value,(posX,posY,action))

    moves=battleLogPrey["movements"]-battleLogPrey["debuffSlow"]
    if moves > 0:
        
        reacheableList=reacheablePos(battleLogPrey,battleLogPredator,myMap,1)
        iCount=globals.tempPredictions
        for item in reacheableList:
            
            if iCount==0:
                break
            
            iCount-=1
            
            newDiccPredator=copyBattleLog(battleLogPredator)
            newDiccPrey=copyBattleLog(battleLogPrey)
            newDiccPrey["xPosition"]=item[1]
            newDiccPrey["yPosition"]=item[2]
            
            tempresult=combatTurnPredator(predator,prey,newDiccPredator,newDiccPrey,myMap,whosPredicting,iteration-1)
            
            if tempresult==None:continue
            if result4==None:
                result4=tempresult
            if whosPredicting == 1:
                if result4[0]>tempresult[0]:
                    result4=tempresult
            else:
                if result4[0]<tempresult[0]:
                    result4=tempresult
            result4=(result4[0],(posX,posY,battleLogPrey["action"]))
            
    
    
    if battleLogPrey["action"]==None and hitRange((posX,posY),(battleLogPredator["xPosition"],battleLogPredator["yPosition"])):
        newDiccPredator1=copyBattleLog(battleLogPredator)
        newDiccPrey1=copyBattleLog(battleLogPrey)
        newDiccPrey1["action"]="normalHit"
        standarAttack(prey,predator,newDiccPredator1,(2,1,1))
        result1=combatTurnPredator(predator,prey,newDiccPredator1,newDiccPrey1,myMap,whosPredicting,iteration-1)
        result1=(result1[0],(posX,posY,"normalHit"))
        
        newDiccPredator2=copyBattleLog(battleLogPredator)
        newDiccPrey2=copyBattleLog(battleLogPrey)
        newDiccPrey2["action"]="critHit"
        standarAttack(prey,predator,newDiccPredator2,(1,2,1))
        result2=combatTurnPredator(predator,prey,newDiccPredator2,newDiccPrey2,myMap,whosPredicting,iteration-1)
        result2=(result2[0],(posX,posY,"critHit"))
        
        newDiccPredator3=copyBattleLog(battleLogPredator)
        newDiccPrey3=copyBattleLog(battleLogPrey)
        newDiccPrey3["action"]="slowHit"
        standarAttack(prey,predator,newDiccPredator1,(1,1,2))
        result3=combatTurnPredator(predator,prey,newDiccPredator3,newDiccPrey3,myMap,whosPredicting,iteration-1)
        result3=(result3[0],(posX,posY,"slowHit"))
        
    if whosPredicting==1:
        fullResult=bestResultMax([result1,result2,result3,result4])
    else:
        fullResult=bestResultMin([result1,result2,result3,result4])
    return fullResult

def reacheablePos(newDiccFirst,newDiccSecond,myMap,whosPredicting):
    valuePosible=0
    oldX=newDiccFirst["xPosition"]
    oldY=newDiccFirst["yPosition"]
    
    resultList=[]
    
    tempMap=mapCreator(len(myMap))
    tempQueu=queue.Queue()
    value=0
    if whosPredicting==0:
        value=euristicaHunt(newDiccFirst,newDiccSecond,myMap)
    else:
        value=euristicaHuir(newDiccFirst,newDiccSecond,myMap)
    
    tempQueu.put((0,oldX,oldY))
    while tempQueu.qsize()>0:
        currentElement=tempQueu.get()
        if newDiccFirst["movements"]-newDiccFirst["debuffSlow"]<currentElement[0]:
            break
        for j in range(len(dir1Row)):
            if indexChecker((currentElement[1]+dir1Row[j],currentElement[1]+dir2Col[j]),len(myMap)) and tempMap[currentElement[1]+dir1Row[j]][currentElement[1]+dir2Col[j]]==1000:
                tempMap[currentElement[1]+dir1Row[j]][currentElement[1]+dir2Col[j]]=currentElement[0]+1
                tempQueu.put((currentElement[0]+1,currentElement[1]+dir1Row[j],currentElement[1]+dir2Col[j]))
    

            
    for i in range(len(tempMap)):
        for j in range(len(tempMap[0])):
            if tempMap[i][j]!=1000:
                newDiccFirst["xPosition"]=i
                newDiccFirst["yPosition"]=j
                if whosPredicting==0:
                    valuePosible=euristicaHunt(newDiccFirst,newDiccSecond,myMap)
                else:
                    valuePosible=euristicaHuir(newDiccFirst,newDiccSecond,myMap)
                
                if  valuePosible>=value:
                    resultList.append((valuePosible,i,j))
                
    newDiccFirst["xPosition"]=oldX
    newDiccFirst["yPosition"]=oldY
    
    resultList.sort(key= lambda x: x[0],reverse=True)
    return resultList



def bestResultMax(listRes):
    tempMax=None
        
    for i in range(len(listRes)):
        if listRes[i]==None:
            continue
        if tempMax==None:
            tempMax=listRes[i]
        else:
            if listRes[i][0]>tempMax[0]:
                tempMax=listRes[i]
    
    return tempMax


def bestResultMin(listRes):
    tempMax=None
        
    for i in range(len(listRes)):
        if listRes[i]==None:
            continue
        if tempMax==None:
            tempMax=listRes[i]
        else:
            if listRes[i][0]<tempMax[0]:
                tempMax=listRes[i]
    
    return tempMax
    

def hitRange(predatorPos,preyPos):
    if abs(predatorPos[0]-preyPos[0])<=1 and abs(predatorPos[1]-preyPos[1])<=1:
        return True
    return False

def mapCreator(sizeMap):
    result=[]
    for i in range(sizeMap):
        result.append([])
        for j in range(sizeMap):
            result[i].append(1000)
    
    return result

def fixFutureSigth(futureSigthPredator,futureSigthPrey):
    if futureSigthPredator>futureSigthPrey:
        sigthTempPredator=secondPercent(futureSigthPrey,futureSigthPredator)
        futureSigthPredator=5
        if sigthTempPredator<25:
            futureSigthPrey=1
        elif sigthTempPredator<50:
            futureSigthPrey=2
        elif sigthTempPredator<75:
            futureSigthPrey=3
        else :
            futureSigthPrey=4
    elif futureSigthPredator==futureSigthPrey:
        futureSigthPredator=5
        futureSigthPrey=5
    else:
        sigthTempPrey=secondPercent(futureSigthPredator,futureSigthPrey)
        futureSigthPrey=5
        if sigthTempPrey<25:
            futureSigthPredator=1
        elif sigthTempPrey<50:
            futureSigthPredator=2
        elif sigthTempPrey<75:
            futureSigthPredator=3
        else :
            futureSigthPredator=4
            
    return (futureSigthPredator,futureSigthPrey)

#este es el metodo a invocar para que ocurra el combate
def fullCombat(predator,prey):
    
    futureSigthPredator=(predator.naturalDefenseInd["Inteligencia"]+predator.naturalDefenseInd["Percepcion_de_mundo"])//2
    futureSigthPrey=(prey.naturalDefenseInd["Inteligencia"]+prey.naturalDefenseInd["Percepcion_de_mundo"])//2
    
    if max(futureSigthPredator,futureSigthPrey)>5:
        tempSigth= fixFutureSigth(futureSigthPredator,futureSigthPrey)
        futureSigthPredator=tempSigth[0]
        futureSigthPrey=tempSigth[1]
        
    mapLentgh=max(predator.naturalDefenseInd["Velocidad_agua"],prey.naturalDefenseInd["Velocidad_agua"])
    #parche por si la matrix se hace muy grande
    if mapLentgh>100 :
        mapLentgh=100
    myMap=mapCreator(mapLentgh*10+1)
    
    predatorBattleLog=battleLogGenerator(predator)
    preyBattleLog=battleLogGenerator(prey)
    preyBattleLog["xPosition"]=len(myMap)//2
    preyBattleLog["yPosition"]=len(myMap)//2
    
    sneakWalk(predator,prey,predatorBattleLog,preyBattleLog,myMap)
    
    
    

    
    
    i=0
    move=None
    #llamado a combatTurn
    while True:
        myMap=mapCreator(mapLentgh*10+1)
        if i%2==0:
            
            move= combatTurnPredator(predator,prey,predatorBattleLog,preyBattleLog,myMap,0,futureSigthPredator)
            predatorBattleLog["xPosition"]=move[1][0]
            predatorBattleLog["yPosition"]=move[1][1]
            if(move[1][2])=="normalHit":
                standarAttack(predator,prey,preyBattleLog,(2,1,1))
            elif (move[1][2])=="critHit":
                standarAttack(predator,prey,preyBattleLog,(1,2,1))
            elif (move[1][2])=="slowHit":
                standarAttack(predator,prey,preyBattleLog,(1,1,2))
        else :
            
            combatTurnPrey(predator,prey,predatorBattleLog,preyBattleLog,myMap,1,futureSigthPrey)
            preyBattleLog["xPosition"]=move[1][0]
            preyBattleLog["yPosition"]=move[1][1]
            if(move[1][2])=="normalHit":
                standarAttack(prey,predator,predatorBattleLog,(2,1,1))
            elif (move[1][2])=="critHit":
                standarAttack(prey,predator,predatorBattleLog,(1,2,1))
            elif (move[1][2])=="slowHit":
                standarAttack(prey,predator,predatorBattleLog,(1,1,2))
        if preyBattleLog["life"]<=0: return 0
        if predatorBattleLog["life"]<=0: return 1
        if checkBorderEscape((preyBattleLog["xPosition"],preyBattleLog["yPosition"]),myMap):
            return 2
        
        i+=1


def checkBorderEscape(pos,map):
    if (pos[0]==0 or pos[0]==len(map)-1) and (pos[1]==0 or pos[1]==len(map[0])-1):
        return True
    return False    

def euristicaHuir(firstIndividualBattlelog,secondIndividualBattlelog,mapa,peso=1):
    distXPredator=abs(firstIndividualBattlelog["xPosition"]-secondIndividualBattlelog["xPosition"])
    distYPredator=abs(firstIndividualBattlelog["yPosition"]-secondIndividualBattlelog["yPosition"])
    distXEdge= max(len(mapa)-firstIndividualBattlelog["xPosition"],firstIndividualBattlelog["xPosition"])//2
    distYEdge=max(len(mapa[0])-firstIndividualBattlelog["yPosition"],firstIndividualBattlelog["yPosition"])//2
    
    
    return (distXEdge+distYEdge+distXPredator+distYPredator+firstIndividualBattlelog["life"]-firstIndividualBattlelog["life"])*peso
    
def euristicaHunt(firstIndividualBattlelog,secondIndividualBattlelog,mapa,peso=1):
    distXPredator=len(mapa)-abs( firstIndividualBattlelog["xPosition"]-secondIndividualBattlelog["xPosition"])
    if distXPredator==len(mapa)-1:
        distXPredator+=1
    distYPredator=len(mapa)-abs(firstIndividualBattlelog["yPosition"]-secondIndividualBattlelog["yPosition"])
    if distYPredator==len(mapa)-1:
        distYPredator+=1
    distXEdge=min(len(mapa)-secondIndividualBattlelog["xPosition"],secondIndividualBattlelog["xPosition"])
    distYEdge=min(len(mapa[0])-secondIndividualBattlelog["xPosition"],secondIndividualBattlelog["yPosition"])   
    
    
    return (distXEdge+distYEdge+distXPredator+distYPredator+firstIndividualBattlelog["life"]-secondIndividualBattlelog["life"])*peso

#realiza un ataque recibe un peso para ver que tipo de ataque sera
#weithgs=(min%attack,max%attack,critIncrease,slowIncrease,)
def standarAttack(currentIndividual, secondIndividual,battleLogSecond,weithgs):
    attack=calculatePercent(currentIndividual.naturalDefenseInd["Vida"],random.randint(15,20))*weithgs[0]
    
    armorChance=random.randint(0,100)
    defense=0
    if armorChance>secondIndividual.naturalDefenseInd["Armadura"]:
        defense=calculatePercent(secondIndividual.naturalDefenseInd["Armadura"],random.randint(10,20))
    else:
        defense=calculatePercent(secondIndividual.naturalDefenseInd["Armadura"],random.randint(0,10))
    
    critChance=random.randint(0,100)*weithgs[1]
    if critChance>100-currentIndividual.naturalDefenseInd["Crit_chance_increase"]:
        attack*=3
        
    slowChance=random.randint(0,100)*weithgs[2]
    slowDone=0
    if slowChance>100-currentIndividual.naturalDefenseInd["Slow_chance"]:
        slowDone=calculatePercent(currentIndividual.naturalDefenseInd["Slow_done"],random.randint(25,40))
        battleLogSecond["debuffSlow"]=battleLogSecond["debuffSlow"]+slowDone
        
    bleedChance=random.randint(0,100)
    bleedDone=0
    if bleedChance>100-currentIndividual.naturalDefenseInd["Bleed_chance"]:
        bleedDone=calculatePercent(secondIndividual.naturalDefenseInd["Vida"],currentIndividual.naturalDefenseInd["Bleed_damage"])
        battleLogSecond["debuffBleed"]=battleLogSecond["debuffBleed"]+bleedDone
            
    result=0
    if defense<attack: 
        result=attack-defense
    
    battleLogSecond["life"]-=result

#el depredador se acerca sigilosamente
def sneakWalk(predator,prey,battleLogPredator,battleLogPrey,mapa):
    
    tempX,tempY=0,0
    if battleLogPredator["xPosition"]==battleLogPrey["xPosition"]:
        dirX=0
    else:
        dirX=battleLogPredator["xPosition"]-battleLogPrey["xPosition"]//abs(battleLogPredator["xPosition"]-battleLogPrey["xPosition"])*-1
    
    if battleLogPredator["yPosition"]==battleLogPrey["yPosition"]:
        dirY=0
    else:
        dirY=battleLogPredator["yPosition"]-battleLogPrey["yPosition"]//abs(battleLogPredator["yPosition"]-battleLogPrey["yPosition"])*-1
    
    while True:
        if indexChecker((dirX+battleLogPredator["xPosition"],dirY+battleLogPredator["yPosition"]),len(mapa)):
            if dirX+battleLogPredator["xPosition"]== battleLogPrey["xPosition"] and dirY+battleLogPredator["yPosition"]==battleLogPrey["yPosition"]:
                standarAttack(predator,prey,battleLogPrey,(2,2,2))
                return
            else:
                predatorChance=20*(int(predator.naturalDefenseInd["Sigilo"])-(int(prey.naturalDefenseInd["Inteligencia"])+(int(prey.naturalDefenseInd["Inteligencia"])))//2)
                sneakChance=random.randint(0,100)
                if predatorChance>sneakChance:
                    battleLogPredator["xPosition"]=dirX+battleLogPredator["xPosition"]
                    battleLogPredator["yPosition"]=dirY+battleLogPredator["yPosition"]
                else:
                    return    
    
    
def calculatePercent(number,percent):
    return number*percent//100 

def secondPercent(number1,number2):
    return number1*100/number2

def battleLogGenerator(individuo):
    battleLog={}
    battleLog["life"]=int(individuo.naturalDefenseInd["Vida"])
    battleLog["currentLife"] =int(individuo.naturalDefenseInd["Vida"])
    battleLog["movements"] =int(individuo.naturalDefenseInd["Velocidad_agua"])
    battleLog["xPosition"] =0
    battleLog["yPosition"] =0
    
    battleLog["action"] =None
    
    battleLog["turnsLeft"] =(int(individuo.naturalDefenseInd["Percepcion_de_mundo"])+int(individuo.naturalDefenseInd["Inteligencia"]))//2
    
    battleLog["debuffSlow"]=0
    battleLog["debuffBleed"]=0
    return battleLog

def resetBattleLog(individuo,battleLog):
    result=copyBattleLog(battleLog)
    
    result["currentMovements"]=int(individuo.naturalDefenseInd["Velocidad_agua"])
    result["action"] =None
    return result
    
def copyBattleLog(firstBattleLog):
    newBattleLog={}
    for key in firstBattleLog:
        newBattleLog[key]=firstBattleLog[key]
        
    return newBattleLog


def findPrey(Individuo ):
    individuoStats = Individuo.naturalDefenseInd["Vida"]+Individuo.naturalDefenseInd["Inteligencia"]+Individuo.naturalDefenseInd["Sigilo"]+Individuo.naturalDefenseInd["Percepcion_de_mundo"]
    + Individuo.naturalDefenseInd["Armadura"]+ Individuo.naturalDefenseInd["Armadura_debil"]+Individuo.naturalDefenseInd["Armadura_debil_porciento"]
    +Individuo.naturalDefenseInd["Crit_chance_increase"]+ Individuo.naturalDefenseInd["Bleed_chance"]+Individuo.naturalDefenseInd["Crit_chance_increase"]
    + Individuo.naturalDefenseInd["Bleed_damage"]+Individuo.naturalDefenseInd["Slow_chance"]+Individuo.naturalDefenseInd["Slow_done"]+Individuo.naturalDefenseInd["Velocidad_agua"]
    
    prey = None
    preyStats= -1
    actualTile = globals.worldMap.Tiles[Individuo.xMundo][Individuo.yMundo]
    
    for creature in actualTile.CreatureList:
        #modificar para canibalismo
        if (creature.especie == Individuo.especie and not creature.especie.basicInfo["Canibal"]) or creature==Individuo:
            pass
        
        else:
            
            if Individuo.naturalDefenseInd["Inteligencia"]>=5:
                creatureStats= creature.naturalDefenseInd["Vida"]+creature.naturalDefenseInd["Inteligencia"]+creature.naturalDefenseInd["Percepcion_de_mundo"]
                + creature.naturalDefenseInd["Armadura"]+ creature.naturalDefenseInd["Armadura_debil"]+creature.naturalDefenseInd["Armadura_debil_porciento"]
                +creature.naturalDefenseInd["Crit_chance_increase"]+ creature.naturalDefenseInd["Bleed_chance"]+creature.naturalDefenseInd["Crit_chance_increase"]
                + creature.naturalDefenseInd["Bleed_damage"]+creature.naturalDefenseInd["Slow_chance"]+creature.naturalDefenseInd["Slow_done"]+creature.naturalDefenseInd["Velocidad_agua"]


                hunger=int(Individuo.naturalDefenseInd["Cantidad_de_energia_almacenable"])-int(Individuo.saciedad)
                #modificar esto dependiendo del hambre
                careless=hunger/int(Individuo.naturalDefenseInd["Cantidad_de_energia_almacenable"])


                if prey == None and (individuoStats*careless+ individuoStats)/3 > creatureStats:
                    preyStats = creatureStats
                    prey = creature

                elif preyStats< creatureStats < (individuoStats*careless+ individuoStats)/3:
                    preyStats = creatureStats
                    prey = creature
            else:
                prey=creature
                break
    return prey


def reset():

    globals.WorldSize = 10
    globals.ZoneCount = 3

    #Todas las zonas con las que trabaja la simulación
    globals.ZoneList = ['Prairie', 'Mountain', 'Ocean']
    #La peligrosidad de cada zona
    globals.ZoneDanger = {'Prairie': 2, 'Mountain': 8, 'Ocean' : 5}

    globals.voidValue = 10000000

    #Un entero de 1 hasta 100 que representa el porcentaje de posibilidad
    #con la que puede ocurrir un fenómeno al inicio de la simulación
    #o luego de que haya acabado de ocurrir otro fenómeno
    globals.CatastrophyPosibility = 5

    #Aumento de probabilidad por turno con la que ocurrirá un fenómeno
    globals.TurnsToCatastrophy = 2

    #Máximo de fenómenos que pueden estar ocurriendo al mismo tiempo
    globals.MaxCatastrophy = 15

    #Categoría máxima que puede tener generalmente un fenómeno(cantidad máxima de peligro en zona)
    globals.MaxCategory = 5

    #Lista de fenómenos
    globals.CatastrophyList = []

    #Frecuencia con la que una especie evoluciona (mientras más grande, menos común son las evluciones)
    globals.EvolutionFrequency =1

    #valor para aumentar el chance de muerte cuando se pasa por una zona al caminar
    globals.killerModifier=2
    #maximo peligro posible de una zona
    globals.MaxDangerinTile = 9*globals.MaxCategory*5


    #Todos los elementos con los que trabaja la simulación
    globals.WorldComponents = { 'Solar Light','Water', 'Organic Matter', 'Phosil' ,'Iron' , 'Aluminum' , 'Oxygen' , 'Carbon Dioxide' , 'Helium' , 'Nitrogen' }

    globals.InfiniteRange = (10000, 100000)
    globals.LargeRandomRange = (3000, 5000)
    globals.MediumRandomRange = (1000, 3000)
    globals.LowRandomRange = (200, 1000)
    globals.NoneRandomRange = (0, 200)



    globals.PrairieGenerationList = {'Solar Light' : globals.InfiniteRange ,
                            'Water' : globals.LowRandomRange,
                            'Organic Matter' : globals.MediumRandomRange,
                            'Phosil' : globals.NoneRandomRange ,
                            'Iron': globals.LowRandomRange ,
                            'Aluminum' : globals.NoneRandomRange ,
                            'Oxygen' : globals.LargeRandomRange,
                            'Carbon Dioxide': globals.LargeRandomRange ,
                            'Helium': globals.NoneRandomRange,
                            'Nitrogen' :globals.NoneRandomRange}


    MountainGenerationList = {'Solar Light' : globals.InfiniteRange ,
                            'Water' : globals.NoneRandomRange,
                            'Organic Matter' : globals.NoneRandomRange,
                            'Phosil' : globals.LargeRandomRange ,
                            'Iron': globals.MediumRandomRange ,
                            'Aluminum' : globals.MediumRandomRange ,
                            'Oxygen' : globals.MediumRandomRange,
                            'Carbon Dioxide': globals.LargeRandomRange ,
                            'Helium': globals.LowRandomRange,
                            'Nitrogen' :globals.LowRandomRange}



    OceanGenerationList = {'Solar Light' : globals.InfiniteRange ,
                            'Water' : globals.InfiniteRange,
                            'Organic Matter' : globals.MediumRandomRange,
                            'Phosil' : globals.NoneRandomRange ,
                            'Iron': globals.LowRandomRange ,
                            'Aluminum' : globals.NoneRandomRange ,
                            'Oxygen' : globals.MediumRandomRange,
                            'Carbon Dioxide': globals.LowRandomRange ,
                            'Helium': globals.LowRandomRange,
                            'Nitrogen' :globals.LowRandomRange}


    #numero de predicciones en el combate 9 por defecto
    globals.tempPredictions=9


    #diccionario de especies
    globals.allSpecies ={}
    globals.lastNameSpecie=0
    #mapa
    globals.worldMap=""
    #lista de todos individuos
    globals.worldIndividuals={}

    #cola de fenomenos
    globals.worldFenomenos=queue.PriorityQueue()

    #lista de individuos muertos para eliminar al final del siglo
    globals.deadIndividuals=[]

    #lista de individuos nacidos para agregar al final del siglo
    globals.bornIndividuals=[]


    #-------------------------------------------------NEW STUFF--------------------------------------------------------------------

    #Variable de caza, mientra más grande más probable que el individuo decida cazar (0--->infinito)
        # 0: nunca cazará, 
        # 1: podrá cazar aprox un 1/10 porciento de veces que evolucione , 
        # 1000000: siempre cazará(probablemente))
    globals.Hunting = 1

    #Que tan débil debe ser la craitura que se va a cazar, (1---->10)
        # 10: más debil que yo, pero no me importa cuan débil
        # 5: siempre será el doble de débil o más que yo
        # 1: siempre será 10 veces más debil que yo
    globals.Weakness = 10

    #-------------------------------------------------NEW STUFF--------------------------------------------------------------------

    #el arbol que muestra la evolucion de las especies
    globals.arb_evo = Arbol_Evo()

    #tamaño minimo de individuos de una nueva especie
    globals.minSizeOfNewEspecies=20

    #lista para agregar nuevas especies
    globals.waitSpeciesList=[]

    #tipos de muertes posibles
    globals.deadTypesList=["Natural","Hunted","Hunting","Ciclon","Landslide","Volcan","Tsunami","Moving","Evolving"]

    #cantidad de ciclos que se van a realizar
    globals.iterationCicles=500

    #iteracion actual del ciclo o dia del ciclo
    globals.globalTime=1

    #cada cuanto tiempo se revisan las evoluciones
    globals.evolutionTimeCheck=10