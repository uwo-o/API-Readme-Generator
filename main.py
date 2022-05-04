# We import the following modules:
from flask import Flask, request
from packages import md_creator
import json

app = Flask(__name__)

data = json.load(open('examples/input.json'), encoding='utf-8')

# We create the MD file.
md_creator.create_md(data)

# This route gets a JSON file from the frontend with the parameters to create the MD
@app.route('/create_md', methods=['POST'])
def create_md():

    # We get the JSON file from the frontend.
    # data = request.get_json()
    data = json.loads(request.data)

    # We create the MD file.
    md_creator.create_md(data)

    # We return a message to the frontend.
    return 'MD file created!'


if __name__ == '__main__':
    app.run(debug=True)