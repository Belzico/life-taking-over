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
    "die":[[TokeTypes.tokDie,TokeTypes.tokOpenParen,TokeTypes.tokIndividual,TokeTypes.tokClosedParen]],
    
    #lenguage funtion create
    "create":[[TokeTypes.tokCreate,TokeTypes.tokOpenParen,"leng_type",TokeTypes.tokComma,"args_list",TokeTypes.tokClosedParen]],
    
    #Modify leng_type
    "modify":[[TokeTypes.tokCreate,TokeTypes.tokOpenParen,"leng_type",TokeTypes.tokComma,"args_list",TokeTypes.tokClosedParen]],
    
    #lenguage funtion die
    "evolve":[[TokeTypes.tokOpenParen,TokeTypes.tokSpecies,TokeTypes.tokClosedParen]],
    
    #lenguage funtion add al mapa cosas como fenomeno o especie
    "add":[[TokeTypes.tokID,TokeTypes.tokOpenParen,TokeTypes.tokSpecies,TokeTypes.tokClosedParen]],
    
    #lenguage funtion die
    "move":[[TokeTypes.tokMove,TokeTypes.tokOpenParen,TokeTypes.tokIndividual,TokeTypes.tokClosedParen]],
    
    #lenguage funtion die
    "eat":[[TokeTypes.tokMove,TokeTypes.tokOpenParen,TokeTypes.tokIndividual,TokeTypes.tokClosedParen]],
    
    #lenguaje types
    "leng_type":[[TokeTypes.tokIndividual],[TokeTypes.tokSpecies],[TokeTypes.tokMap],[TokeTypes.tokphenomenon]],
    
    #args_list
    "args_list":[[TokeTypes.tokID],[TokeTypes.tokID,TokeTypes.tokComma,"args_list"]],
    
    #types
    "type":[[TokeTypes.tokInt],[TokeTypes.tokDouble],[TokeTypes.tokString],[TokeTypes.tokBool],[TokeTypes.tokNone],[TokeTypes.tokTrue],[TokeTypes.tokFalse]],
    
    #expresions
    "expr":[["expr",TokeTypes.tokSum,"term"],["expr",TokeTypes.tokSub,"term"],["term"]],
    
    #terminos
    "term":[["term",TokeTypes.tokMul,"factor"],["term",TokeTypes.tokDiv,"factor"],["factor"]],
    
    #factor
    "factor":[["atom"],[TokeTypes.tokOpenParen,"expr",TokeTypes.tokClosedParen]],
    
    #atomos
    "atom":[[TokeTypes.tokID],["func_call"],["type"],["leng_type"]],
    
    #llamados a funciones
    "func_call":[["matrix_func"],[TokeTypes.tokID,TokeTypes.tokOpenParen,"expr_list",TokeTypes.tokClosedParen]],
    
    #separacion para los metodos que usan escalares y los que usen 2 matrices
    "matrix_func":[["escalar"],["vectorial"]],
    
    #suma y resta vectorial
    "vectorial":[["matrix_vec",TokeTypes.tokOpenParen,TokeTypes.tokMatrix,TokeTypes.tokMatrix,TokeTypes.tokClosedParen]],
    
    #matrices vec
    "matrix_vec":[[TokeTypes.tokMSum],[TokeTypes.tokMSub]],
    
    #multiplicacion y division escalar
    "escalar":[["matrix_esca",TokeTypes.tokOpenParen,TokeTypes.tokMatrix,TokeTypes.tokInt,TokeTypes.tokClosedParen]],
    
    #matrices esca
    "matrix_esca":[[TokeTypes.tokMDiv],[TokeTypes.tokMMul]],
    
    #lista de expresiones
    "expr_list":[["expr"],["expr",TokeTypes.tokComma,"expr_list"]]
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
