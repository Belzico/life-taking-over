import enum

from compilacion.tokens import TokenType


class TokeTypes(enum.Enum):
    tokSemicolon=enum.auto() # ;     -------
    tokPoint=enum.auto() # .
    tokArrow=enum.auto() # :
    
    tokComennt=enum.auto() # #   -------
    
    tokOpenParen=enum.auto() # (     -------
    tokClosedParen=enum.auto() # )     -------
    tokOpenBracket=enum.auto() # {     -------
    tokClosedBracket=enum.auto() # }     -------
    tokOpenSquareBracket=enum.auto() #[     -------
    tokClosedSquareBracket=enum.auto() #]     -------
    
    tokInt=enum.auto() # int     -------
    tokDouble=enum.auto() # double     -------
    tokString=enum.auto() # string     -------
    tokBool=enum.auto() #bool     -------
    tokNone=enum.auto() #None
    #tokTrue=enum.auto()  #True     -------
    #tokFalse=enum.auto() #False     -------
    tokDicc=enum.auto() #Dicc     -------
    
    tokList=enum.auto() # list (propio)     -------
    tokMatrix=enum.auto() # matrix (propio)     -------
    tokIndividual=enum.auto() #Individuo (propio)     -------
    tokSpecies=enum.auto() #Especie (propio)     -------
    tokMap=enum.auto() #mapa (propio)     -------
    tokphenomenon=enum.auto() #fenomeno (propio)     -------
    
    tokIf=enum.auto() # if     -------
    tokElif=enum.auto() # elif     -------
    tokElse=enum.auto() # else     -------
    tokLoop=enum.auto() # loop     -------
    tokBreak=enum.auto() # break     -------
    tokContinue=enum.auto() # continue     -------
    tokLet=enum.auto() # let     -------
    tokDef=enum.auto() # TokeTypes.tokDef     -------
    
    tokImport=enum.auto() # continue
    
    
    tokComma=enum.auto() #,
    tokNextLine=enum.auto() # /n
    tokNot=enum.auto() #!
    
    tokEqual=enum.auto() #==     -------
    tokNotEqual=enum.auto() #!=     -------
    tokLessOrEqual=enum.auto() #<=     -------
    tokGreaterOrEqual=enum.auto() #>=     -------
    tokGreater=enum.auto() #>     -------
    tokLess=enum.auto() #<     -------
    
    tokSum=enum.auto() #+     -------
    tokSub=enum.auto() #-     -------
    tokMul=enum.auto() #*     -------
    tokDiv=enum.auto() #/     -------
    tokModDiv=enum.auto() #%     -------
    tokPow=enum.auto() #^     -------
    
    tokAnd=enum.auto() #&&     -------
    tokOr=enum.auto() #||     -------
    
    tokID=enum.auto() #     -------
    
    tokModify=enum.auto() # $Modify    -------
    tokCreate=enum.auto() # $Create       --------
    tokDie=enum.auto() # $Die     -------
    tokEvolve=enum.auto() # $Evolve     -------
    tokAdd=enum.auto() # $Add     -------
    tokMove=enum.auto() # $Move     -------
    tokEat=enum.auto()   # $Eat     -------
    
    tokMSum=enum.auto() # $MatrixSum
    tokMSub=enum.auto() # $MatrixSub
    tokMMul=enum.auto() # $MatrixMul
    tokMDiv=enum.auto() # $MatrixDiv
    
    tokAssign=enum.auto() # Assign     -------
    tokReturn=enum.auto() # Return      -------
    tokPrint=enum.auto() # Print     -------
    
    
    
    




keywordsDicc={
    #Keywords Condicionales
    "if"       : TokeTypes.tokIf, 
    "elif"     : TokeTypes.tokElif,
    "else"     : TokeTypes.tokElse,
    
    #declaracion
    "let"     : TokeTypes.tokLet,
    "def"     : TokeTypes.tokDef,
    
    #Keywords de Ciclos
    "loop"     : TokeTypes.tokLoop,
    
    "break"    : TokeTypes.tokBreak,
    "continue" : TokeTypes.tokContinue,
    
    #Keywords de tipos
    "int"      : TokeTypes.tokInt,
    "double"   : TokeTypes.tokDouble,
    "string"   : TokeTypes.tokString,
    "dict"     : TokeTypes.tokDicc,
    
    #Keywords de valor
    "bool"     : TokeTypes.tokBool,
    "None"     : TokeTypes.tokNone,
    #"True"     : TokeTypes.tokTrue,
    #"False "   : TokeTypes.tokFalse,
    
    #Kewords del trabajo
    "Individuo": TokeTypes.tokIndividual,
    "Especie"  : TokeTypes.tokSpecies,
    "mapa"     : TokeTypes.tokMap,
    "fenomeno" : TokeTypes.tokphenomenon,
    
    #especiales
    "print" : TokenType.tokPrint
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
    
    #simbolo para especificar tipos de retorno
    "->" : TokenType.tokArrow,
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
