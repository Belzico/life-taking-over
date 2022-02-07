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
        print('---------------------------------NEW CYCLE-------------------------------------------------')
        #####################################    
        #####################################
    print("Simulation finished!!!!!")        



    
def main():
    globals.worldMap=map.Map(10,10,5)
    especies.Especies(5,0,0)
    especies.Especies(5,0,0)
    #globals.allSpecies["1"].ModifyCaracteristic("Vida",100) #ej de modify
    especies.Especies.initSpecies()
    
    print("star world")
    worldController()
    
main()
    
