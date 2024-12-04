from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Amico Tables ------------------------------------------------------------------------------------------------------------------------
class AmicoCCT(db.Model):
    __tablename__ = 'amico_CCT'
    id = db.Column(db.Integer, primary_key=True)
    CCT = db.Column(db.String, nullable=False)

class AmicoAccessories(db.Model):
    __tablename__ = 'amico_accessories'
    id = db.Column(db.Integer, primary_key=True)
    options = db.Column(db.String, nullable=False)

class AmicoDiffuser(db.Model):
    __tablename__ = 'amico_diffuser'
    id = db.Column(db.Integer, primary_key=True)
    diffuser = db.Column(db.String, nullable=False)

class AmicoDoorframe(db.Model):
    __tablename__ = 'amico_doorframe'
    id = db.Column(db.Integer, primary_key=True)
    doorframe = db.Column(db.String, nullable=False)

class AmicoDriver(db.Model):
    __tablename__ = 'amico_driver'
    id = db.Column(db.Integer, primary_key=True)
    driver = db.Column(db.String, nullable=False)

class AmicoFunction(db.Model):
    __tablename__ = 'amico_function'
    id = db.Column(db.Integer, primary_key=True)
    function = db.Column(db.String, nullable=False)

class AmicoModel(db.Model):
    __tablename__ = 'amico_model'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String, nullable=False)

class AmicoMounting(db.Model):
    __tablename__ = 'amico_mounting'
    id = db.Column(db.Integer, primary_key=True)
    mounting = db.Column(db.String, nullable=False)

class AmicoOptions(db.Model):
    __tablename__ = 'amico_options'
    id = db.Column(db.Integer, primary_key=True)
    options = db.Column(db.String, nullable=False)

class AmicoSwitch(db.Model):
    __tablename__ = 'amico_switch'
    id = db.Column(db.Integer, primary_key=True)
    switch = db.Column(db.String, nullable=False)

class AmicoVoltage(db.Model):
    __tablename__ = 'amico_voltage'
    id = db.Column(db.Integer, primary_key=True)
    voltage = db.Column(db.String, nullable=False)

# Kenall Tables ------------------------------------------------------------------------------------------------------------------------
class KenallAccessories(db.Model):
    __tablename__ = 'kenall_accessories'
    id = db.Column(db.Integer, primary_key=True)
    accessories = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico_accessories.id'), nullable=False)

class KenallDiffuser(db.Model):
    __tablename__ = 'kenall_diffuser'
    id = db.Column(db.Integer, primary_key=True)
    diffuser = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico_diffuser.id'), nullable=False)

class KenallDoorframe(db.Model):
    __tablename__ = 'kenall_doorframe'
    id = db.Column(db.Integer, primary_key=True)
    doorframe = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico_doorframe.id'), nullable=False)

class KenallDriver(db.Model):
    __tablename__ = 'kenall_driver'
    id = db.Column(db.Integer, primary_key=True)
    driver = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico_driver.id'), nullable=False)

class KenallLamp(db.Model):
    __tablename__ = 'kenall_lamp'
    id = db.Column(db.Integer, primary_key=True)
    diffuser = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico_function.id'), nullable=False)
    amico_id_CCT = db.Column(db.Integer, db.ForeignKey('amico_CCT.id'), nullable=False)

class KenallModel(db.Model):
    __tablename__ = 'kenall_model'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico_model.id'), nullable=False)

class KenallMounting(db.Model):
    __tablename__ = 'kenall_mounting'
    id = db.Column(db.Integer, primary_key=True)
    mounting = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico_mounting.id'), nullable=False)

class KenallOptions(db.Model):
    __tablename__ = 'kenall_options'
    id = db.Column(db.Integer, primary_key=True)
    options = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico_options.id'), nullable=False)
    amico_id_switch = db.Column(db.Integer, db.ForeignKey('amico_switch.id'), nullable=False)

class KenallVoltage(db.Model):
    __tablename__ = 'kenall_voltage'
    id = db.Column(db.Integer, primary_key=True)
    voltage = db.Column(db.String, nullable=False)
    amico_id = db.Column(db.Integer, db.ForeignKey('amico_voltage.id'), nullable=False)
