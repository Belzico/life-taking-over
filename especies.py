import random
import globals
import misc
import copy

#clase especies
#una especie es un vector donde en cada posicion se llevaran distinatas propiedades de la especie,
#ejemplo en la posicion i puede guardarse la temperatura maxima que puede resistir.
class Especies():
    
    
    
    def __init__(self,individuos,x,y,evolve=None):
        #para ver si se cae en el caso de la evolucion donde se reciben todos los parametros en un dic
        if evolve!=None:
            self.evolve(evolve)
            return
            
        #datos como el tiempo de vida, tipo de alimentacion...etc
        self.basicInfo={}
        #datos como partes de veneno, piel dura, colmillos afilados...etc
        #esto sera utilizado en lucha entre especies
        self.naturalDefense={}
        #datos para saber que tan resistente a algun elemento es...etc
        self.resistenciaElemental={}
        #lisa de tidos los individuos de la especie
        self.individuos={}
        #lista de elementos de donde puede sacar parte de la energix
        self.alimentos={}
        
        #llamada al generador
        self.especieGenerator(x,y,individuos)
        #nueva especie a la que puede estar evolucionando
        self.newEvolution="0"
        #proximo numero de reproducciones que degeneran en la nueva especies
        self.countEvolutions="0"

        #numero del proximo individuo
        self.nextName=int(individuos)

    
        
    #aca generaremos especies siguiendo algunos criterios pero de forma aleatoria
    def especieGenerator(self,x,y,individuos):
        self.basicInfo=Especies.basicInfoGenerator(individuos)
        
        

        self.naturalDefense=Especies.naturalDefenseGenerator()
        self.foodListGenerator()
        self.resistenciaElemental=Especies.resistenciasElementalesGenerator()
        self.individuos=self.listaIndividuosGenerator(x,y,individuos)
        
    
    def listaIndividuosGenerator(self,x,y,miembros,varianzas=None):
        individuals={}
        i=0
        
        while(i<miembros):
            name=self.basicInfo["name"]
            creatureName=""+str(name)+""+"$"+str(i)+""
            individuals[""+str(name)+""+"$"+str(i)+""]=Individuo(x,y,self,creatureName,0,varianzas)
            i+=1
        #empezaran en las coordenadas 0,0,0,0
        
        return individuals
    
    
    def basicInfoGenerator(individuos):
        basicInfo={}
        #nombrar la especie
        name=str(int(globals.lastNameSpecie)+1)
        globals.lastNameSpecie+=1
        basicInfo["name"]=name
        globals.lastNameSpecie+=1
        #dos tipos unicelular y pluricelular
        basicInfo["Tipo_de_celula"]="unicelular"
        #por definir, por ahora asexual y sexual entre 2 individuos de distinto sexo
        basicInfo["Tipo_de_reproduccion"]="asexual"
        #sexo del indi
        basicInfo["Cantidad_de_miembros"]=0

        
        basicInfo["Canibal"]==True
        
        #por definir, por ahora seran dos opciones, alimentarse del entorno(aire, minerales) o alimentarse de otro individuo o los restos de este
        basicInfo["Tipo_de_alimentacion"]="element"
        #sexo del individuo
        basicInfo["Sexo"]="0"
        #el ultimo numero para nombrar al siguiente individuo
        basicInfo["Ultimo_numero"]=str(individuos)
        #generamos los individuos
        
        return basicInfo
    
    def naturalDefenseGenerator():
        naturalDefense={}
        #vida maxima del individuo
        life=random.randint(20,25)
        naturalDefense["Vida"]=str(life)
        #la percepcion no es mas que cuantas casillas sin contar en la que esta es capaz de ver/oir...etc el individuo
        naturalDefense["Percepcion_de_mundo"]="1"
        #la inteligencia es un factor que puede influir en varios campos
        naturalDefense["Inteligencia"]="0"
        #factor que indica que tan sigiloso puede llegar a ser un individuo en un combate
        naturalDefense["Sigilo"]=0
        #armadura que indica que tan dura es la piel del individuo
        armor=random.randint(1,4)
        naturalDefense["Armadura"]=str(armor)
        #armadura en zona debil ej: la parte de abajo de los cocodrilos es suave contrario a la espalda
        naturalDefense["Armadura_debil"]=str(int(armor/random.randint(1,armor)))
        #porciento de armadura fuerte del cuerpo
        naturalDefense["Armadura_fuerte_porciento"]=str(random.randint(0,51))
        #probabilidad de aumentar el golpe critico en la zona debil
        naturalDefense["Crit_chance_increase"]="0"
        #probabilidad de aplicar daño de sangrado al enemigo
        naturalDefense["Bleed_chance"]="0"
        #daño por sangrado
        naturalDefense["Bleed_damage"]="1"
        #probabilidad de ralentizar al objetivo permanentemente mientras dure el combate, se acumula
        naturalDefense["Slow_chance"]="0"
        #velocidad reducida
        naturalDefense["Slow_done"]="1"
        #cantidad de casillas que puede recorrer en un dia en el agua
        naturalDefense["Velocidad_agua"]=str(random.randint(10,12))
        #cantidad de casillas que puede recorrer en un dia en volando
        #naturalDefense["Velocidad_aire"]=str(random.randint(0,1))
        #cantidad de casillas que puede recorrer en un dia en la tierra
        #naturalDefense["Velocidad_tierra"]=str(random.randint(0,1))
        
        naturalDefense["Edad_de_madurez_sexual_en_dias"]=str(random.randint(10,21))
        naturalDefense["Tiempo_de_gestacion"]=str(random.randint(10,21))
        
        #cuantos hijos por reproduccion puede consebir por reproduccion
        naturalDefense["Tiempo_entre_reproducccion"]="5"
        naturalDefense["Tiempo_de_vida_en_dias"]=str(random.randint(50,101))

        #cuanta energia daran al que los mate y se alimente de ellos
        naturalDefense["Cantidad_de_energia_dropeada"]=str(life)
        #cantidad de energia diaria requerida por individuo
        temporalEnergy=str(random.randint(1,4))
        naturalDefense["Cantidad_de_energia_necesaria"]=1+life/5
        #cantidad de energia que pueden almacenar maxima
        naturalDefense["Cantidad_de_energia_almacenable"]=1+(life/5)*3
        #cantidad de energia almacenada a partir de la cual le da hambre
        naturalDefense["Nivel_de_Hambre"]=1+2*life/3
        
        return naturalDefense
        
    def resistenciasElementalesGenerator():
        resistenciasElementales={}
        return resistenciasElementales
    
    def foodListGenerator(self):
        self.alimentos["Solar Light"]=int(self.naturalDefense["Cantidad_de_energia_almacenable"])
        
    
    #metodo para evolucionar una especie
    def evolve(self,paramsDic):
        #se reciben todos los parametros en el dic
        father=paramsDic["EspeciePadre"] 
        self.basicInfo= copy.deepcopy(father.basicInfo)
        self.naturalDefense=paramsDic["Promedio"]
        self.resistenciaElemental=copy.deepcopy(father.resistenciaElemental)
        self.alimentos=copy.deepcopy(father.alimentos)
        self.nextName=paramsDic["Individuos"]
        
        
        #revisando si se agrega el elemento a los comestibles o se elimina alguno existente
        if int(father.naturalDefense["Vida"])>int(self.naturalDefense["Vida"]):
            self.removeFood()
        if int(father.naturalDefense["Vida"])<int(self.naturalDefense["Vida"]):
            self.addFood(paramsDic["Elemento"])
            
        
        self.basicInfo["name"]=int(globals.lastNameSpecie)
        globals.lastNameSpecie=int(globals.lastNameSpecie)+1
        
        #chance de evolucionar a pluricelular
        if self.basicInfo["Tipo_de_celula"]=="unicelular":
            tempRandom=random.randint(0,100)
            if tempRandom>50:
                print("La especie "+str(self.basicInfo["name"])+" es pluricelular")   
                self.basicInfo["Tipo_de_celula"]="pluricelular"
        
        
        if self.basicInfo["Canibal"]==True:
            tempRandom=random.randint(0,100)
            if tempRandom>50:
                print("La especie "+str(self.basicInfo["name"])+" es canibal")   
                self.basicInfo["Canibal"]=True
            else:
                print("La especie "+str(self.basicInfo["name"])+" no es canibal")   
                self.basicInfo["Canibal"]=False
        
        #chance de evolucionar a reproduccion sexual
        if self.basicInfo["Tipo_de_reproduccion"]=="asexual":
            tempRandom=random.randint(0,100)
            if tempRandom>-1:
                self.basicInfo["Tipo_de_reproduccion"]="sexual"        
                print("La especie "+str(self.basicInfo["name"])+" tiene reproduccion sexual")
        
        #varianza de las especies
        varianza=paramsDic["Varianza"]
        self.individuos=self.listaIndividuosGenerator(paramsDic["x"] ,paramsDic["y"],paramsDic["Individuos"],varianza)
    
    #agrega un elemento comestible o aumenta su eficacia    
    def addFood(self,food):
        if food in self.alimentos:
            self.alimentos[food]=int(self.alimentos[food])+1
        else:
            self.alimentos[food]=1
    #resta 1 a la energia q se obtiene de un elemento random y en caso de q llegue a 0 lo elimina
    def removeFood(self):
        for item in self.alimentos:
            self.alimentos[item]=self.alimentos[item]-1
            break
        if int(self.alimentos[item])<=0:
                del self.alimentos[item]

