import globals
import misc
class Zone:

    def __init__(self, tileCount, ZoneType):
        self.TileCount = tileCount
        self.ZoneType = ZoneType
        self.Danger = globals.ZoneDanger[ZoneType]
        self.TileList = []



#El método recibe la especie con la que se trabajará    
    def startEvolving(self, especie):
        varianza = -1
        #Añadiedno la NaturalDefense de la especie original al diccionario
        AllDictionary = {"NaturalDefense" : especie.naturalDefense}
        
        #Añadiendo la lista de individuos
        AllDictionary = {"Individuos" : []}
        individualsCount = 0

        #Dicionario donde guardaré el promedio de valores de todos los individuos de la especie
        PromedDictionary = {}
        
        #Rellenando los valores promedios de los individuos con todos los que se encuentran en esa zona
        for i in range(self.TileCount):
            for j in range(len(self.TileList[i].CreatureList)):
                if j.especie == especie:
                    individualsCount +=1
                    #Añadiendo el individuo a la lista
                    AllDictionary["Individuos"].append(j)             
                    promedDictionary = misc.dictMergeSum(j.naturalDefenseInd, promedDictionary)
                    

        #Dividiendo cada valor entre la cantidad de individuos para hallar el promedio
        for i in promedDictionary.keys():
            promedDictionary[i] = promedDictionary[i]/individualsCount
            
        #Calculando la varianza de todos los valores
        for i in promedDictionary.keys():
           varianza += int(especie.naturalDefense[i])- int(promedDictionary[i])
        varianza = varianza/individualsCount
        
        #añadiendo el valor de varianza y los promedios al diccionario
        AllDictionary["Varianza"]= varianza
        AllDictionary["Promedio"]= promedDictionary
    
    
        return AllDictionary

        
        
    
    def ChangeDanger(self, newDangerInt):
        self.Danger = newDangerInt