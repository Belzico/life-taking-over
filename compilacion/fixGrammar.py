from compGlobals import TokeTypes 

terminales = ["epsilon",TokeTypes.tokComma,TokeTypes.tokOpenSquareBracket,TokeTypes.tokClosedSquareBracket,TokeTypes.tokList,TokeTypes.tokID,
            TokeTypes.tokMatrix,TokeTypes.tokIndividual,TokeTypes.tokMap,TokeTypes.tokphenomenon,TokeTypes.tokModify,TokeTypes.tokMSum,
            TokeTypes.tokMSub,TokeTypes.tokMMul,TokeTypes.tokMDiv,TokeTypes.tokDie,TokeTypes.tokEvolve,TokeTypes.tokAdd,TokeTypes.tokMove,
            TokeTypes.tokEat,TokeTypes.tokElse,TokeTypes.tokElif,TokeTypes.tokOpenParen,TokeTypes.tokClosedParen, 
            TokeTypes.tokOpenBracket,TokeTypes.tokOr,TokeTypes.tokAnd,TokeTypes.tokGreaterOrEqual,TokeTypes.tokLessOrEqual,TokeTypes.tokNotEqual,
            TokeTypes.tokEqual,TokeTypes.tokGreater,TokeTypes.tokLess,TokeTypes.tokIf,TokeTypes.tokContinue,
            TokeTypes.tokBreak,TokeTypes.tokReturn,TokeTypes.tokLoop,TokeTypes.tokSum,TokeTypes.tokSub,TokeTypes.tokMul,TokeTypes.tokDiv,TokeTypes.tokModDiv,
            TokeTypes.tokPow,TokeTypes.tokString,TokeTypes.tokInt,TokeTypes.tokDouble,TokeTypes.tokTrue,TokeTypes.tokFalse,TokeTypes.tokBool,TokeTypes.tokAssign,
            TokeTypes.tokSemicolon,TokeTypes.tokClosedBracket,]


productions={
    #program
    "program":[["stat_list"]],
    
    #lista de statments
    "stat_list":[["stat",TokeTypes.tokSemicolon],["stat",TokeTypes.tokSemicolon,"stat_list"]],
    
    #statment
    "stat":[["let_dec"],["func_dec"],["print_stat"],["condictional_stat"],["loop_stat"],["lenguage_funtion"]],
    
    #let declarator
    "let_dec":[[TokeTypes.tokLet,"type",TokeTypes.tokID,TokeTypes.tokEqual,"expr"]],
    
    #declarador de funciones
    "func_dec":[[TokeTypes.tokDef,TokeTypes.tokID,TokeTypes.tokOpenParen,"arg-list",TokeTypes.tokClosedParen,TokeTypes.tokArrow,"type",TokeTypes.tokOpenBracket,"stat_list",TokeTypes.tokClosedBracket]],
    
    #print statment
    "print_stat":[TokeTypes.tokOpenParen,"expr",TokeTypes.tokClosedParen],
    
    #condicionales
    "condictional_stat":[["if_stat"],["else_stat"],["elif_stat"]],
    
    #if statment   (aca regla semantica para q exp sea bool)
    "if_stat":[[TokeTypes.tokIf,TokeTypes.tokOpenParen,"expr",TokeTypes.tokClosedParen,TokeTypes.tokOpenBracket,"stat_list",TokeTypes.tokClosedBracket]], 
    
    #elif statment   (aca regla semantica para q exp sea bool)
    "elif_stat":[[TokeTypes.tokElif,TokeTypes.tokOpenParen,"expr",TokeTypes.tokClosedParen,TokeTypes.tokOpenBracket,"stat_list",TokeTypes.tokClosedBracket]], 
    
    #else statment
    "else_stat":[[TokeTypes.tokElse,TokeTypes.tokOpenBracket,"stat_list",TokeTypes.tokClosedBracket]], 
    
    
    #loop statment   (aca regla semantica para q exp sea bool) y añadir a expr Tokbreak, como usar el break se hara mediante los contextos al ponerle el nombre de un loop si es un loop quien lo llama 
    "loop_stat":[[TokeTypes.tokLoop,TokeTypes.tokOpenParen,"expr",TokeTypes.tokClosedParen,TokeTypes.tokOpenBracket,"stat_list",TokeTypes.tokClosedBracket]], 
    
    #funciones especiales del lenguaje
    "lenguage_funtion":[["die"],["modify"],["create"],["evolve"],["add"],["move"],["eat"]],
    
    #lenguage funtion die
    "die":[[TokeTypes.tokOpenParen,TokeTypes.tokIndividual,TokeTypes.tokClosedParen]],
    
    #lenguage funtion create
    "create":[[TokeTypes.tokIndividual,TokeTypes.tokOpenParen,TokeTypes.tokInt,TokeTypes.tokInt,TokeTypes.tokInt,TokeTypes.tokClosedParen]],
    
    #types
    "type":[[TokeTypes.tokInt],[TokeTypes.tokDouble],[TokeTypes.tokString],[TokeTypes.tokBool],[TokeTypes.tokNone],[TokeTypes.tokTrue],[TokeTypes.tokFalse]]
}




class Terminal:
    def __init__(self, Name, Type):
        self.name = Name
        self.type = Type


class Production:

    def __init__(self, NonTerminal ,Components):
        self.components = Components
        self.nonTerminal = NonTerminal


class NonTerminal:
    def __init__(self, Name, Productions):
        self.name = Name
        self.productions = Productions

    def __iadd__(self, prod: Production):
        self.add(prod)
        return self


class Grammar:
    def __init__(self, nonTList, Head):
        self.nonTList = nonTList
        self.head = Head 
