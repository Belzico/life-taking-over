from tkinter import Misc
import especies
import globals
import map
import misc
import json
import os


def worldController():
    i=500
    while (i>0):
        
        value=''
        for val in globals.worldIndividuals:
            value=globals.worldIndividuals[val]
            tempMap=globals.worldMap.movementMatrix(value) 
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
    print("Simulation finished!!!!!")        



    
def main():
    globals.worldMap=map.Map(10,10,5)
    globals.allSpecies["1"]=especies.Especies(5,0,0)
    
    #Poner en true si se quiere guardar el mapa generado en un JSON
    save= True
    if save == True:
        filename = 'map.json'         
        with open(filename, 'w') as file_object:
            json.dump(globals.worldMap, file_object) 
    
    #Poner en True si se quiere cargar el mapa de un JSON
    load = False
    
    #current=globals.allSpecies["Alfie"]
    #current.individuos["Alfie1"].breed()
    #print(len(current.individuos))
    print("star world")
    worldController()
    
  

main()
    
