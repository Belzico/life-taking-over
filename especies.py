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
        self.basicInfo=Especies.basicInfoGenerator()
        
        

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
    
    
    def basicInfoGenerator():
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
        temporalMiembros=str(random.randint(2,9))
        basicInfo["Cantidad_de_miembros"]=temporalMiembros

        #por definir, por ahora seran dos opciones, alimentarse del entorno(aire, minerales) o alimentarse de otro individuo o los restos de este
        basicInfo["Tipo_de_alimentacion"]="element"
        #sexo del individuo
        basicInfo["Sexo"]="0"
        #el ultimo numero para nombrar al siguiente individuo
        basicInfo["Ultimo_numero"]=str(temporalMiembros)
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
        naturalDefense["Armadura_debil_porciento"]=str(random.randint(0,51))
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
        naturalDefense["Velocidad_agua"]=str(random.randint(0,1))
        #cantidad de casillas que puede recorrer en un dia en volando
        naturalDefense["Velocidad_aire"]=str(random.randint(0,1))
        #cantidad de casillas que puede recorrer en un dia en la tierra
        naturalDefense["Velocidad_tierra"]=str(random.randint(0,1))
        
        naturalDefense["Edad_de_madurez_sexual_en_dias"]=str(random.randint(20,31))
        naturalDefense["Tiempo_de_gestacion"]=str(random.randint(20,31))
        
        #cuantos hijos por reproduccion puede consebir por reproduccion
        naturalDefense["Cantidad_de_hijos"]="1"
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
        self.naturalDefense=copy.deepcopy(father.naturalDefense)
        self.resistenciaElemental=copy.deepcopy(father.resistenciaElemental)
        self.alimentos=copy.deepcopy(father.alimentos)
        self.nextName=copy.deepcopy(father.individuos)
        
        self.basicInfo["name"]=int(globals.lastNameSpecie)
        globals.lastNameSpecie=int(globals.lastNameSpecie)+1
        
        #chance de evolucionar a pluricelular
        if self.basicInfo["Tipo_de_celula"]=="unicelular":
            tempRandom=random.randint(0,101)
            if tempRandom>200:
                self.basicInfo["Tipo_de_celula"]=="pluricelular"
        
        #chance de evolucionar a reproduccion sexual
        if self.basicInfo["Tipo_de_reproduccion"]=="asexual":
            tempRandom=random.randint(0,101)
            if tempRandom>80:
                self.basicInfo["Tipo_de_celula"]=="sexual"        
        
        #varianza de las especies
        varianza=paramsDic["Varianza"]
        self.individuos=self.listaIndividuosGenerator(paramsDic["x"] ,paramsDic["y"],paramsDic["Individuos"],varianza)
        
        
        


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
            self.sexo=random.randint(0,2)
        #Fecha en la que muere, (la edad sera la resta con la fecha actual)
        #la muerte se debera tratar de forma lazy, x cada iteracion no hay q actualizar, 
        #solo en kso de que sea necesario
        self.edad=especie.naturalDefense["Tiempo_de_vida_en_dias"]
        #nombre del individuos
        self.name=name

        self.lastReproduction=""
        #agregando aa la casilla
        globals.worldMap.IsBorn(self)
        
        #agregando a la lista de individuos global    
        #globals.worldIndividuals[self.name]=self
        globals.bornIndividuals.append((self.name,self))
        
        #lista con las defensas naturales del individuo simulando que no todos son iwales
        self.naturalDefenseInd={}
        
        if father==0:
            self.naturalDefenseGeneratorInd(especie.naturalDefense,varianza)
        elif father==0:
            self.naturalDefenseGeneratorInd(varianza)
    
    
    #este sera el metodo encargado de reproducir a un individuo, y de el se derivara a los distintos tipos de reproduccion   
    def naturalDefenseGeneratorInd(self,defences,varianza=None):
        

        self.naturalDefenseInd["Vida"]=int(defences["Vida"])+random.randint(-1,2)
        self.naturalDefenseInd["Percepcion_de_mundo"]=int(defences["Percepcion_de_mundo"])+random.randint(-1,2)
        self.naturalDefenseInd["Inteligencia"]=int(defences["Inteligencia"])+random.randint(-1,2)
        self.naturalDefenseInd["Sigilo"]=int(defences["Sigilo"])+random.randint(-1,2)
        self.naturalDefenseInd["Armadura"]=int(defences["Armadura"])+random.randint(-1,2)
        self.naturalDefenseInd["Armadura_debil"]=int(defences["Armadura_debil"])+random.randint(-1,2)
        self.naturalDefenseInd["Armadura_debil_porciento"]=int(defences["Armadura_debil_porciento"])+random.randint(-1,2)
        self.naturalDefenseInd["Crit_chance_increase"]=int(defences["Crit_chance_increase"])+random.randint(-1,2)
        self.naturalDefenseInd["Bleed_chance"]=int(defences["Bleed_chance"])+random.randint(-1,2)
        self.naturalDefenseInd["Crit_chance_increase"]=int(defences["Crit_chance_increase"])+random.randint(-1,2)
        self.naturalDefenseInd["Bleed_damage"]=int(defences["Bleed_damage"])+random.randint(-1,2)
        self.naturalDefenseInd["Slow_chance"]=int(defences["Slow_chance"])+random.randint(-1,2)
        self.naturalDefenseInd["Slow_done"]=int(defences["Slow_done"])+random.randint(-1,2)
        self.naturalDefenseInd["Velocidad_agua"]=int(defences["Velocidad_agua"])+random.randint(-1,2)
        self.naturalDefenseInd["Velocidad_aire"]=int(defences["Velocidad_aire"])+random.randint(-1,2)
        self.naturalDefenseInd["Velocidad_tierra"]=int(defences["Velocidad_tierra"])+random.randint(-1,2)
        self.naturalDefenseInd["Edad_de_madurez_sexual_en_dias"]=int(defences["Edad_de_madurez_sexual_en_dias"])+random.randint(-1,2)
        self.naturalDefenseInd["Tiempo_de_gestacion"]=int(defences["Tiempo_de_gestacion"])+random.randint(-1,2)
        self.naturalDefenseInd["Cantidad_de_hijos"]=int(defences["Cantidad_de_hijos"])+random.randint(-1,2)
        self.naturalDefenseInd["Tiempo_de_vida_en_dias"]=int(defences["Tiempo_de_vida_en_dias"])+random.randint(-1,2)        
        self.naturalDefenseInd["Cantidad_de_energia_dropeada"]=int(defences["Vida"])
        self.naturalDefenseInd["Cantidad_de_energia_necesaria"]=1+int(defences["Vida"])/5
        self.naturalDefenseInd["Cantidad_de_energia_almacenable"]=1+3*int(defences["Vida"])/5
        self.naturalDefenseInd["Nivel_de_Hambre"]=1+2*int(self.naturalDefenseInd["Vida"])/3


        if varianza!=None:
            self.naturalDefenseInd["Vida"]=int(self.naturalDefenseInd["Vida"])+int(random.randint(int(varianza["Vida"]),int(varianza["Vida"])))
            self.naturalDefenseInd["Percepcion_de_mundo"]=int(self.naturalDefenseInd["Percepcion_de_mundo"])+int(random.randint(int(varianza["Percepcion_de_mundo"]),int(varianza["Percepcion_de_mundo"])))
            self.naturalDefenseInd["Inteligencia"]=int(self.naturalDefenseInd["Inteligencia"])+int(random.randint(int(varianza["Inteligencia"]),int(varianza["Inteligencia"])))
            self.naturalDefenseInd["Sigilo"]=int(self.naturalDefenseInd["Sigilo"])+int(random.randint(int(varianza["Sigilo"]),int(varianza["Sigilo"])))
            self.naturalDefenseInd["Armadura"]=int(self.naturalDefenseInd["Armadura"])+int(random.randint(int(varianza["Armadura"]),int(varianza["Armadura"])))
            self.naturalDefenseInd["Armadura_debil"]=int(self.naturalDefenseInd["Armadura_debil"])+int(random.randint(int(varianza["Armadura_debil"]),int(varianza["Armadura_debil"])))
            self.naturalDefenseInd["Armadura_debil_porciento"]=int(self.naturalDefenseInd["Armadura_debil_porciento"])+int(random.randint(int(varianza["Armadura_debil_porciento"]),int(varianza["Armadura_debil_porciento"])))
            self.naturalDefenseInd["Crit_chance_increase"]=int(self.naturalDefenseInd["Crit_chance_increase"])+int(random.randint(int(varianza["Crit_chance_increase"]),int(varianza["Crit_chance_increase"])))
            self.naturalDefenseInd["Bleed_chance"]=int(self.naturalDefenseInd["Bleed_chance"])+int(random.randint(int(varianza["Bleed_chance"]),int(varianza["Bleed_chance"])))
            self.naturalDefenseInd["Crit_chance_increase"]=int(self.naturalDefenseInd["Crit_chance_increase"])+int(random.randint(int(varianza["Crit_chance_increase"]),int(varianza["Crit_chance_increase"])))
            self.naturalDefenseInd["Bleed_damage"]=int(self.naturalDefenseInd["Bleed_damage"])+int(random.randint(int(varianza["Bleed_damage"]),int(varianza["Bleed_damage"])))
            self.naturalDefenseInd["Slow_chance"]=int(self.naturalDefenseInd["Slow_chance"])+int(random.randint(int(varianza["Slow_chance"]),int(varianza["Slow_chance"])))
            self.naturalDefenseInd["Slow_done"]=int(self.naturalDefenseInd["Slow_done"])+int(random.randint(int(varianza["Slow_done"]),int(varianza["Slow_done"])))
            self.naturalDefenseInd["Velocidad_agua"]=int(self.naturalDefenseInd["Velocidad_agua"])+int(random.randint(int(varianza["Velocidad_agua"]),int(varianza["Velocidad_agua"])))
            self.naturalDefenseInd["Velocidad_aire"]=int(self.naturalDefenseInd["Velocidad_aire"])+int(random.randint(int(varianza["Velocidad_aire"]),int(varianza["Velocidad_aire"])))
            self.naturalDefenseInd["Velocidad_tierra"]=int(self.naturalDefenseInd["Velocidad_tierra"])+int(random.randint(int(varianza["Velocidad_tierra"]),int(varianza["Velocidad_tierra"])))
            self.naturalDefenseInd["Edad_de_madurez_sexual_en_dias"]=int(self.naturalDefenseInd["Edad_de_madurez_sexual_en_dias"])+int(random.randint(int(varianza["Edad_de_madurez_sexual_en_dias"]),int(varianza["Edad_de_madurez_sexual_en_dias"])))
            self.naturalDefenseInd["Tiempo_de_gestacion"]=int(self.naturalDefenseInd["Tiempo_de_gestacion"])+int(random.randint(int(varianza["Tiempo_de_gestacion"]),int(varianza["Tiempo_de_gestacion"])))
            self.naturalDefenseInd["Cantidad_de_hijos"]=int(self.naturalDefenseInd["Cantidad_de_hijos"])+int(random.randint(int(varianza["Cantidad_de_hijos"]),int(varianza["Cantidad_de_hijos"])))
            self.naturalDefenseInd["Tiempo_de_vida_en_dias"]=int(self.naturalDefenseInd["Tiempo_de_vida_en_dias"])+int(random.randint(int(varianza["Tiempo_de_vida_en_dias"]),int(varianza["Tiempo_de_vida_en_dias"])))
            self.naturalDefenseInd["Cantidad_de_energia_dropeada"]=int(self.naturalDefenseInd["Vida"])
            self.naturalDefenseInd["Cantidad_de_energia_necesaria"]=1+(int(self.naturalDefenseInd["Vida"]))/5
            self.naturalDefenseInd["Cantidad_de_energia_almacenable"]=1+3*(int(self.naturalDefenseInd["Vida"]))/5
            self.naturalDefenseInd["Nivel_de_Hambre"]=2*int(self.naturalDefenseInd["Vida"])/3


        
        
        
        if self.naturalDefenseInd["Vida"]<=0:
            self.naturalDefenseInd["Vida"]=1
            
        if self.naturalDefenseInd["Percepcion_de_mundo"]<=0:
            self.naturalDefenseInd["Percepcion_de_mundo"]=1
            
        if int(self.naturalDefenseInd["Armadura_debil_porciento"])<0:
            self.naturalDefenseInd["Armadura_debil_porciento"]=0
        if int(self.naturalDefenseInd["Armadura_debil_porciento"])>100:
            self.naturalDefenseInd["Armadura_debil_porciento"]=100 
            
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
            
        if int(self.naturalDefenseInd["Slow_chance"])<0:
            self.naturalDefenseInd["Slow_chance"]=0
        if int(self.naturalDefenseInd["Slow_chance"])>100:
            self.naturalDefenseInd["Slow_chance"]=100 
            
        if self.naturalDefenseInd["Slow_done"]<=0:
            self.naturalDefenseInd["Slow_done"]=1
            
        if self.naturalDefenseInd["Velocidad_agua"]<=0:
            self.naturalDefenseInd["Velocidad_agua"]=0
        if self.naturalDefenseInd["Velocidad_aire"]<0:
            self.naturalDefenseInd["Velocidad_aire"]=0
        if self.naturalDefenseInd["Velocidad_tierra"]<0:
            self.naturalDefenseInd["Velocidad_tierra"]=0
            
        if self.naturalDefenseInd["Edad_de_madurez_sexual_en_dias"]<20:
            self.naturalDefenseInd["Edad_de_madurez_sexual_en_dias"]=20
        if self.naturalDefenseInd["Tiempo_de_gestacion"]<20:
            self.naturalDefenseInd["Tiempo_de_gestacion"]=20
        if self.naturalDefenseInd["Cantidad_de_hijos"]<1:
            self.naturalDefenseInd["Cantidad_de_hijos"]=1
            
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
            pass
    
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
        
        newName=self.especie.basicInfo["name"]+"$"+str(lastNumber+1)
        #def __init__(self,xMundo,yMundo,especie,name,varianza=None):
        newIndividual=Individuo(self.xMundo,self.yMundo,self.especie,newName,1,dicPromedyDefenses)
        
        currentSpicie.individuos[newName]=newIndividual
        currentSpicie.basicInfo["Ultimo_numero"]=str(lastNumber+1)
                                     #move
    #############################################################################
    #movimiento del individuo
    def move(self,map):
        #aca se valorara segun que criterio moverse
        tup=()
        #por ahora solo nos movemos random
        if True:
            tup=self.moveRandom(map)
            
        previusX=self.xMundo
        previusY=self.yMundo
        self.xMundo+=tup[0]
        self.yMundo+=tup[1]
        
        print("Yo "+self.name+" me movi hacia "+str(self.xMundo) +","+str(self.yMundo)+"")
        globals.worldMap.udpdateIndividual(self,previusX,previusY)
    
    def moveRandom(seflf,myMap):
        #ausmiendo que el mapa es cuadrado y el individuo esta en la posicion central
        myPosition=int(len(list(myMap))/2)
        i=10
        while i>0:
            xRandom=random.randint(-1,1)
            yRandom=random.randint(-1,1)
            if myMap[xRandom+myPosition][yRandom+myPosition]!="":
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
        listDestroy=[]
        for resource in globals.worldMap.Tiles[self.xMundo][self.yMundo].ComponentsDict:
            
            ##################################
            #cosumiendo energia
            #self.saciedad=int(self.saciedad)-int(self.especie.naturalDefense["Cantidad_de_energia_necesaria"])
            #revisando el hambre de la especie
            #hambre=int(self.especie.naturalDefense["Nivel_de_Hambre"]) 
            ###################################################
            
            neededFood= int(self.naturalDefenseInd["Cantidad_de_energia_almacenable"])-int(self.saciedad)
           
            if resource in self.especie.alimentos:
                #aca revisa si hay suficiente para saciarse con este elemento y si es asi manda a eliminar esa cantidad al mapa mientras come
                if int(globals.worldMap.Tiles[self.xMundo][self.yMundo].ComponentsDict[resource])>1+neededFood/int(self.especie.alimentos[resource]):
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
            globals.worldMap.Tiles[self.xMundo][self.yMundo].eliminate((item[0],item[1]))
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
               self.eat()
                        
            self.move(map)
                
        #reproduccion del individuo
        if int(int(mySpecie.naturalDefense["Tiempo_de_vida_en_dias"])-int(mySpecie.naturalDefense["Edad_de_madurez_sexual_en_dias"]))>=int(self.edad):
                fixEdad=int(self.especie.naturalDefense["Tiempo_de_vida_en_dias"])-int(self.edad)
                reproduccionCicle=(int(self.especie.naturalDefense["Tiempo_de_vida_en_dias"])-int(self.especie.naturalDefense["Edad_de_madurez_sexual_en_dias"]))/int(self.especie.naturalDefense["Cantidad_de_hijos"])
                if fixEdad % reproduccionCicle==0:
                    if self.especie.basicInfo["Tipo_de_reproduccion"]=="asexual":
                        self.breed()                    
                    elif self.especie.basicInfo["Tipo_de_reproduccion"]=="sexual" and self.sexo==int(1):
                        for item in globals.worldMap.Tiles[self.xMundo][self.yMundo].CreatureList:
                            fixEdad=int(item.especie.naturalDefense["Tiempo_de_vida_en_dias"])-int(item.edad)
                            reproduccionCicle=(int(item.especie.naturalDefense["Tiempo_de_vida_en_dias"])-int(item.especie.naturalDefense["Edad_de_madurez_sexual_en_dias"]))/int(item.especie.naturalDefense["Cantidad_de_hijos"])       
                            if fixEdad % reproduccionCicle==0:
                                self.breed(item)
                                break                                                      
        
        
        #actualizacion de edad del individuo                
        self.edad=int(self.edad)-1
        if int(self.edad)==0:
            self.die(mySpecie)
    
        
    def die(self,mySpecie):
        globals.deadIndividuals.append(self.name)
        mySpecie.basicInfo["Cantidad_de_miembros"]=int(mySpecie.basicInfo["Cantidad_de_miembros"])-1
        
        #######AQUI INTENTAS ELIMINAR A ALGUIEN QUE YA NO EXISTE
        #######ESTA ES UNA SOLUCIÓN TEMPORAL
        if self.name in mySpecie.individuos.keys():
            del mySpecie.individuos[self.name]
        #matar en casilla de mapa
        globals.worldMap.Tiles[self.xMundo][self.yMundo].CreatureList.remove(self)
        
        
