


class CompError():
    
    
    def __init__(self,text,line,column):
        self.text=text
        self.line=line
        self.column=column
        
        
    def __repr__(self) -> str:
        tempErrorString=str(self.text)+ " in line: " +str(self.line)+" in column: "+str(self.column)
        return tempErrorString