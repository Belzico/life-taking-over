
from dataclasses import dataclass

from numpy import true_divide

@dataclass
class ClassNode():
    

    def EvalNode():
        pass
    
    def validateNode(self,context):
        pass


class Context():
    def __init__(self,name,fatherContext=None):
        
        self.diccVarContext : dict(str,ClassNode)= {}
        self.diccFuncContext : dict(str,ClassNode)={} 
        self.fatherContext= fatherContext
        self.name=name
    
        
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
    
    def define_var(self,var,varType):
        if not self.checkVar(var,varType):
            self.diccVarContext[var]=[var,varType]
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
        while True:
            if self==None: return None
            if var in current.diccVarContext:
                return current.diccVarContext[var]
            current=self.fatherContext
    
    #este metodo devuelve una lista con el formator [name,arg1Type,arg2Type....,argNType]
    def retFun(self,var,argList):
        current=self
        while True:
            if self==None: return None
            if (var,argList) in current.diccFuncContext:
                return current.diccFuncContext[var]
            current=self.fatherContext
    
    def create_hild(self,name):
        chilcontext=Context(name,self)
        return chilcontext

#--------------------------------------------------------------------------- #
#-------------------------- Nodos Operadores ------------------------------- #
#--------------------------------------------------------------------------- #


class SumNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
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

class SubNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.Left = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.Right = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
            
    def Eval(self):
        return self.Left - self.Right

class MulNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.Left = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.Right = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
            
    def Eval(self):
        return self.Left * self.Right

class DivNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.Left = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.Right = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
            
    def Eval(self):
        return self.Left / self.Right

class ModNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.Left = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.Right = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
            
    def Eval(self):
        return self.Left % self.Right

#class PowNode(ClassNode):
#    def __init__(self,value,hijos):
#        super().__init__(value,hijos)
#        
#        try:
#            self.Left = hijos[0]
#        except:
#            Exception("No fue mandado el primer hijo")
#            
#        try:
#            self.Right = hijos[1]
#        except:
#            Exception("No fue mandado el primer hijo")
#            
#    def Eval(self):
#        return self.Left ^ self.Right

#--------------------------------------------------------------------------- #
#-----------------------Comparer Oper -------------------------------------- #
#--------------------------------------------------------------------------- #

class EqualNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.Left = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.Right = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
            
    def Eval(self):
        return self.Left == self.Right

class NotEqualNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.Left = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.Right = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
            
    def Eval(self):
        return self.Left != self.Right

class LoENode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.Left = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.Right = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
            
    def Eval(self):
        return self.Left <= self.Right

class GoENode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.Left = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.Right = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
            
    def Eval(self):
        return self.Left >= self.Right

class GreaterNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.Left = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.Right = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
            
    def Eval(self):
        return self.Left > self.Right

class LessNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.Left = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.Right = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
            
    def Eval(self):
        return self.Left < self.Right
    

#--------------------------------------------------------------------------- #
#--------------------------Condicional ------------------------------------- #
#--------------------------------------------------------------------------- #

    
class AndNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.Left = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.Right = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
            
    def Eval(self):
        return self.Left and self.Right

class OrNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.Left = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.Right = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
            
    def Eval(self):
        return self.Left or self.Right

class LoopNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.Condicional = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.Cuerpo = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
            
    def Eval(self):
        if self.Condicional:
            return self.Cuerpo.Eval()
        return None
    
#--------------------------------------------------------------------------- #
#--------------------------Func Program ------------------------------------ #
#--------------------------------------------------------------------------- #


class ModifyNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.name = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.args = hijos[1]
        except:
            Exception("No fue mandado el primer hijo")
    
    def EvalNode():
        pass

class CreateNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.name = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.args = hijos[1,...]
        except:
            Exception("No fue mandado el primer hijo")
    
    def EvalNode():
        pass

class DieNode():
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.name = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.args = hijos[1,...]
        except:
            Exception("No fue mandado el primer hijo")
    
    def EvalNode():
        pass
    

class EvolveNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.name = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.args = hijos[1,...]
        except:
            Exception("No fue mandado el primer hijo")
    
    def EvalNode():
        pass

class AddNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.name = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.args = hijos[1,...]
        except:
            Exception("No fue mandado el primer hijo")
    
    def EvalNode():
        pass
    
class MoveNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.name = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.args = hijos[1,...]
        except:
            Exception("No fue mandado el primer hijo")
    
    def EvalNode():
        pass
    
class EatNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.name = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.args = hijos[1,...]
        except:
            Exception("No fue mandado el primer hijo")
    
    def EvalNode():
        pass
    
    
#--------------------------------------------------------------------------- #
#--------------------------Non Terminals ----------------------------------- #
#--------------------------------------------------------------------------- #

class ProgramNode(ClassNode):
    def __init__(self,value,hijos):
        super().__init__(value,hijos)
        
        try:
            self.name = hijos[0]
        except:
            Exception("No fue mandado el primer hijo")
            
        try:
            self.args = hijos[1,...]
        except:
            Exception("No fue mandado el primer hijo")
    
    def EvalNode():
        pass