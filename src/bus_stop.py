class BusStop():
    def __init__(self, name):
        self.name = name
        self.passengers = []

    def add_to_queue(self, passengers):
        self.passengers.append(passengers)
    