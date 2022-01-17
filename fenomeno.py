from MyQueue import MyQueue
from random import Random, randint, random
from types import coroutine
import globals
import map
import especies
import misc
import queue
from tiles import Tile

class Fenomeno():
    def __init__(self, nombre, grado, cor, mapa):
        self.nombre = nombre
        self.grado = grado
        self.Recorrido = MyQueue()
        self.pos = 0
        self.cor = cor
        self.count_maxDistance = randint(0,10)
        self.vecmov = []
        self.map = mapa
        
        #cambiar por probabilidad
        duracion = randint(1,7)
        self.Recorrido.put((duracion, None))

    
    def GenerarRecorrido(self,mapa,corulti):
        duracion = randint(0,7)
        if corulti[2] == self.count_maxDistance:
            return []
        
        elif corulti[1] == None:
            return [(duracion,self.cor,0)]
        
        elif self.vecmov == "Random":
            ult_pos = corulti
            
            x = randint(-1,1)
            y = randint(-1,1)
            
            cornew = (ult_pos[1][0] + x, ult_pos[1][1] + y)
            if cornew[0] < mapa.SizeX and cornew[1] < mapa.SizeY:
                return [(duracion,cornew,corulti[2]+ 1)]
            
        return []
                
    
    def GenerateVector(self):
        self.vecmov.append("Random")
    
    def Refresc(self,time):
        queueCom = MyQueue()
        lenrecorrido = len(self.Recorrido)
        for i in range(0,lenrecorrido):
            posrecorrido = self.Recorrido.get()
            queueCom.put((posrecorrido[0],posrecorrido[1],time))
            
            while len(queueCom) != 0:
                posrecorrido = queueCom.get()
                move = (posrecorrido[0],posrecorrido[1],posrecorrido[2])
                duracion = posrecorrido[0]
                rest = posrecorrido[2]
                if duracion > rest:
                    posrecorrido = (duracion - time,posrecorrido[1],posrecorrido[2])
                    self.EfectuarFenomeno(self.map,move)
                    self.Recorrido.put(posrecorrido)
        
                elif duracion == rest:
                    duracion = duracion - time
                    self.EfectuarFenomeno(self.map,move)
                    listmove = self.GenerarRecorrido(self.map,move)
                    self.CambiarZona(posrecorrido,listmove)
                    for i in range(0,len(listmove) - 1):
                        self.Recorrido.append(listmove[i])
        
                elif duracion < rest:
                    rest = rest - duracion
                    self.EfectuarFenomeno(self.map,move)
                    duracion = 0
                    listmove = self.GenerarRecorrido(self.map,move)
                    self.CambiarZona(move,listmove)
                    for i in range(0,len(listmove)):
                        queueCom.put((listmove[i][0],listmove[i][1],rest))
                
            
    def EfectuarFenomeno(self,mapa,move):
        print("Efectuando Fenomeno")
        return
    
    def CambiarZona(self,corulti,listmove):
        i = 0
        for zone in self.map.Zones:
            for tile in zone.TileList:
                if tile.Coordinates == corulti:
                   i += 1
                   #eliminar fenomeno
                   if tile.ComComponentsDict["fenomeno"]:
                       value = tile.ComponentsDict["fenomeno"]
                       tile.ComponentsDict.pop("fenomeno")
                       if value == 0:
                           print("Ocurrio un error al eliminar un fenomeno")
                       tile.ComponentsDict["fenomeno"] = value - 1
                    
                   else:
                       print("No hay fenomenos en esa posicion")
                
                for j in range(0,len(listmove)):
                    if tile.Coordinates == listmove[j]:
                        i += 1
                        #añadir fenomeno
                        if tile.ComComponentsDict["fenomeno"]:
                            value = tile.ComponentsDict["fenomeno"]
                            tile.ComponentsDict.pop("fenomeno")
                            if value == 0:
                                print("Ocurrio un error al eliminar un fenomeno")
                            tile.ComponentsDict["fenomeno"] = value + 1
                    
                        else:
                            tile.ComponentsDict["fenomeno"] = 1
                    
                if i == 1 + len(listmove):
                    return
                    
    def Generar_Fenomeno(mapa):
        Fenomeno.GenerarCiclon(mapa)
        Fenomeno.GenerarErupcion(mapa)
        return
    
    def GenerarCiclon(mapa):
        for zone in mapa.Zones:
            zonetype = zone.ZoneType
            dicGenericFen = ""
            
            if zonetype in globals.ZoneFenomeno:
                dicGenericFen = globals.ZoneFenomeno[zonetype]
            else:
                continue
            
            randp = randint(0,100)
            if dicGenericFen["Ciclon"]*100 >= randp:
                counTile = len(zone.TileList)
                if counTile == 0:
                    continue
                pos_origin = randint(0,counTile-1)
            
                globals.counterFenomeno += 1
                globals.counterCiclon += 1
            
                nameCiclon = "Ciclon" + str(globals.counterCiclon)
                grado_peligrosidad = randint(0,5)
                cor = zone.TileList[pos_origin].Coordinates
            
                c = Ciclon(nameCiclon, grado_peligrosidad, cor, mapa)
                globals.worldFenomenos.put(c)
            
            

    def GenerarErupcion(mapa):
         for zone in mapa.Zones:
            zonetype = zone.ZoneType
            dicGenericFen = ""
            
            if zonetype in globals.ZoneFenomeno:
                dicGenericFen = globals.ZoneFenomeno[zonetype]
            else:
                continue
            
            if not "Volcan" in dicGenericFen:
                continue
            
            randp = randint(0,100)
            if dicGenericFen["Volcan"]*100 >= randp:
                tilesList_Volcan = []
                for tile in zone.TileList:
                    if "Volcan" in tile.ComponentsDict.keys():
                        tilesList_Volcan.append(tilesList_Volcan)

                counTile = len(tilesList_Volcan)
                if counTile == 0:
                    continue
                pos_origin = randint(0,counTile-1)
                
                globals.counterFenomeno += 1
                globals.counterErupcion += 1
            
                nameErupcion = "Erupcion" + str(globals.counterErupcion)
                grado_peligrosidad = randint(0,5)
                cor = zone.TileList[pos_origin].Coordinates
            
                e = ErupcionVolcánica(nameErupcion, grado_peligrosidad, cor, mapa)
                globals.worldFenomenos.put(e)
                
            
        
