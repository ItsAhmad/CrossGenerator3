import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *

app = Flask(__name__)

# Use the connection URL from Render's database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    "DATABASE_URL",
    "postgresql://amico_cross_db_user:cgY8HXuK313UxBOnacSOKfDccWl9pGYl@dpg-ct49jhlumphs73e4l150-a.oregon-postgres.render.com/amico_cross_db"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

@app.route('/api/search-part', methods=['POST'])
def search_part():
    data = request.json  # Receive JSON data
    if not data:
        return jsonify({"error": "Invalid or missing input data."}), 400

    # Extract input values
    model = data.get('model')
    mounting = data.get('mounting')
    diffuser = data.get('diffuser')
    lamp = data.get('lamp')
    driver = data.get('driver')
    voltage = data.get('voltage')
    doorframe = data.get('doorframe')
    options = data.get('options')
    accessories = data.get('accessories')

    # Validate required fields
    required_fields = [model, mounting, diffuser, lamp, driver, voltage, doorframe]
    if not all(required_fields):
        return jsonify({"error": "All required fields must be provided."}), 400

    try:
        # Search for equivalents in the database
        results = {}

        # Search Model
        if model:
            kenall_model = KenallModel.query.filter_by(model=model).first()
            results['amicoModel'] = kenall_model.amico_id if kenall_model else None

        # Search Mounting
        if mounting:
            kenall_mounting = KenallMounting.query.filter_by(mounting=mounting).first()
            results['amicoMounting'] = (
                AmicoMounting.query.get(kenall_mounting.amico_id).mounting
                if kenall_mounting and kenall_mounting.amico_id
                else None
            )

        # Search Diffuser
        if diffuser:
            kenall_diffuser = KenallDiffuser.query.filter_by(diffuser=diffuser).first()
            results['amicoDiffuser'] = (
                AmicoDiffuser.query.get(kenall_diffuser.amico_id).diffuser
                if kenall_diffuser and kenall_diffuser.amico_id
                else None
            )

        # Search Lamp
        if lamp:
            kenall_lamp = KenallLamp.query.filter_by(diffuser=lamp).first()
            results['amicoLamp'] = (
                AmicoFunction.query.get(kenall_lamp.amico_id).function
                if kenall_lamp and kenall_lamp.amico_id
                else None
            )

        # Search Driver
        if driver:
            kenall_driver = KenallDriver.query.filter_by(driver=driver).first()
            results['amicoDriver'] = (
                AmicoDriver.query.get(kenall_driver.amico_id).driver
                if kenall_driver and kenall_driver.amico_id
                else None
            )

        # Search Voltage
        if voltage:
            kenall_voltage = KenallVoltage.query.filter_by(voltage=voltage).first()
            results['amicoVoltage'] = (
                AmicoVoltage.query.get(kenall_voltage.amico_id).voltage
                if kenall_voltage and kenall_voltage.amico_id
                else None
            )

        # Search Doorframe
        if doorframe:
            kenall_doorframe = KenallDoorframe.query.filter_by(doorframe=doorframe).first()
            results['amicoDoorframe'] = (
                AmicoDoorframe.query.get(kenall_doorframe.amico_id).doorframe
                if kenall_doorframe and kenall_doorframe.amico_id
                else None
            )

        # Search Options
        if options:
            kenall_options = KenallOptions.query.filter_by(options=options).first()
            results['amicoOptions'] = (
                AmicoOptions.query.get(kenall_options.amico_id).options
                if kenall_options and kenall_options.amico_id
                else None
            )

        # Search Accessories
        if accessories:
            kenall_accessories = KenallAccessories.query.filter_by(accessories=accessories).first()
            results['amicoAccessories'] = (
                AmicoAccessories.query.get(kenall_accessories.amico_id).options
                if kenall_accessories and kenall_accessories.amico_id
                else None
            )

        # Return results
        return jsonify(results), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred while processing the request."}), 500


if __name__ == '__main__':
    app.run(debug=True)
