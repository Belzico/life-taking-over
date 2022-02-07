import random
import numpy
import globals
import misc
import tiles

class Fenomeno():
    def __init__(self, Magnitude, position):
        
        self.Magnitude = Magnitude 
        self.ExecutingTimes = 0
        self.Range = 2
        self.Position = position
        self.xMundo = position.Coordinates[0]
        self.yMundo = position.Coordinates[1]
        self.DangerSumMatrix = []
        self.MapMatrix =  []
        self.amount_of_turns = 0
        
    def Finalize(self):
        raise ValueError('Method not implemented.')
        
    
    def Executing(self):
        
        if self.amount_of_turns <= 0:
            self.Finalize()
            return

        for i in range(len(self.MapMatrix)):
            for j in range(len(self.MapMatrix[i])):
                if self.MapMatrix[i][j] == globals.voidValue: continue
                self.DangerSumMatrix[i][j] += max( min(self.Magnitude - (self.Range -i),self.Magnitude - (self.Range -j)), 0)
                self.MapMatrix[i][j].Danger += max( min(self.Magnitude - (self.Range -i),self.Magnitude - (self.Range -j)), 0)
                
        self.amount_of_turns -=1
    
    def Prepare(self, map):
        self.MapMatrix = RangeMatrix(self,self.Range,globals.worldMap)
        
        self.DangerSumMatrix = []
        
        for i in range(len(self.MapMatrix)):
            self.DangerSumMatrix.append([])
            for j in range(len(self.MapMatrix[i])):
                self.DangerSumMatrix[i].append(0)
        
        self.amount_of_turns = misc.round_half_up(numpy.random.normal(5,1,1)[0])
        
class Ciclon(Fenomeno):
    def __init__(self, Magnitude, position):
        super().__init__( Magnitude, position)
        
        
    def Finalize(self):
        globals.CatastrophyList.remove(self)
        
        for individuo in self.Position.CreatureList:
            rand = random.randint(0, globals.MaxCategory)
            if rand > self.Magnitude:
                individuo.die("Ciclon")
        
        for i in range(len(self.MapMatrix)):
            for j in range(len(self.MapMatrix[i])):
                if self.MapMatrix[i][j] == globals.voidValue: continue
                self.MapMatrix[i][j].Danger -= self.DangerSumMatrix[i][j]

    

class Landslide(Fenomeno):
    def __init__(self, Magnitude, position):
        super().__init__(Magnitude, position)
        
    def EfectuarFenomeno(self,mapa,cor):
        if cor[1] == None:
            return
        
    def Finalize(self):
        globals.CatastrophyList.remove(self)
        
        for individuo in self.Position.CreatureList:
            rand = random.randint(0, globals.MaxCategory)
            if rand > self.Magnitude:
                individuo.die("Landslide")
        
        for i in range(len(self.MapMatrix)):
            for j in range(len(self.MapMatrix[i])):
                if self.MapMatrix[i][j] == globals.voidValue: continue
                self.MapMatrix[i][j].Danger -= self.DangerSumMatrix[i][j]
                self.MapMatrix[i][j].createPrairieTile()
                
                
                
            
class Volcan(Fenomeno):
    def __init__(self, Magnitude, position):
        super().__init__(Magnitude, position)
            
        
        
    def Finalize(self):
        globals.CatastrophyList.remove(self)
        
        for individuo in self.Position.CreatureList:
            rand = random.randint(0, globals.MaxCategory)
            if rand > self.Magnitude:
                individuo.die("Volcan")
        
        for i in range(len(self.MapMatrix)):
            for j in range(len(self.MapMatrix[i])):
                if self.MapMatrix[i][j] == globals.voidValue: continue
                self.MapMatrix[i][j].Danger -= self.DangerSumMatrix[i][j]
                self.MapMatrix[i][j].createMountainTile()
                
                
    


class Tsunami(Fenomeno):
    def __init__(self, Magnitude, position):
        super().__init__(Magnitude, position)
        
        
        
    def Finalize(self):
        globals.CatastrophyList.remove(self)
        
        for individuo in self.Position.CreatureList:
            rand = random.randint(0, globals.MaxCategory)
            if rand > self.Magnitude:
                individuo.die("Tsunami")
        
        for i in range(len(self.MapMatrix)):
            for j in range(len(self.MapMatrix[i])):
                if self.MapMatrix[i][j] == globals.voidValue: continue
                self.MapMatrix[i][j].Danger -= self.DangerSumMatrix[i][j]
                self.MapMatrix[i][j].createOceanTile()
                
                


