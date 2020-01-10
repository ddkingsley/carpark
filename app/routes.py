from app import app
from flask import render_template, flash
from app.forms import ParkOrPickupForm
from app.garage import Car
from app import garage
import json

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ParkOrPickupForm()
    path = None
    car_found = False
    # set already occupied spots for map images
    occupied_spots = []
    for s in garage.spot_index:
        if s.occupied:
            occupied_spots.append(s)
    # if browser sends POST request and fields validate
    if form.validate_on_submit():
        # if Park It button 
        if form.submit_park.data:
            if len(garage.free_q.q) > 0:
                car = Car(form.name.data, form.license_plate.data)
                spot, path = garage.park_car(car)
                flash(f"Your car is parked in spot: {spot}")
            else:
                path = None 
                flash("We're sorry but the lot is full. Please try again later!")
        # if Pick It Up button
        else:
            car_found, path = garage.get_car(form.name.data, form.license_plate.data)
            if car_found: 
                occupied_spots = []
                # update occupied spots for map images
                for s in garage.spot_index:
                    if s.occupied:
                        occupied_spots.append(s)
                flash(f"Here is your car, {form.name.data}!")
            else: flash("Your car was not found. It must have been stolen!!!")      
    return render_template('index.html', form=form, spot_index=garage.spot_index, 
        occupied_spots=occupied_spots, json_path=json.dumps(path), car_found=car_found)

@app.route('/about')
def about():
    return render_template('about.html', heading='About AutoCarPark')