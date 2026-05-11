from flask import Flask, jsonify
# Allows frontend (HTML/JS) to communicate with Flask
from flask_cors import CORS
# Lets Python run external programs like C++ executables
import subprocess

# Create the Flask application
app = Flask(__name__)
# Enable CORS so browser fetch() requests are allowed
CORS(app)

# Create an API route
# When user visits: http://127.0.0.1:5000/get-cpp-data, this function will run
@app.route('/get-cpp-data')
def get_data():
  # Python runs the compiled C++ executable and grabs the output
  result = subprocess.check_output(["main.exe"])

  # Send data back to JS as JSON
  return jsonify({
      "status": "success",
      # result is bytes, so decode it into readable text
      "output": result.decode('utf-8')
  })

if __name__ == "__main__":
  # Run server on port 5000, URL becomes: http://127.0.0.1:5000
  app.run(debug=True, port=5000)