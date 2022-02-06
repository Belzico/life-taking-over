from ArbolEvolutivo.node import Node
import queue  

class Arbol_Evo:
    def __init__(self, especie = "origen"):
        self.node = Node(especie)
        self.hijos = []
                
    def peek(self):
        return self.node.peek()
    
    def peek_hijos(self):
        return self.hijos
    
    def add_hijo(self,especie):
        self.hijos.append(Arbol_Evo(especie))
    
    def ChangeValue(self,values):
        self.node.ChangeValues(values)
        
    def IsSpecieEqual(self,especie):
        nodEsp = self.node
        value = nodEsp.peek()
        if value == especie:
            return self
        
        return None
        
    def InsertEvolution(self,esp_new, esp_ant = "origen"):
        if esp_ant == 'origen':
            self.hijos.append(Arbol_Evo(esp_new))
            return True
        
        arb_evo = Arbol_Evo.SearchEvolution(esp_ant, self)
        if arb_evo == None:
            print("La especie " + esp_ant + " no existe")
            return False
            
        arb_evo.hijos.append(Arbol_Evo(esp_new))
        return True
        
        
    def SearchEvolution(especie, arb_evo):
        queueArboles = queue.Queue()
        queueArboles.put(arb_evo)
        
        while not queueArboles.empty():
            arbol = queueArboles.get()
            
            cmp = arbol.IsSpecieEqual(especie)
            if cmp != None:
                return cmp
            
            for arb_hijo in arbol.peek_hijos():
                queueArboles.put(arb_hijo)
                
        return None