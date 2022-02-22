

class ClassNode():
    
    def __init__(self,value,hijos):
        self.value = value
        self.hijos = hijos
        
    def Eval(self):
        return

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

class PowNode(ClassNode):
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
        return self.Left ^ self.Right

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