from flask import Flask, request, redirect
from packages import md_creator
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# This route gets a JSON file from the frontend with the parameters to create the MD
@app.route('/create_md', methods=['POST'])
def create_md():

    # We get the JSON file from the frontend.
    data = request.get_json()

    filename=''

    try:
        # We create the MD file.
        filename = md_creator.create_md(data)

    except Exception as e:
        # We return the error.
        return str(e)

    text = str(open('output/'+filename+'.md', 'r').read())

    # We delete the file.
    os.remove('output/'+filename+'.md')

    # We return the file created.
    return text


if __name__ == '__main__':
    app.run(debug=False)