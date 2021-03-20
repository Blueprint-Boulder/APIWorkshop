# APIWorkshop
T9Hacks Spring 2021 Workshop

## Prerequisites
To complete this workshop, you need to have Python 3 installed, as well as `flask` and `requests`.

To download Python 3: https://www.python.org/downloads/

To install `flask` and `requests`, execute the following commands:
```
> pip install flask
> pip install requests
```

## High Level Idea
Whichever track you’re working on (underserved populations, health, children and education, earth protection and sustainability, or equality), the Teleport API has something that can be relevant to you. Depending where you are in the world, your access to healthcare, affordable housing, and education (and much more) vary immensely -- so, we are going to make a dashboard showcasing these key stats for any given location (available from the API). Hopefully, your newfound API skills will help you bring your hackathon idea to life!

## Instructions
1. First, we will set up our development environment. Download the code from this repository and open up `starter_code.py`.

2. Go to https://developers.teleport.org/ and click 'API' to access Teleport API's documentation. Documentation is super important for software development in general, but it's especially invaluable when using APIs!

    a. Click 'Get Started'

    b. Now you will see various examples of endpoint calls and data returned when you make those calls.

    c. Scroll down to the section titled "INCOME, LIVING COSTS & QUALITY OF LIFE DATA"
    
    d. Copy the example URL (https://api.teleport.org/api/urban_areas/slug:san-francisco-bay-area/scores/) and paste it into your browser. Notice how the data looks!

3. Open up your terminal and run `python starter_code.py`. If you type in `localhost:5000` to your browser, you should see the message "DELETEME -- as you can see, your webpage displays what this function returns!" appear.

4. Yay, our dev environment is all set up! Now we start modifying the code: take a minute to interpret what is happening in the file currently.

    a. Import/initilization code: this gets all of the resources we need, including `flask` (Python library for server-side code), `requests` (the standard Python 3 library to use when querying APIs), and `importlib` (which is used to import other Python files as libraries). Don't worry too much about Flask and ImportLib, those are just to build our dashboard.
    ```
    import requests
    from flask import Flask
    import importlib
    util = importlib.import_module('util')

    app = Flask(__name__)
    ```

    b. The next part of the code is also a result of Flask syntax. This just says that the HTML code returned by this function will go to the home page of our app -- since we have no other pages, this is the default screen. **We will write the code for our dashboard here!**
    ```
    @app.route("/")
    def home():
    ```

    c. This part just starts the Flask app!
    ```
    if __name__ == "__main__":
        app.run(debug=True)
    ```

5. First, let's try using the example URL we found in the Teleport API docs. Replace the empty string in line 14:
```
url = 'https://api.teleport.org/api/urban_areas/slug:san-francisco-bay-area/scores/'
```

6. Now, let's grab all of the data from that endpoint using a `GET` request. On line 15, replace the empty string with the follow code. Return the response status code to see if we had a successful API call (status code 200 means the transaction returned `OK`).
```
response = requests.get(url)
return str(response.status_code)
```

7. If you got 200, yay! That means we're ready to turn this data into JSON format -- delete the status code return line from step 6, and add the following code (which transforms the requested data into json and then returns the result). If you would like to better understand what this response looks like, copy the json output. Then, paste this output into a json beautifier and examine the data (if you don't have a preferred one, I would suggest https://jsonformatter.curiousconcept.com/#)
```
json_resp = response.json()
return str(json_resp)
```

8. Now we're ready to generate our dashboard! Delete the line that returns json, and the line `util.generate_html(LOCATION, json_resp)` uses a helper function will do this for us. Refresh our browser at `localhost:5000` and we should see our dashboard for San Francisco! 

9. Now, we want to make our dashboard work for other locations! We can do this using the helper function provided in `util.py` called `check_valid_location()`. As you can see by the comments in `util.py`, this function takes in a location and returns a URL if the location is valid in the Teleport API. If it isn't, the function returns an empty string. Thus, add the following code, replacing the LOCATION string with whatever place you'd like! (major cities tend to work better)
```
LOCATION = 'Denver'
url = util.check_valid_location(LOCATION)
if url == '':
    return 'invalid location'
```

10. Refresh the page again -- if you see `invalid location` on the page, that means Teleport doesn't have your selected city. Try another one, like Denver! Once you see the dashboard again, you should see new stats for your particular location!

And you're done! Congrats, you have completed the workshop!

## More Resources
Want to learn more about APIs? Here are some great resources!
- High level description of APIS: https://www.howtogeek.com/343877/what-is-an-api/ 
- How to use an API: https://rapidapi.com/blog/how-to-use-an-api/
- How to build an API (a great next step if you'd like a challenge!): https://rapidapi.com/blog/how-to-build-an-api-in-python/

Happy learning!