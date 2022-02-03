
import zones
import misc
import random
import globals
import especies




class Tile:

    

    def __init__(self,x,y,zone):
        self.Coordinates =  (x,y)
        self.Zone = zone
        self.CreatureList = []
        self.ComponentsDict = {}
        self.Danger = zone.Danger
        #self.EnergyValue = -1
        if zone.ZoneType == 'Prairie'  :
            self.createPrairieTile()
        if zone.ZoneType == 'Mountain' :
            self.createMountainTile()
        if zone.ZoneType == 'Ocean'  :
            self.createOceanTile()
        zone.TileList.append(self)

    def deleteCreaturesEspecies(self, Creatures , Especie):
        tempCount = Creatures
        for j in self.CreatureList:
            if tempCount <= 0:
                pass
            else:
                if j.especie == Especie:
                    j.die()
                   # self.CreatureList.delete(j)
                   # j.especie.individuos.delete(j)
                    tempCount = tempCount -1
                    
    
    def eliminate(self,elementTuple):
        if elementTuple[0] == 'Solar Light' or elementTuple[0] == 'Water':
            return
        
        else:
            self.ComponentsDict[elementTuple[0]] = self.ComponentsDict[elementTuple[0]] - elementTuple[1]
        if self.ComponentsDict[elementTuple[0]] < 0:
            self.ComponentsDict[elementTuple[0]] = 0

    def createPrairieTile(self):
        for component in globals.PrairieGenerationList.items():
            self.ComponentsDict[component[0]]  =  random.randint(component[1][0], component[1][1])
       

    def createMountainTile(self):
        for component in globals.MountainGenerationList.items():
            self.ComponentsDict[component[0]]  =  random.randint(component[1][0], component[1][1])
        
    
    def createOceanTile(self):
        for component in globals.OceanGenerationList.items():
            self.ComponentsDict[component[0]]  =  random.randint(component[1][0], component[1][1])
        
     