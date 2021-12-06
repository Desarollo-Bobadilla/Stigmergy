from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "Bobs"

if __name__ == "__main__":
    app.run()

class HubsForm(FlaskForm):
    id = IntegerField("Ingrese el ID del Hub", validators=[DataRequired()])
    localizacion = StringField("Ingrese el nombre del puesto donde está", validators=[DataRequired()])
    lat = FloatField("Ingrese la latitud del puesto", validators=[DataRequired()])
    log = FloatField("Ingrese la longitud del puesto", validators=[DataRequired()])
    summit = SubmitField("Crear")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hubs/create', methods = ['GET', 'POST'])
def hub_create():

    form = HubsForm()
    if form.validate_on_submit():
        form.id.data = ''
        form.localizacion.data = ''
        form.lat.data = ''
        form.log.data = ''
        flash("SIUUUUU")
        

    return render_template('hubs_create.html', form = form)