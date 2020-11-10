class BusStop():
    def __init__(self, name):
        self.name = name
        self.passengers = []
        self.queue = [] 
        

    def queue_length(self):
       return len(self.queue)

    def add_to_queue(self, passengers_1):
        self.queue.append(passengers_1)

    def clear(self):
        self.queue.clear()

        