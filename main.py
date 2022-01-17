from tkinter import Misc
import especies
from fenomeno import Fenomeno
import globals
import map
import misc


def worldController():
    i=50
    while (i>0):
        
        #Generando nuevos fenomenos
        Fenomeno.Generar_Fenomeno(globals.worldMap)
        
        #Refrescando cada fenomeno existente
        c = len(globals.worldFenomenos)
        while c > 0:
            fen = globals.worldFenomenos.get()
            fen.Refresc(globals.time_refresch)
        
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
    globals.worldMap=map.Map(5,10,10)
    globals.allSpecies["1"]=especies.Especies(5,0,0)
    #current=globals.allSpecies["Alfie"]
    #current.individuos["Alfie1"].breed()
    #print(len(current.individuos))
    print("star world")
    worldController()
    
  
main()
    
