import zones
import misc
import random
import tiles


class Map:
    def __init__(self,sizeX,sizeY,amount_of_zones):
        self.TilesCount = sizeX* sizeY
        self.SizeX = sizeX
        self.SizeY = sizeY
        self.ZoneCount = amount_of_zones
        self.Tiles = []
        self.Zones = {}
        self.CreateNotSoRandmo()


    def CreateNotSoRandmo(self):

        self.CreateZonesNotSoRandom()
        self.PopulateNotSoRandom()


    def CreateZonesNotSoRandom(self):
        zoneCount= self.ZoneCount
        extraTiles = 0
        while zoneCount > 0:
            zoneIndex = random.randint(0, len(misc.ZoneList)-1)
            if zoneCount == 1:
                extraTiles = self.TilesCount % self.ZoneCount
            tiles_per_zone = self.TilesCount/ self.ZoneCount + extraTiles
            tempZone = zones.Zone(tiles_per_zone, misc.ZoneList[zoneIndex])
            self.Zones.append(tempZone)
            zoneCount = zoneCount - 1

    def PopulateNotSoRandom(self):
        tileCount = 0
        zoneCount = 0
        for row in range (self.SizeX):
            for col in range (self.SizeY):
                tileCount += 1
                tempTile = tiles.Tile(row , col, self.Zones[zoneCount])
                self.Tiles[row][col] = tempTile
                if tileCount == self.Zones[zoneCount].TileCount:
                    zoneCount +=1
        