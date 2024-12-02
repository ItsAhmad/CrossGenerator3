from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Output table
class Output(db.Model):
    __tablename__ = 'output'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    series = db.Column(db.String, nullable=False)  # Matches InputKenall's Model
    voltage = db.Column(db.Integer, nullable=False)  # Matches InputKenall's Voltage
    functions = db.Column(db.String, nullable=True)  # Matches InputKenall's Lamp Type
    colour_temp = db.Column(db.String, nullable=True)  # Matches InputKenall's Lamp Type
    cri = db.Column(db.String, nullable=True)  # Matches InputKenall's Lamp Type
    switching = db.Column(db.String, nullable=True)  # Matches InputKenall's Driver
    options = db.Column(db.String, nullable=True)  # Matches InputKenall's Options or Accessories

# Input table (InputKenall)
class InputKenall(db.Model):
    __tablename__ = 'input_kenall'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String, nullable=False)  # Matches Output's Series
    voltage = db.Column(db.String, nullable=False)  # Matches Output's Voltage
    lamp_type = db.Column(db.String, nullable=False)  # Matches Output's Functions, Colour Temp, and CRI
    driver = db.Column(db.String, nullable=True)  # Matches Output's Switching
    options = db.Column(db.String, nullable=True)  # Matches Output's Options
    accessories = db.Column(db.String, nullable=True)  # Matches Output's Options

    # Foreign key linking to the Output table
    output_id = db.Column(db.Integer, db.ForeignKey('output.id'), nullable=True)
    output = db.relationship('Output', backref='input_kenall')
