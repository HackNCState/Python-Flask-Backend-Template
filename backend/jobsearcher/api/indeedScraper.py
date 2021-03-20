import requests
from bs4 import BeautifulSoup

## This file is the Indeed.com scraper for the Backend PackHacks workshop. This file is set
## up in a extract, transform, and return format, which should be followed for other similar
## scrappers if you are wanting to scrape other sites.
## We import requests and BeautifulSoup from pip install beautifulsoup4 to do the scrapping.
## @author Travis Walter - 3/16/2021

## This extract function extracts the html webpage from the url we are giving it and returning
## it to the caller (using request and BeautifulSoup). This function needs one parameter that
## I haven't added in this template. This will return an instance of BeautifulSoup, which I
## haven't added in this template.
def extract():
    return ""

## This transform function pulls the information from the html content extracted by the extract
## function. We pull all the information we want from the html here and add a job dictionary to
## a joblist list. This function needs two paramters that I haven't added in this template.
## This will return one of the edited parameters we pass in, which I haven't added in this
## template.
def transform():
    return ""

## This getList function is the frontfacing function for this file. This function is called
## by the Flask endpoint to get the full list of job dictionaries. This will return a list of
## jobs, which I haven't implemented in this template.
def getList():
    return ""