from ast import arg
from calendar import TextCalendar
from cgitb import text
from dataclasses import dataclass
from distutils.log import error
from inspect import ArgSpec
from itertools import chain
from lib2to3.pytree import Node
from multiprocessing import Condition, context
from ntpath import join
from pickle import FALSE
from platform import node
from tokenize import Double
from unittest import result
from unittest.mock import NonCallableMagicMock
from webbrowser import Opera
from wsgiref import validate

import enum

from compGlobals import TokeTypes 
import enum

from numpy import true_divide

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

    def build_ast(productionList):
        pass

class CompareNode(ClassNode):
    def Eval(self,context):
        pass
    
    def validateNode(self,context):
        pass
    
    def transpilar(self):
        pass

    def build_ast(productionList):
        pass

class Context():
    def __init__(self,name,classNode,fatherContext=None,breakCheck=False):
        
        self.diccVarContext = {}
        self.diccFuncContext = {}
        self.diccFunStatement = {} 
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
        if var in self.diccFuncContext or (self.fatherContext!=None and self.fatherContext.checkFun(var,typeList)):
            varAtributes=self.retFun(var)
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
            self.diccFuncContext[var]=[var,typeList]
            return True
        return False
    
    def define_statement(self,var,statementNode):
        if var in self.define_statement:
            return False
        self.define_statement[var] = statementNode
        return True

    #este metodo devuelve una lista con el formator [name,type]
    def retVar(self,var):
        current=self
        while current!=None:
            if self==None: return None
            if var in current.diccVarContext:
                return current.diccVarContext[var]
            current=self.fatherContext
    
    #este metodo devuelve una lista con el formator [name,arg1Type,arg2Type....,argNType]
    def retFun(self,var):
        current=self
        while current!=None:
            if self==None: return None
            if var in current.diccFuncContext:
                return current.diccFuncContext[var]
            current=self.fatherContext
    
    def retStatement(self,var):
        if var in self.diccFunStatement:
            return self.diccFunStatement[var]

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

    def overrideVar(self,varname,vartype,varvalue):
        if varname in self.diccVarContext:
            dicvar = self.diccVarContext[varname]
            typeold = dicvar[1]
            if typeold != vartype:
                return False
            
            self.diccVarContext[varname] = [varname,vartype,varvalue]
            return True
        
        return False

    def overrideFun(self,nameF,nameNF):
        if nameF in self.diccFuncContext and nameNF in self.diccFuncContext:
            val = self.diccFuncContext[nameNF]
            self.diccFuncContext[nameF] = val
            return True
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

        self.ReturnType = None
        self.EspecterType = None
    
    def Eval(self):
        value1=self.Left.Eval(self.context)
        value2=self.Right.Eval(self.context)

        if value1.isnumeric() and value2.isnumeric():
            return  value1+value2
        #return error de tipo no puedo sumar eso en linea y columnas bla bla bla

    def transpilar(self):
        return str(self.Left) + " + " +  str(self.Right)

    def checkTypes(self):
        type1 = self.Left.ReturnType
        type2 = self.Left.ReturnType
        return type1 == type2 and not type1 != None and self.ReturnType == int

    def validateNode(self,context):
        valid= self.Left.validateNode(context) and self.Right.validateNode(context)
        return valid
        
    def build_ast(self,productionList,indeProduc):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET

