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
  def __init__(self,ItemsList):
      
      #Estados que continúan luego de este
      self.continuationStates = {}
      
      #Representación del string de este estado de a siguiente forma S==>X|X,acd ;
      self.stringRep = ""
      
      self.expectedExpressions = []
      self.id = 0
      
      self.kernel=ItemsList
      self.items = {ItemsList}
      
      
      #Creando la representación de Estados en string
      for item in ItemsList:
        self.stringRep = f"{item} :|: "
          
  def AddItem(self,Item):
    self.items.add(Item)
    
  def Develop(self,Items):
    developingQueue = deque(self.kernel)
    
    while len(developingQueue)!= 0:
      item =developingQueue.popleft()
      
      if item.index == len(item.components): continue
      
      element = item.components[item.index]
      
      if element in self.expectedExpressions: self.expectedExpressions[element].add(item)
      else : self.expectedExpressions[element] = {item}
      
      if Type(element) != NonTerminal:
        for i in Items[element]:
          if item.index + 1 == len(item.components):
            newlookahead = item.lookahead
          else:
            lookahead = item.components[item.index + 1]
          newItem = Item(i.components,i.index,lookahead)
          if newItem not in self.items:
            self.AddItem(newItem)
            developingQueue.append(newItem)
  
  def GOTO(self,states,state_List):
    pass
    
    
    
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
            state.go_to(sym, states_dict, states_list)
    
    
    
    #return states_lis


  