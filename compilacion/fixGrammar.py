from classNode import classnode
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
    "stat_list":[["stat",TokeTypes.tokSemicolon,"stat_list_fix"]],

    #si un statment se va en epsilon o sigue con una lista de statments
    "stat_list_fix":[["epsilon"],["stat_list"]],
    
    #statment
    "stat":[["override_expr"],["let_dec"],["func_dec"],["var_reasign"],["print_stat"],["condictional_stat"],["loop_stat"],["lenguage_funtion"],["break_exp"],["return_exp"],["continue_exp"],["epsilon"]],
    
    #statement
    "override_expr":[TokeTypes.tokOverride,TokeTypes.tokOpenParen,"leng_type","lenguage_funtion",TokeTypes.tokID,TokeTypes.tokClosedParen],
    
    #reasignacion de variable
    "var_reasign":[TokeTypes.tokID,TokeTypes.tokAssign,"expr"],
    
    #return expresion
    "return_exp":[[TokeTypes.tokReturn,"expr"]],
    
    #expresion continue
    "continue_exp":[[TokeTypes.tokContinue]],
        
    #expresion break
    "break_exp":[[TokeTypes.tokBreak]],
    
    #let declarator
    "let_dec":[[TokeTypes.tokLet,"all_types",TokeTypes.tokID,TokeTypes.tokAssign,"expr"]],
    
    #declarador de funciones
    "func_dec":[[TokeTypes.tokDef,TokeTypes.tokID,TokeTypes.tokOpenParen,"args_list",TokeTypes.tokClosedParen,TokeTypes.tokArrow,"all_types",TokeTypes.tokOpenBracket,"stat_list",TokeTypes.tokClosedBracket]],
    
    #print statment
    "print_stat":[TokeTypes.tokOpenParen,"expr",TokeTypes.tokClosedParen],
    
    #condicionales
    "condictional_stat":[["if_stat"]],
    
    #if statment   (aca regla semantica para q exp sea bool)
    "if_stat":[[TokeTypes.tokIf,TokeTypes.tokOpenParen,"expr",TokeTypes.tokClosedParen,TokeTypes.tokOpenBracket,"stat_list",TokeTypes.tokClosedBracket,"elif_stat","else_stat"]], 
    
    #elif statment   (aca regla semantica para q exp sea bool)
    "elif_stat":[[TokeTypes.tokElif,TokeTypes.tokOpenParen,"expr",TokeTypes.tokClosedParen,TokeTypes.tokOpenBracket,"stat_list",TokeTypes.tokClosedBracket],["epsilon"]], 
    
    #else statment
    "else_stat":[[TokeTypes.tokElse,TokeTypes.tokOpenBracket,"stat_list",TokeTypes.tokClosedBracket],["epsilon"]], 
    
    
    #loop statment   (aca regla semantica para q exp sea bool) y añadir a expr Tokbreak, como usar el break se hara mediante los contextos al ponerle el nombre de un loop si es un loop quien lo llama 
    "loop_stat":[[TokeTypes.tokLoop,TokeTypes.tokOpenParen,"expr",TokeTypes.tokClosedParen,TokeTypes.tokOpenBracket,"stat_list",TokeTypes.tokClosedBracket]], 
    
    #funciones especiales del lenguaje
    "lenguage_funtion":[["die"],["modify"],["evolve"],["add"],["move"],["eat"],["create"]],  # sacado para ponerlo en expresion
    
    #lenguage funtion die
    "die":[[TokeTypes.tokDie,TokeTypes.tokOpenParen,TokeTypes.tokIndividual,TokeTypes.tokClosedParen]],
    
    #Modify leng_type
    "modify":[[TokeTypes.tokModify,TokeTypes.tokOpenParen,"args_list",TokeTypes.tokClosedParen]],
    
    #lenguage funtion die
    "evolve":[[TokeTypes.tokOpenParen,"args_list",TokeTypes.tokClosedParen]],
    
    #lenguage funtion add al mapa cosas como fenomeno o especie
    "add":[[TokeTypes.tokID,TokeTypes.tokPoint,TokeTypes.tokAdd,TokeTypes.tokOpenParen,"args_list",TokeTypes.tokClosedParen]],
    
    #lenguage funtion die
    "move":[[TokeTypes.tokMove,TokeTypes.tokOpenParen,"args_list",TokeTypes.tokClosedParen]],
    
    #lenguage funtion die
    "eat":[[TokeTypes.tokEat,TokeTypes.tokOpenParen,"args_list",TokeTypes.tokClosedParen]],
    
    #lenguage funtion create
    "create":[[TokeTypes.tokCreate,TokeTypes.tokOpenParen,"args_list",TokeTypes.tokClosedParen]],
    
    #todos los tipos del lenguaje
    "all_types":[["leng_type"],["type"]],
    
    #lenguaje types
    "leng_type":[[TokeTypes.tokIndividual],[TokeTypes.tokSpecies],[TokeTypes.tokMap],[TokeTypes.tokphenomenon]],
    
    #args_list
    "args_list":[[TokeTypes.tokID,"args_list_fix"],["epsilon"]],
    
    #si un arg se va en epsilon o sigue con una lista de statments
    "args_list_fix":[["epsilon"],[TokeTypes.tokComma,"args_list"]],
    
    #types
    "type":[[TokeTypes.tokInt],[TokeTypes.tokDouble],[TokeTypes.tokString],[TokeTypes.tokBool],[TokeTypes.tokNone]],
    
    #expresions
    "expr":[["term",TokeTypes.tokSum,"expr"],["term",TokeTypes.tokSub,"expr"],["term","comparer","expr"],["term"]],
    
    #terminos
    "term":[["term",TokeTypes.tokMul,"factor"],["term",TokeTypes.tokDiv,"factor"],["factor"]],
    
    #factor
    "factor":[["atom"],[TokeTypes.tokOpenParen,"expr",TokeTypes.tokClosedParen]],
    
    #atomos
    "atom":[[TokeTypes.tokID],["func_call"],[TokeTypes.tokNumber],[TokeTypes.tokChain],[TokeTypes.tokNone],[TokeTypes.tokChain],[TokeTypes.tokTrue],[TokeTypes.tokFalse],["dic_dec"],["epsilon"]],
    
    #comparadores
    "comparer":[[TokeTypes.tokEqual],[TokeTypes.tokNot],[TokeTypes.tokNotEqual],[TokeTypes.tokGreaterOrEqual],[TokeTypes.tokGreater],[TokeTypes.tokLess],[TokeTypes.tokLessOrEqual],[TokeTypes.tokAnd],[TokeTypes.tokOr]],
    
    #declaracion de diccionario
    "dic_dec":[[TokeTypes.tokDicc,TokeTypes.tokOpenSquareBracket,"all_types",TokeTypes.tokComma,"all_types",TokeTypes.tokClosedSquareBracket]],


    
    #llamados a funciones
    "func_call":[["matrix_func"],["dic_func"],[TokeTypes.tokID,TokeTypes.tokOpenParen,"expr_list",TokeTypes.tokClosedParen]],
    
    #funciones de diccionario    
    "dic_func":[["search_dic"],["recieve_dic"]],
    
    #pregunta si una funcion
    "search_dic":[[TokeTypes.tokSearchDicc,TokeTypes.tokOpenParen,"expr",TokeTypes.tokClosedParen]],
    
    #retorna el valor asociado a la llave
    "recieve_dic":[[TokeTypes.tokReturnDicc,TokeTypes.tokOpenParen,"expr",TokeTypes.tokClosedParen]],
    
    #separacion para los metodos que usan escalares y los que usen 2 matrices
    "matrix_func":[["escalar"],["vectorial"]],
    
    #suma y resta vectorial
    "vectorial":[["matrix_vec",TokeTypes.tokOpenParen,TokeTypes.tokID,TokeTypes.tokID,TokeTypes.tokClosedParen]],
    
    #matrices vec
    "matrix_vec":[[TokeTypes.tokMSum],[TokeTypes.tokMSub]],
    
    #multiplicacion y division escalar
    "escalar":[["matrix_esca",TokeTypes.tokOpenParen,TokeTypes.tokID,TokeTypes.tokID,TokeTypes.tokClosedParen]],
    
    #matrices esca
    "matrix_esca":[[TokeTypes.tokMDiv],[TokeTypes.tokMMul]],
    
    #lista de expresiones
    "expr_list":[["expr"],["expr_list_fix"]],
    
    #fix de expresion list
    "expr_list_fix":[[TokeTypes.tokComma,"expr_list"],["epsilon"]]
}

