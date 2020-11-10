class Bus():
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
        
        
    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up_from_stop(self, passengers):
        self.passengers.append(passengers)

    def drop_off(self, passengers):
        self.passengers.remove(passengers)

    def empty(self):
        self.passengers.clear()

    def can_pick_up_passenger_from_bus_stop(self, passenger, busstop):
        pass  

        
        

    

  