class Individuo():
    def __init__(self,xMundo,yMundo,especie,name,father,varianza=None):
        
        
        #coordenadas
        self.xMundo=xMundo
        self.yMundo=yMundo

        #la cantidad de energia con la que empiezan
        self.saciedad=especie.naturalDefense["Cantidad_de_energia_almacenable"]
        #string con el nombre de la especie
        self.especie=especie
        #sexo del individuo, en caso de ser asexual sera por defecto cero
        if especie.basicInfo["Tipo_de_reproduccion"]=="asexual":
            self.sexo=0
        elif especie.basicInfo["Tipo_de_reproduccion"]=="sexual":
            self.sexo=random.randint(0,1)
        #Fecha en la que muere, (la edad sera la resta con la fecha actual)
        #la muerte se debera tratar de forma lazy, x cada iteracion no hay q actualizar, 
        #solo en kso de que sea necesario
        self.edad=especie.naturalDefense["Tiempo_de_vida_en_dias"]
        #nombre del individuos
        self.name=name

        self.lastReproduction=0
        #agregando aa la casilla
        globals.worldMap.IsBorn(self)
        
        
                
        #agregando a la lista de individuos global    
        #globals.worldIndividuals[self.name]=self
        globals.bornIndividuals.append((self.name,self))
        
        
        self.especie.basicInfo["Cantidad_de_miembros"]=str(int(self.especie.basicInfo["Cantidad_de_miembros"])+1)
        #lista con las defensas naturales del individuo simulando que no todos son iwales
        self.naturalDefenseInd={}
        
        if father==0:
            self.naturalDefenseGeneratorInd(especie.naturalDefense,varianza)
        else:
            self.naturalDefenseGeneratorInd(varianza)

        self.priorities={}
        self.setPriorities()
        
            
    
    #def battleLogGenerator(individuo):
    #    battleLog={}
    #    battleLog["life"]=int(individuo.naturalDefenseInd["Vida"])
    #    battleLog["currentLife"] =int(individuo.naturalDefenseInd["Vida"])
    #    battleLog["movements"] =int(individuo.naturalDefenseInd["Velocidad_agua"])
    #    battleLog["xPosition"] =0
    #    battleLog["xPosition"] =0
    #    
    #    battleLog["debuffSlow"]=0
    #    battleLog["debuffBleed"]=0
    #    return battleLog

    #def resetBattleLog(individuo,battleLog):
    #    battleLog["currentMovements"]=int(individuo.naturalDefenseInd["Velocidad_agua"])
    #    
    #def copyBattleLog(firstBattleLog):
    #    newBattleLog={}
    #    for key in firstBattleLog:
    #        newBattleLog[key]=firstBattleLog[key]
    #        
    #    return newBattleLog
    
    def setPriorities(self):
        self.priorities["hambre"]=1 +(1-self.saciedad/self.naturalDefenseInd["Cantidad_de_energia_almacenable"])
        self.priorities["danger"]=2-(1-self.saciedad/self.naturalDefenseInd["Cantidad_de_energia_almacenable"])
        self.priorities["mate"]=1
        self.priorities["imanEspecie"]=1
        
    
    
    #este sera el metodo encargado de reproducir a un individuo, y de el se derivara a los distintos tipos de reproduccion   
    def naturalDefenseGeneratorInd(self,defences,varianza=None):
        
        a=-1        
        b=2
        
        self.naturalDefenseInd["Vida"]=int(defences["Vida"])+random.randint(a,b)
        self.naturalDefenseInd["Percepcion_de_mundo"]=int(defences["Percepcion_de_mundo"])+random.randint(a,b)
        self.naturalDefenseInd["Inteligencia"]=int(defences["Inteligencia"])+random.randint(-a,b)
        self.naturalDefenseInd["Sigilo"]=int(defences["Sigilo"])+random.randint(a,b)
        self.naturalDefenseInd["Armadura"]=int(defences["Armadura"])+random.randint(a,b)
        self.naturalDefenseInd["Armadura_debil"]=int(defences["Armadura_debil"])+random.randint(a,b)
        self.naturalDefenseInd["Armadura_fuerte_porciento"]=int(defences["Armadura_fuerte_porciento"])+random.randint(a,b)
        self.naturalDefenseInd["Crit_chance_increase"]=int(defences["Crit_chance_increase"])+random.randint(-a,b)
        self.naturalDefenseInd["Bleed_chance"]=int(defences["Bleed_chance"])+random.randint(a,b)
        self.naturalDefenseInd["Crit_chance_increase"]=int(defences["Crit_chance_increase"])+random.randint(a,b)
        self.naturalDefenseInd["Bleed_damage"]=int(defences["Bleed_damage"])+random.randint(a,b)
        self.naturalDefenseInd["Slow_chance"]=int(defences["Slow_chance"])+random.randint(a,b)
        self.naturalDefenseInd["Slow_done"]=int(defences["Slow_done"])+random.randint(a,b)
        self.naturalDefenseInd["Velocidad_agua"]=int(defences["Velocidad_agua"])+random.randint(a,b)
        #self.naturalDefenseInd["Velocidad_aire"]=int(defences["Velocidad_aire"])+random.randint(a,b)
        #self.naturalDefenseInd["Velocidad_tierra"]=int(defences["Velocidad_tierra"])+random.randint(a,b)
        self.naturalDefenseInd["Edad_de_madurez_sexual_en_dias"]=int(defences["Edad_de_madurez_sexual_en_dias"])+random.randint(a,b)
        self.naturalDefenseInd["Tiempo_de_gestacion"]=int(defences["Tiempo_de_gestacion"])+random.randint(a,b)
        self.naturalDefenseInd["Tiempo_entre_reproducccion"]=int(defences["Tiempo_entre_reproducccion"])+random.randint(a,b)
        self.naturalDefenseInd["Tiempo_de_vida_en_dias"]=int(defences["Tiempo_de_vida_en_dias"])+random.randint(a,b)        
        self.naturalDefenseInd["Cantidad_de_energia_dropeada"]=int(defences["Vida"])
        self.naturalDefenseInd["Cantidad_de_energia_necesaria"]=1+int(defences["Vida"])/5
        self.naturalDefenseInd["Cantidad_de_energia_almacenable"]=1+3*int(defences["Vida"])/5
        self.naturalDefenseInd["Nivel_de_Hambre"]=1+2*int(self.naturalDefenseInd["Vida"])/3


        if varianza!=None:


            self.naturalDefenseInd["Vida"]=int(self.naturalDefenseInd["Vida"])+int(random.randint( int(varianza["Vida"]),int(varianza["Vida"])))
            self.naturalDefenseInd["Percepcion_de_mundo"]=int(self.naturalDefenseInd["Percepcion_de_mundo"])+int(random.randint(int(varianza["Percepcion_de_mundo"]),int(varianza["Percepcion_de_mundo"])))
            self.naturalDefenseInd["Inteligencia"]=int(self.naturalDefenseInd["Inteligencia"])+int(random.randint(int(varianza["Inteligencia"]),int(varianza["Inteligencia"])))
            self.naturalDefenseInd["Sigilo"]=int(self.naturalDefenseInd["Sigilo"])+int(random.randint(int(varianza["Sigilo"]),int(varianza["Sigilo"])))
            self.naturalDefenseInd["Armadura"]=int(self.naturalDefenseInd["Armadura"])+int(random.randint(int(varianza["Armadura"]),int(varianza["Armadura"])))
            self.naturalDefenseInd["Armadura_debil"]=int(self.naturalDefenseInd["Armadura_debil"])+int(random.randint(int(varianza["Armadura_debil"]),int(varianza["Armadura_debil"])))
            self.naturalDefenseInd["Armadura_fuerte_porciento"]=int(self.naturalDefenseInd["Armadura_fuerte_porciento"])+int(random.randint(int(varianza["Armadura_fuerte_porciento"]),int(varianza["Armadura_fuerte_porciento"])))
            self.naturalDefenseInd["Crit_chance_increase"]=int(self.naturalDefenseInd["Crit_chance_increase"])+int(random.randint(int(varianza["Crit_chance_increase"]),int(varianza["Crit_chance_increase"])))
            self.naturalDefenseInd["Bleed_chance"]=int(self.naturalDefenseInd["Bleed_chance"])+int(random.randint(int(varianza["Bleed_chance"]),int(varianza["Bleed_chance"])))
            self.naturalDefenseInd["Crit_chance_increase"]=int(self.naturalDefenseInd["Crit_chance_increase"])+int(random.randint(int(varianza["Crit_chance_increase"]),int(varianza["Crit_chance_increase"])))
            self.naturalDefenseInd["Bleed_damage"]=int(self.naturalDefenseInd["Bleed_damage"])+int(random.randint(int(varianza["Bleed_damage"]),int(varianza["Bleed_damage"])))
            self.naturalDefenseInd["Slow_chance"]=int(self.naturalDefenseInd["Slow_chance"])+int(random.randint(int(varianza["Slow_chance"]),int(varianza["Slow_chance"])))
            self.naturalDefenseInd["Slow_done"]=int(self.naturalDefenseInd["Slow_done"])+int(random.randint(int(varianza["Slow_done"]),int(varianza["Slow_done"])))
            self.naturalDefenseInd["Velocidad_agua"]=int(self.naturalDefenseInd["Velocidad_agua"])+int(random.randint(int(varianza["Velocidad_agua"]),int(varianza["Velocidad_agua"])))
            #self.naturalDefenseInd["Velocidad_aire"]=int(self.naturalDefenseInd["Velocidad_aire"])+int(random.randint(int(varianza["Velocidad_aire"]),int(varianza["Velocidad_aire"])))
            #self.naturalDefenseInd["Velocidad_tierra"]=int(self.naturalDefenseInd["Velocidad_tierra"])+int(random.randint(int(varianza["Velocidad_tierra"]),int(varianza["Velocidad_tierra"])))
            self.naturalDefenseInd["Edad_de_madurez_sexual_en_dias"]=int(self.naturalDefenseInd["Edad_de_madurez_sexual_en_dias"])+int(random.randint(int(varianza["Edad_de_madurez_sexual_en_dias"]),int(varianza["Edad_de_madurez_sexual_en_dias"])))
            self.naturalDefenseInd["Tiempo_de_gestacion"]=int(self.naturalDefenseInd["Tiempo_de_gestacion"])+int(random.randint(int(varianza["Tiempo_de_gestacion"]),int(varianza["Tiempo_de_gestacion"])))
            self.naturalDefenseInd["Tiempo_entre_reproducccion"]=int(self.naturalDefenseInd["Tiempo_entre_reproducccion"])+int(random.randint(int(varianza["Tiempo_entre_reproducccion"]),int(varianza["Tiempo_entre_reproducccion"])))
            self.naturalDefenseInd["Tiempo_de_vida_en_dias"]=int(self.naturalDefenseInd["Tiempo_de_vida_en_dias"])+int(random.randint(int(varianza["Tiempo_de_vida_en_dias"]),int(varianza["Tiempo_de_vida_en_dias"])))
            self.naturalDefenseInd["Cantidad_de_energia_dropeada"]=int(self.naturalDefenseInd["Vida"])
            self.naturalDefenseInd["Cantidad_de_energia_necesaria"]=1+(int(self.naturalDefenseInd["Vida"]))/5
            self.naturalDefenseInd["Cantidad_de_energia_almacenable"]=1+3*(int(self.naturalDefenseInd["Vida"]))/5
            self.naturalDefenseInd["Nivel_de_Hambre"]=2*int(self.naturalDefenseInd["Vida"])/3


        
        
        if self.naturalDefenseInd["Vida"]<=0:
            self.naturalDefenseInd["Vida"]=1
            
        if self.naturalDefenseInd["Sigilo"]<=0:
            self.naturalDefenseInd["Sigilo"]=0
            
        if self.naturalDefenseInd["Percepcion_de_mundo"]<=0:
            self.naturalDefenseInd["Percepcion_de_mundo"]=1

        if int(self.naturalDefenseInd["Armadura"])<0:
            self.naturalDefenseInd["Armadura"]=0            
        if int(self.naturalDefenseInd["Armadura_debil"])<0:
            self.naturalDefenseInd["Armadura_debil"]=0
        if int(self.naturalDefenseInd["Armadura_fuerte_porciento"])>90:
            self.naturalDefenseInd["Armadura_fuerte_porciento"]=90
        if int(self.naturalDefenseInd["Armadura_fuerte_porciento"])<10:
            self.naturalDefenseInd["Armadura_fuerte_porciento"]=10  
            
        if int(self.naturalDefenseInd["Crit_chance_increase"])<0:
            self.naturalDefenseInd["Crit_chance_increase"]=0
        if int(self.naturalDefenseInd["Crit_chance_increase"])>100:
            self.naturalDefenseInd["Crit_chance_increase"]=100
            
        if int(self.naturalDefenseInd["Bleed_chance"])<0:
            self.naturalDefenseInd["Bleed_chance"]=0
        if int(self.naturalDefenseInd["Bleed_chance"])>100:
            self.naturalDefenseInd["Bleed_chance"]=100
            
        if self.naturalDefenseInd["Bleed_damage"]<=0:
            self.naturalDefenseInd["Bleed_damage"]=1
        if self.naturalDefenseInd["Bleed_damage"]>=90:
            self.naturalDefenseInd["Bleed_damage"]=90
            
        if int(self.naturalDefenseInd["Slow_chance"])<0:
            self.naturalDefenseInd["Slow_chance"]=0
        if int(self.naturalDefenseInd["Slow_chance"])>100:
            self.naturalDefenseInd["Slow_chance"]=100 
            
        if self.naturalDefenseInd["Slow_done"]<=0:
            self.naturalDefenseInd["Slow_done"]=1
            
        if self.naturalDefenseInd["Velocidad_agua"]<=0:
            self.naturalDefenseInd["Velocidad_agua"]=0
        #if self.naturalDefenseInd["Velocidad_aire"]<0:
        #    self.naturalDefenseInd["Velocidad_aire"]=0
        #if self.naturalDefenseInd["Velocidad_tierra"]<0:
        #    self.naturalDefenseInd["Velocidad_tierra"]=0
            
        if self.naturalDefenseInd["Edad_de_madurez_sexual_en_dias"]<10:
            self.naturalDefenseInd["Edad_de_madurez_sexual_en_dias"]=10
        if self.naturalDefenseInd["Tiempo_de_gestacion"]<10:
            self.naturalDefenseInd["Tiempo_de_gestacion"]=10
        if self.naturalDefenseInd["Tiempo_entre_reproducccion"]<1:
            self.naturalDefenseInd["Tiempo_entre_reproducccion"]=1
            
        if self.naturalDefenseInd["Tiempo_de_vida_en_dias"]<1:
            self.naturalDefenseInd["Tiempo_de_vida_en_dias"]=1
            
        if self.naturalDefenseInd["Cantidad_de_energia_dropeada"]<1:
            self.naturalDefenseInd["Cantidad_de_energia_dropeada"]=1
        if self.naturalDefenseInd["Cantidad_de_energia_necesaria"]<1:
            self.naturalDefenseInd["Cantidad_de_energia_necesaria"]=1
        if self.naturalDefenseInd["Cantidad_de_energia_almacenable"]<1:
            self.naturalDefenseInd["Cantidad_de_energia_almacenable"]=1
        if self.naturalDefenseInd["Nivel_de_Hambre"]<1:
            self.naturalDefenseInd["Nivel_de_Hambre"]=1
            
    #este metodo se encarga de la reproduccion
    def breed(self,mate=None):
        #caso en q la reproduccion es asexual y tiene un solo padre
        currentSpicie=self.especie
        if currentSpicie.basicInfo["Tipo_de_reproduccion"]=="asexual":
            self.clonateIndividual()
        elif currentSpicie.basicInfo["Tipo_de_reproduccion"]=="sexual":
            self.sexualReproduction(mate)
    
    #este metodo simplemente clona al individuo    
    def clonateIndividual(self):
        currentSpicie=self.especie
        lastNumber=int(currentSpicie.basicInfo["Ultimo_numero"])
        
        newName=str(self.especie.basicInfo["name"]) +"$"+str(int(lastNumber)+1)
        #def __init__(self,xMundo,yMundo,especie,name,varianza=None):
        newIndividual=Individuo(self.xMundo,self.yMundo,self.especie,newName,0)
        
        currentSpicie.individuos[newName]=newIndividual
        currentSpicie.basicInfo["Ultimo_numero"]=str(lastNumber+1)
    
    #este metodo crea un nuevo individuo promedio de los dos padres
    def sexualReproduction(self,mate):
        dicPromedyDefenses=misc.dictPromed(self.naturalDefenseInd,mate.naturalDefenseInd)
        
        currentSpicie=self.especie
        lastNumber=int(currentSpicie.basicInfo["Ultimo_numero"])
        
        newName=str(self.especie.basicInfo["name"])+"$"+str(int(lastNumber)+1)
        #def __init__(self,xMundo,yMundo,especie,name,varianza=None):
        newIndividual=Individuo(self.xMundo,self.yMundo,self.especie,newName,1,dicPromedyDefenses)
        
        currentSpicie.individuos[newName]=newIndividual
        currentSpicie.basicInfo["Ultimo_numero"]=str(lastNumber+1)
                                    #move
    #############################################################################
    #movimiento del individuo
    def move(self,mapa):
        #aca se valorara segun que criterio moverse
        tup=()
        
        previusX=self.xMundo
        previusY=self.yMundo
        #por ahora solo nos movemos random
        if self.naturalDefenseInd["Inteligencia"]<2:
            tup=self.moveRandom(mapa["Tile"])
            self.xMundo+=tup[0]
            self.yMundo+=tup[1]
            globals.worldMap.udpdateIndividual(self,previusX,previusY)
            print("Yo "+self.name+" me movi hacia "+str(self.xMundo) +","+str(self.yMundo)+"")
        else:
            #tempDic=globals.worldMap.movementMatrix(self)   
            #pathFinder(currentIndividual,foodMatrix,dangerMatrix,mateMatrix,especiesMatrix):
            die=misc.pathFinder(self,mapa) 
            
        

        
        
        
    
    def moveRandom(seflf,myMap):
        #ausmiendo que el mapa es cuadrado y el individuo esta en la posicion central
        myPosition=int(len(list(myMap))/2)
        i=10
        while i>0:
            xRandom=random.randint(-1,1)
            yRandom=random.randint(-1,1)
            if myMap[xRandom+myPosition][yRandom+myPosition]!=globals.voidValue:
                break
            i-=1
            #caso donde no se mueve
            if i==0:
                xRandom=0
                yRandom=0
        return (xRandom,yRandom)  


