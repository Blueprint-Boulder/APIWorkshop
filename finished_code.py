import requests
from flask import Flask
import importlib
util = importlib.import_module('util')

app = Flask(__name__)

@app.route("/")
def home():

    # Choose a location and use the utility to find the URL for it
    LOCATION = 'Denver'
    url = util.check_valid_location(LOCATION)
    if url == '':
        return 'invalid location'
    
    # Make GET request and ensure it has an okay status code
    response = requests.get(url)
    json_resp = response.json()
    if response.status_code != 200:
        return 'Error -- notify instructor to help with troubleshooting!'

    # Construct HTML code to return
    return util.generate_html(LOCATION, json_resp)
    
if __name__ == "__main__":
    # Visit localhost:5000 to view!
    app.run(debug=True)
