from calendar import TextCalendar
from dataclasses import dataclass
from distutils.log import error
from inspect import ArgSpec
from itertools import chain
from lib2to3.pytree import Node
from multiprocessing import Condition, context
from pickle import FALSE
from platform import node
from tokenize import Double
from webbrowser import Opera
from wsgiref import validate

from numpy import true_divide

from compGlobals import TokeTypes 
import enum

class nodetypes(enum.Enum):
    IdNode = enum.auto()
    SumNode = enum.auto()
    SubNode = enum.auto()
    MulNode = enum.auto()
    DivNode = enum.auto()
    ModNode = enum.auto()
    PowNode = enum.auto()
    VectorialNode = enum.auto()
    NumberNode = enum.auto()
    ChainNode = enum.auto()
    TrueNode = enum.auto()
    FalseNode = enum.auto()
    NoneNode = enum.auto()

@dataclass
class ClassNode():
    

    def Eval(self,context):
        pass
    
    def validateNode(self,context):
        pass
    
    def transpilar(self):
        pass

    def checkTypes(self):
        pass

    def build_ast(productionList):
        pass

class OperatorNode(ClassNode):
    def Eval(self,context):
        pass
    
    def validateNode(self,context):
        pass

    def transpilar(self):
        pass
    
    def checkTypes(self):
        pass

    def build_ast(productionList,indexPro):
        pass

class CompareNode(ClassNode):
    def Eval(self,context):
        pass
    
    def validateNode(self,context):
        pass
    
    def transpilar(self):
        pass

    def build_ast(self,productionList,indexProduc):
        pass

class Context():
    def __init__(self,name,classNode,fatherContext=None,breakCheck=False):
        
        self.diccVarContext : dict(str,ClassNode)= {}
        self.diccFuncContext : dict(str,ClassNode)={} 
        self.fatherContext= fatherContext
        self.name=name
        self.breakCheck=breakCheck
        self.classNode=classNode
    
        
    def checkVar(self,var,varType):
        #declarada
        if var in self.diccVarContext or (self.fatherContext!=None and self.fatherContext.checkVar()):
            varAtributes=self.retVar(var)
            if varAtributes==None:
                #error de tipo
                return False
            if varAtributes[1]==varType:
                return True
        #no declarada
        return False

    def checkFun(self,var,typeList):
        #declarada
        if var in self.diccFuncContext or (self.fatherContext!=None and self.fatherContext.checkFun()):
            varAtributes=self.retFun(var,typeList)
            if varAtributes==None:
                #error de tipo
                return False
            #i=1
            #while i<len(typeList):
            #    if varAtributes[i]!=typeList[i]:
            #        return False
            return True
        #no declarada
        return False
    
    def define_var(self,var,varType,varValue):
        if not self.checkVar(var,varType):
            self.diccVarContext[var]=[var,varType,varValue]
            return True
        return False
            
    def define_func(self,var,typeList:list):
        if not self.checkVar(var,typeList):
            typeList.insert(0,var)
            self.diccVarContext[var]=[var,typeList]
            return True
        return False
    
    #este metodo devuelve una lista con el formator [name,type]
    def retVar(self,var):
        current=self
        while current!=None:
            if self==None: return None
            if var in current.diccVarContext:
                return current.diccVarContext[var]
            current=self.fatherContext
    
    #este metodo devuelve una lista con el formator [name,arg1Type,arg2Type....,argNType]
    def retFun(self,var,argList):
        current=self
        while current!=None:
            if self==None: return None
            if (var,argList) in current.diccFuncContext:
                return current.diccFuncContext[var]
            current=self.fatherContext
    
    def redeclareVar(self,var,varType,varValue):
        current=self
        while current!=None:
            if self==None: return None
            if var in current.diccVarContext:
                oldVar= current.diccVarContext[var]
                if oldVar[1]==varType:
                    current[var]=(var,varType,varValue)
                    return True
                #error los tipos son diferentes
                return False
            current=self.fatherContext
            
        #error la variable no existe
        return False
        
    def create_hild(self,name,node):
        chilcontext=Context(name,self,node)
        return chilcontext




