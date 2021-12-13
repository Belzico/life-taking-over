
import zones
import misc
import random





class Tile:



    def __init__(self,x,y,zone):
        self.Coordinates =  (x,y)
        self.Zone = zone
        #self.EnergyValue = -1
        if zone.ZoneType is 'Forest'  :
            self.createForestTile()
        if zone is 'Mountain' :
            self.createMountainTile()
        if zone is 'Ocean'  :
             self.createOceanTile()
        zone.TileList.append(self)



    def createForestTile(self):
        pass

    def createMountainTile(self):
        pass
    
    def createOceanTile(self):
        pass