###########################################################################################


####################################feed###################################################

    def eat(self):
        eatSuccess=True
        listDestroy=[]
        for resource in globals.worldMap.Tiles[self.xMundo][self.yMundo].ComponentsDict:
            if self.saciedad>=self.naturalDefenseInd["Cantidad_de_energia_almacenable"]:
                break
            ##################################
            #cosumiendo energia
            #self.saciedad=int(self.saciedad)-int(self.especie.naturalDefense["Cantidad_de_energia_necesaria"])
            #revisando el hambre de la especie
            #hambre=int(self.especie.naturalDefense["Nivel_de_Hambre"]) 
            ###################################################
            
            neededFood= int(self.naturalDefenseInd["Cantidad_de_energia_almacenable"])-int(self.saciedad)

            if resource in self.especie.alimentos:
                if resource=="Cazador":
                    prey= misc.FindPrey(self)
                    
                    combatResult=misc.fullCombat(self,prey)
                    if combatResult==0:
                        print(self.name+" intento cazar a "+prey.name+" y lo consiguio")
                        if int(prey.naturalDefenseInd["Cantidad_de_energia_almacenable"])//3>1+neededFood//int(self.especie.alimentos[resource]):
                            print(self.name+" se comio a "+prey.name+" y se lleno")
                            self.saciedad=int(self.naturalDefenseInd["Cantidad_de_energia_almacenable"])
                            prey.die()
                            break
                        else:
                            print(self.name+" se comio a "+prey.name+" pero pero no se lleno")
                            self.saciedad+=int(self.especie.alimentos[resource])*(int(prey.naturalDefenseInd["Cantidad_de_energia_almacenable"])//3)
                            prey.die()
                    elif combatResult==1:
                        print(self.name+" intento cazar a "+prey.name+" y murio")
                        if  "cazador" in prey.especie.alimentos:
                            
                            preyNeededFood=int(prey.naturalDefenseInd["Cantidad_de_energia_almacenable"])-int(prey.saciedad)
                            if int(self.naturalDefenseInd["Cantidad_de_energia_almacenable"])//3>1+preyNeededFood//int(prey.especie.alimentos[resource]):
                                print(prey.name+" comio a "+self.name+" y se lleno")
                                prey.saciedad=int(prey.naturalDefenseInd["Cantidad_de_energia_almacenable"])
                                
                            else:
                                print(prey.name+" comio a "+self.name+" y no se lleno")
                                prey.saciedad+=int(prey.especie.alimentos[resource])*(int(self.naturalDefenseInd["Cantidad_de_energia_almacenable"])//3)
                    
                        self.die()
                        eatSuccess=False
                        break
                    
                    #la presa escapo
                    elif combatResult==2:
                        print(self.name+" intento cazar a "+prey.name+" pero se le escapo")
                        continue
                
                else:
                    #aca revisa si hay suficiente para saciarse con este elemento y si es asi manda a eliminar esa cantidad al mapa mientras come
                    if int(globals.worldMap.Tiles[self.xMundo][self.yMundo].ComponentsDict[resource])>1+neededFood//int(self.especie.alimentos[resource]):
                        listDestroy.append((resource,1+neededFood/(int(self.especie.alimentos[resource]))))
                        self.saciedad=int(self.naturalDefenseInd["Cantidad_de_energia_almacenable"])

                        break
                
                    #en este caso no hay suficiente por lo q tiene q seguir buscando recursos despues de comerse todo lo q hay
                    else:
                        self.saciedad+=globals.worldMap.Tiles[self.xMundo][self.yMundo].ComponentsDict[resource]*int(self.alimentos[resource])
                        listDestroy.append((resource,int(globals.worldMap.Tiles[self.xMundo][self.yMundo].ComponentsDict[resource])))

        #comprobando si ya esta lleno
            if int(self.saciedad) >= int(self.naturalDefenseInd["Cantidad_de_energia_almacenable"]):
                self.saciedad=int(self.naturalDefenseInd["Cantidad_de_energia_almacenable"])
        
        
        
        for item in listDestroy:
            print("Yo "+self.name+" me comi "+str(int(item[1]))+" unidades de "+str(item[0]))
            #globals.worldMap.Tiles[self.xMundo][self.yMundo].eliminate(item[0],item[1])
        return eatSuccess
###########################################################################################

    #en este metodo se decidira lo que hara el individuos 
    def resolveIteration(self,map):
        mySpecie=self.especie
        #cosumiendo energia
        self.saciedad=str(int(self.saciedad)-int(mySpecie.naturalDefense["Cantidad_de_energia_necesaria"]))
        #revisando el hambre de la especie
        hambre=int(mySpecie.naturalDefense["Nivel_de_Hambre"]) 

        #move del individuos
        if int(self.saciedad)<=int(hambre):
            #caso especial de Alfie
            if mySpecie.basicInfo["Tipo_de_alimentacion"]=="entorno":
                self.saciedad=str(int(self.saciedad)+1)
            if mySpecie.basicInfo["Tipo_de_alimentacion"]=="element":
                eatSucces=self.eat()
                if not eatSucces:
                    return
                        
        self.move(map)
                
        #reproduccion del individuo
        if self.giveMeRealAge()-int(self.naturalDefenseInd["Edad_de_madurez_sexual_en_dias"])>=0:
            if self.giveMeRealAge()- int(self.lastReproduction)>int(self.naturalDefenseInd["Tiempo_entre_reproducccion"]):
                if self.especie.basicInfo["Tipo_de_reproduccion"]=="asexual":
                    self.lastReproduction=self.giveMeRealAge()
                    self.breed()                    
                elif self.especie.basicInfo["Tipo_de_reproduccion"]=="sexual" and self.sexo==int(1):
                    for item in globals.worldMap.Tiles[self.xMundo][self.yMundo].CreatureList:
                        if item.sexo==int(0):
                            if item.giveMeRealAge()-int(item.naturalDefenseInd["Edad_de_madurez_sexual_en_dias"])>=0 and self.giveMeRealAge()- int(item.lastReproduction)>int(item.naturalDefenseInd["Tiempo_entre_reproducccion"]):
                                self.lastReproduction=self.giveMeRealAge()
                                item.lastReproduction=self.giveMeRealAge()
                                self.breed(item)
                                break                                                      
        
        
        #actualizacion de edad del individuo                
        self.edad=int(self.edad)-1
        if int(self.edad)==0:
            self.die()
    
    def giveMeRealAge(self):
        return int(self.naturalDefenseInd["Tiempo_de_vida_en_dias"]) - int(self.edad)
        
    def die(self):
        globals.deadIndividuals.append(self.name)
        self.especie.basicInfo["Cantidad_de_miembros"]=int(self.especie.basicInfo["Cantidad_de_miembros"])-1
        
        #######AQUI INTENTAS ELIMINAR A ALGUIEN QUE YA NO EXISTE
        #######ESTA ES UNA SOLUCIÓN TEMPORAL
        if self.name in self.especie.individuos.keys():
            del self.especie.individuos[self.name]
        #matar en casilla de mapa
        if self in globals.worldMap.Tiles[self.xMundo][self.yMundo].CreatureList:
            globals.worldMap.Tiles[self.xMundo][self.yMundo].CreatureList.remove(self)
        
        if self.naturalDefenseInd["Inteligencia"]<2:        
            count=0
            #for tile in globals.worldMap.Tiles:
            #    for i in range(len(tile)):
            #        for creature in tile[i].CreatureList:
            #            if creature.name==self.name:
            #                count+=1
            #print(count)
        
