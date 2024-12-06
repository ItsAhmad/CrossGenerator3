import os
from flask_cors import CORS
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

CORS(app)

db.init_app(app)
with app.app_context():
    db.create_all()
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
  required_fields = [model, mounting, diffuser, lamp, driver, voltage, doorframe, options, accessories]
  if not all(required_fields):
     return jsonify({"error": "All required fields must be provided."}), 400

  try:
        # Search for equivalents in the database
        results = {}

        print("Recieved JSON Data:", request.json)

        def get_amico_model(model):
          kenall_query = KenallModel.query.filter_by(model=model)
          kenall_parts = kenall_query.all()
          if kenall_parts:
            for kenall_part in kenall_parts:
              amico_id = kenall_part.amico_id
              amico_part = AmicoModel.query.get(amico_id)
              if amico_part:
                 return amico_part.model
              else:
                 print("nothing found")


        def get_amico_mounting(mounting):
           kenall_query = KenallMounting.query.filter_by(mounting=mounting)
           kenall_parts = kenall_query.all()
           if kenall_parts:
              for kenall_part in kenall_parts:
                 amico_id = kenall_part.amico_id
                 amico_part = AmicoMounting.query.get(amico_id)
                 if amico_part:
                    return amico_part.mounting
                 else:
                    print("nothing found")

        def get_amico_diffuser(diffuser):
           kenall_query = KenallDiffuser.query.filter_by(diffuser=diffuser)
           kenall_parts = kenall_query.all()
           if kenall_parts:
              for kenall_part in kenall_parts:
                 amico_id = kenall_part.amico_id
                 amico_part = AmicoDiffuser.query.get(amico_id)
                 if amico_part:
                    return amico_part.diffuser
                 else:
                    print("nothing found")

        def get_amico_lamp(lamp):
           kenall_query = KenallLamp.query.filter_by(lamp=lamp)
           kenall_parts = kenall_query.all()
           if kenall_parts:
              for kenall_part in kenall_parts:
                 amico_id = kenall_part.amico_id
                 amico_part = AmicoFunction.query.get(amico_id)
                 if amico_part:
                    return amico_part.function 
                 else:
                    print("nothing found - error")

        def get_amico_driver(driver):
           kenall_query = KenallDriver.query.filter_by(driver=driver)
           kenall_parts = kenall_query.all()
           if kenall_parts:
              for kenall_part in kenall_parts:
                 amico_id = kenall_part.amico_id
                 amico_part = AmicoDriver.query.get(amico_id)
                 if amico_part:
                    return amico_part.driver
                 else:
                    print("nothing found")

        def get_amico_voltage(voltage):
           kenall_query = KenallVoltage.query.filter_by(voltage=voltage)
           kenall_parts = kenall_query.all()
           if kenall_parts: 
              for kenall_part in kenall_parts:
                 amico_id = kenall_part.amico_id
                 amico_part = AmicoVoltage.query.get(amico_id)
                 if amico_part:
                    return amico_part.voltage
                 else: 
                    print("nothing found")

        def get_amico_doorframe(doorframe):
           kenall_query = KenallDoorframe.query.filter_by(doorframe=doorframe)
           kenall_parts = kenall_query.all()
           if kenall_parts:
              for kenall_part in kenall_parts:
                 amico_id = kenall_part.amico_id
                 amico_part = AmicoDoorframe.query.get(amico_id)
                 if amico_part:
                    return amico_part.doorframe
                 else:
                    print("nothing found")

        def get_amico_options(options):
           kenall_query = KenallOptions.query.filter_by(options=options)
           kenall_parts = kenall_query.all()
           if kenall_parts:
              for kenall_part in kenall_parts:
                 amico_id = kenall_part.amico_id
                 amico_part = AmicoOptions.query.get(amico_id)
                 if amico_part:
                    return amico_part.options
                 else:
                    print("nothing found")
        
        def get_amico_accessories(accessories):
           kenall_query = KenallAccessories.query.filter_by(accessories=accessories)
           kenall_parts = kenall_query.all()
           if kenall_parts:
              for kenall_part in kenall_parts:
                 amico_id = kenall_part.amico_id
                 amico_part = AmicoAccessories.query.get(amico_id)
                 if amico_part:
                    return amico_part.options
                 else:
                    print("nothing found")

    
        results['amicoModel'] = get_amico_model(model)
        results['amicoMounting'] = get_amico_mounting(mounting)
        results['amicoDiffuser'] = get_amico_diffuser(diffuser)
        results['amicoFunction'] = get_amico_lamp(lamp)
        results['amicoDriver'] = get_amico_driver(driver)
        results['amicoVoltage'] = get_amico_voltage(voltage)
        results['amicoDoorframe'] = get_amico_doorframe(doorframe)
        results['amicoOptions'] = get_amico_options(options)
        results['amicoAccessories'] = get_amico_accessories(accessories)

        return jsonify(results), 200

  except Exception as e:
    print(f"Error processing request: {e}")
    return jsonify({"error": "Internal server error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)

