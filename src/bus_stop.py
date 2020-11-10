class BusStop():
    def __init__(self, name):
        self.name = name
        self.passengers = []
        self.queue = [] 
        

    def queue_length(self):
       return len(self.queue)

    
        
