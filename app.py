import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Use the connection URL from Render's database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "postgresql://amico_cross_db_user:cgY8HXuK313UxBOnacSOKfDccWl9pGYl@dpg-ct49jhlumphs73e4l150-a.oregon-postgres.render.com/amico_cross_db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Table: KenallModel
class KenallModel(db.Model):
    __tablename__ = 'kenall_model'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico.id'), nullable=False)

# Table: KenallMounting
class KenallMounting(db.Model):
    __tablename__ = 'kenall_mounting'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mounting = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico.id'), nullable=False)

# Table: KenallDiffuser
class KenallDiffuser(db.Model):
    __tablename__ = 'kenall_diffuser'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    diffuser = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico.id'), nullable=False)

# Table: KenallLamp
class KenallLamp(db.Model):
    __tablename__ = 'kenall_lamp'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lamp = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico.id'), nullable=False)

# Table: KenallDriver
class KenallDriver(db.Model):
    __tablename__ = 'kenall_driver'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    driver = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico.id'), nullable=False)

# Table: KenallVoltage
class KenallVoltage(db.Model):
    __tablename__ = 'kenall_voltage'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    voltage = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico.id'), nullable=False)

# Table: KenallDoorframe
class KenallDoorframe(db.Model):
    __tablename__ = 'kenall_doorframe'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doorframe = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico.id'), nullable=False)


# Table: KenallOptions
class KenallOptions(db.Model):
    __tablename__ = 'kenall_options'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doorframe = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico.id'), nullable=False)
    

# Table: KenallAccessories 
class KenallAccessories(db.Model):
    __tablename__ = 'kenall_accessories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doorframe = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico.id'), nullable=False)



# Table: Amico (central table)
class Amico(db.Model):
    __tablename__ = 'amico'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    part_number = db.Column(db.String, nullable=False, unique=True)

    # Relationships
    kenall_models = db.relationship('KenallModel', backref='amico', lazy=True)
    kenall_mountings = db.relationship('KenallMounting', backref='amico', lazy=True)
    kenall_diffuser = db.relationship('KenallDiffuser', backref='amico', lazy=True)
    kenall_lamp = db.relationship('KenallLamp', backref='amico', lazy=True)
    kenall_driver = db.relationship('KenallDriver', backref='amico', lazy=True)
    kenall_voltage = db.relationship('KenallVoltage', backref='amico', lazy=True)
    kenall_doorframe = db.relationship('KenallDoorframe', backref='amico', lazy=True)
    kenall_options = db.relationship('KenallOptions', backref='amico', lazy=True)
    kenall_accessories = db.relationship('KenallAccessories', backref='amico', lazy=True)

''' API route example for fetching Amico part details - commenting out for now 
@app.route('/api/get-amico-part/<int:amico_id>', methods=['GET'])
def get_amico_part(amico_id):
    amico = Amico.query.get(amico_id)
    if not amico:
        return jsonify({"error": "Amico part not found"}), 404

    return jsonify({
        "id": amico.id,
        "part_number": amico.part_number,
        "kenall_models": [model.model for model in amico.kenall_models],
        "kenall_mountings": [mounting.mounting for mounting in amico.kenall_mountings],
        "kenall_diffuser": [diffuser.diffuser for diffuser in amico.kenall_diffuser],
        "kenall_lamp": [lamp.lamp for lamp in amico.kenall_lamp],
        "kenall_driver": [driver.driver for driver in amico.kenall_driver],
        "kenall_voltage": [voltage.voltage for voltage in amico.kenall_cris],
        "kenall_doorframe": [doorframe.doorframe for doorframe in amico.kenall_cris],
        "kenall_options":[options.options for options in amico.kenall_cris],
        "kenall_accessories":[accessories.accessories for accessories in amico.kenall_cris],
    })
'''

if __name__ == '__main__':
    app.run(debug=True)
