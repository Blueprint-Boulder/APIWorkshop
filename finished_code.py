import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    # ********************* YOUR CODE HERE *********************
    LOCATION = 'Enter your location here!' # Start with Denver!
    # **********************************************************


    # Check if location can be found
    urban_areas = 'https://api.teleport.org/api/urban_areas/'
    ua_json = requests.get(urban_areas).json()
    BASE_URL = ''
    for location in ua_json["_links"]["ua:item"]:
        if LOCATION.lower() in location['name'].lower():
            BASE_URL = location['href']
            break
    
    if BASE_URL == '':
        return "Location not found! Maybe try another one?"
        

    # ********************* YOUR CODE HERE *********************
    url = BASE_URL + "scores/"
    response = requests.get(url)
    json_resp = response.json()
    if response.status_code != 200:
        return 'Error -- notify instructor to help with troubleshooting!'
    # **********************************************************


    # Construct HTML code to return
    html = """
    <h1>Quality of Living</h1><br>
    """

    html += "<h3>Location: " + LOCATION + "</h3>"

    for val in json_resp['categories']:
        if(val['name'] == 'Cost of Living' or val['name'] == 'Healthcare' or val['name'] == 'Education'
        or val['name'] == 'Environmental Quality' or val['name'] == 'Tolerance'):
            color = 'gold'
            if val['score_out_of_10'] > 7:
                color = 'green'
            elif val['score_out_of_10'] < 4:
                color = 'red'
            html += '<p>' + val['name'] + ': <span style="color:' + color + ';">'+ str(round(val['score_out_of_10'], 2)) +'</span>/10</p>'

    return html
    
if __name__ == "__main__":
    # Visit localhost:5000 to view!
    app.run(debug=True)
