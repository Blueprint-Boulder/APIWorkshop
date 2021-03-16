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

3. Open up your terminal and run `python starter_code.py`. If you type in `localhost:5000` to your browser, you should see the message "Location not found! Maybe try another one?" appear.

4. Yay, our dev environment is all set up! Now we start modifying the code: take a minute to interpret what is happening in the file currently.

    a. The top of the file contains the import statement for `requests` (the standard Python 3 library to use when querying APIs) and standard imports for Flask apps. Don't worry about the Flask portions, that's just to make the dashboard, and has nothing to do with using APIs.
    ```
    import requests
    from flask import Flask
    app = Flask(__name__)
    ```

    b. The next part of the code is also a result of Flask syntax. This just says that the HTML code returned by this function will go to the home page of our app -- since we have no other pages, this is the default screen. We will write the code for our dashboard here!
    ```
    @app.route("/")
    def home():
    ```

    c. 'YOUR CODE HERE' segment allocated for step 5.

    d. Checking if location can be found -- this has been done for you. This basically checks whether the location you are choosing to search for actually exists within the API server. If it doesn't, you will get that location error we saw after running our app for the first time.

    e. 'YOUR CODE HERE' segment allocated for steps 6, 7, and 8.

    f. Construct HTML code -- `def home()` returns HTML code for the page, so this is where we construct the dashboard. This has already been done for you.

    g. Starts the Flask app!
    ```
    if __name__ == "__main__":
        app.run(debug=True)
    ```

5. On line 10, choose the location you would like to search. It's best to choose a major city and/or capital -- if you can't decide, feel free to start with Denver.

6. On line 29, make the get request to the API. We do this with the following command, where `url` is the specified endpoint that we are querying. Print the status code of the API response, and ensure that you got `200` (status codes indicate whether the query was successful, and 200 means the transaction returned `OK`).
```
response = requests.get(url)
print(response.status_code)
```

7. Remove the status code troubleshooting statement. Then, on the line with `json_resp`, retrieve the response content from line 29 in json format using the following command. If you would like to better understand what this response looks like, print the json response and copy the output. Then, paste this output into a json beautifier and examine the data (if you don't have a preferred one, I would suggest https://jsonformatter.curiousconcept.com/#).
```
json_resp = response.json()
print(json_resp)
```

8. Lastly, we need to have a check for instances of when we don't get `200` (i.e. success) for our status code response. It's good practice to check for other status codes, so add the following:
```
if response.status_code != 200:
        return 'Error -- notify instructor to help with troubleshooting!'
```

9. If you refresh your page (you may have to rerun the `python starter_code.py` command), you should now see a dashboard containing quality of life statistics for whichever location you chose. 

Congrats, you have completed the workshop!

## More Resources
Want to learn more about APIs? Here are some great resources!
- High level description of APIS: https://www.howtogeek.com/343877/what-is-an-api/ 
- How to use an API: https://rapidapi.com/blog/how-to-use-an-api/
- How to build an API (a great next step if you'd like a challenge!): https://rapidapi.com/blog/how-to-build-an-api-in-python/

Happy learning!