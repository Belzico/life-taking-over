import random
import globals



#clase especies
#una especie es un vector donde en cada posicion se llevaran distinatas propiedades de la especie,
#ejemplo en la posicion i puede guardarse la temperatura maxima que puede resistir.
class Especies():
    
    
    
    def __init__(self,basicInfo,naturalDefense,resistenciaElemental,individuos,x=None,y=None):
        if "name" in basicInfo:
            pass
        else:
            
            #datos como el tiempo de vida, tipo de alimentacion...etc
            self.basicInfo={}
            #datos como partes de veneno, piel dura, colmillos afilados...etc
            #esto sera utilizado en lucha entre especies
            self.naturalDefense={}
            #datos para saber que tan resistente a algun elemento es...etc
            self.resistenciaElementa={}
            #lisa de tidos los individuos de la especie
            self.individuos={}
            #lista de elementos de donde puede sacar parte de la energix
            self.alimentos={}
        
            #llamada al generador
            self.especieGenerator(x,y,individuos)

    #aca generaremos especies siguiendo algunos criterios pero de forma aleatoria
    def especieGenerator(self,X,Y,size):
        self.basicInfo=Especies.basicInfoGenerator()
        
        self.individuos=Especies.listaIndividuosGenerator(self.basicInfo["Cantidad_de_miembros"],self.basicInfo["name"])
        self.naturalDefense=Especies.naturalDefenseGenerator()
        self.resistenciaElemental=Especies.resistenciasElementalesGenerator()
    
    def listaIndividuosGenerator(miembros,name,energy,vida):
        individuals={}
        i=0
        
        while(i<miembros):
            #(self,xMundo,yMundo,xZona,yZona,sexo,edad,especie,saciedad, name,vida):
            individuals[""+name+""+i+""]=Individuo(0,0,0,0,0,0,name,energy,i,vida)
            i+=1
        #empezaran en las coordenadas 0,0,0,0
        
        return individuals
    
    
    def basicInfoGenerator():
        basicInfo={}
        #nombrar la especie
        name=""+globals.lastNameSpecie+1++"$"
        basicInfo["name"]=name
        globals.lastNameSpecie+=1
        #dos tipos unicelular y pluricelular
        basicInfo["Tipo_de_celula"]="unicelular"
        #por definir, por ahora asexual y sexual entre 2 individuos de distinto sexo
        basicInfo["Tipo_de_reproduccion"]="asexual"
        temporalMiembros=""+random.randint(2,9)+""
        basicInfo["Cantidad_de_miembros"]=temporalMiembros
        basicInfo["Edad_de_madurez_sexual_en_dias"]=""+random.randint(20,31)+""
        basicInfo["Tiempo_de_gestacion"]=""+random.randint(20,31)+""
        #cuantos hijos por reproduccion puede consebir por reproduccion
        basicInfo["Cantidad_de_hijos"]="1"
        basicInfo["Tiempo_de_vida_en dias"]=""+random.randint(50,101)+""
        #por definir, por ahora seran dos opciones, alimentarse del entorno(aire, minerales) o alimentarse de otro individuo o los restos de este
        basicInfo["Tipo_de_alimentacion"]="entorno"
        #cuanta energia daran al que los mate y se alimente de ellos
        basicInfo["Cantidad_de_energia_dropeada"]=""+random.randint(1,4)+""
        #cantidad de energia diaria requerida por individuo
        temporalEnergy=""+random.randint(1,4)+""
        basicInfo["Cantidad_de_energia_necesaria"]=temporalEnergy
        #cantidad de energia que pueden almacenar maxima
        basicInfo["Cantidad_de_energia_almacenable"]=""+int(temporalEnergy)+random.randint(1,4)+""
        #cantidad de energia almacenada a partir de la cual le da hambre
        basicInfo["Nivel_de_Hambre"]=3
        #cantidad de casillas que puede recorrer en un dia en el agua
        basicInfo["Velocidad_agua"]=""+random.randint(0,1)+""
        #cantidad de casillas que puede recorrer en un dia en volando
        basicInfo["Velocidad_agua"]=""+random.randint(0,1)+""
        #cantidad de casillas que puede recorrer en un dia en la tierra
        basicInfo["Velocidad_agua"]=""+random.randint(0,1)+""
        #el ultimo numero para nombrar al siguiente individuo
        basicInfo["Ultimo_numero"]=""+temporalMiembros+""
        #generamos los individuos
        
        return basicInfo
    
    def naturalDefenseGenerator():
        naturalDefense={}
        #vida maxima del individuo
        naturalDefense["Vida"]=""+random.randint(5,11)+""
        #la percepcion no es mas que cuantas casillas sin contar en la que esta es capaz de ver/oir...etc el individuo
        naturalDefense["Percepcion_de_mundo"]="1"
        #la inteligencia es un factor que puede influir en varios campos
        naturalDefense["Inteligencia"]="0"
        #factor que indica que tan sigiloso puede llegar a ser un individuo en un combate
        naturalDefense["Sigilo"]=0
        #armadura que indica que tan dura es la piel del individuo
        armor=random.randint(1,4)
        naturalDefense["Armadura"]=""+armor+""
        #armadura en zona debil ej: la parte de abajo de los cocodrilos es suave contrario a la espalda
        naturalDefense["Armadura_debil"]=str(int(armor/random.randint(0,armor)))
        #porciento de armadura fuerte del cuerpo
        naturalDefense["Armadura_debil_porciento"]=""+random.randint(0,51) +""
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
        return naturalDefense
        
    def resistenciasElementalesGenerator():
        resistenciasElementales={}
        return resistenciasElementales
    