#--------------------------------------------------------------------------- #
#-------------------------- Nodos Operadores ------------------------------- #
#--------------------------------------------------------------------------- #

@dataclass
class SumNode(OperatorNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context

        self.RT = None
        self.ET = None
    
    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)

        if value1.isnumeric() and value2.isnumeric():
            return  value1+value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla

    def transpilar(self):
        return str(self.Left) + " + " +  str(self.Right)

    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
        
    def build_ast(self,productionList,indeProduc):
        self.Left=eatExpression(productionList,indeProduc)
        self.Right=eatExpression(productionList,indeProduc)
        self.RT=self.Left.RT
        self.ET=self.Right.ET
        

class SubNode(OperatorNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context

        self.RT = None
        self.ET = None
    
    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        if value1.isnumeric() and value2.isnumeric():
            return  value1-value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)

    def transpilar(self):
        return str(self.Left) + " - " +  str(self.Right)


    def build_ast(self,productionList):
        pass
    

class MulNode(OperatorNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        if value1.isnumeric() and value2.isnumeric():
            return  value1*value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
    
    def transpilar(self):
        return str(self.Left) + " * " +  str(self.Right)


    def build_ast(self,productionList):
        pass
    
class DivNode(OperatorNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context

        self.RT = None
        self.ET = None
    
    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        if value1.isnumeric() and value2.isnumeric()and value2!=0:
            return  value1/value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)

    def transpilar(self):
        return str(self.Left) + " / " +  str(self.Right)
    
    def build_ast(self,productionList):
        pass

class ModNode(OperatorNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        if value1.isnumeric() and value2.isnumeric()and value2!=0:
            return  value1%value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)

    def transpilar(self):
        return str(self.Left) + " % " +  str(self.Right)

    def build_ast(self,productionList):
        pass

class PowNode(OperatorNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context

        self.RT = None
        self.ET = None
    
    def Eval(self):
        value1=self.Left.Eval()
        value2=self.Right.Eval()
        if int==type(value1)  and int==type(value2):
            return  value1**value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
    
    def transpilar(self):
        return str(self.Left) + " ^ " +  str(self.Right)

    def build_ast(self,productionList):
        pass

#--------------------------------------------------------------------------- #
#-----------------------Comparer Oper -------------------------------------- #
#--------------------------------------------------------------------------- #


class EqualNode(CompareNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context

        self.RT = None
        self.ET = None
    
    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        type1 = type(value1)
        type2 = type(value2)
        if type1 == type2:
            return  value1==value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)

    def transpilar(self):
        return str(self.Left) + " == " +  str(self.Right)

    def build_ast(self,productionList):
        pass
    
    
class NotEqualNode(CompareNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context

        self.RT = None
        self.ET = None
    
    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        if int==type(value1)  and int==type(value2):
            return  value1!=value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
    
    def transpilar(self):
        return str(self.Left) + " != " +  str(self.Right)


    def build_ast(self,productionList):
        pass
    
class LoENode(CompareNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
        self.RT = None
        self.ET = None

    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        type1 = type(value1)
        type2 = type(value2)
        if type1 == type2:
            return  value1<=value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
    
    def transpilar(self):
        return str(self.Left) + " <= " +  str(self.Right)

    def build_ast(self,productionList):
        pass

class GoENode(CompareNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context

        self.RT = None
        self.ET = None

    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        type1 = type(value1)
        type2 = type(value2)
        if type1 == type2:
            return  value1>=value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
        
    def transpilar(self):
        return str(self.Left) + " >= " +  str(self.Right)

    def build_ast(self,productionList):
        pass

class GreaterNode(CompareNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
        self.RT = None
        self.ET = None

    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        type1 = type(value1)
        type2 = type(value2)
        if type1 == type2:
            return  value1>value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
    
    def transpilar(self):
        return str(self.Left) + " > " +  str(self.Right)

    def build_ast(self,productionList):
        pass

class LessNode(CompareNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
        self.RT = None
        self.ET = None

    def Eval(self,context):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        type1 = type(value1)
        type2 = type(value2)
        if type1 == type2:
            return  value1<value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
        
    def transpilar(self):
        return str(self.Left) + " < " +  str(self.Right)

    def build_ast(self,productionList):
        pass
    

#--------------------------------------------------------------------------- #
#--------------------------Condicional ------------------------------------- #
#--------------------------------------------------------------------------- #

    
class AndNode(ClassNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
        self.RT = None
        self.ET = None

    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        type1 = type(value1)
        type2 = type(value2)
        if type1 == type2:
            return  value1 and value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
        
    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
    
    def transpilar(self):
        return str(self.Left) + " and " +  str(self.Right)

    def build_ast(self,productionList):
        pass

class OrNode(ClassNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
        self.RT = None
        self.ET = None

    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)
        if bool==type(value1)  and bool==type(value2):
            return  value1 and value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla
    
    def transpilar(self):
        return str(self.Left) + " or " +  str(self.Right)

    def validateNode(self,context):
        valid= self.Left.validateNode(context) or self.Right.validateNode(context)
        
    def build_ast(self,productionList):
        pass

# -------------------------------------------------------------------------
# Ciclos ------------------------------------------------------------------
# -------------------------------------------------------------------------

class LoopNode(ClassNode):
    def __init__(self,context:Context):
        self.Conditional=None
        self.Body=None
        self.context=context
    
        self.RT = None
        self.ET = None

    #hijo del break
    def breakValue(self):
        return self
    
    def Eval(self):
        while (self.Left.Eval()):
            newContext=self.context.create_hild("loop",self)
            self.Body.Eval(newContext)
            
    def transpilar(self):
        textcode = ""
        textcode += "while " + self.Conditional.transpilar() + ":"
        textcode += "\n \t"
        textcode += self.transpilar()

        return textcode
        
    def validateNode(self,context):
        valid= self.Conditional.validateNode(context) and self.Body.validateNode(context)
        
    def build_ast(self,productionList):
        pass
#--------------------------------------------------------------------------- #
#--------------------------Func Program ------------------------------------ #
#--------------------------------------------------------------------------- #


class ModifyNode(ClassNode):
    def __init__(self,context):
        self.leng_Type = None
        self.args = None
        self.context = context
    
        self.RT = None
        self.ET = None

    def Eval(self,context):
        valid= self.leng_Type.validateNode(context) 
        for item in self.args:
            item.validateNode(context)
        
        
    def validateNode(self,context):
        valid= self.leng_Type.validateNode(context) 
        for item in self.args:
            self.Right.validateNode(context)

    def transpilar(self):
        textcode = ""
        textcode += "modify("
        i = 0
        for arg in self.args:
            textcode += arg.transpilar()
            i+=1
            if i < len(self.args) - 1:
                textcode += ","
        
        textcode += ")"

        return textcode
        
    def build_ast(self,productionList):
        pass

#----------------------------------------------------------------
#--------------------------------------------------------------
#------------------------------------------------------------------
class CreateNode(ClassNode):
    def __init__(self,context):
        self.leng_Type = None
        self.args = None
        self.context = context
        
        self.RT = None
        self.ET = None

    def validateNode(self,context):
        valid= self.leng_Type.validateNode(context) 
        for item in self.args:
            item.validateNode(context)


    def transpilar(self):
        textcode = ""
        textcode += "create("
        i = 0
        for arg in self.args:
            textcode += arg.transpilar()
            i+=1
            if i < len(self.args) - 1:
                textcode += ","
        
        textcode += ")"

        return textcode

    def Eval(self):
        pass

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------

class DieNode(ClassNode):
    def __init__(self,context):
        self.leng_Type = None
        self.args = None
        self.context = context

        self.RT = None
        self.ET = None

    def validateNode(self,context):
        valid= self.leng_Type.validateNode(context) 
        for item in self.args:
            item.validateNode(context)
    
    def transpilar(self):
        textcode = ""
        textcode += "Die("
        i = 0
        for arg in self.args:
            textcode += arg.transpilar()
            i+=1
            if i < len(self.args) - 1:
                textcode += ","
        
        textcode += ")"

        return textcode
    
    def Eval(self,context):
        pass
    

class EvolveNode(ClassNode):
    def __init__(self,context):
        self.leng_Type = None
        self.args = None
        self.context = context

        self.RT = None
        self.ET = None

    def validateNode(self,context):
        valid= self.leng_Type.validateNode(context) 
        for item in self.args:
            item.validateNode(context)
    
    def transpilar(self):
        textcode = ""
        textcode += "Evolve("
        i = 0
        for arg in self.args:
            textcode += arg.transpilar()
            i+=1
            if i < len(self.args) - 1:
                textcode += ","
        
        textcode += ")"

        return textcode

    def Eval(self,context):
        pass

class AddNode(ClassNode):
    def __init__(self,context):
        self.leng_Type = None
        self.args = None
        self.context = context

        self.RT = None
        self.ET = None

    def validateNode(self,context):
        valid= self.leng_Type.validateNode(context) 
        for item in self.args:
            item.validateNode(context)
    
    def transpilar(self):
        textcode = ""
        textcode += "Add("
        i = 0
        for arg in self.args:
            textcode += arg.transpilar()
            i+=1
            if i < len(self.args) - 1:
                textcode += ","
        
        textcode += ")"

        return textcode

    def Eval(self,context):
        pass
    
class MoveNode(ClassNode):
    def __init__(self,context):
        self.leng_Type = None
        self.args = None
        self.context = context

        self.RT = None
        self.ET = None

    def validateNode(self,context):
        valid= self.leng_Type.validateNode(context) 
        for item in self.args:
            item.validateNode(context)

    def transpilar(self):
        textcode = ""
        textcode += "Move("
        i = 0
        for arg in self.args:
            textcode += arg.transpilar()
            i+=1
            if i < len(self.args) - 1:
                textcode += ","
        
        textcode += ")"

        return textcode

    def Eval():
        pass
    
class EatNode(ClassNode):
    def __init__(self,context):
        self.leng_Type = None
        self.args = None
        self.context = context

        self.RT = None
        self.ET = None

    def validateNode(self,context):
        valid= self.leng_Type.validateNode(context) 
        for item in self.args:
            item.validateNode(context)
    
    def transpilar(self):
        textcode = ""
        textcode += "transpilar("
        i = 0
        for arg in self.args:
            textcode += arg.transpilar()
            i+=1
            if i < len(self.args) - 1:
                textcode += ","
        
        textcode += ")"

        return textcode

    def Eval(self,context):
        pass


#-------------------------- Modificar----------------------------------

class ProgramNode(ClassNode):
    def __init__(self,context):
        self.ListStatement = None
        self.context = context

        self.RT = None
        self.ET = None

    def Eval(self):
        for statement in self.ListStatement:
            value = statement.Eval(self.context)
    
    def transpilar(self):
        textcode = ""
        for statement in self.ListStatement:
            textcode += statement.transpilar()
            textcode += "\n"

    def validateNode(self, context):
        for statement in self.ListStatement:
            if statement.validateNode(context):
                return False
            
    #["override_expr"],["let_dec"],["func_dec"],["var_reasign"],["print_stat"],["condictional_stat"],["loop_stat"],["lenguage_funtion"],["break_exp"],["return_exp"],["continue_exp"],["epsilon"]
    def build_ast(self,productionList,indexProduc=[0]):
        indexProduc[0]=0
        self.ListStatement=[]
        self.buildPosible()
        head=None
        while indexProduc[0]<len(productionList) :
            head=productionList[indexProduc].head
            indexProduc[0]+=1
            if head in self.posibleProductions:
                
                #arreglar esto
                node=self.posibleProductions[head]()
                #resolver el nodo
                node.build_ast(productionList,indexProduc)
                #agregarlo a los hijos
                self.ListStatement.append(node)
                
    
    def buildPosible(self):
        #arreglar esto
        self.posibleProductions={}
        
        self.posibleProductions["override_expr"]=OverrideNode
        self.posibleProductions["let_dec"]=LetNode
        self.posibleProductions["func_dec"]=FucNode
        self.posibleProductions["var_reasign"]=ReasignNode
        self.posibleProductions["print_stat"]=PrintNode
        self.posibleProductions["if_stat"]=IfNode
        self.posibleProductions["loop_stat"]=LoopNode
        #["die"],["modify"],["evolve"],["add"],["move"],["eat"],["create"]
        self.posibleProductions["die"]=DieNode
        self.posibleProductions["modify"]=ModifyNode
        self.posibleProductions["evolve"]=EvolveNode
        self.posibleProductions["add"]=AddNode
        self.posibleProductions["move"]=MoveNode
        self.posibleProductions["eat"]=EatNode
        self.posibleProductions["create"]=CreateNode
        
        self.posibleProductions["break_exp"]=BreakNode
        self.posibleProductions["return_exp"]=returnNode
        self.posibleProductions["continue_exp"]=continueNode
    
    
class StatementNode(ClassNode):
    def __init__(self,context):
        self.actionNode = None
        self.context = context

        self.RT = None
        self.ET = None

    def Eval(self,context):
        self.actionNode.Eval(self.context)

    def transpilar(self):
        return self.actionNode.transpilar()

    
    def validateNode(self, context):
        if not self.actionNode.validateNode(context):
            return False


class BreakNode(StatementNode):
    def __init__(self, context):
        self.context = context
        self.RT = None
        self.ET = None


    def Eval(self, context):
        return

    def transpilar(self):
        return "break"
    
    def validateNode(self, context):
        contexttemp = context
        while True:
            name = contexttemp.name
            breakCheck = contexttemp.breakCheck
            classNode = contexttemp.classNode

            if name == "loop":
                if breakCheck == False:
                    context.breakCheck = True
                    return True

            if contexttemp.fatherContext == None:
                break

            contexttemp = contexttemp.fatherContext

        return False




class LetNode(StatementNode):
    def __init__(self, context):
        self.type = None
        self.idnode = None
        self.val = None
        self.context = context

        self.RT = None
        self.ET = None

    def Eval(self,context):
        return
    
    def validateNode(self, context):
        if not self.idnode is IdNode or not valNode(self.val):
            return False

        validate = self.idnode.validateNode(context) and self.val.validateNode(context)
        return validate

    def transpilar(self):
        return "Let " + str(self.type) + " " + str(self.idnode) + " = " + self.val
    
    def build_ast(self,productionList,indexProduc):
        
        #agregado el tipo "sale como token todavia no es grave"
        self.type = productionList[indexProduc][0].components[1]
        #creando id
        idn=IdNode()
        #self,id,funcOrVar,defineOrCall,valType=None
        idn.build_ast(productionList[indexProduc][0].components[1].value,"var","define",self.type)
        
        self.idnode = idn
        self.ET=self.idnode.RT
        indexProduc[0]+=1
        self.val=eatExpression(productionList,indexProduc)
        self.RT=self.val.RT
    
# Revisar como crearlo

def eatExpression(productionList,indexProduc):
    if len(productionList[indexProduc][0].components)==3:
        component=productionList[indexProduc][0][1]
        if component in expresionDicc:
            #creamos el node
            node =expresionDicc[component]()
            
            indexProduc[0]+=1
            node.build_ast(productionList,indexProduc)
            return node
        elif component=="comparer":
            indexProduc[0]+=1
            return eatComparer(productionList,indexProduc)
    else:
        indexProduc[0]+=1
        return eatTerm(productionList,indexProduc)

def eatComparer(productionList,indexProduc):
    component=productionList[indexProduc][0][0]
    #buscando cual comparador es
    node =expresionDicc[component]()
    
    indexProduc[0]+=1
    node.build_ast(productionList,indexProduc)
    return node

def eatTerm(productionList,indexProduc):
    if len(productionList[indexProduc][0].components)==3:
        component=productionList[indexProduc][0][1]
        if component in termDicc:
            #creamos el node
            node =expresionDicc[component]()
            
            indexProduc[0]+=1
            node.build_ast(productionList,indexProduc)
            return node
    else:
        indexProduc[0]+=1
        return eatAtom(productionList,indexProduc)

def eatAtom(productionList,indexProduc):
    component=productionList[indexProduc][0][0]
    if component in termDicc:
        #buscando cual atomo es
        node =expresionDicc[component]()

        indexProduc[0]+=1
        node.build_ast(productionList,indexProduc)
        return node
    elif component=="func_call":
        indexProduc[0]+=1
        if len(productionList[indexProduc][0].component)==4:
            node=func_callNode()
            node.build_ast(productionList,indexProduc)
            return node
        elif productionList[indexProduc][0].component=="dic_func":
            indexProduc[0]+=2
            return eatDiccFunc()
        elif productionList[indexProduc][0].component=="matrix_func":
            indexProduc[0]+=1
            eatMatrixFunc()

def eatMatrixFunc(productionList,indexProduc):
    pass

def eatDiccFunc(productionList,indexProduc):
    component=productionList[indexProduc][0][0]
    node =expresionDicc[component]()
    
    indexProduc[0]+=1
    node.build_ast(productionList,indexProduc)
    return node
    
class Condictional_statNode(StatementNode):
    def __init__(self,context):
        self.condition = None
        self.context = context

        self.RT = None
        self.ET = None

    def Eval(self,context):
        return self.condition.Eval()

    def transpilar(self):
        textcode = ""
        textcode += self.condition.tranpilar()
        return textcode

    def validateNode(self, context):
        return self.validateNode(self.condition)

class IfNode(StatementNode):
    def __init__(self,context):
        self.condition = None
        self.ListStatements = None
        #self.elsenode = None
        #self.elifnode = None
        self.context = context

        self.RT = None
        self.ET = None

    def Eval(self,context):
        if self.condition.Eval(self.context):
            for statement in self.ListStatements:
                statement.Eval(self.context)

        else:
            self.elsenode.Eval()
        
        if self.elifnode != None:
            self.elifnode.Eval()
    
    def transpilar(self):
        textcode = ""
        textcode += "if "
        textcode += self.condition.transpilar()
        textcode += ":"
        for statement in self.ListStatements:
            textcode += "\n \t"
            textcode += statement.transpilar
        
        textcode += "\n"
        textcode += self.elsenode.transpilar()

        if self.elifnode != None:
            textcode += "\n"
            textcode += self.elifnode.transpilar()

        return textcode


    def validateNode(self, context):
        validate1 = self.condition.validateNode(self.context)
        if not validate1:
            return False
        for statement in self.ListStatements:
            if not statement.validateNode(self.context):
                return False

        validate2 = self.elsenode.validateNode(self.context)
        if not validate2:
            return False

        if self.elifnode != None:
            validate3 = self.elifnode.validateNode(self.context)
            if not validate3:
                return False

        return True


class ElifNode(StatementNode):
    def __init__(self,context):
        self.condition = None
        self.ListStatements = None
        self.elsenode = None
        self.elifnode = None
        self.context = context

        self.RT = None
        self.ET = None

    def Eval(self,context):
        if self.condition.Eval(self.context):
            for statement in self.ListStatements:
                statement.Eval(self.context)

        else:
            self.elsenode.Eval()
        
        if self.elifnode != None:
            self.elifnode.Eval()
    
    def transpilar(self):
        textcode = ""
        textcode += "elif "
        textcode += self.condition.transpilar()
        textcode += ":"
        for statement in self.ListStatements:
            textcode += "\n \t"
            textcode += statement.transpilar
        
        textcode += "\n"
        textcode += self.elsenode.transpilar()

        if self.elifnode != None:
            textcode += "\n"
            textcode += self.elifnode.transpilar()

        return textcode

    def validateNode(self, context):
        validate1 = self.condition.validateNode(self.context)
        if not validate1:
            return False
        for statement in self.ListStatements:
            if not statement.validateNode(self.context):
                return False

        validate2 = self.elsenode.validateNode(self.context)
        if not validate2:
            return False

        if self.elifnode != None:
            validate3 = self.elifnode.validateNode(self.context)
            if not validate3:
                return False

        return True


# Preguntar
class elseNode(StatementNode):
    def __init__(self,context):
        self.ListStatement = None
        
        self.RT = None
        self.ET = None


    def Eval(self,context):
        for statement in self.ListStatement:
            statement.Eval(self.context)

    def transpilar(self):
        textcode = ""
        textcode += "else:"
        textcode += "\n"
        
        for statement in self.ListStatements:
            textcode += "\n \t"
            textcode += statement.transpilar
        
        return textcode


    def validateNode(self, context):
        if not self.context.name == "if" and not self.context.name == "elif":
            return False

        for statement in self.ListStatement:
            validate = statement.validateNode(self.context)
            if not validate:
                return False
            
        return True


# Faltantes

class FucNode(StatementNode):
    def __init__(self,context):
        self.name = None
        self.args = None
        self.context = context

        self.RT = None
        self.ET = None

    def Eval(self,context):
        return self.Left + self.Right

class func_callNode(StatementNode):
    def __init__(self,value = None,hijos = None):
        super().__init__(value,hijos)
        
        self.RT = None
        self.ET = None

        try:
            self.Left = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.Right = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
            
    def Eval(self):
        return self.Left + self.Right
    
class PrintNode(StatementNode):
    def __init__(self,context):
        self.name = "print"
        self.args = None
        self.context = context

        self.RT = None
        self.ET = None

    def Eval(self,context):
        val = self.args[0].Eval(self.context)
        #print(val)
        return
    
    


# ------------------------------------------------------------------------------- #
# ----------------------- Nodes Terminator -------------------------------------- #
# ------------------------------------------------------------------------------- #

class vectorialNode(StatementNode):
    def __init__(self,context):
        self.ejex = None
        self.ejey = None
        self.context = context

        self.RT = None
        self.ET = None

    def Eval(self,context):
        return (self.ejex,self.ejey)
    
    def transpilar(self):
        return "("+str(self.ejex) + "," +  str(self.ejey)+")"

    def validateNode(self, context):
        return isnumeric(self.ejex) and isnumeric(self.ejey)

class IdNode(StatementNode):
    def __init__(self,context):
        self.id = None
        self.context = context

        self.RT = None
        self.ET = None

    def Eval(self):
        return self.id

    def transpilar(self):
        return str(self.id)

    def validateNode(self, context):
        return self.id is str
    
    #primer termino 
    def build_ast(self,id,funcOrVar,defineOrCall,valType=None):
        self.id=id
        self.RT=valType
        self.funcOrVar=funcOrVar
        self.defineOrCall=defineOrCall
        
        

class NumberNode(StatementNode):
    def __init__(self,context):
        self.val = None
        self.context = context

        self.RT = None
        self.ET = None

    def Eval(self,context):
        return self.val

    def transpilar(self):
        return str(self.val)

    def validateNode(self, context):
        return isnumeric(self.val)


class ChainNode(StatementNode):
    def __init__(self,context):
        self.chain = None
        self.context = context

        self.RT = None
        self.ET = None

    def Eval(self,context):
        return chain

    def transpilar(self):
        return str(self.chain)

    def validateNode(self, context):
        return self.chain is str

class TrueNode(StatementNode):
    def __init__(self,context):
        self.context = context

        self.RT = None
        self.ET = None

    def Eval(self):
        return True

    def transpilar(self):
        return str(True)

    def validateNode(self, context):
        return True

class FalseNode(StatementNode):
    def __init__(self,context):
        self.context = context

        self.RT = None
        self.ET = None

    def Eval(self):
        return False

    def transpilar(self):
        return str(False)

    def validateNode(self, context):
        return True

class NoneNode(StatementNode):
    def __init__(self,context):
        self.context = context

        self.RT = None
        self.ET = None

    def Eval(self, context):
        return None

    def transpilar(self):
        return str(None)

    def validateNode(self, context):
        return True

# ---------------------------------------------------------------------------------------------
# ---------------------------------- Funciones de apoyo ---------------------------------------
# ---------------------------------------------------------------------------------------------

def isnumeric(num):
    return num is Double or num is int or num is float


def valNode(node):
    if node is OperatorNode:
        return True
    
    elif node is NumberNode:
        return True

    elif node is CompareNode:
        return True

    return False


#-------------------------------------dics------------------------------------
atomDicc={}
#[TokeTypes.tokID],["func_call"],[TokeTypes.tokNumber],[TokeTypes.tokChain],[TokeTypes.tokNone],[TokeTypes.tokChain],[TokeTypes.tokTrue],[TokeTypes.tokFalse],["dic_func"],["epsilon"]
def fillAtom():
    atomDicc[TokeTypes.tokID]=IdNode
    
    atomDicc[TokeTypes.tokNumber]=NumberNode
    atomDicc[TokeTypes.tokChain]=ChainNode
    atomDicc[TokeTypes.tokNone]=NoneNode
    atomDicc[TokeTypes.tokTrue]=TrueNode
    atomDicc[TokeTypes.tokFalse]=FalseNode
    #atomDicc["dic_dec"]=dic_func?
    
expresionDicc={}
def fillExpresion():
    expresionDicc[TokeTypes.tokSub]=FalseNode
    expresionDicc[TokeTypes.tokSum]=FalseNode
    
termDicc={}
def fillTerm():
    termDicc[TokeTypes.tokMul]=FalseNode
    termDicc[TokeTypes.tokDiv]=FalseNode

#[TokeTypes.tokEqual],[TokeTypes.tokNot],[TokeTypes.tokNotEqual],[TokeTypes.tokGreaterOrEqual],[TokeTypes.tokGreater],[TokeTypes.tokLess],[TokeTypes.tokLessOrEqual],[TokeTypes.tokAnd],[TokeTypes.tokOr]
comparerDicc={}
def fillComparer():
    comparerDicc[TokeTypes.tokEqual]=FalseNode
    comparerDicc[TokeTypes.tokNot]=FalseNode
    comparerDicc[TokeTypes.tokNotEqual]=FalseNode
    comparerDicc[TokeTypes.tokGreaterOrEqual]=FalseNode
    comparerDicc[TokeTypes.tokGreater]=FalseNode
    comparerDicc[TokeTypes.tokLess]=FalseNode
    comparerDicc[TokeTypes.tokLessOrEqual]=FalseNode
    comparerDicc[TokeTypes.tokAnd]=FalseNode
    comparerDicc[TokeTypes.tokOr]=FalseNode

diccFunDicc={}
def fillDiccFun():
    diccFunDicc["search_dic"]=RecieveDiccNode
    diccFunDicc["recieve_dic"]=SearchDiccNode
    diccFunDicc["insert_dic"]=InsertDiccNode
    
diccMatrixFuncVec={}
def fillDiccFunVec():
    diccMatrixFuncVec[TokeTypes.tokMSum]=matrixSumNode
    diccMatrixFuncVec[TokeTypes.tokMSub]=matrixSubNode
    
diccMatrixFuncEsc={}
def fillDiccFunVec():
    diccMatrixFuncEsc[TokeTypes.tokMMul]=matrixMulNode
    diccMatrixFuncEsc[TokeTypes.tokMDiv]=matrixDivNode