def Euristics(mapa):
    
    globals.CatastrophyPosibility += globals.TurnsToCatastrophy
    if random.randint(0,100) > globals.CatastrophyPosibility:
        return

    if len(globals.CatastrophyList) >= globals.MaxCatastrophy:
        globals.CatastrophyPosibility = 5
        return
    

    
    #Seleccionando la posición
    positionX = random.choice(mapa.Tiles)
    position = random.choice(positionX)
    
    #Seleccionando la zona
    zoneToCreate = position.Zone
    
    #Seleccionando la probabilidad del tipo de fenómeno(normal)
    normalDistrib = numpy.random.normal(5,1,1)
    
    #Seleccionando la catgoría del fenómeno
    catgoryNormalDistrib = misc.round_half_up(numpy.random.normal(globals.MaxCategory/2,1))
    
    phenomena = -1
    if zoneToCreate.ZoneType == 'Prairie':
        if 4<=normalDistrib<=6:
            phenomena = Landslide(catgoryNormalDistrib,position)
            phenomena.Prepare(mapa)
            globals.CatastrophyList.append(phenomena)
            
        elif 3<=normalDistrib<4 or 6<normalDistrib<=7:
            phenomena = Ciclon(catgoryNormalDistrib,position)
            phenomena.Prepare(mapa)
            globals.CatastrophyList.append(phenomena)
            
        elif 2<=normalDistrib<3 or 7<normalDistrib<=8:
            phenomena = Volcan(catgoryNormalDistrib,position)
            phenomena.Prepare(mapa)
            globals.CatastrophyList.append(phenomena)
            
        elif normalDistrib<2 or normalDistrib> 8:
            phenomena = Tsunami(catgoryNormalDistrib,position)
            phenomena.Prepare(mapa)
            globals.CatastrophyList.append(phenomena)
    
    elif zoneToCreate.ZoneType == 'Mountain':
        if 4<=normalDistrib<=6:
            phenomena = Volcan(catgoryNormalDistrib,position)
            phenomena.Prepare(mapa)
            globals.CatastrophyList.append(phenomena)
            
        elif 3<=normalDistrib<4 or 6<normalDistrib<=7:
            phenomena = Ciclon(catgoryNormalDistrib,position)
            phenomena.Prepare(mapa)
            globals.CatastrophyList.append(phenomena)
            
        elif 2<=normalDistrib<3 or 7<normalDistrib<=8:
            phenomena = Landslide(catgoryNormalDistrib,position)
            phenomena.Prepare(mapa)
            globals.CatastrophyList.append(phenomena)
            
        elif normalDistrib<2 or normalDistrib> 8:
            phenomena = Tsunami(catgoryNormalDistrib,position)
            phenomena.Prepare(mapa)
            globals.CatastrophyList.append(phenomena)
            

    elif zoneToCreate.ZoneType == 'Ocean':
        if 4<=normalDistrib<=6:
            phenomena = Tsunami(catgoryNormalDistrib,position)
            phenomena.Prepare(mapa)
            globals.CatastrophyList.append(phenomena)
            
        elif 3<=normalDistrib<4 or 6<normalDistrib<=7:
            phenomena = Ciclon(catgoryNormalDistrib,position)
            phenomena.Prepare(mapa)
            globals.CatastrophyList.append(phenomena)
            
        elif 2<=normalDistrib<3 or 7<normalDistrib<=8:
            phenomena = Volcan(catgoryNormalDistrib,position)
            phenomena.Prepare(mapa)
            globals.CatastrophyList.append(phenomena)
            
        elif normalDistrib<2 or normalDistrib> 8:
            phenomena = Landslide(catgoryNormalDistrib,position)
            phenomena.Prepare(mapa)
            globals.CatastrophyList.append(phenomena)
            
        
    
        pass
    
        

def RangeMatrix (Individuo, valor_de_percepcion,mapa):
    perceptionValue = int(valor_de_percepcion)

    
    actRow = Individuo.xMundo  - perceptionValue
    actCol = Individuo.yMundo - perceptionValue
    perceptionList = []
    tileCount = 0
    ##LLenando perceptionlist
    for i in range(0, 1  + 2 * int(perceptionValue)):
        newList = []
        for j in range(0,  1  + 2 * int(perceptionValue)):
            newList.append(globals.voidValue)
            tileCount +=1
        perceptionList.append(newList)
    
    
    
    countX=0
    countY=0
    
    #Movimiento con límites del mapa
    while actRow <= Individuo.xMundo  + perceptionValue:
        actCol = Individuo.yMundo - perceptionValue
        countY=0
        while actCol <= Individuo.yMundo + perceptionValue:
            if not(0<=actRow< mapa.SizeX) or not(0<=actCol< mapa.SizeY):
                perceptionList[countX][countY]= globals.voidValue
            else:
                perceptionList[countX][countY]= mapa.Tiles[actRow][actCol]
        
            countY+=1
            actCol +=1
        actRow+=1
        countX+=1

    return perceptionList

