from flask import Flask, render_template, request, jsonify
import urllib.parse
import requests

app = Flask(__name__)

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "6e2VRrxJZLUOJTCyDcYbLAgceo9vQAOR"  # Replace with your MapQuest API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_directions', methods=['POST'])
def get_directions():
    orig = request.form['source']
    dest = request.form['destination']
    unit = request.form['unit']
    path = request.form['path']
    avoids = request.form.getlist('avoid')

    # You can now use the 'orig', 'dest', 'unit', 'path', and 'avoids' values to make your MapQuest API request.
    # Build your MapQuest API request URL and process the response.

    # Example code for constructing the URL (you may need to modify it according to your needs):
    url = main_api + urllib.parse.urlencode({
        "key": key,
        "from": orig,
        "to": dest,
        "unit": unit,  # Use the user-selected unit
        "routeType": path,  # Use the user-selected path
        "doNotUse": avoids  # Use the user-selected avoids
    })

    json_data = requests.get(url).json()

    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True, port=5006)

