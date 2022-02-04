from compGlobals import TokeTypes 


              #Una línea(L) de nuestro lenguaje puede ser: 1-DECLARACIONES  2-CICLO  3-CONDICIONAL
production = { "L":[["D",TokeTypes.tokSemicolon],  ["L"],   ["K"]],
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
            
            #Condicional
            "K":[[TokeTypes.tokIf, TokeTypes.tokOpenParen, "X", TokeTypes.tokClosedParen,TokeTypes.tokOpenBracket]],
                #Cuerpo de condicional: Una Expresión y/o una comparación
                "X":[["E","O"]],
                "O": [["empty"], ["C", "E", "N"]],
                #Comparación
                "C": [[TokeTypes.tokGreaterOrEqual], [TokeTypes.tokLessOrEqual], [TokeTypes.tokNotEqual],[TokeTypes.tokEqual],[TokeTypes.tokGreater], [TokeTypes.tokLess]],
                #Comparación compuesta
                "N": [["empty"],[TokeTypes.tokOr,"X"],[TokeTypes.tokAnd,"X"]]
            
                }
