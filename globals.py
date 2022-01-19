import sys
import queue

#Todas las zonas con las que trabaja la simulación
ZoneList = ['Prairie', 'Mountain', 'Ocean']
#La peligrosidad de cada zona
ZoneDanger = {'Prairie': 2, 'Mountain': 8, 'Ocean' : 5}

#Variable de caza, mientra más grande más probable que el individuo decida cazar (0--->infinito)
    # 0: nunca cazará, 
    # 1: podrá cazar aprox un 1/10 porciento de veces que evolucione , 
    # 1000000: siempre cazará(probablemente))
Hunting = 1

#Que tan débil debe ser la craitura que se va a cazar, (1---->10)
    # 10: más debil que yo, pero no me importa cuan débil
    # 5: siempre será el doble de débil o más
    # 1: siempre  será 10 veces más debil que yo
Weakness = 

voidValue = 10000000

#Frecuencia con la que una especie evoluciona (mientras más grande, menos común son las evluciones)
EvolutionFrequency = 1

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