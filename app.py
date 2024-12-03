import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Use the connection URL from Render's database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "postgresql://amico_cross_db_user:cgY8HXuK313UxBOnacSOKfDccWl9pGYl@dpg-ct49jhlumphs73e4l150-a.oregon-postgres.render.com/amico_cross_db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)


# Tables: Kenall Model & Amico Model
class KenallModel(db.Model):
    __tablename__ = 'kenall_model'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String, nullable=False)
    amico_model_ref = db.Column(db.Integer, db.ForeignKey('amico_model.id'), nullable=False)
# Relationship 
    amico_model = db.relationship('AmicoModel', backref='kenall_model')
class AmicoModel(db.Model):
    __tablename__ = 'amico_model'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String, nullable=False, unique=True) 



# Tables: Kenall Mounting & Amico Mounting
class KenallMounting(db.Model):
    __tablename__ = 'kenall_mounting'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mounting = db.Column(db.String, nullable=False)
    amico_mounting_ref = db.Column(db.Integer, db.ForeignKey('amico_mounting.id'), nullable=False)
# Relationship
    amico_mounting = db.relationship('AmicoMounting', backref='kenall_mounting')
class AmicoMounting(db.Model):
    __tablename__ = 'amico_mounting'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mounting = db.Column(db.String, nullable=False, unique=True)



# Tables: Kenall Diffuser & Amico Diffuser
class KenallDiffuser(db.Model):
    __tablename__ = 'kenall_diffuser'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    diffuser = db.Column(db.String, nullable=False)
    amico_diffuser_ref = db.Column(db.Integer, db.ForeignKey('amico_diffuser.id'), nullable=False)
# Relationship
    amico_diffuser = db.relationship('AmicoDiffuser', backref='kenall_diffuser')
class AmicoDiffuser(db.Model): 
    __tablename__ = 'amico_diffuser'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    diffuser = db.Column(db.String, nullable=False, unique=True)


# Tables: Kenall Lamp & Amico Lamp
class KenallLamp(db.Model):
    __tablename__ = 'kenall_lamp'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lamp = db.Column(db.String, nullable=False)
    amico_lamp_ref = db.Column(db.Integer, db.ForeignKey('amico_lamp.id'), nullable=False)
# Relationship
    amico_lamp = db.relationship('AmicoLamp', backref='kenall_lamp')
class AmicoLamp(db.Model):
    __tablename__ = 'amico_lamp'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lamp = db.Column(db.String, nullable=False, unique=True) 


# Tables: Kenall Driver & Amico Driver
class KenallDriver(db.Model):
    __tablename__ = 'kenall_driver'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    driver = db.Column(db.String, nullable=False)
    amico_driver_ref = db.Column(db.Integer, db.ForeignKey('amico_driver.id'), nullable=False)
# Relationship
    amico_driver = db.relationship('AmicoDriver', backref='kenall_driver')
class AmicoDriver(db.Model):
    __tablename__ = 'amico_driver'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    driver = db.Column(db.String, nullable=False, unique=True)


# Tables: Kenall Voltage & Amico Voltage
class KenallVoltage(db.Model):
    __tablename__ = 'kenall_voltage'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    voltage = db.Column(db.String, nullable=False)
    amico_voltage_ref = db.Column(db.Integer, db.ForeignKey('amico_voltage.id'), nullable=False)
# Relationship
    amico_voltage = db.relationship('AmicoVoltage', backref='kenall_voltage')
class AmicoVoltage(db.Model):
    __tablename__ = 'amico_voltage'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    voltage = db.Column(db.String, nullable=False, unique=True)


# Tables: Kenall Doorframe & Amico Doorframe
class KenallDoorframe(db.Model):
    __tablename__ = 'kenall_doorframe'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doorframe = db.Column(db.String, nullable=False)
    amico_doorframe_ref = db.Column(db.Integer, db.ForeignKey('amico_doorframe.id'), nullable=False)
# Relationship 
    amico_doorframe = db.relationship('AmicoDoorframe', backref='kenall_doorframe')
class AmicoDoorframe(db.Model):
    __tablename__ = 'amico_doorframe'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doorframe = db.Column(db.String, nullable=False, unique=True)


# Tables: Kenall Options & Amico Options
class KenallOptions(db.Model):
    __tablename__ = 'kenall_options'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    options = db.Column(db.String, nullable=False)
    amico_options_ref = db.Column(db.Integer, db.ForeignKey('amico_options.id'), nullable=False)
# Relationship
    amico_options = db.relationship('AmicoOptions', backref='kenall_options')
class AmicoOptions(db.Model):
    __tablename__ = 'amico_options'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    options = db.Column(db.String, nullable=False, unique=True)
    

# Tables: Kenall Accessories & Amico Accessories
class KenallAccessories(db.Model):
    __tablename__ = 'kenall_accessories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    accessories = db.Column(db.String, nullable=False)
    amico_accessories_ref = db.Column(db.Integer, db.ForeignKey('amico_accessories.id'), nullable=False)
# Relationship 
    amico_accessories = db.relationship('AmicoAccessories', backref='kenall_accessories')
class AmicoAccessories(db.Model):
    __tablename__ = 'amico_accessories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    options = db.Column(db.String, nullable=False, unique=True)


@app.route('/api/get-amico-part', methods=['GET'])
def get_amico_part():
    data = request.json
    kenall_part_number = data.get('part_number')
    category = data.get('category')  # E.g., "lamp", "driver", "voltage", etc.

    if not kenall_part_number or not category:
        return jsonify({"error": "Part number and category are required"}), 400

    # Mapping category to the respective Kenall table
    category_table_mapping = {
        "lamp": KenallLamp,
        "driver": KenallDriver,
        "voltage": KenallVoltage,
        "model": KenallModel,
        "mounting": KenallMounting,
        "diffuser": KenallDiffuser,
        "doorframe": KenallDoorframe,
        "options": KenallOptions,
        "accessories": KenallAccessories,
    }

    kenall_table = category_table_mapping.get(category.lower())
    if not kenall_table:
        return jsonify({"error": "Invalid category"}), 400

    # Search for the Kenall part in the specified table
    kenall_part = kenall_table.query.filter_by(**{category: kenall_part_number}).first()
    if not kenall_part:
        return jsonify({"error": "Kenall part not found"}), 404

    # Use the amico_id to fetch the Amico part details
    amico_id = kenall_part.amico_id
    amico_table_mapping = {
        "lamp": AmicoLamp,
        "driver": AmicoDriver,
        "voltage": AmicoVoltage,
        "model": AmicoModel,
        "mounting": AmicoMounting,
        "diffuser": AmicoDiffuser,
        "doorframe": AmicoDoorframe,
        "options": AmicoOptions,
        "accessories": AmicoAccessories,
    }

    amico_table = amico_table_mapping.get(category.lower())
    amico_part = amico_table.query.get(amico_id) if amico_table else None

    if not amico_part:
        return jsonify({"error": "Amico part not found"}), 404

    # Return Amico part details
    return jsonify({
        "kenall_part_number": kenall_part_number,
        "amico_part_number": amico_part.lamp if category.lower() == "lamp" else amico_part.driver,
    })


if __name__ == '__main__':
    app.run(debug=True)
