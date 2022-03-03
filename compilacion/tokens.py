import enum





    

class Token():
    def __init__(self,tokenType,line,column,value=None):
        self.value=value
        self.tokenType=tokenType
        self.line=line
        self.column=column
    
    def __str__(self) -> str:
        return str(self.tokenType)
    
    
class TokenType():
    diccType={}
    