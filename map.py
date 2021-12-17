import zones
import misc
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
        destinyTile = self.Tiles[Coordinates[0]][Coordinates[1]]
        actualTile = self.Tiles[Individuo.Coordinates[0]][Individuo.Coordinates[1]]
        actualTile.CreatureList.remove(Individuo)
        Individuo.Coordinates = Coordinates
        destinyTile.CreatureList.append(Individuo)
        
    def movementWithBoundries (self,Individuo, valor_de_percepcion):
        perceptionValue = int(valor_de_percepcion)
     
        #ESSTO HAY QUE CAMBIARLOOOOO CUANDO SE CAMBIE EL TIPO DE COORDENADAS DE LA ESPECIE
        actRow = Individuo.xMundo  - perceptionValue
        actCol = Individuo.yMundo - perceptionValue
        perceptionList = []
        ##LLenando perceptionlist
        for i in range(0, Individuo.xMundo  + 1 + perceptionValue):
            newList = []
            for j in range(0, Individuo.yMundo  + 1 + perceptionValue):
                newList.append("")
            perceptionList.append(newList)
        
     
        countX=0
        countY=0
     
        for actRow in range(0, Individuo.xMundo  + 1 + perceptionValue):
            for actCol in range(0, Individuo.yMundo  + 1 + perceptionValue):
                if not(0<=actRow<= self.SizeX) and not(0<=actCol<=self.SizeY):
                    perceptionList[countX][countY]= ""
                else:
                    perceptionList[countX][countY]= self.Tiles[actRow][actCol]
            
                countY+=1
        
        
            countX+=1
     
            return perceptionList
     