#------------------------------------------------------------------------------------------------------#
#------------------------------------- DicNode --------------------------------------------------------#
#------------------------------------------------------------------------------------------------------#

dicNode = {
    "program": classnode.ProgramNode(),
    "stat": classnode.StatementNode(),
    "break": classnode.BreakNode(),
    "let_dec": classnode.LetNode(),
    "func_dec": classnode.FucNode(),
    "print_stat": classnode.PrintNode(),
    "condictional_stat": classnode.Condictional_statNode(),
    "if_stat": classnode.IfNode(),
    "elif_stat": classnode.ElifNode(),
    "else_stat": classnode.elseNode(),
    "loop_stat": classnode.loopNode(),
    "die": classnode.dieNode(),
    "modify": classnode.modifyNode(),
    "evolve": classnode.evolveNode(),
    "add": classnode.AddNode(),
    "move": classnode.moveNode(),
    "eat": classnode.eatNode(),
    "create": classnode.createNode(),
    "func_call": classnode.func_callNode(),
    "vectorial": classnode.vectorialNode(),
    "dic_dec": classnode.DicNode(),
    "search_dic": classnode.SearchDicNode(),
    "recieve_dic": classnode.RecieveDicNode(),
    "var_reasign":classnode.RedeclareVar(),
    "return_exp": classnode.ReturnNode(),
    
    #------------------------------------- TokTerminales -----------------------------------------------#
    
    TokeTypes.tokBreak: classnode.TookBreakNode(),
    TokeTypes.tokID: classnode.IdNode(),
    TokeTypes.tokEqual: classnode.EqualNode(),
    TokeTypes.tokSum: classnode.SumNode(),
    TokeTypes.tokSub: classnode.SubNode(),
    TokeTypes.tokMul: classnode.MulNode(),
    TokeTypes.tokDiv: classnode.DivNode(),
    TokeTypes.tokNumber: classnode.NumberNode(),
    TokeTypes.tokChain: classnode.ChainNode(),
    TokeTypes.tokTrue: classnode.TrueNode(),
    TokeTypes.tokFalse: classnode.FalseNode(),
    TokeTypes.tokNone: classnode.NoneNode()
}





class Terminal:
    def __init__(self, Name, Type):
        self.name = Name
        self.type = Type


class Production:

    def __init__(self, head ,Components):
        self.components = Components
        self.head = head


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