import random
import globals



#clase especies
#una especie es un vector donde en cada posicion se llevaran distinatas propiedades de la especie,
#ejemplo en la posicion i puede guardarse la temperatura maxima que puede resistir.
class Especies():
    
    
    
    def __init__(self,basicInfo,naturalDefense,resistenciaElemental,individuos):
        #datos como el tiempo de vida, tipo de alimentacion...etc
        self.basicInfo={}
        #datos como partes de veneno, piel dura, colmillos afilados...etc
        #esto sera utilizado en lucha entre especies
        self.naturalDefense={}
        #datos para saber que tan resistente a algun elemento es...etc
        self.resistenciaElementa={}
        #lisa de tidos los individuos de la especie
        self.individuos={}

    #aca generaremos especies siguiendo algunos criterios pero de forma aleatoria
    def especieGenerator(self):
        self.basicInfo=Especies.basicInfoGenerator()
        self.individuos=Especies.listaIndividuosGenerator(self.basicInfo["Cantidad_de_miembros"],self.basicInfo["name"],self.basicInfo["Cantidad_de_energia_almacenable"])
        self.naturalDefense=Especies.naturalDefenseGenerator()
        self.resistenciaElemental=Especies.resistenciasElementalesGenerator()
    
    def listaIndividuosGenerator(miembros,name,energy):
        individuals={}
        i=0
        while(i<miembros):
            individuals[""+name+""+i+""]=Individuo(0,0,0,0,0,0,name,energy)
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
        #la percepcion no es mas que cuantas casillas sin contar en la que esta es capaz de ver/oir...etc el individuo
        naturalDefense["Percepcion_de_mundo"]="0"
        return naturalDefense
        
    def resistenciasElementalesGenerator():
        resistenciasElementales={}
        return resistenciasElementales
    



class Individuo():
    def __init__(self,xMundo,yMundo,xZona,yZona,sexo,edad,especie,saciedad):
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
        
    def move(self):
        pass
        
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
        basicInfo["Cantidad_de_energia_almacenable"]="3"
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
        individuals["Alfie0"]=Individuo(0,0,0,0,0,0,"Alfie",3)
        individuals["Alfie1"]=Individuo(0,0,0,0,0,0,"Alfie",3)
        individuals["Alfie2"]=Individuo(0,0,0,0,0,0,"Alfie",3)
        individuals["Alfie3"]=Individuo(0,0,0,0,0,0,"Alfie",3)
        return individuals
    
    
        
        

print(3+2)      