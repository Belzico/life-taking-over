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
    tokColom=31 #.
    
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
    
    
    




keywordsDicc={}

operatorsDicc={}

puntuationDicc={}

errorsList=[]
