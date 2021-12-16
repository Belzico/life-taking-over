import especies
import globals
import map



def movementWithBoundries (Individuo, valor_de_percepcion, mapa):
     perceptionValue = int(valor_de_percepcion)
     
     #ESSTO HAY QUE CAMBIARLOOOOO CUANDO SE CAMBIE EL TIPO DE COORDENADAS DE LA ESPECIE
     actRow = Individuo.xMundo  - perceptionValue
     actCol = Individuo.yMundo - perceptionValue
     perceptionList = []
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
     
     
def movmentWithoutBoundries (Individuo, valor_de_percepcion, mapa):
    perceptionValue = int(valor_de_percepcion)
    
    actRow = Individuo.xMundo  - perceptionValue
    actCol = Individuo.yMundo - perceptionValue
    perceptionList = []
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



def moveCreature (Individuo , Coordinates , Mapa):
    destinyTile = Mapa.Tiles[Coordinates[0]][Coordinates[1]]
    actualTile = Mapa.Tiles[Individuo.Coordinates[0]][Individuo.Coordinates[1]]
    actualTile.CreatureList.remove(Individuo)
    Individuo.Coordinates = Coordinates
    destinyTile.CreatureList.append(Individuo)
    
    
def main():
    globals.allSpecies["Alfie"]=especies.Alfie()
    current=globals.allSpecies["Alfie"]
    current.individuos["Alfie1"].breed()
    print(len(current.individuos))

    
    
main()