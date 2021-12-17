
import zones
import misc
import random
import globals





class Tile:



    def __init__(self,x,y,zone):
        self.Coordinates =  (x,y)
        self.Zone = zone
        self.CreatureList = {}
        self.ComponentsDict = {}
        #self.EnergyValue = -1
        if zone.ZoneType == 'Prairie'  :
            self.createPrairieTile()
        if zone.ZoneType == 'Mountain' :
            self.createMountainTile()
        if zone.ZoneType == 'Ocean'  :
             self.createOceanTile()
        zone.TileList.append(self)



    def createPrairieTile(self):
        for component in globals.PrairieGenerationList.items():
            self.ComponentsDict[component[0]]  =  random.randint(component[1][0], component[1][1])
       

    def createMountainTile(self):
        for component in globals.MountainGenerationList.items():
            self.ComponentsDict[component[0]]  =  random.randint(component[1][0], component[1][1])
        
    
    def createOceanTile(self):
        for component in globals.OceanGenerationList.items():
            self.ComponentsDict[component[0]]  =  random.randint(component[1][0], component[1][1])
        
     