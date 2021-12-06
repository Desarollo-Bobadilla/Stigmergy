from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://tanjiro:hashira@localhost:5432/hubs_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "Bobs"

if __name__ == "__main__":
    app.run()

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

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

        hub = Hub(localizacion = form.localizacion.data, lat = form.lat.data, log = form.log.data)
        db.session.add(hub)
        db.session.commit()
        flash("SIUUUUU")
        
    our_hubs = Hub.query.order_by(Hub.id)
    return render_template('hubs_create.html', form = form, our_hubs = our_hubs)

@app.route('/hubs/get/<int:id>', methods = ['GET', 'POST'])
def hub_get(id):
    hub = Hub.query.get_or_404(id)

@app.route('/hubs/delete/<int:id>')
def hub_delete(id):
    hub = Hub.query.get_or_404(id)
    try:
        db.session.delete(hub)
        db.session.commit()
        flash("Delete")

        our_hubs = Hub.query.order_by(Hub.id)
        form = HubsForm()
        return render_template('hubs_create.html', form = form, our_hubs = our_hubs)

    except:
        flash('BUU')
        our_hubs = Hub.query.order_by(Hub.id)
        form = HubsForm()
        return render_template('hubs_create.html', form = form, our_hubs = our_hubs)