from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

# https://program-design-project.onrender.com/
@app.route('/')
def home():
  return "Flask backend is running :D"

# https://program-design-project.onrender.com/get-backend-data
@app.route('/get-backend-data')
def get_data():
  try:
    result = subprocess.check_output(["./main"])
    return jsonify({
      "status": "success",
      "output": result.decode('utf-8'),
    })
  except Exception as err:
    return jsonify({
      "status": "error",
      "message": str(err),
    })

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))