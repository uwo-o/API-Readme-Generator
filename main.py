# We import the following modules:
from flask import Flask, request
import json

app = Flask(__name__)

# This route gets a JSON file from the frontend with the parameters to create the MD
@app.route('/create_md', methods=['POST'])
def create_md():
    # We get the JSON file from the frontend.
    data = request.get_json()

if __name__ == '__main__':
    app.run(debug=True)