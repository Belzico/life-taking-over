from tkinter import Misc
import especies
import globals
import map
import misc


def worldController():
    i=200
    while (i>0):
        
        value=''
        for val in globals.worldIndividuals:
            value=globals.worldIndividuals[val]
            tempMap=globals.worldMap.movementWithBoundries(value,1) 
            value.resolveIteration(tempMap)
        i-=1
        
        misc.dieList()
        misc.bornList()
        
        if i%10 == 0:
            for h in  globals.worldMap.Zones:
                for j in globals.allSpecies.keys():
                    h.startEvolving(globals.allSpecies[j])
                
        
        
        #globals.worldMap.PrintMap()
        print('---------------------------------NEW CYCLE-------------------------------------------------')
        #####################################    
        #aca meter el codigo de ejecucion de la cola de fenomenos.
        #####################################
            



    
def main():
    globals.worldMap=map.Map(1,1,1)
    globals.allSpecies["1"]=especies.Especies(5,0,0)
    #current=globals.allSpecies["Alfie"]
    #current.individuos["Alfie1"].breed()
    #print(len(current.individuos))
    
    worldController()
    
    
    
main()
    
