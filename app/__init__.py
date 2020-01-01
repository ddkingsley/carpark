from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from app.garage import Car, ParkingSpot, Garage
from app.nodes import enter_paths, exit_paths

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

# CREATE GARAGE MODEL
# build empty spot_index for simulated 10 car garage
spot_index = []
for i in range(10):
    spot_id = f"P{i}"
    distance = i
    path_enter = enter_paths[spot_id]
    path_exit = exit_paths[spot_id]
    new_spot = ParkingSpot(spot_id, distance, path_enter, path_exit)
    spot_index.append(new_spot)

garage = Garage(spot_index)

#fill garage with a few example cars
cars = [['Dwight', '1234AEI'], ['Michael', '5678OU'], ['Jim', '9876ABC'], ['Pam', '5432DEF']]
for c in cars:
    car = Car(c[0], c[1])
    garage.park_car(car)

from app import routes



