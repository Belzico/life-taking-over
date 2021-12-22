import especies
import globals
import map


def worldController():
    i=30
    while (i>0):
        
        value=''
        for val in globals.worldIndividuals:
            value=globals.worldIndividuals[val]
            tempMap=globals.worldMap.movementWithBoundries(value,1) 
            value.resolveIteration(tempMap)
        i-=1
        
        #globals.worldMap.PrintMap()
        print('---------------------------------NEW CYCLE-------------------------------------------------')
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
    
