from typing import Type
from compGlobals import TokeTypes 
from fixGrammar import NonTerminal,Production,Terminal,Grammar
from collections import deque

              #Una línea(L) de nuestro lenguaje puede ser: 1-DECLARACIONES  2-CICLO 3-LUEGO DEL CICLO PUEDE VENIR  4-CONDICIONAL  5-CONTINUACIÓN DE CONDICIONAL 6-NUESTROS MÉTODOS  7-NUESTRAS CLASES
production = { "L":[["D",TokeTypes.tokSemicolon],  ["L"],  ["K",TokeTypes.tokOpenBracket] , [TokeTypes.tokClosedBracket,"Q"], ["P",TokeTypes.tokOpenParen,TokeTypes.tokID,"A",TokeTypes.tokClosedParen,TokeTypes.tokSemicolon] ],
            #Primero las declaraciones
            "D":[["R"],["I"], [TokeTypes.tokBool, TokeTypes.tokID, TokeTypes.tokAssign,"E"], [TokeTypes.tokInt, TokeTypes.tokID, TokeTypes.tokAssign, "E"],  [TokeTypes.tokString, TokeTypes.tokID, TokeTypes.tokAssign, "E"], [TokeTypes.tokDouble, TokeTypes.tokID, TokeTypes.tokAssign, "E"] ],
              #Luego las  expresiones de valores (que pueden estar formadas por valores o cálculos)
                "E":[["V","S"]],
                # cálculo y valores
                #Primeramente paréntesis y valores, o calculos y multiplicación
                "V":[["P","M"]],
                #Paréntesis
                "P":[["B"], [TokeTypes.tokOpenParen, "E", TokeTypes.tokClosedParen]],
                #Valores
                "B":[[TokeTypes.tokString],[TokeTypes.tokInt],[TokeTypes.tokDouble],[TokeTypes.tokTrue],[TokeTypes.tokFalse],[TokeTypes.tokID]],
                #Multiplicación
                "M":[["empty"], [TokeTypes.tokMul, "P", "Y"],[TokeTypes.tokDiv, "P", "Y"],[TokeTypes.tokModDiv, "P", "Y"],[TokeTypes.tokPow, "P", "Y"]],
                #Suma
                "S": [["empty"],[TokeTypes.tokSum, "V","S"], [TokeTypes.tokSub,"V","S"]],
            
            #Ciclos
            "L":[[TokeTypes.tokLoop,TokeTypes.tokOpenBracket]],
            
            #Luego del ciclo puede venir
            "R":[[TokeTypes.tokContinue], [TokeTypes.tokBreak],[TokeTypes.tokReturn , "E"]],
            
            #Condicional
            "K":[["G"],[TokeTypes.tokIf, TokeTypes.tokOpenParen, "X", TokeTypes.tokClosedParen]],
                #Cuerpo de condicional: Una Expresión y/o una comparación
                "X":[["E","O"]],
                "O": [["empty"], ["C", "E", "N"]],
                #Comparación
                "C": [[TokeTypes.tokGreaterOrEqual], [TokeTypes.tokLessOrEqual], [TokeTypes.tokNotEqual],[TokeTypes.tokEqual],[TokeTypes.tokGreater], [TokeTypes.tokLess]],
                #Comparación compuesta
                "N": [["empty"],[TokeTypes.tokOr,"X"],[TokeTypes.tokAnd,"X"]],
                #Método Propio
                "G": [TokeTypes.tokID,TokeTypes.tokOpenParen,"U","W",TokeTypes.tokClosedParen],
                "U":[["empty"],[TokeTypes.tokID]],
                "W":[["empty"],[TokeTypes.tokComma ,TokeTypes.tokID,"W"]],
            
            #Luego de la condicional puede venir:
            "Q": [["empty"],[TokeTypes.tokElse, TokeTypes.tokOpenBracket],[TokeTypes.tokElif, TokeTypes.tokOpenParen, "X", TokeTypes.tokClosedParen, TokeTypes.tokOpenBracket]],
                
                
            #Nuestros métodos:
            "P":[[TokeTypes.tokModify],[TokeTypes.tokMSum],[TokeTypes.tokMSub],[TokeTypes.tokMMul],[TokeTypes.tokMDiv], [TokeTypes.tokDie] ,[TokeTypes.tokEvolve], [TokeTypes.tokAdd], [TokeTypes.tokMove], [TokeTypes.tokEat]],
            #Los otros términos que reciben nuestros métodos
            "A":[["empty"],[TokeTypes.tokComma,TokeTypes.tokID], ["A"]],
            
            #Nuestras clases:
            "I":[["Z","B"]],
                #Declaraciones de nuestras clases
                "Z":[[TokeTypes.tokList, TokeTypes.tokID],[TokeTypes.tokMatrix, TokeTypes.tokID],[TokeTypes.tokIndividual, TokeTypes.tokID],[TokeTypes.tokMap, TokeTypes.tokID],[TokeTypes.tokphenomenon, TokeTypes.tokID]],
                #Lo que reciben nuestras clases
                "B":[[TokeTypes.tokAssign,"R"]],
                #Declarando listas y arrays para las matrices (y nuestras listas)
                "R":[[TokeTypes.tokOpenSquareBracket,"F","N",TokeTypes.tokClosedSquareBracket]],
                "F":[["empty"],["R"],["E"]],
                "N": [["empty"], [TokeTypes.tokComma ,"E", "N"]],
                }


