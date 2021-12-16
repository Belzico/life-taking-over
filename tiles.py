
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
        if zone.ZoneType is 'Prairie'  :
            self.createForestTile()
        if zone is 'Mountain' :
            self.createMountainTile()
        if zone is 'Ocean'  :
             self.createOceanTile()
        zone.TileList.append(self)



    def createPrairieTile(self):
        for component in globals.PrairieGenerationList:
            self.ComponentsDict.append({component.iteritems[0] : random.randint(component.get(component.iteritems[0])[0],component.get(component.iteritems[0])[1])})
       

    def createMountainTile(self):
        for component in globals.MountainGenerationList:
            self.ComponentsDict.append({component.iteritems[0] : random.randint(component.get(component.iteritems[0])[0],component.get(component.iteritems[0])[1])})
        
    
    def createOceanTile(self):
        for component in globals.OceanGenerationList:
            self.ComponentsDict.append({component.iteritems[0] : random.randint(component.get(component.iteritems[0])[0],component.get(component.iteritems[0])[1])})
        
     