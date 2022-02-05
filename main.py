from tkinter import Misc
import especies
import globals
import map
import misc
import fenomeno


def worldController():
    
    while (globals.iterationCicles>=globals.globalTime):
        
        value=''
        for val in globals.worldIndividuals:
            value=globals.worldIndividuals[val]
            tempMap=globals.worldMap.movementMatrix(value) 
            value.resolveIteration(tempMap)
        
        
        misc.dieList()
        misc.bornList()
        
        if globals.globalTime%globals.evolutionTimeCheck == 0:
            for h in  globals.worldMap.Zones:
                for j in globals.allSpecies.keys():
                    h.startEvolving(globals.allSpecies[j])
                
        fenomeno.Euristics(globals.worldMap)
        for n in globals.CatastrophyList:
            n.Executing()

        for item in globals.waitSpeciesList:
            globals.allSpecies[item[0]]=item[1]
        
        globals.waitSpeciesList=[]
        
        globals.globalTime+=1
        #globals.worldMap.PrintMap()
        print('---------------------------------NEW CYCLE-------------------------------------------------')
        #####################################    
        #aca meter el codigo de ejecucion de la cola de fenomenos.
        #####################################
    print("Simulation finished!!!!!")        



    
def main():
    globals.worldMap=map.Map(10,10,5)
    globals.allSpecies["1"]=especies.Especies(5,0,0)
    #current=globals.allSpecies["Alfie"]
    #current.individuos["Alfie1"].breed()
    #print(len(current.individuos))
    print("star world")
    worldController()
    
print(type(3)==int)
main()
    
