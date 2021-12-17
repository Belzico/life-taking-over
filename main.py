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
            


def movementWithBoundries (Individuo, valor_de_percepcion, mapa):
     perceptionValue = int(valor_de_percepcion)
     
     #ESSTO HAY QUE CAMBIARLOOOOO CUANDO SE CAMBIE EL TIPO DE COORDENADAS DE LA ESPECIE
     actRow = Individuo.xMundo  - perceptionValue
     actCol = Individuo.yMundo - perceptionValue
     perceptionList = []
     ##LLenando perceptionlist
     for i in range(0, Individuo.xMundo  + 1 + perceptionValue):
        newList = []
        for j in range(0, Individuo.yMundo  + 1 + perceptionValue):
           newList.append("")
        perceptionList.append(newList)
        
     
     countX=0
     countY=0
     
     for actRow in range(0, Individuo.xMundo  + 1 + perceptionValue):
        for actCol in range(0, Individuo.yMundo  + 1 + perceptionValue):
            if not(0<=actRow<= mapa.SizeX) and not(0<=actCol<=mapa.SizeY):
                perceptionList[countX][countY]= ""
            else:
                perceptionList[countX][countY]= mapa.Tiles[actRow][actCol]
            
            countY+=1
        
        
     countX+=1
     
     return perceptionList
     

    
def main():
    globals.allSpecies["Alfie"]=especies.Alfie()
    current=globals.allSpecies["Alfie"]
    #current.individuos["Alfie1"].breed()
    #print(len(current.individuos))
    globals.worldMap=map.Map(5,5,4)
    
    
    

    
KK = map.Map(6,6,2)

for i in range(KK.SizeX):
    for j in range(KK.SizeY):
        print(KK.Tiles[i][j].Zone.ZoneType)
        print(KK.Tiles[i][j].Coordinates)
        print(KK.Tiles[i][j].ComponentsDict)
        