nonTerminals =["L", "D","E","V","P","B","M","S","L","R","K","X", "O", "C","N","G","U", "W","Q","P","A", "I","Z","B", "R", "F", "N"]

Terminales = ["empty",TokeTypes.tokComma,TokeTypes.tokOpenSquareBracket,TokeTypes.tokClosedSquareBracket,TokeTypes.tokList,TokeTypes.tokID,
              TokeTypes.tokMatrix,TokeTypes.tokIndividual,TokeTypes.tokMap,TokeTypes.tokphenomenon,TokeTypes.tokModify,TokeTypes.tokMSum,
              TokeTypes.tokMSub,TokeTypes.tokMMul,TokeTypes.tokMDiv,TokeTypes.tokDie,TokeTypes.tokEvolve,TokeTypes.tokAdd,TokeTypes.tokMove,
              TokeTypes.tokEat,TokeTypes.tokElse,TokeTypes.tokElif,TokeTypes.tokOpenParen,TokeTypes.tokClosedParen, 
              TokeTypes.tokOpenBracket,TokeTypes.tokOr,TokeTypes.tokAnd,TokeTypes.tokGreaterOrEqual,TokeTypes.tokLessOrEqual,TokeTypes.tokNotEqual,
              TokeTypes.tokEqual,TokeTypes.tokGreater,TokeTypes.tokLess,TokeTypes.tokIf,TokeTypes.tokContinue,
              TokeTypes.tokBreak,TokeTypes.tokReturn,TokeTypes.tokLoop,TokeTypes.tokSum,TokeTypes.tokSub,TokeTypes.tokMul,TokeTypes.tokDiv,TokeTypes.tokModDiv,
              TokeTypes.tokPow,TokeTypes.tokString,TokeTypes.tokInt,TokeTypes.tokDouble,TokeTypes.tokTrue,TokeTypes.tokFalse,TokeTypes.tokBool,TokeTypes.tokAssign,
              TokeTypes.tokSemicolon,TokeTypes.tokClosedBracket,]






#Creando los items que son generados por la gramática
#Cada uno de ellos tiene un índice ("."), una cabeza no terminal, una producción, y un lookahead (follow)
class Item:
    def __init__(self,Production : Production, Index, Lookahead):
      
      #String Representation es utilizado para observar el item de manera intuitiva (Ej: F==>a|XY,acf)
        self.stringRep = f"{Production.nonTerminal} ==>"
        
      #Lookahead me representa los lookahead del item (los firsts del follow del item)
        self.lookahead = Lookahead
        
      # Lugar donde se encuentra el punto en estos momentos ("|")
        self.index = Index
      
      # Cada uno de los valores de la producción
        self.components = Production.components

      #Creando la representación de string del item
        for i in range(len(self.components)):
            self.stringRep = f"{self.components[i]}"
            if i == self.index-1:
                self.stringRep = f"|"
            
        self.stringRep = f",{self.lookahead}"
        
      


