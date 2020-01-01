# AutoCarPark

AutoCarPark is a software model of an automatic parking garage. It simulates a garage in which a driver drops off a car and an automated garage mechanism finds and avaible parking spot and automatically moves the car into the appropriate spot. The garage would then find the car and route it back to the exit when the driver is ready to pick it up. 

#### The interactive app can be found at: https://autocarpark.herokuapp.com/

#### The garage mechanism is primarily handled by:
- app/garage.py
- app/heapqueue.py
- app/routes.py

#### The objects used in building the car routing path are in:
- app/nodes.py

#### The animation script and most app html is found in:
- app/templates/index.html<br>
(bootstrap and app/static/mystyle.css are used for styling and positioning)

#### Flask is the web framework used. 

#### Created By: Daniel Kingsley