class SubNode(OperatorNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context

        self.ReturnType = None
        self.EspecterType = None
    
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

    def checkTypes(self):
        type1 = self.Left.ReturnType
        type2 = self.Left.ReturnType
        return type1 == type2 and not type1 != None and self.ReturnType == int

    def build_ast(self,productionList,indeProduc):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET
    

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

    def checkTypes(self):
        type1 = self.Left.ReturnType
        type2 = self.Left.ReturnType
        return type1 == type2 and not type1 != None and self.ReturnType == int

    def build_ast(self,productionList,indeProduc):
        self.Left=eatFactor(productionList,indeProduc,context)
        self.Right=eatTerm(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET
    
class DivNode(OperatorNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context

        self.ReturnType = None
        self.EspecterType = None
    
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

    def checkTypes(self):
        type1 = self.Left.ReturnType
        type2 = self.Left.ReturnType
        return type1 == type2 and not type1 != None and self.ReturnType == int

    def build_ast(self,productionList,indeProduc):
        self.Left=eatFactor(productionList,indeProduc,context)
        self.Right=eatTerm(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET

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

    def checkTypes(self):
        type1 = self.Left.ReturnType
        type2 = self.Left.ReturnType
        return type1 == type2 and not type1 != None and self.ReturnType == int

    def build_ast(self,productionList,indeProduc):
        self.Left=eatFactor(productionList,indeProduc,context)
        self.Right=eatTerm(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET

class PowNode(OperatorNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context

        self.ReturnType = None
        self.EspecterType = None
    
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

    def checkTypes(self):
        type1 = self.Left.ReturnType
        type2 = self.Left.ReturnType
        return type1 == type2 and not type1 != None and self.ReturnType == int

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

        self.ReturnType = None
        self.EspecterType = None
    
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

    def checkTypes(self):
        type1 = self.Left.ReturnType
        type2 = self.Left.ReturnType
        return type1 == type2 and not type1 != None and self.ReturnType == bool

    def build_ast(self,productionList,indeProduc):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET
    
    
class NotEqualNode(CompareNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context

        self.ReturnType = None
        self.EspecterType = None
    
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

    def checkTypes(self):
        type1 = self.Left.ReturnType
        type2 = self.Left.ReturnType
        return type1 == type2 and not type1 != None and self.ReturnType == bool

    def build_ast(self,productionList,indeProduc):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET
    
class LoENode(CompareNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
        self.ReturnType = None
        self.EspecterType = None

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

    def checkTypes(self):
        type1 = self.Left.ReturnType
        type2 = self.Left.ReturnType
        return type1 == type2 and not type1 != None and self.ReturnType == bool

    def build_ast(self,productionList,indeProduc):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET

class GoENode(CompareNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context

        self.ReturnType = None
        self.EspecterType = None

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

    def checkTypes(self):
        type1 = self.Left.ReturnType
        type2 = self.Left.ReturnType
        return type1 == type2 and not type1 != None and self.ReturnType == bool

    def build_ast(self,productionList,indeProduc):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET

class GreaterNode(CompareNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
        self.ReturnType = None
        self.EspecterType = None

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

    def checkTypes(self):
        type1 = self.Left.ReturnType
        type2 = self.Left.ReturnType
        return type1 == type2 and not type1 != None and self.ReturnType == bool

    def build_ast(self,productionList,indeProduc):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET

class LessNode(CompareNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
        self.ReturnType = None
        self.EspecterType = None

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

    def checkTypes(self):
        type1 = self.Left.ReturnType
        type2 = self.Left.ReturnType
        return type1 == type2 and not type1 != None and self.ReturnType == bool

    def build_ast(self,productionList,indeProduc):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET
    

#--------------------------------------------------------------------------- #
#--------------------------Condicional ------------------------------------- #
#--------------------------------------------------------------------------- #

    
class AndNode(ClassNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
        self.ReturnType = None
        self.EspecterType = None

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

    def checkTypes(self):
        type1 = self.Left.ReturnType
        type2 = self.Left.ReturnType
        return type1 == type2 and not type1 == bool and self.ReturnType == bool

    def build_ast(self,productionList,indeProduc):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET

class OrNode(ClassNode):
    def __init__(self,context):
        self.Left=None
        self.Right=None
        self.context=context
    
        self.ReturnType = None
        self.EspecterType = None

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
    
    def checkTypes(self):
        type1 = self.Left.ReturnType
        type2 = self.Left.ReturnType
        return type1 == type2 and not type1 == bool and self.ReturnType == bool

    def build_ast(self,productionList,indeProduc):
        self.Left=eatTerm(productionList,indeProduc,context)
        self.Right=eatExpression(productionList,indeProduc,context)
        self.RT=self.Left.RT
        self.ET=self.Right.ET

# -------------------------------------------------------------------------
# Ciclos ------------------------------------------------------------------
# -------------------------------------------------------------------------

class LoopNode(ClassNode):
    def __init__(self,context:Context):
        self.Conditional=None
        self.Body=None
        self.context=context
    
        self.ReturnType = None
        self.EspecterType = None

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
        return valid
        
    def checkTypes(self):
        return self.Conditional.checkTypes()

    def build_ast(self,productionList,indexProduc):
        indexProduc[0]+=1
        node=eatExpression(productionList,indexProduc,self.context)
        
        
        node.build_ast(productionList,indexProduc)
        self.Conditional=node
        
        newcontext=self.context.create_hild("loop",self)
        node=ProgramNode(newcontext)
        node.build_ast(productionList,indexProduc)
        self.Body=node
#--------------------------------------------------------------------------- #
#--------------------------Func Program ------------------------------------ #
#--------------------------------------------------------------------------- #


class ModifyNode(ClassNode):
    def __init__(self,context):
        self.id = None
        self.args = None
        self.context = context
    
        self.ReturnType = None
        self.EspecterType = None

    def Eval(self,context):
        valid= self.id.validateNode(context) 
        for item in self.args:
            item.validateNode(context)
        
        
    def validateNode(self,context):
        valid= self.id.validateNode(context) 
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

    def checkTypes(self):
        return self.context.checkFun("modify", [self.id] + self.args)
        
    def build_ast(self,productionList):
        pass

#----------------------------------------------------------------
#--------------------------------------------------------------
#------------------------------------------------------------------
class CreateNode(ClassNode):
    def __init__(self,context):
        self.id = None
        self.args = None
        self.context = context
        
        self.ReturnType = None
        self.EspecterType = None

    def validateNode(self,context):
        valid= self.id.validateNode(context) 
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

    def checkTypes(self):
        return self.context.checkFun("create", [self.id] + self.args)

    def Eval(self):
        pass

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------

class DieNode(ClassNode):
    def __init__(self,context):
        self.id = None
        self.args = None
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def validateNode(self,context):
        valid= self.id.validateNode(context) 
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
    
    def checkTypes(self):
        return self.context.checkFun("die", [self.id] + self.args)

    def Eval(self,context):
        pass
    

class EvolveNode(ClassNode):
    def __init__(self,context):
        self.id = None
        self.args = None
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def validateNode(self,context):
        valid= self.id.validateNode(context) 
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

    def checkTypes(self):
        return self.context.checkFun("evolve", [self.id] + self.args)

    def Eval(self,context):
        pass

class AddNode(ClassNode):
    def __init__(self,context):
        self.id = None
        self.args = None
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def validateNode(self,context):
        valid= self.id.validateNode(context) 
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

    def checkTypes(self):
        return self.context.checkFun("evolve", [self.id] + self.args)

    def Eval(self,context):
        pass
    
class MoveNode(ClassNode):
    def __init__(self,context):
        self.id = None
        self.args = None
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def validateNode(self,context):
        valid= self.id.validateNode(context) 
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

    def checkTypes(self):
        return self.context.checkFun("move", [self.id] + self.args)

    def Eval(self):
        pass
    
class EatNode(ClassNode):
    def __init__(self,context):
        self.id = None
        self.args = None
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def validateNode(self,context):
        valid= self.id.validateNode(context) 
        for item in self.args:
            item.validateNode(context)
    
    def transpilar(self):
        textcode = ""
        textcode += "eat("
        i = 0
        for arg in self.args:
            textcode += arg.transpilar()
            i+=1
            if i < len(self.args) - 1:
                textcode += ","
        
        textcode += ")"

        return textcode

    def checkTypes(self):
        return self.context.checkFun("eat", [self.id] + self.args)

    def Eval(self,context):
        pass


#-------------------------- Modificar----------------------------------

class ProgramNode(ClassNode):
    def __init__(self,context):
        self.ListStatement = None
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def Eval(self):
        for statement in self.ListStatement:
            value = statement.Eval(self.context)
    
    def transpilar(self):
        textcode = ""
        for statement in self.ListStatement:
            textcode += statement.transpilar()
            textcode += "\n"

    def checkTypes(self):
        return True

    def validateNode(self, context):
        for statement in self.ListStatement:
            if statement.validateNode(context):
                return False

    def build_ast(self,productionList,indexProduc=[0]):
        indexProduc[0]=0
        self.ListStatement=[]
        self.buildPosible()
        head=None
        while indexProduc[0]<len(productionList) :
            head=productionList[indexProduc].head
            if productionList[indexProduc].components[0]==TokeTypes.tokClosedBracket:
                break
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
        self.posibleProductions["return_exp"]=ReturnNode
        self.posibleProductions["continue_exp"]=ContinueNode

class StatementNode(ClassNode):
    def __init__(self,context):
        self.actionNode = None
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def Eval(self,context):
        self.actionNode.Eval(self.context)

    def transpilar(self):
        return self.actionNode.transpilar()

    def checkTypes(self):
        return self.actionNode.checkTypes()
    
    def validateNode(self, context):
        if not self.actionNode.validateNode(context):
            return False


class BreakNode(StatementNode):
    def __init__(self, context):
        self.context = context
        self.ReturnType = None
        self.EspecterType = None


    def Eval(self, context):
        return

    def transpilar(self):
        return "break"

    def checkTypes(self):
        return True
    

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

    def build_ast(self,productionList,indexProduc):
        indexProduc[0]+=1
        #esto hay que implementarlo ya que el el break al crease solo guarda a su hijo como el nodo loop mas cercano
        #esto seria buscar en el contexto



class LetNode(StatementNode):
    def __init__(self, context):
        self.type = None
        self.idnode = None
        self.val = None
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def Eval(self,context):
        self.context.define_var(self.idnode.name, self.type, self.val)
    
    def checkTypes(self):
        if not self.idnode.checkTypes():
            return False
        return self.type == type(self.val) and self.ReturnType == type(self.val)

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
        idn=IdNode(self.context)
        #self,id,funcOrVar,defineOrCall,valType=None
        idn.build_ast(productionList[indexProduc][0].components[1].value,"var","define",self.type)
        
        self.idnode = idn
        self.ET=self.idnode.RT
        indexProduc[0]+=1
        self.val=eatExpression(productionList,indexProduc,context)
        self.RT=self.val.RT
# Revisar como crearlo

    
class Condictional_statNode(StatementNode):
    def __init__(self,context):
        self.condition = None
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def Eval(self,context):
        return self.condition.Eval()

    def transpilar(self):
        textcode = ""
        textcode += self.condition.tranpilar()
        return textcode

    def checkTypes(self):
        return self.condition.checkTypes()

    def validateNode(self, context):
        return self.validateNode(self.condition)

class IfNode(StatementNode):
    def __init__(self,context):
        self.condition = None
        self.ListStatements = None
        #self.elsenode = None
        #self.elifnode = None
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

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

    def checkTypes(self):
        return self.condition.checkTypes()

    def validateNode(self, context):
        validate1 = self.condition.validateNode(self.context)
        if not validate1:
            return False
        for statement in self.ListStatements:
            if not statement.validateNode(self.context):
                return False

        #validate2 = self.elsenode.validateNode(self.context)
        #if not validate2:
        #    return False

        #if self.elifnode != None:
        #    validate3 = self.elifnode.validateNode(self.context)
        #    if not validate3:
        #        return False

        return True

    def build_ast(self,productionList,indexProduc):
        
        
        indexProduc[0]+=1
        self.condition = eatExpression(productionList,indexProduc,self.context)
        
        #indexProduc[0]+=1 #? esto va aqui?
        self.ListStatements = ProgramNode(productionList,indexProduc,self.context)


#class ElifNode(StatementNode):
#    def __init__(self,context):
#        self.condition = None
#        self.ListStatements = None
#        self.elsenode = None
#        self.elifnode = None
#        self.context = context
#
#        self.ReturnType = None
#        self.EspecterType = None
#
#    def Eval(self,context):
#        if self.condition.Eval(self.context):
#            for statement in self.ListStatements:
#                statement.Eval(self.context)
#
#        else:
#            self.elsenode.Eval()
#        
#        if self.elifnode != None:
#            self.elifnode.Eval()
#    
#    def transpilar(self):
#        textcode = ""
#        textcode += "elif "
#        textcode += self.condition.transpilar()
#        textcode += ":"
#        for statement in self.ListStatements:
#            textcode += "\n \t"
#            textcode += statement.transpilar
#        
#        textcode += "\n"
#        textcode += self.elsenode.transpilar()
#
#        if self.elifnode != None:
#            textcode += "\n"
#            textcode += self.elifnode.transpilar()
#
#        return textcode
#
#    def validateNode(self, context):
#        validate1 = self.condition.validateNode(self.context)
#        if not validate1:
#            return False
#        for statement in self.ListStatements:
#            if not statement.validateNode(self.context):
#                return False
#
#        validate2 = self.elsenode.validateNode(self.context)
#        if not validate2:
#            return False
#
#        if self.elifnode != None:
#            validate3 = self.elifnode.validateNode(self.context)
#            if not validate3:
#                return False
#
#        return True
#
#
## Preguntar
#class elseNode(StatementNode):
#    def __init__(self,context):
#        self.ListStatement = None
#        
#        self.ReturnType = None
#        self.EspecterType = None
#
#
#    def Eval(self,context):
#        for statement in self.ListStatement:
#            statement.Eval(self.context)
#
#    def transpilar(self):
#        textcode = ""
#        textcode += "else:"
#        textcode += "\n"
#        
#        for statement in self.ListStatements:
#            textcode += "\n \t"
#            textcode += statement.transpilar
#        
#        return textcode
#
#
#    def validateNode(self, context):
#        if not self.context.name == "if" and not self.context.name == "elif":
#            return False
#
#        for statement in self.ListStatement:
#            validate = statement.validateNode(self.context)
#            if not validate:
#                return False
#            
#        return True
#
#

class ReturnNode(StatementNode):
    def __init__(self, context):
        self.val = None
        self.context = context


    
    def validateNode(self,context):
        contexttemp = context
        while contexttemp != None:
            classNodeFather = contexttemp.classNode is FucNode
            if classNodeFather:
                return True
            contexttemp = contexttemp.fatherContext

        return False
    
    def transpilar(self):
        if self.value == None:
            return "return"
        return "return " + str(self.val)

    def Eval(self,context):
        pass

    def checkTypes(self):
        return True

    def build_ast(productionList):
        pass

class ContinueNode(StatementNode):
    def __init__(self, context):
        self.cicle = None
        self.context = context

    
    def validateNode(self,context):
        contexttemp = context
        while contexttemp != None:
            classNodeFather = contexttemp.classNode is FucNode
            if classNodeFather:
                return True
            contexttemp = contexttemp.fatherContext

        return False
    
    def transpilar(self):
        return "continue"

    def Eval(self,context):
        self.cicle.Eval(context)
    
    def checkTypes(self):
        return True

    def build_ast(productionList):
        pass

class OverrideNode(StatementNode):
    def __init__(self, context):
        self.type = None
        self.metodo = None
        self.newmetodo = None

        self.context = context
        self.state1 = None
        self.state2 = None

    
    def validateNode(self,context):
        self.state1 = self.context.retFun(self.metodo)
        self.state2 = self.context.retFun(self.newmetodo)
        return self.state1 != None and self.state2 != None
    
    def transpilar(self):
        return "override " + str(type(self.type)) + " " + self.metodo + " " + self.newmetodo

    def Eval(self,context):
        self.context.overrideFun(self.metodo,self.newmetodo)
    
    def checkTypes(self):
        return True

    def build_ast(productionList):
        pass

class ReasignNode(StatementNode):
    def __init__(self, context):
        self.id = None
        self.value = None
        self.context = context

        self.name = None
        self.type = None
        self.valueant = None

    
    def validateNode(self,context):
        result = self.context.retVar(self.value)
        if result == None:
            return False
        
        name, typevar, value = result
        self.name = name
        self.type = typevar
        self.valueant = value
        

    def transpilar(self):
        return self.id.transpilar() + " = " + self.value

    def Eval(self,context):
        self.context.redeclareVar(self.name,type(self.value),self.value)
    
    def checkTypes(self):
        return self.type == type(self.value)

    def build_ast(productionList):
        pass



class func_callNode(StatementNode):
    def __init__(self,context):
        self.name = None
        self.args = None
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def validateNode(self,context):
        valueargs = []
        for val in self.args:
            if not val.validate(context):
                return False
            valueargs.append(val.Eval(context))

        
        typs = []
        for arg in valueargs:
            typs.append(arg)

        state = self.context.checkFun(self.name,typs)

        if not state:
            return False

        return True
    
    def transpilar(self):
        textcode = ""
        textcode += self.name
        textcode += "("
        i = 0
        for arg in self.args:
            if i != 0:
                textcode += ","
            textcode += arg.transpilar()
            i += 1
        textcode += ")"

    def Eval(self,context):
        valueargs = []
        for val in self.args:
            valueargs.append(val.Eval(context))

        #reasignar valores del contexto
        ret = self.context.retFun(self.name)
        statement = self.context.retStatement(self.name)

        for i in range(0,len(valueargs)-1):
            statement.context.overrideVar(self.name, ret[1][i], valueargs[i])

        return statement.Eval(statement.context)
            
    def checkTypes(self):
        typs = []
        for arg in self.args:
            typs.append(type(arg))

        state = self.context.checkFun(self.name,typs)

        if not state:
            return False

        return True

    def build_ast(self,productionList,indexProduc):
        indexProduc[0]+=1
        self.condition = eatExpression(productionList,indexProduc,self.context)
        
        #indexProduc[0]+=1 #? esto va aqui?
        self.ListStatements = ProgramNode(productionList,indexProduc,self.context)

class FucNode(StatementNode):
    def __init__(self,context):
        self.argstypes = None
        self.argsid = None
        self.name = None
        self.node_statements = None
        self.context = context
        
        self.ReturnType = None
        self.EspecterType = None

    def validateNode(self,context):
        state = self.context.define_func(self.name,self.argstypes)
        if state == None:
            return False

        for idvar in self.argsid:
            if not idvar.validateNode(context):
                return False

        for i in range(0,len(self.argsid)-1):
            self.context.define_var(self.argsid[i].name, self.argstypes[i], None)
        
        return self.node_statements.validateNode(context)
    
    def transpilar(self):
        textcode = ""
        textcode += self.name
        textcode += "("

        i = 0
        for arg in self.args:
            if i != 0:
                textcode += ","
            textcode += arg.transpilar()
            i += 1
        
        textcode += "):"
        codestatement = self.node_statements.transpilar()
        temp = codestatement.split("\n")

        for line in temp:
            textcode += "\n\t " + line

        return textcode

    def Eval(self,context):
        self.context.define_statement(self.name,self.node_statements)

    def checkTypes(self):
        return True

    def build_ast(self,productionList,indexProduc):
        
        #creando id
        idn=IdNode(self.context)
        #self,id,funcOrVar,defineOrCall,valType=None
        idn.build_ast(productionList[indexProduc][0].components[1],"func","define",None)
        
        self.idnode = idn
        #esta parte busca los parametros 
        indexProduc[0]+=1
        argsss=eatArgList(productionList,indexProduc,context)
        self.argsid=argsss[1]
        self.argstypes=argsss[0]
        indexProduc[0]+=2
        self.RT= eatType(productionList,indexProduc,context)
        indexProduc[0]+=1
        newcontext=self.context.create_hild("func",self)
        node=ProgramNode(newcontext)
        node.build_ast(productionList,indexProduc)
        self.node_statements=node

class DeclaretDicNode(StatementNode):
    def __init__(self, context):
        self.ListKeys = None
        self.ListValues = None
        self.context = context

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


class RecieveDicNode(StatementNode):
    def __init__(self, context):
        self.name = None
        self.dicNode = None
        self.key = None
        self.context = context

    def Eval(self,context):
        i = 0
        for keyval in self.dicNode.ListKeys:
            if keyval == self.key:
                return self.dicNode.ListValues[i]
            i += 1
        
    
    def validateNode(self,context):
        return True
    
    def transpilar(self):
        return self.name + "[" + self.key + "]"

    def checkTypes(self):
        return True

    def build_ast(productionList):
        pass

class SearchDicNode(StatementNode):
    def __init__(self, context):
        self.name = None
        self.dicNode = None
        self.key = None
        self.context = context

    def Eval(self,context):
        i = 0
        for keyval in self.dicNode.ListKeys:
            if keyval == self.key:
                return True
            i += 1
        return False
    
    def validateNode(self,context):
        return True
    
    def transpilar(self):
        return self.key + " in " + self.name

    def checkTypes(self):
        return True

    def build_ast(productionList):
        pass

class InsertDicNode(StatementNode):
    def __init__(self, context):
        self.namedic = None
        self.value = None
        self.context = context

    def Eval(self,context):
        pass
    
    def validateNode(self,context):
        pass
    
    def transpilar(self):
        return self.namedic + ".append(" + self.value + ")"

    def checkTypes(self):
        pass

    def build_ast(productionList):
        pass


class PrintNode(StatementNode):
    def __init__(self,context):
        self.name = "print"
        self.args = None
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

        self.funcOrVar=None
        self.defineOrCall=None


    def Eval(self,context):
        val = self.args[0].Eval(self.context)
        print(val)
        return

    def build_ast(self,productionList,indexProduc):
        indexProduc[0]+=1
        self.args = eatExpression(productionList,indexProduc,self.context)
    
class matrixSumNode(StatementNode):
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

class matrixSubNode(StatementNode):
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

class matrixMulNode(StatementNode):
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

class matrixDivNode(StatementNode):
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


# ------------------------------------------------------------------------------- #
# ----------------------- Nodes Terminator -------------------------------------- #
# ------------------------------------------------------------------------------- #

class vectorialNode(StatementNode):
    def __init__(self,context):
        self.ejex = None
        self.ejey = None
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def Eval(self,context):
        return (self.ejex,self.ejey)
    
    def transpilar(self):
        return "("+str(self.ejex) + "," +  str(self.ejey)+")"

    def checkTypes(self):
        return True

    def validateNode(self, context):
        return isnumeric(self.ejex) and isnumeric(self.ejey)

class IdNode(StatementNode):
    def __init__(self,context):
        self.fathercontext = None
        self.type = None
        self.id = None
        self.context = context

        self.value = None

        self.ReturnType = None
        self.EspecterType = None

    def Eval(self):
        if self.ReturnType == "reference":
            return self.value
        return self.id

    def transpilar(self):
        return str(self.id)

    def checkTypes(self):
        return self.id is str

    def validateNode(self, context):
        if self.ReturnType == "reference":
            self.value = self.context.retVar(self.name)
        return True

    def build_ast(self,id,funcOrVar,defineOrCall,valType="referencia"):
        self.id=id
        self.RT=valType
        self.funcOrVar=funcOrVar
        self.defineOrCall=defineOrCall

class NumberNode(StatementNode):
    def __init__(self,context):
        self.val = None
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def Eval(self,context):
        return self.val

    def transpilar(self):
        return str(self.val)

    def checkTypes(self):
        return True

    def validateNode(self, context):
        return isnumeric(self.val)

    def build_ast(self,value,valtype):
        self.val=value
        self.valtype=valtype


class ChainNode(StatementNode):
    def __init__(self,context):
        self.chain = None
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def Eval(self,context):
        return chain

    def transpilar(self):
        return str(self.chain)

    def checkTypes(self):
        return True

    def validateNode(self, context):
        return self.chain is str

    def build_ast(self,value,valtype):
        self.val=value
        self.valtype=valtype

class TrueNode(StatementNode):
    def __init__(self,context):
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def Eval(self):
        return True

    def transpilar(self):
        return str(True)

    def checkTypes(self):
        return True

    def validateNode(self, context):
        return True

    def build_ast(self,value,valtype):
        self.val=value
        self.valtype=valtype

class FalseNode(StatementNode):
    def __init__(self,context):
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def Eval(self):
        return False

    def transpilar(self):
        return str(False)

    def checkTypes(self):
        return True

    def validateNode(self, context):
        return True

    def build_ast(self,value,valtype):
        self.val=value
        self.valtype=valtype

class NoneNode(StatementNode):
    def __init__(self,context):
        self.context = context

        self.ReturnType = None
        self.EspecterType = None

    def Eval(self, context):
        return None

    def transpilar(self):
        return str(None)

    def checkTypes(self):
        return True

    def validateNode(self, context):
        return True

    def build_ast(self,value,valtype):
        self.val=value
        self.valtype=valtype

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

def eatExpression(productionList,indexProduc,context):
    if len(productionList[indexProduc][0].components)==3:
        component=productionList[indexProduc][0][1]
        if component in expresionDicc:
            #creamos el node
            node =expresionDicc[component](context)
            
            indexProduc[0]+=1
            node.build_ast(productionList,indexProduc)
            return node
        elif component=="comparer":
            indexProduc[0]+=1
            return eatComparer(productionList,indexProduc,context)
    else:
        indexProduc[0]+=1
        return eatTerm(productionList,indexProduc,context)

def eatComparer(productionList,indexProduc,context):
    component=productionList[indexProduc][0][0]
    #buscando cual comparador es
    node =expresionDicc[component](context)
    
    indexProduc[0]+=1
    node.build_ast(productionList,indexProduc)
    return node

def eatFactor(productionList,indexProduc,context):
    component=productionList[indexProduc][0][1]
    if component==productionList[indexProduc][0][0]==TokeTypes.tokOpenParen:
            indexProduc[0]+=1
            return eatExpression(productionList,indexProduc,context)
    else:
        indexProduc[0]+=1
        return eatAtom(productionList,indexProduc,context)
        
    
def eatTerm(productionList,indexProduc,context):
    if len(productionList[indexProduc][0].components)==3:
        component=productionList[indexProduc][0][1]    
        if component in termDicc:
            #creamos el node
            node =expresionDicc[component](context)
            
            indexProduc[0]+=1
            node.build_ast(productionList,indexProduc)
            return node
        else:
            indexProduc[0]+=1
            return eatFactor
        
termDicc={}
def fillTerm():
    termDicc[TokeTypes.tokMul]=FalseNode
    termDicc[TokeTypes.tokDiv]=FalseNode   

def eatAtom(productionList,indexProduc,context):
    component=productionList[indexProduc][0][0]
    if component in termDicc:
        #buscando cual atomo es
        node =expresionDicc[component](context)

        indexProduc[0]+=1
        node.build_ast(productionList,indexProduc)
        return node
    elif component=="func_call":
        indexProduc[0]+=1
        if len(productionList[indexProduc][0].component)==4:
            node=func_callNode(context)
            node.build_ast(productionList,indexProduc)
            return node
        elif productionList[indexProduc][0].component=="dic_func":
            indexProduc[0]+=2
            return eatDiccFunc(productionList,indexProduc,context)
        elif productionList[indexProduc][0].component=="matrix_func":
            indexProduc[0]+=2
            eatMatrixFunc(productionList,indexProduc,context)

def eatMatrixFunc(productionList,indexProduc,context):
    component=productionList[indexProduc][0][0]
    node =diccMatrixFunc[component](context)
    
    indexProduc[0]+=1
    node.build_ast(productionList,indexProduc)
    return node

def eatDiccFunc(productionList,indexProduc,context):
    component=productionList[indexProduc][0][0]
    node =diccFunDicc[component](context)
    
    indexProduc[0]+=1
    node.build_ast(productionList,indexProduc,context)
    return node

def eatArgList(productionList,indexProduc,context):
    resultTypes=[]
    resultId=[]
    while productionList[indexProduc][1].head!="args_list" or productionList[indexProduc][1].head!="args_list_fix":
        resultId.append(productionList[indexProduc][1].components[1]) 
        indexProduc[0]+=2
        resultTypes.append(eatType(productionList,indexProduc))
    return (resultTypes,resultId)

def eatType(productionList,indexProduc):
    return productionList[indexProduc][0].components[0]

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

diccFunDicc={}
def fillDiccFun():
    diccFunDicc["search_dic"]=RecieveDicNode
    diccFunDicc["recieve_dic"]=SearchDicNode
    diccFunDicc["insert_dic"]=InsertDicNode
    diccFunDicc["dic_dec"]=DeclaretDicNode
    
    
diccMatrixFunc={}
def fillDiccFunVec():
    diccMatrixFunc[TokeTypes.tokMSum]=matrixSumNode
    diccMatrixFunc[TokeTypes.tokMSub]=matrixSubNode
    diccMatrixFunc[TokeTypes.tokMMul]=matrixMulNode
    diccMatrixFunc[TokeTypes.tokMDiv]=matrixDivNode