#Creando los estados posibles de la gramaática
class State:
  def __init__(self,Kernel,id):
      
    #Estados que continúan luego de este
    self.continuationStates = {}
    
    #Representación del string de este estado de a siguiente forma S==>X|X,acd :|: X==>i ,acdi
    self.stringRep = ""
    
    self.expectedExpressions = []
    self.id = 0
    
    self.kernel=Kernel
    self.items = {Kernel}
    
    
    #Creando la representación de Estados en string
    for item in Kernel:
      self.stringRep = f"{item} :|: "

          
  def AddItem(self,Item):
    self.items.add(Item)
    
  #Desarrollando el estado
  def Develop(self,AllItems):
    developingQueue = deque(self.kernel)
    
    
    #Revisando todos los items que son generados en este estado
    while len(developingQueue)!= 0:
      
      #Tomamos el item que no ha sido analizado
      item =developingQueue.popleft()
      
      #Si ese item es final, entonces no genera más ninguno
      if item.index == len(item.components): continue
      
      #Tomando el símbolo que viene
      element = item.components[item.index]
      
      #Añadiendo en el diccionario del estado, que este símbolo que espero me genera un estado nuevo
      if element in self.expectedExpressions: self.expectedExpressions[element].add(item)
      else : self.expectedExpressions[element] = {item}
      
      
      #Si ese símbolo es un No terminal, entonces hay que hallarle su clausura
      if Type(element) != NonTerminal:
        
        #Revisando todos los items que crea el elemento para agragrlos al estado
        for i in AllItems[element]:
          
          #Si el es el último elemento del item, entonces generará un item nuevo, pero su lookahead no cambia
          if item.index + 1 == len(item.components):
            newlookahead = item.lookahead
          
          else:
            #ESTE LOOKAHEAD ESTA MAL
            newlookahead = item.components[item.index+1]
          
          #Creando el nuevo item para agregarrlo al estado
          newItem = Item(i.components, i.index, newlookahead)

          #Añadiendo el item al estado
          if newItem not in self.items:
            self.AddItem(newItem)
            #Añadiendolo a la cola de análisis
            developingQueue.append(newItem)

  def GOTO(self,states,stateList, InitialItems,queue,elements):
    tempkernel = []
    for i in self.expectedExpressions[elements]:
      new_item = Item(i.production, i.index + 1, i.lookahead)
      tempkernel.append(new_item)

    new_state = State(tempkernel)
    
    
    if new_state not in states:
      new_state.number = len(states)
      new_state.build(InitialItems)
      states[new_state] = new_state
      stateList.append(new_state)
      queue.append(new_state)
    else:
      new_state = states[new_state]
      
    self.continuationStates[elements] = new_state

    
class Automata:
  def __init__(self,Grammar):
    self.grammar =Grammar
    
  def Construct(self):
    
    beginingProd = NonTerminal("program'",Production([self.grammar.head]))
    
    firstItems = {beginingProd: [Item(beginingProd.productions[0],0,Terminal('$',TokeTypes.tokFinal))] }
    
    for nonTerminal in self.grammar.nonTList:
      firstItems[nonTerminal] = []
      for production in nonTerminal.productions:
        firstItems[nonTerminal].append(Item(production,0,None))
        
    firstState = State(firstItems[beginingProd])

    states_dict = {firstState: firstState}
    states_list = [firstState]
    queue = deque(states_list)
    
    
    while len(queue) != 0:
        state = queue.popleft()
        state.build(firstItems)
        
        for sym in state.expected_elements:
            state.GOTO(sym, states_dict, states_list)
    
    
    
    return states_list
  
  
class GOTOACTION:
  def __init__(self,grammar):
    self.grammar =grammar

  def build(self):
    
    states = Automata(self.grammar).create()

    go_to = []
    action = []
    for state in states:
        state_action = {}
        state_go_to = {}
        lookA_item = {}
        for element_item in state.items:
            if element_item.index == len(element_item.production):
                if element_item.lookahead in lookA_item:
                    raise Exception('There has been a Reduce-Reduce conflict')
                lookA_item[element_item.lookahead] = element_item
        for next_element in state.next_states:
            if next_element.is_terminal:
                state_action[next_element.name] = ('R', state.next_states[next_element].number)
            else:
                state_go_to[next_element.name] = state.next_states[next_element].number
        go_to.append(state_go_to)
        action.append(state_action)
    statesDict = Automata(self.grammar).Construct()

   # if element in self.expectedExpressions: self.expectedExpressions[element].add(item)
      # else : self.expectedExpressions[element] = {item}
      
      # if Type(element) != NonTerminal:
      #   for i in Items[element]:
      #     if item.index + 1 == len(item.components):
      #       newlookahead = item.lookahead
      #     else:
      #       lookahead = item.components[item.index + 1]
      #     newItem = Item(i.components,i.index,lookahead)
      #     if newItem not in self.items:
      #       self.AddItem(newItem)
      #       developingQueue.append(newItem)
  