from compGlobals import TokeTypes 


               #Una línea(L) de nuestro lenguaje puede ser: 1-DECLARACIONES  2-CICLO 3-LUEGO DEL CICLO PUEDE VENIR  4-CONDICIONAL  5-CONTINUACIÓN DE CONDICIONAL 6-NUESTROS MÉTODOS  7-NUESTRAS CLASES
production = { "L":[["D",TokeTypes.tokSemicolon],  ["L"], ["R",TokeTypes.tokSemicolon],  ["K"] , [TokeTypes.tokClosedBracket,"Q"], ["U",TokeTypes.tokOpenParen,TokeTypes.tokID,"A",TokeTypes.tokClosedParen,TokeTypes.tokSemicolon] , ["I",TokeTypes.tokSemicolon]],
            #Primero las declaraciones
            "D":[ [TokeTypes.tokBool, TokeTypes.tokID, TokeTypes.tokAssign,"E"], [TokeTypes.tokInt, TokeTypes.tokID, TokeTypes.tokAssign, "E"],  [TokeTypes.tokString, TokeTypes.tokID, TokeTypes.tokAssign, "E"], [TokeTypes.tokDouble, TokeTypes.tokID, TokeTypes.tokAssign, "E"] ],
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
            "R":[[TokeTypes.tokContinue], [TokeTypes.tokBreak]],
            
            #Condicional
            "K":[[TokeTypes.tokIf, TokeTypes.tokOpenParen, "X", TokeTypes.tokClosedParen,TokeTypes.tokOpenBracket]],
                #Cuerpo de condicional: Una Expresión y/o una comparación
                "X":[["E","O"]],
                "O": [["empty"], ["C", "E", "N"]],
                #Comparación
                "C": [[TokeTypes.tokGreaterOrEqual], [TokeTypes.tokLessOrEqual], [TokeTypes.tokNotEqual],[TokeTypes.tokEqual],[TokeTypes.tokGreater], [TokeTypes.tokLess]],
                #Comparación compuesta
                "N": [["empty"],[TokeTypes.tokOr,"X"],[TokeTypes.tokAnd,"X"]],
            
            #Luego de la condicional puede venir:
            "Q": [["empty"],[TokeTypes.tokElse, TokeTypes.tokOpenBracket],[TokeTypes.tokElif, TokeTypes.tokOpenParen, "X", TokeTypes.tokClosedParen, TokeTypes.tokOpenBracket]],
                
                
            #Nuestros métodos:
            "U":[[TokeTypes.tokModify],[TokeTypes.tokModify], [TokeTypes.tokDie] ,[TokeTypes.tokEvolve], [TokeTypes.tokAdd], [TokeTypes.tokMove], [TokeTypes.tokEat]],
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
