from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ParkOrPickupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    license_plate = StringField('License Plate', validators=[DataRequired()])
    submit_park = SubmitField('Park It')
    submit_pickup = SubmitField('Pick It Up')

