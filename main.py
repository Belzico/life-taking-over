import especies
import globals
import map


def worldController():
    while (True):
        
        i=10
        value=''
        for val in globals.worldIndividuals:
            value=globals.worldIndividuals[val]
            tempMap=globals.worldMap.movementWithBoundries(value,1) 
            value.resolveIteration(tempMap)
        i-=1
        
        globals.worldMap.PrintMap()
        print('---------------------------------NEW CYCLE-----------------------------------------------------------------')
        #####################################    
        #aca meter el codigo de ejecucion de la cola de fenomenos.
        #####################################
            



    
def main():
    globals.allSpecies["Alfie"]=especies.Alfie()
    current=globals.allSpecies["Alfie"]
    #current.individuos["Alfie1"].breed()
    #print(len(current.individuos))
    globals.worldMap=map.Map(5,5,4)
    worldController()
    
    
    
main()
    

        