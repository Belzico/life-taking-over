import enum


class TokeTypes(enum.Enum):
    tokSemicolon=0 # ;
    tokPoint=1 # .
    
    tokComennt=2 # #
    
    tokOpenParen=3 # (
    tokClosedParen=4 # )
    tokOpenBracket=5 # {
    tokClosedBracket=6 # }
    tokOpenSquareBracket=7 #[
    tokClosedSquareBracket=8
    
    tokInt=9 # int
    tokDouble=10 # double
    tokString=11 # string
    tokBool=12 #bool
    tokNone=13 #None
    tokTrue=14  #True
    tokFalse=15 #False
    
    tokList=16 # list (propio)
    tokMatrix=17 # matrix (propio)
    tokIndividual=18 #Individuo (propio)
    tokSpecies=19 #Especie (propio)
    tokMap=20 #mapa (propio)
    tokphenomenon=21 #fenomeno (propio)
    
    tokIf=22 # if
    tokElif=23 # elif
    tokElse=24 # else
    tokLoop=25 # loop
    tokBreak=26 # break
    tokContinue=27 # continue
    
    tokImport=28 # continue
    
    
    tokComma=29 #,
    tokNextLine=30 # /n
    tokNot=31 #!
    
    tokEqual=32 #==
    tokNotEqual=33 #!=
    tokLessOrEqual=34 #<=
    tokGreaterOrEqual=35 #>=
    tokGreater=36 #>
    tokLess=36 #<
    
    tokSum=37 #+
    tokSub=38 #-
    tokMul=39 #*
    tokDiv=40 #/
    tokModDiv=41 #%
    tokPow=42 #^
    
    tokAnd=43 #&&
    tokOr=44 #||
    
    tokID=45 #
    
    tokModify=46 # $Modify
    tokCreate=47 # $Create
    tokDie=48 # $Die
    tokEvolve=49 # $Evolve
    tokAdd=50 # $Add
    tokMove=51 # $Move
    tokEat=52   # $Eat
    
    tokMSum=53 # $MatrixSum
    tokMSub=54 # $MatrixSub
    tokMMul=55 # $MatrixMul
    tokMDiv=56 # $MatrixDiv
    
    tokAssign=57 # Assign
    
    
    
    




keywordsDicc={
    #Keywords Condicionales
    "if"       : TokeTypes.tokIf, 
    "elif"     : TokeTypes.tokElif,
    "else"     : TokeTypes.tokElse,
    
    #Keywords de Ciclos
    "loop"     : TokeTypes.tokLoop,
    
    "break"    : TokeTypes.tokBreak,
    "continue" : TokeTypes.tokContinue,
    
    #Keywords de tipos
    "int"      : TokeTypes.tokInt,
    "double"   : TokeTypes.tokDouble,
    "string"   : TokeTypes.tokString,
    
    #Keywords de valor
    "bool"     : TokeTypes.tokBool,
    "None"     : TokeTypes.tokNone,
    "True"     : TokeTypes.tokTrue,
    "False "   : TokeTypes.tokFalse,
    
    #Kewords del trabajo
    "Individuo": TokeTypes.tokIndividual,
    "Especie"  : TokeTypes.tokSpecies,
    "mapa"     : TokeTypes.tokMap,
    "fenomeno" : TokeTypes.tokphenomenon
}

operatorsDicc={
    #Operadores de calculo
    "+" : TokeTypes.tokSum,
    "-" : TokeTypes.tokSub,
    "*" : TokeTypes.tokMul,
    ":" : TokeTypes.tokDiv,
    "%" : TokeTypes.tokModDiv,
    "^" : TokeTypes.tokPow,
    
    #operador de asignacion
    "=" : TokeTypes.tokAssign,
    
    #Operadores condicionales
    "&&" : TokeTypes.tokAnd,
    "||" : TokeTypes.tokOr,
    "!":    TokeTypes.tokNot,
    #Operadores de comparacion
    "==" : TokeTypes.tokEqual,
    "!=" : TokeTypes.tokNotEqual,
    "<=" : TokeTypes.tokLessOrEqual,
    ">=" : TokeTypes.tokGreaterOrEqual,
    ">"  : TokeTypes.tokGreater,
    "<"  : TokeTypes.tokLess,
    
    #solo para la tokenizacion
    "&":None,
    "|":None,
    
    
    
}

bracketDicc={
    "("        : TokeTypes.tokOpenParen,
    ")"        : TokeTypes.tokClosedParen,
    "["        : TokeTypes.tokOpenSquareBracket,
    "]"        : TokeTypes.tokClosedSquareBracket,
    "{"        : TokeTypes.tokOpenBracket,
    "}"        : TokeTypes.tokClosedBracket,
}

puntuationDicc={
    #Signos de comentario
    "#"        : TokeTypes.tokComennt,
    
    #Signos de puntuacion
    ";" :  TokeTypes.tokSemicolon,
    #"." :  TokeTypes.tokPoint,
    
    #Signos de Separacion
    ","  : TokeTypes.tokComma, 
    #"."  : TokeTypes.tokColom,
    
    #Signos Especiales
    #"\n" : TokeTypes.tokNextLine
}

specialKeywordsDicc={
    
    "$Modify": TokeTypes.tokModify, 
    "$Create" :TokeTypes.tokCreate,
    "$Die": TokeTypes.tokDie,
    "$Evolve":TokeTypes.tokEvolve,
    "$Add":TokeTypes.tokAdd, 
    "$Move":TokeTypes.tokMove,
    "$Eat":TokeTypes.tokEat,
    
    "$MatrixSum":TokeTypes.tokMSum, 
    "$MatrixSub":TokeTypes.tokMSub,
    "$MatrixMul":TokeTypes.tokMMul,
    "$MatrixDiv":TokeTypes.tokMDiv
    
}

errorsList=[]