class Individuo():
    def __init__(self,xMundo,yMundo,xZona,yZona,sexo,edad,especie,saciedad, name,vida):
        #coordenadas
        self.xMundo=xMundo
        self.yMundo=yMundo
        self.xZona=xZona
        self.yZona=yZona
        #la cantidad de energia con la que empiezan
        self.saciedad=saciedad
        #string con el nombre de la especie
        self.especie=especie
        #sexo del individuo, en caso de ser asexual sera por defecto cero
        self.sexo=sexo
        #Fecha en la que muere, (la edad sera la resta con la fecha actual)
        #la muerte se debera tratar de forma lazy, x cada iteracion no hay q actualizar, 
        #solo en kso de que sea necesario
        self.edad=edad
        #nombre del individuos
        self.name=name
        self.vida=vida    
    
        #agregando aa la casilla
        globals.worldMap.IsBorn(self)
        #agregando a la lista de individuos global    
        globals.worldIndividuals[self.name]=self
     
    #este sera el metodo encargado de reproducir a un individuo, y de el se derivara a los distintos tipos de reproduccion   
    def breed(self):
        currentSpicie=globals.allSpecies[self.especie]
        if currentSpicie.basicInfo["Tipo_de_reproduccion"]=="asexual":
            self.clonateIndividual()
    
    #este metodo simplemente clona al individuo    
    def clonateIndividual(self):
        currentSpicie=globals.allSpecies[self.especie]
        lastNumber=int(currentSpicie.basicInfo["Ultimo_numero"])
        newIndividual=Individuo(self.xMundo,self.yMundo,self.xZona,self.yZona,self.sexo,0,self.especie,currentSpicie.basicInfo["Cantidad_de_energia_almacenable"])
        newName=self.especie+str(lastNumber+1)
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
        
        print("me movi hacia "+str(self.xMundo) +","+str(self.yMundo)+"")
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


    #en este metodo se decidira lo que hara el individuos 
    def resolveIteration(self,map):
        mySpecie=globals.allSpecies[self.especie]
        #cosumiendo energia
        self.saciedad=str(int(self.saciedad)-int(mySpecie.basicInfo["Cantidad_de_energia_necesaria"]))
        #revisando el hambre de la especie
        hambre=int(mySpecie.basicInfo["Cantidad_de_energia_necesaria"]) 
        if int(self.saciedad)<=int(hambre):
            #caso especial de Alfie
            if mySpecie.basicInfo["Tipo_de_alimentacion"]=="entorno":
                self.saciedad=str(int(self.saciedad)+1)
                
                self.move(map)
                return
            

        
        
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
        basicInfo["Tiempo_de_vida_en dias"]="100"
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