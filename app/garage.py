from app.heapqueue import PriorityQueue
from app.nodes import edges

class Car:
    def __init__(self, name, license_plate):
        self.name = name
        self.license_plate = license_plate

class ParkingSpot:
    def __init__(self, spot_id, distance, path_enter, path_exit, occupied=False, car=None):
        self.id = spot_id
        self.distance = distance # used in spot priority queue
        self.path_enter = path_enter # path from entrance to spot
        self.path_exit = path_exit # path from spot to exit
        self.occupied = occupied
        self.car = car # current car object in the spot or None

    def add_car(self, car):
        self.occupied = True
        self.car = car

    def remove_car(self):
        self.occupied = False
        self.car = None

class Garage:
    def __init__(self, spot_index):
        self.spot_index = spot_index # index of all spots in garage
        self.free_q = PriorityQueue(spot_index) # min heap priority queue of open spots
        self.occ_list = [] # list of occupied spots

    def park_car(self, car):
        spot = self.free_q.pop_min() # gets closest free ParkingSpot object
        # simulate calling mechanism control to route car to spot
        path = self.control_route(spot.path_enter) # builds path from entrance to spot
        spot.add_car(car)
        self.occ_list.append(spot)
        return spot.id, path

    def get_car(self, name, license_plate):
        car_not_found = True
        for i in range(len(self.occ_list)):
            spot = self.occ_list[i]
            if spot.car.name == name and spot.car.license_plate == license_plate:
                # simulate calling mechanism control to route car back to driver
                path = self.control_route(spot.path_exit) # builds path from spot to exit
                spot.remove_car()
                self.occ_list.pop(i)
                self.free_q.insert(spot) # inserts empty spot into priority queue
                car_not_found = False
                break
        if car_not_found: return False, None 
        else: return spot.id, path
            
    def control_route(self, enter_exit_path):
        # build path to or from parking spot    
        path = []
        for edge in enter_exit_path:
            path.append(edges[edge])
        return path
        


