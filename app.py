from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route('/get-backend-data')
def get_data():
  result = subprocess.check_output(["./main"])

  # Send data back to JS as JSON
  return jsonify({
      "status": "success",
      "output": result.decode('utf-8')
  })

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))