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

        def get_equivalent(kenall_query, amico_model, attr):
            kenall_part = kenall_query.first()
            if kenall_part and getattr(kenall_part, "amico_id", None):
                amico_part = amico_model.query.get(kenall_part.amico_id)
                return getattr(amico_part, attr, None) if amico_part else None
            return None

        # Search each field
        results['amicoModel'] = get_equivalent(
            KenallModel.query.filter_by(model=model), AmicoModel, 'model'
        )
        results['amicoMounting'] = get_equivalent(
            KenallMounting.query.filter_by(mounting=mounting), AmicoMounting, 'mounting'
        )
        results['amicoDiffuser'] = get_equivalent(
            KenallDiffuser.query.filter_by(diffuser=diffuser), AmicoDiffuser, 'diffuser'
        )
        results['amicoLamp'] = get_equivalent(
            KenallLamp.query.filter_by(lamp=lamp), AmicoFunction, 'function'
        )
        results['amicoDriver'] = get_equivalent(
            KenallDriver.query.filter_by(driver=driver), AmicoDriver, 'driver'
        )
        results['amicoVoltage'] = get_equivalent(
            KenallVoltage.query.filter_by(voltage=voltage), AmicoVoltage, 'voltage'
        )
        results['amicoDoorframe'] = get_equivalent(
            KenallDoorframe.query.filter_by(doorframe=doorframe), AmicoDoorframe, 'doorframe'
        )
        results['amicoOptions'] = get_equivalent(
            KenallOptions.query.filter_by(options=options), AmicoOptions, 'options'
        )
        results['amicoAccessories'] = get_equivalent(
            KenallAccessories.query.filter_by(accessories=accessories), AmicoAccessories, 'options'
        )

        # Return results
        if not any(results.values()):  # Check if all results are empty
            return jsonify({"error": "No matching records found."}), 404

        return jsonify(results), 200

    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "Internal server error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
