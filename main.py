import especies
import globals
import map


def worldController():
    while (True):
        
        
        for val in globals.individuos.values:
            tempMap=map.Map.movementWithBoundries(val.xMundo,val.yMundo,1) 
            val.resolveIteration(tempMap)
        
        #####################################    
        #aca meter el codigo de ejecucion de la cola de fenomenos.
        #####################################
            



def moveCreature (Individuo , Coordinates , Mapa):
    destinyTile = Mapa.Tiles[Coordinates[0]][Coordinates[1]]
    actualTile = Mapa.Tiles[Individuo.Coordinates[0]][Individuo.Coordinates[1]]
    actualTile.CreatureList.remove(Individuo)
    Individuo.Coordinates = Coordinates
    destinyTile.CreatureList.append(Individuo)
    
    
def main():
    globals.allSpecies["Alfie"]=especies.Alfie()
    current=globals.allSpecies["Alfie"]
    #current.individuos["Alfie1"].breed()
    #print(len(current.individuos))
    globals.worldMap=map.Map(5,5,4)
    
    
    

    
    
main()