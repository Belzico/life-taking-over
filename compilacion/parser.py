from compGlobals import TokeTypes 


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