class Ciclon(Fenomeno):
    def __init__(self, nombre, grado, cor, mapa):
        super().__init__(nombre,grado,cor,mapa)
        
    def Rand_Mov_CC(cor_ciclon, map, poder_ciclon):
        cor_EjeX_low = cor_ciclon[1]
        cor_EjeX_up = map.SizeY-cor_ciclon[1]
        
        cor_EjeY_low = cor_ciclon[0]
        cor_EjeY_up = cor_ciclon[0]
        
        cord_rand_move = misc.randCord(-cor_EjeY_low, cor_EjeY_up, -cor_EjeX_low, cor_EjeX_up)
        cor_new = (cor_ciclon[0] + cord_rand_move[0]*poder_ciclon, cor_ciclon[1] + cord_rand_move[1]*poder_ciclon)
        return cor_new
    
    def EfectuarFenomeno(self,mapas,cor):
        if cor[1] == None:
            return
        
        ListaCriaturas = self.MoverCriaturas(mapas,cor)
    
    def MoverCriaturas(self,mapa,cor):
        pos = self.Recorrido.get()
        self.Recorrido.put(pos)
        
        if pos != None: 
            for zone in mapa.Zones:
                for tile in zone.TileList:
                    if tile.Coordinates == self.cor[1]:
                        i = 0
                        for creature in tile.CreatureList:
                            cordnew = self.Rand_Mov_CC(cor,mapa,1)
                            creature = tile.CreatureList.pop()
                            mapa.MoveCreature(creature,cordnew)

class ErupcionVolcánica(Fenomeno):
    def __init__(self, nombre, grado, cor, mapa):
        super().__init__(nombre,grado,cor,mapa)
                
        
    def EfectuarFenomeno(self,mapa,cor):
        if cor[1] == None:
            return
        
        if cor == self.cor:
            list_caida_rocas = ErupcionVolcánica.PosCaida_Rocas(mapa,self.corvolcan)
            ErupcionVolcánica.Lluvia_De_Rocas(mapa,list_caida_rocas)
        
        ErupcionVolcánica.LavaRecorrido(mapa)
        
    def PosCaida_Rocas(self,mapa):
        for zone in mapa.Zones:
            for tile in zone.TileList:
                if tile.Coordinates == self.cor_volcan:
                    cantidad_rocas = randint(0,20)
                    Lpos_caida_rocas = ErupcionVolcánica.Coordenadas_Caida_Rocas(cantidad_rocas)
                    return Lpos_caida_rocas
    

    def Lluvia_De_Rocas(self,mapa,list_rocas):
        for roca_cor in range(0,len(list_rocas)):
            for zone in mapa.Zones:
                for tile in zone.TileList:
                    if tile.Coordinates == roca_cor:
                        i = 0
                        while i < len(tile.CreatureList):
                            #Cambiar por probabilidades:
                            creature = tile.CreatureList[i]
                            death = randint(0,1)
                            if death == 1:
                                tile.CreatureList.pop(i)
                            else: 
                                i += 1
                                 
        
    def LavaRecorrido(self,mapa,cor):
        if self.Recorrido[self.pos] != None: 
            for zone in mapa.Zones:
                for tile in zone.TileList:
                    if tile.Coordinates == self.Recorrido[self.pos]:
                        ErupcionVolcánica.DamageLava(tile)
    
    def DamageLava(self,tile):
        i = 0
        while i < len(tile.CreatureList):
            creature = tile.CreatureList[i]
            death = randint(0,1)
            if death == 1:
                tile.CreatureList.pop(i)
            else: 
                i += 1
            
    
        
class Terremoto(Fenomeno):
    def __init__(self, nombre, grado, cor, mapa):
        super().__init__(nombre, grado, cor, mapa)
        
    def EfectuarFenomeno(self,mapa,cor):
        if cor[1] == None:
            return
        
        for zone in mapa.Zones:
            for tile in zone.TileList:
                if tile.Coordinates == self.corini:
                    return
                
    def Agrietar():
        pass
