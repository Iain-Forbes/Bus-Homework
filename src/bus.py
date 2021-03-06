class Bus():
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
        
        
    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passengers_1):
        self.passengers.append(passengers_1)
        

    def drop_off(self, passengers_2):
        self.passengers.remove(passengers_2)
        
    def empty(self):
        self.passengers.clear()

    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.queue:
            self.pick_up(passenger)  
            
        bus_stop.clear()  

    