class BusStop():
    def __init__(self, stop):
        self.stop = stop
        self.passengers = []

    def add_to_queue(self, passengers):
        self.passengers.append(passengers)
    