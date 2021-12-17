import especies
import globals
import map


def worldController():
    while (True):
        
        value=''
        for val in globals.worldIndividuals:
            value=globals.worldIndividuals[val]
            tempMap=globals.worldMap.movementWithBoundries(value,1) 
            value.resolveIteration(tempMap)
        
        #####################################    
        #aca meter el codigo de ejecucion de la cola de fenomenos.
        #####################################
            



    
def main():
    globals.worldMap=map.Map(5,5,4)
    globals.allSpecies["Alfie"]=especies.Alfie()
    current=globals.allSpecies["Alfie"]
    #current.individuos["Alfie1"].breed()
    #print(len(current.individuos))
    
    worldController()
    
    
    
main()
    
KK = map.Map(6,6,2)

for i in range(KK.SizeX):
    for j in range(KK.SizeY):
        print(KK.Tiles[i][j].Zone.ZoneType)
        print(KK.Tiles[i][j].Coordinates)
        print(KK.Tiles[i][j].ComponentsDict)
        