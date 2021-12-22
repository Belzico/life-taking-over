import sys
import queue

#Todas las zonas con las que trabaja la simulación
ZoneList = ['Prairie', 'Mountain', 'Ocean']

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
#mapa
worldMap=""
#lista de todos individuos
worldIndividuals={}

#cola de fenomenos
worldFenomenos=queue.PriorityQueue()


