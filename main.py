import especies
import globals
import map


def worldController():
    i=10
    while (i>0):
        
        value=''
        for val in globals.worldIndividuals:
            value=globals.worldIndividuals[val]
            tempMap=globals.worldMap.movementWithBoundries(value,1) 
            value.resolveIteration(tempMap)
        i-=1
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

for i in range(globals.worldMap.SizeX):
    for j in range(globals.worldMap.SizeY):
        print(KK.Tiles[i][j].Zone.ZoneType)
        print(KK.Tiles[i][j].Coordinates)
        print(KK.Tiles[i][j].ComponentsDict)
        