from flask import Flask, request, jsonify
from flask.wrappers import Request
from flask_cors import CORS

## This file is the Flask GET API endpoint for the Backend PackHacks workshop.
## We import flask and the getList function from the indeedScraper file we created.
## @author Travis Walter - 3/16/2021
app = Flask(__name__)
CORS(app)

## This is the API GET @ endpoint /retrieveJobs that returns the list of jobs to the caller.
## It uses the Indeed Scraper and returns the parsed information as JSON.
@app.route('/retrieveJobs', methods=['GET'])

## This is the function that is run when the /retrieveJobs endpoint is called, which runs
## the Indeed Scraper and returns the JSON.
##
## *Currently this does not run the Indeed Scraper, as this is something we will work on
## implementing in the workshop!!
def getJobs():
    data = []
    if request.method == 'GET': # Checks if it's a GET request
        ## This sets the data variable to a list of dictionaries, and places one dictionary,
        ## the example dictionary below, to the list.
        data = [dict(id='1', name='max', email='max@gmail.com')]

        ## This "JSON"ifys the dictionary list into a JSON object for returning.
        response = jsonify(data);

        ## This places the HTTP status code 202 ("Accepted")
        response.status_code = 202

        ## Return the JSON object to the caller.
        return response