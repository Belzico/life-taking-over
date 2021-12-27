import globals
import misc
import especies
class Zone:

    def __init__(self, tileCount, ZoneType):
        self.TileCount = tileCount
        self.ZoneType = ZoneType
        self.Danger = globals.ZoneDanger[ZoneType]
        self.TileList = []



#El método recibe la especie con la que se trabajará    
    def startEvolving(self, especie):
        varianzaPromedio = -1
        #Añadiedno la especie original al diccionario
        AllDictionary = {"EspeciePadre" : especie}

        #Contadores para saber cuantos evoluciono
        individualsInZone = 0
        MajorityOfindividuals = 0
        TileToEvolve = -1
        
        varianzaDictionary = {}
        

        #Dicionario donde guardaré el promedio de valores de todos los individuos de la especie
        promedDictionary = {}
        
        #Rellenando los valores promedios de los individuos con todos los que se encuentran en esa zona
        for i in self.TileList:
            temcount = 0
            for j in i.CreatureList:
                if j.especie == especie:
                    temcount += 1
                    individualsInZone +=1
                    #Añadiendo el individuo a la lista          
                    promedDictionary = misc.dictMergeSum(j.naturalDefenseInd, promedDictionary)
            
            if temcount > MajorityOfindividuals:
                MajorityOfindividuals = temcount
                TileToEvolve = i
        
        
        #Dividiendo cada valor entre la cantidad de individuos para hallar el promedio
        for i in promedDictionary.keys():
            promedDictionary[i] = promedDictionary[i]/individualsInZone
            
            
        #Añadiendo el promedio al diccionario
        AllDictionary["Promedio"]= promedDictionary

        
        #Rellenando todos los valores de varianza
        for i in self.TileList:
            for j in i.CreatureList:
                if j.especie == especie:
                    #Añadiendo el individuo a la lista        
                    tempdict = misc.dictMergeSubstract(j.naturalDefenseInd, promedDictionary)
                    varianzaDictionary = misc.dictMergeSum(tempdict,varianzaDictionary)
        
        #Terminando de hallar la varianza
        for i in varianzaDictionary.keys():
            varianzaDictionary[i] = varianzaDictionary[i]/individualsInZone
        
        AllDictionary["Varianza"] = varianzaDictionary
        
        if TileToEvolve != -1:
            AllDictionary["x"] = TileToEvolve.Coordinates[0]
            AllDictionary["y"] = TileToEvolve.Coordinates[1]
        else:
            return
        
        #Hallando la varianza general con respecto a la especie padre
        for i in promedDictionary.keys():
           varianzaPromedio += int(especie.naturalDefense[i])- int(promedDictionary[i])
        varianza = varianzaPromedio/individualsInZone
        
  

        #Si la varianza general es lo suficientemente grande entonces evoluciona
        if varianza >= globals.EvolutionFrequency or varianza <= -1*(globals.EvolutionFrequency) :
            print("Una especie ha evolucionado en la casilla ( "+ str(TileToEvolve.Coordinates[0])+", " +str(TileToEvolve.Coordinates[1]) +")" )
            if MajorityOfindividuals <= (len(especie.individuos)/2):
                AllDictionary["Individuos"] = MajorityOfindividuals
                TileToEvolve.deleteCreaturesEspecies(MajorityOfindividuals, especie)
                especies.Especies(MajorityOfindividuals,TileToEvolve.Coordinates[0],TileToEvolve.Coordinates[1],AllDictionary)
              
            
            else:
                AllDictionary["Individuos"] = MajorityOfindividuals/2
                TileToEvolve.deleteCreaturesEspecies(MajorityOfindividuals/2, especie)
                especies.Especies(MajorityOfindividuals/2,TileToEvolve.Coordinates[0],TileToEvolve.Coordinates[1],AllDictionary)
            
    
        
    
        
    
  
        #Calculando el promedio de la varianza de todos los valores


    
        return AllDictionary

        

    
    
        
    
    def ChangeDanger(self, newDangerInt):
        self.Danger = newDangerInt