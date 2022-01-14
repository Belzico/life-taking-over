from queue import Queue

class MyQueue():
    def __init__(self):
        self.queue = Queue()
        self.len = 0
        
    def __len__(self):
        return self.len
    
    def put(self,value):
        self.queue.put(value)
        self.len += 1
        
    def get(self):
        self.len -= 1
        return self.queue.get()