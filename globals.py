import queue
from ArbolEvolutivo.arbolEvolutivo import Arbol_Evo

#Todas las zonas con las que trabaja la simulación
ZoneList = ['Prairie', 'Mountain', 'Ocean']
#La peligrosidad de cada zona
ZoneDanger = {'Prairie': 2, 'Mountain': 8, 'Ocean' : 5}

voidValue = 10000000

#Un entero de 1 hasta 100 que representa el porcentaje de posibilidad
#con la que puede ocurrir un fenómeno al inicio de la simulación
#o luego de que haya acabado de ocurrir otro fenómeno
CatastrophyPosibility = 5

#Aumento de probabilidad por turno con la que ocurrirá un fenómeno
TurnsToCatastrophy = 2

#Máximo de fenómenos que pueden estar ocurriendo al mismo tiempo
MaxCatastrophy = 15

#Categoría máxima que puede tener generalmente un fenómeno(cantidad máxima de peligro en zona)
MaxCategory = 5

#Lista de fenómenos
CatastrophyList = []

#Frecuencia con la que una especie evoluciona (mientras más grande, menos común son las evluciones)
EvolutionFrequency =1

#valor para aumentar el chance de muerte cuando se pasa por una zona al caminar
killerModifier=2
#maximo peligro posible de una zona
MaxDangerinTile = 9*MaxCategory*5


#Todos los elementos con los que trabaja la simulación
WorldComponents = { 'Solar Light','Water', 'Organic Matter', 'Phosil' ,'Iron' , 'Aluminum' , 'Oxygen' , 'Carbon Dioxide' , 'Helium' , 'Nitrogen' }

InfiniteRange = (10000, 100000)
LargeRandomRange = (3000, 5000)
MediumRandomRange = (1000, 3000)
LowRandomRange = (200, 1000)
NoneRandomRange = (0, 200)



PrairieGenerationList = {'Solar Light' : InfiniteRange ,
                        'Water' : LowRandomRange,
                        'Organic Matter' : MediumRandomRange,
                        'Phosil' : NoneRandomRange ,
                        'Iron': LowRandomRange ,
                        'Aluminum' : NoneRandomRange ,
                        'Oxygen' : LargeRandomRange,
                        'Carbon Dioxide': LargeRandomRange ,
                        'Helium': NoneRandomRange,
                        'Nitrogen' :NoneRandomRange}


MountainGenerationList = {'Solar Light' : InfiniteRange ,
                        'Water' : NoneRandomRange,
                        'Organic Matter' : NoneRandomRange,
                        'Phosil' : LargeRandomRange ,
                        'Iron': MediumRandomRange ,
                        'Aluminum' : MediumRandomRange ,
                        'Oxygen' : MediumRandomRange,
                        'Carbon Dioxide': LargeRandomRange ,
                        'Helium': LowRandomRange,
                        'Nitrogen' :LowRandomRange}



OceanGenerationList = {'Solar Light' : InfiniteRange ,
                        'Water' : InfiniteRange,
                        'Organic Matter' : MediumRandomRange,
                        'Phosil' : NoneRandomRange ,
                        'Iron': LowRandomRange ,
                        'Aluminum' : NoneRandomRange ,
                        'Oxygen' : MediumRandomRange,
                        'Carbon Dioxide': LowRandomRange ,
                        'Helium': LowRandomRange,
                        'Nitrogen' :LowRandomRange}


#numero de predicciones en el combate 9 por defecto
tempPredictions=9


#diccionario de especies
allSpecies ={}
lastNameSpecie=0
#mapa
worldMap=""
#lista de todos individuos
worldIndividuals={}

#cola de fenomenos
worldFenomenos=queue.PriorityQueue()

#lista de individuos muertos para eliminar al final del siglo
deadIndividuals=[]

#lista de individuos nacidos para agregar al final del siglo
bornIndividuals=[]


#-------------------------------------------------NEW STUFF--------------------------------------------------------------------

#Variable de caza, mientra más grande más probable que el individuo decida cazar (0--->infinito)
    # 0: nunca cazará, 
    # 1: podrá cazar aprox un 1/10 porciento de veces que evolucione , 
    # 1000000: siempre cazará(probablemente))
Hunting = 1

#Que tan débil debe ser la craitura que se va a cazar, (1---->10)
    # 10: más debil que yo, pero no me importa cuan débil
    # 5: siempre será el doble de débil o más que yo
    # 1: siempre será 10 veces más debil que yo
Weakness = 10

#-------------------------------------------------NEW STUFF--------------------------------------------------------------------

#el arbol que muestra la evolucion de las especies
arb_evo = Arbol_Evo()

#tamaño minimo de individuos de una nueva especie
minSizeOfNewEspecies=20

#lista para agregar nuevas especies
waitSpeciesList=[]

#tipos de muertes posibles
deadTypesList=["Natural","Hunted","Hunting","Ciclon","Landslide","Volcan","Tsunami","Moving","Evolving"]

#cantidad de ciclos que se van a realizar
iterationCicles=1000

#iteracion actual del ciclo o dia del ciclo
globalTime=1

#cada cuanto tiempo se revisan las evoluciones
evolutionTimeCheck=10