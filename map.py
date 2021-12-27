import zones
import misc
import graphics
import globals
import random
import tiles
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
        ##LLenando perceptionlist
        for i in range(0, 1  + 2 * int(perceptionValue)):
            newList = []
            for j in range(0,  1  + 2 * int(perceptionValue)):
                newList.append("")
            perceptionList.append(newList)
        
     
        countX=0
        countY=0
     
        while actRow <= Individuo.xMundo  + perceptionValue:
            actCol = Individuo.yMundo - perceptionValue
            countY=0
            while actCol <= Individuo.yMundo + perceptionValue:
                if not(0<=actRow< self.SizeX) or not(0<=actCol< self.SizeY):
                    perceptionList[countX][countY]= ""
                else:
                    perceptionList[countX][countY]= self.Tiles[actRow][actCol]
            
                countY+=1
                actCol +=1
            actRow+=1
            countX+=1
     
        return perceptionList
     
