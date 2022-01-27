import zones
import misc
import graphics
import globals
import random
import tiles
import json
import especies



class Map:
    def __init__(self,sizeX,sizeY,amount_of_zones):
        self.TilesCount = sizeX* sizeY
        self.SizeX = sizeX
        self.SizeY = sizeY
        self.ZoneCount = amount_of_zones
        self.Tiles = []
        self.Zones = []
        self.CreateNotSoRandmo()
        self.SaveInJson()

    
    def SaveInJson(self):
     #   globals.jasonstr = json.dumps(self.__dict__,'map.json')
        pass
        
   
    
    #actualiza en el mundo
    def udpdateIndividual(self,tempInd,x,y):
        self.MoveCreature(tempInd,(x,y))    



    def CreateNotSoRandmo(self):

        self.CreateZonesNotSoRandom()
        self.PopulateNotSoRandom()
        self.Graphics = graphics.MapGraphics(self)

    
    def IsBorn(self, individuo):
        self.Tiles[int(individuo.xMundo)][int(individuo.yMundo)].CreatureList.append(individuo)
        
    
    def CreateZonesNotSoRandom(self):
        zoneCount= self.ZoneCount
        extraTiles = 0
        while zoneCount > 0:
            zoneIndex = random.randint(0, len(globals.ZoneList)-1)
            if zoneCount == 1:
                extraTiles = self.TilesCount % self.ZoneCount
            tiles_per_zone = self.TilesCount/ self.ZoneCount + extraTiles
            tempZone = zones.Zone(tiles_per_zone, globals.ZoneList[zoneIndex])
            self.Zones.append(tempZone)
            zoneCount = zoneCount - 1

    def PopulateNotSoRandom(self):
        tileCount = 0
        zoneCount = 0
        
        for i in range(self.SizeX):
            new = []
            for j in range(self.SizeY):
                new.append('foo')
            self.Tiles.append(new)
        
        
        for row in range (self.SizeX):
            for col in range (self.SizeY):
                tileCount += 1
                tempTile = tiles.Tile(row , col, self.Zones[zoneCount])
                self.Tiles[row][col] = tempTile
                if tileCount == self.Zones[zoneCount].TileCount:
                    zoneCount +=1
                    
    def MoveCreature (self, Individuo , Coordinates):
        oldTile = self.Tiles[Coordinates[0]][Coordinates[1]]
        actualTile = self.Tiles[Individuo.xMundo][Individuo.yMundo]
        
        #########CHECKEAR EL PORQUE EL INDIVIDUO SE MOVIÓ SIN PERMISO
        if Individuo in oldTile.CreatureList:
            oldTile.CreatureList.remove(Individuo)
        if Individuo not in actualTile.CreatureList:
            actualTile.CreatureList.append(Individuo)
        
        
    def PrintMap (self):
        for i in range(self.SizeX):
            for j in range(self.SizeY):
                print ('-----------------------------------------------------------------------')
                print(self.Tiles[i][j].Coordinates)
                print(self.Tiles[i][j].Zone.ZoneType)
                print(self.Tiles[i][j].ComponentsDict)
                print(self.Tiles[i][j].CreatureList)
                print ('-----------------------------------------------------------------------')
                    
        
         
    
    def movementWithBoundries (self,Individuo, valor_de_percepcion):
        perceptionValue = int(valor_de_percepcion)
     
        #ESSTO HAY QUE CAMBIARLOOOOO CUANDO SE CAMBIE EL TIPO DE COORDENADAS DE LA ESPECIE
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
                if not(0<=actRow< self.SizeX) or not(0<=actCol< self.SizeY):
                    perceptionList[countX][countY]= globals.voidValue
                else:
                    perceptionList[countX][countY]= self.Tiles[actRow][actCol]
            
                countY+=1
                actCol +=1
            actRow+=1
            countX+=1
     
        return perceptionList
     

    
    def movementMatrix(self,Individuo) -> dict:
        matrixDict = {}
        #perceptionList = self.movementWithBoundries(Individuo, Individuo.naturalDefenseInd["Percepcion_de_mundo"])
        #Parche de casillas vacías
        perceptionList = self.movementWithoutBoundries(Individuo, Individuo.naturalDefenseInd["Percepcion_de_mundo"])

        
        matrixDict["Tile"] = perceptionList
        
        matrixDict["Especie"]= self.speciesMatrix(Individuo, perceptionList)
        
        matrixDict["Pareja"] = self.PeerMatrix(Individuo,perceptionList)
        
        matrixDict["Comida"] = self.FoodMatrix(Individuo,perceptionList)
       
        matrixDict["Peligro"] = self.dangerMatrix(Individuo,perceptionList)
        
        return matrixDict
        
        
    def PeerMatrix(self,Individuo,TilePerceptionMatrix):
        valuesList = []
        for i in range(len(TilePerceptionMatrix)):
            valuesList.append([])
            for j in range(len(TilePerceptionMatrix[i])):
                valuesList[i].append(globals.voidValue)
                
        #Buscando la casilla con la mayor cantidad de individuos fértiles de la especie
       
        savedValue = -1
        tempvalue= 0
        for i in range(len(TilePerceptionMatrix)):
            for j in range(len(TilePerceptionMatrix[i])):
                tempvalue=0
                #Parche de casillas vacías
                if TilePerceptionMatrix[i][j] == globals.voidValue: continue
                for h in TilePerceptionMatrix[i][j].CreatureList:
                    if h.especie == Individuo.especie:
                        if h.giveMeRealAge()-int(h.naturalDefenseInd["Edad_de_madurez_sexual_en_dias"])>=0 and h.giveMeRealAge()- int(h.lastReproduction)>int(h.naturalDefenseInd["Tiempo_entre_reproducccion"]):
                            tempvalue +=1
                if savedValue< tempvalue:
                    savedValue = tempvalue
    
        for i in range(len(TilePerceptionMatrix)):
            for j in range(len(TilePerceptionMatrix[i])):
                tempvalue= 0
                #Parche de casillas vacías
                if TilePerceptionMatrix[i][j] == globals.voidValue: continue
                for h in TilePerceptionMatrix[i][j].CreatureList:
                    if h.especie == Individuo.especie:
                        if h.giveMeRealAge()-int(h.naturalDefenseInd["Edad_de_madurez_sexual_en_dias"])>=0 and h.giveMeRealAge()- int(h.lastReproduction)>int(h.naturalDefenseInd["Tiempo_entre_reproducccion"]):
                            tempvalue +=1
                if savedValue ==  tempvalue:
                    valuesList[i][j] = 5
                if savedValue>tempvalue>=savedValue*0.7:
                    valuesList[i][j] = 4
                if savedValue*0.7>tempvalue>=savedValue*0.5:
                    valuesList[i][j] = 3
                if savedValue*0.5> tempvalue>=savedValue*0.3:
                    valuesList[i][j] = 2
                if savedValue*0.3> tempvalue:
                    valuesList[i][j] = 1
                
        return valuesList
    
    
    def dangerMatrix(self,Individuo, TilePerceptionMatrix):
        valuesList = []
        for i in range(len(TilePerceptionMatrix)):
            valuesList.append([])
            for j in range(len(TilePerceptionMatrix[i])):
                valuesList[i].append(globals.voidValue)
    
        #Buscando la casilla de menor peligrosidad
        savedValue = -1
        for i in range(len(TilePerceptionMatrix)):
            for j in range(len(TilePerceptionMatrix[i])):
                #Parche de casillas vacías
                if TilePerceptionMatrix[i][j] == globals.voidValue: continue
                if savedValue > TilePerceptionMatrix[i][j].Zone.Danger:
                    savedValue = TilePerceptionMatrix[i][j].Zone.Danger
                    
        for i in range(len(TilePerceptionMatrix)):
            for j in range(len(TilePerceptionMatrix[i])):
                #Parche de casillas vacías
                if TilePerceptionMatrix[i][j] == globals.voidValue: continue
                if savedValue == TilePerceptionMatrix[i][j].Zone.Danger:
                    valuesList[i][j] = 5
                if savedValue<TilePerceptionMatrix[i][j].Zone.Danger< savedValue*1.5:
                    valuesList[i][j] = 4
                if savedValue*1.5<=TilePerceptionMatrix[i][j].Zone.Danger< savedValue*2:
                    valuesList[i][j] = 3
                if savedValue*2 == TilePerceptionMatrix[i][j].Zone.Danger:
                    valuesList[i][j] = 2
                if savedValue*2 < TilePerceptionMatrix[i][j].Zone.Danger:
                    valuesList[i][j] = 1
         
        return valuesList   
    
    def FoodMatrix(self,Individuo, TilePerceptionMatrix):
        valuesList = []
        for i in range(len(TilePerceptionMatrix)):
            valuesList.append([])
            for j in range(len(TilePerceptionMatrix[i])):
                valuesList[i].append(globals.voidValue)
    
        #Buscando la casilla con mayor cantidad de comida
        savedValue = -1
        tempvalue= 0
        for i in range(len(TilePerceptionMatrix)):
            for j in range(len(TilePerceptionMatrix[i])):
                tempvalue= 0
                #Parche de casillas vacías
                if TilePerceptionMatrix[i][j] == globals.voidValue: continue
                for h in Individuo.especie.alimentos.keys():
                    tempvalue += TilePerceptionMatrix[i][j].ComponentsDict[h]
                if tempvalue>savedValue:
                    savedValue = tempvalue

                    
        for i in range(len(TilePerceptionMatrix)):
            for j in range(len(TilePerceptionMatrix[i])):
                tempvalue= 0
                #Parche de casillas vacías
                if TilePerceptionMatrix[i][j] == globals.voidValue: continue
                for h in Individuo.especie.alimentos.keys():
                    tempvalue += TilePerceptionMatrix[i][j].ComponentsDict[h]
                if savedValue == tempvalue:
                    valuesList[i][j] = 5
                if savedValue>tempvalue>=savedValue*0.7:
                    valuesList[i][j] = 4
                if savedValue*0.7>tempvalue>=savedValue*0.5:
                    valuesList[i][j] = 3
                if savedValue*0.5> tempvalue>=savedValue*0.3:
                    valuesList[i][j] = 2
                if savedValue*0.3> tempvalue:
                    valuesList[i][j] = 1
         
        return valuesList   

    def speciesMatrix(self,Individuo, TilePerceptionMatrix):
        valuesList = []
        for i in range(len(TilePerceptionMatrix)):
            valuesList.append([])
            for j in range(len(TilePerceptionMatrix[i])):
                valuesList[i].append(globals.voidValue)
    
        #Buscando la casilla con la mayor cantidad de individuos de la especie
        savedValue = -1
        tempvalue= 0
        for i in range(len(TilePerceptionMatrix)):
            for j in range(len(TilePerceptionMatrix[i])):
                tempvalue=0
                #Parche de casillas vacías
                if TilePerceptionMatrix[i][j] == globals.voidValue: continue
                for h in TilePerceptionMatrix[i][j].CreatureList:
                    if h.especie == Individuo.especie:
                        tempvalue +=1
                if savedValue< tempvalue:
                    savedValue = tempvalue
                    
        for i in range(len(TilePerceptionMatrix)):
            for j in range(len(TilePerceptionMatrix[i])):
                tempvalue= 0
                #Parche de casillas vacías
                if TilePerceptionMatrix[i][j] == globals.voidValue: continue
                for h in TilePerceptionMatrix[i][j].CreatureList:
                    if h.especie == Individuo.especie:
                        tempvalue += 1
                if savedValue ==  tempvalue:
                    valuesList[i][j] = 5
                if savedValue>tempvalue>=savedValue*0.7:
                    valuesList[i][j] = 4
                if savedValue*0.7>tempvalue>=savedValue*0.5:
                    valuesList[i][j] = 3
                if savedValue*0.5> tempvalue>=savedValue*0.3:
                    valuesList[i][j] = 2
                if savedValue*0.3> tempvalue:
                    valuesList[i][j] = 1
        
        return valuesList   
        
    
    
    
    def movementWithoutBoundries (self,Individuo, valor_de_percepcion):
        perceptionValue = int(valor_de_percepcion)
     
        #ESSTO HAY QUE CAMBIARLOOOOO CUANDO SE CAMBIE EL TIPO DE COORDENADAS DE LA ESPECIE
        actRow = Individuo.xMundo  - perceptionValue
        actCol = Individuo.yMundo - perceptionValue
        perceptionList = []
        ##LLenando perceptionlist
        for i in range(0, 1  + 2 * int(perceptionValue)):
            newList = []
            for j in range(0,  1  + 2 * int(perceptionValue)):
                newList.append(globals.voidValue)
            perceptionList.append(newList)
        
     
        countX=0
        countY=0
        
                #Colocando las Tiles en Perception List
        for i in range(len(perceptionList)):
            for j in range(len(perceptionList)):
                perceptionList[i][j] = self.Tiles[Individuo.xMundo  - perceptionValue + i][Individuo.yMundo - perceptionValue + j]
                
     
        return perceptionList
     