#especie inicial previa a la generacion automatica de especies
class Alfie():
    def __init__(self):
        self.basicInfo=Alfie.basicInfoGenerator()
        self.naturalDefense=Alfie.naturalDefenseGenerator()
        self.resistenciaElemental=Alfie.resistenciasElementalesGenerator()
        self.individuos=Alfie.listaIndividuosGenerator()
        
        
      
    def basicInfoGenerator():
        basicInfo={}
        basicInfo["name"]="Alfie"
        #dos tipos unicelular y pluricelular
        basicInfo["Tipo_de_celula"]="unicelular"
        #por definir, por ahora asexual y sexual entre 2 individuos de distinto sexo
        basicInfo["Tipo_de_reproduccion"]="asexual"
        basicInfo["Cantidad_de_miembros"]="4"
        basicInfo["Edad_de_madurez_sexual_en_dias"]="30"
        basicInfo["Tiempo_de_gestacion"]="20"
        #cuantos hijos por reproduccion puede consebir por reproduccion
        basicInfo["Cantidad_de_hijos"]="1"
        basicInfo["Tiempo_de_vida_en_dias"]="100"
        #por definir, por ahora seran dos opciones, alimentarse del entorno(aire, minerales) o alimentarse de otro individuo o los restos de este
        basicInfo["Tipo_de_alimentacion"]="entorno"
        #cuanta energia daran al que los mate y se alimente de ellos
        basicInfo["Cantidad_de_energia_dropeada"]="1"
        #cantidad de energia diaria requerida por individuo
        basicInfo["Cantidad_de_energia_necesaria"]="1"
        #cantidad de energia que pueden almacenar maxima
        basicInfo["Cantidad_de_energia_almacenable"]="5"
        #cantidad de energia almacenada a partir de la cual le da hambre
        basicInfo["Nivel_de_Hambre"]=3
        #cantidad de casillas que puede recorrer en un dia en el agua
        basicInfo["Velocidad_agua"]="0.5"
        #cantidad de casillas que puede recorrer en un dia en volando
        basicInfo["Velocidad_agua"]="0"
        #cantidad de casillas que puede recorrer en un dia en la tierra
        basicInfo["Velocidad_agua"]="0"
        #el ultimo numero para nombrar al siguiente individuo
        basicInfo["Ultimo_numero"]="3"
        return basicInfo
        
    def naturalDefenseGenerator():
        naturalDefense={}
        #la percepcion no es mas que cuantas casillas sin contar en la que esta es capaz de ver/oir...etc el individuo
        naturalDefense["Percepcion_de_mundo"]="0"
        return naturalDefense
        
    def resistenciasElementalesGenerator():
        resistenciasElementales={}
        return resistenciasElementales
    
    def listaIndividuosGenerator():
        individuals={}
        #empezaran en las coordenadas 0,0,0,0
        individuals["Alfie0"]=Individuo(0,0,0,0,0,0,"Alfie",3,0,5)
        individuals["Alfie1"]=Individuo(0,0,0,0,0,0,"Alfie",3,1,5)
        individuals["Alfie2"]=Individuo(0,0,0,0,0,0,"Alfie",3,2,5)
        individuals["Alfie3"]=Individuo(0,0,0,0,0,0,"Alfie",3,3,5)
        return individuals
    
    
        
        

print(3+2)      