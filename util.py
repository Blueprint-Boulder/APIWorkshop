# Utilities file
import requests
from flask import Flask

# Takes in a city (string) and determines whether Teleport has it available
# @param location: string indicating location to check
# @return url: URL if valid, empty string if not
def check_valid_location(LOCATION):
    urban_areas = 'https://api.teleport.org/api/urban_areas/'
    ua_json = requests.get(urban_areas).json()
    BASE_URL = ''
    for location in ua_json["_links"]["ua:item"]:
        if LOCATION.lower() in location['name'].lower():
            BASE_URL = location['href']
            break

    # Return valid url or empty
    if BASE_URL != '':
        BASE_URL += "scores/"
    return BASE_URL

# Generates dashboard HTML code given a location and the API response
# @param location: string indicating dashboard location
# @param json_resp: JSON data from TeleportAPI get request
# @return html: generated dashboard code
def generate_html(LOCATION, json_resp):
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