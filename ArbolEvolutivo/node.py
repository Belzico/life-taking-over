class Node:
    def __init__(self,values):
        self.value = values
        
    def peek(self):
        return self.value
    
    def ChangeValues(self,values):
        self.value = values