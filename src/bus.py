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

    def pick_up_from_stop(self, passengers_1):
        self.pick_up()
        self.pick_up()


    
        
       

    #     @unittest.skip("Delete this line to run the test")
    # def test_can_pick_up_passenger_from_bus_stop(self):
    #     person_1 = Person("Guido van Rossum", 64)
    #     person_2 = Person("Carol Willing", 50)
    #     bus_stop = BusStop("Waverly Station")
    #     bus_stop.add_to_queue(person_1)
    #     bus_stop.add_to_queue(person_2)
        # self.bus.pick_up_from_stop(bus_stop)
        # self.assertEqual(2, self.bus.passenger_count())