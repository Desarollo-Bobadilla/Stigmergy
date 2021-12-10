
# -- Libraries

import logging
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# -- App Configuration

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://tanjiro:hashira@localhost:5432/hubs_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "Bobs"

# -- Run

if __name__ == "__main__":
    app.run()

# -- Data Base

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

# -- Models

class Hub(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    localizacion = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float)
    log = db.Column(db.Float)
    posts = db.relationship('Dron', backref = 'dron')

    def __rerp__(self):
        return '<id %d>' % self.id

class Dron(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    altoMax = db.Column(db.Float)
    anchoMax = db.Column(db.Float)
    largoMax = db.Column(db.Float)
    pesoMax = db.Column(db.Float)
    id_hub = db.Column(db.Integer, db.ForeignKey('hub.id'))

# -- Forms

class HubsForm(FlaskForm):
    id = IntegerField("Ingrese el ID del Hub", validators=[DataRequired()])
    localizacion = StringField("Ingrese el nombre del puesto donde está", validators=[DataRequired()])
    lat = FloatField("Ingrese la latitud del puesto", validators=[DataRequired()])
    log = FloatField("Ingrese la longitud del puesto", validators=[DataRequired()])
    summit = SubmitField("Crear")

class DronForm(FlaskForm):
    id = IntegerField("Ingrese el ID del Dron", validators=[DataRequired()])
    altoMax =  FloatField("Ingrese el alto máximo del paquete que puede llevar el dron", validators=[DataRequired()])
    anchoMax =  FloatField("Ingrese el ancho máximo del paquete que puede llevar el dron", validators=[DataRequired()])
    largoMax =  FloatField("Ingrese el largo máximo del paquete que puede llevar el dron", validators=[DataRequired()])
    pesoMax =  FloatField("Ingrese el peso máximo del paquete que puede llevar el dron", validators=[DataRequired()])
    id_hub = IntegerField("Ingrese el ID del Hub donde va a estár ubicado el dron", validators=[DataRequired()])
    summit = SubmitField("Crear")

# -- HTML

indexh = 'index.html'
create_hub = 'hubs_create.html'
create_dron = 'dron_create.html'
list_hub = 'hubs_list.html'
list_dron = 'drons_list.html'

# -- Index

@app.route('/')
def index():
    return render_template(indexh)

# -- Create

@app.route('/hubs/create', methods = ['GET', 'POST'])
def hub_create():

    form = HubsForm()
    if form.validate_on_submit():

        hub = Hub(id = form.id.data, localizacion = form.localizacion.data, lat = form.lat.data, log = form.log.data)
        db.session.add(hub)
        db.session.commit()
        flash("Se creo con exito el Hub")
        
    our_hubs = Hub.query.order_by(Hub.id)
    return render_template(create_hub, form = form, our_hubs = our_hubs)

@app.route('/dron/create', methods = ['GET', 'POST'])
def dron_create():

    form = DronForm()
    if form.validate_on_submit():

        hub = Dron(id = form.id.data, altoMax = form.altoMax.data, anchoMax = form.anchoMax.data, largoMax = form.largoMax.data, pesoMax = form.pesoMax.data, id_hub = form.id_hub.data)
        db.session.add(hub)
        db.session.commit()
        flash("Se creo con exito el Dron")
        
    our_drons = Dron.query.order_by(Dron.id)
    return render_template(create_dron, form = form, our_drons = our_drons)

# -- Get

@app.route('/hubs/get/', methods = ['GET', 'POST'])
def hub_get_all():
    our_hubs = Hub.query.order_by(Hub.id)
    return render_template(list_hub, our_hubs = our_hubs)

@app.route('/hubs/get/<int:id>', methods = ['GET', 'POST'])
def hub_get(id):
    hub = [Hub.query.get_or_404(id)]
    return render_template(list_hub, our_hubs = hub)

@app.route('/dron/get/', methods = ['GET', 'POST'])
def dron_get_all():
    our_drons = Dron.query.order_by(Dron.id)
    return render_template(list_dron, our_drons = our_drons)

@app.route('/dron/get/<int:id>', methods = ['GET', 'POST'])
def dron_get(id):
    dron = [Dron.query.get_or_404(id)]
    return render_template(list_dron, our_drons = dron)

# -- Delete

@app.route('/hubs/delete/<int:id>')
def hub_delete(id):
    hub = Hub.query.get_or_404(id)
    try:
        db.session.delete(hub)
        db.session.commit()
        flash("Delete")

        our_hubs = Hub.query.order_by(Hub.id)
        return render_template(list_hub, our_hubs = our_hubs)

    except BaseException as e:
        logging.exception('error while deleting')
        raise e

@app.route('/dron/delete/<int:id>')
def dron_delete(id):
    dron = Dron.query.get_or_404(id)
    try:
        db.session.delete(dron)
        db.session.commit()
        flash("Delete")

        our_drons = Dron.query.order_by(Dron.id)
        return render_template(list_dron, our_drons = our_drons)

    except BaseException as e:
        logging.exception('error while deleting')
        raise e