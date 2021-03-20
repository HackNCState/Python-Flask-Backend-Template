# Job Searcher Backend

This is a simple Python based Flask REST API that maps the GET endpoint for job scrapping from Indeed.com. This endpoint is used by the Front End Workshop to build a web-application that displays job listings.

## Install Python

PackHacks Hacker Guide: [How to install Python
](https://www.notion.so/Hacker-Resources-cb0b84f22831494fb174571c065f502c#03d184ea17834231b0cc88b834352b0a)

## Install a Text Editor

Although any text editor will technically work, I'd recommend one that has some tools to help us write Python.

 - [Visual Studio Code](https://code.visualstudio.com/) is an open-source code editor created by Microsoft. It's the editor I use throughout.
 - [Atom](https://atom.io/) is a free and open-source text editor developed by GitHub. You can install a package like [atom-beaufity](https://atom.io/packages/atom-beautify) to help format your code.

 ## Install Postman

 Postman is a platform for API development and testing that I will be using to show that our work is actually working while in development! Please signup for Postmand and download it. If you are intersted in API development, this is a very powerful tool. [Download Here](https://www.postman.com/)

## Clone Your Personal Repo (Optional)
We would recommend creating a personal repo for this project. We have a template repo that we are providing to you, which has a directory structure that is also recommended for you to follow.  
If you would not like to use a GitHub repo, you are free to use a local directory with a similar directory structure.

## Clone Our Template Repo
Clone [this](https://github.com/PackHacks/Python-Flask-Backend-Template) template repo. Please **DO NOT CLONE TO THE SAME DIRECTORY FROM ABOVE** as this will make it hard to work on the next part!


## Building Environment
From your initial project directory, open a terminal window (I'm using the integrated terminal in VSCode).  
### Attending Both Backend and Frontend Workshops
Run these commands:  
`mkdir backend` <br>
`cd backend` <br>
`mkdir jobsearcher` <br>
`cd jobsearcher` <br>
`mkdir api`  

### Attending Only Backend Workshop 
Run these commands:  
`mkdir jobsearcher` <br>
`cd jobsearcher` <br>
`mkdir api`  

### Build Virtual Environment
`cd` to the `api` directory you just made.  
I always create a virtual environment called *env* in my project directory, so let's do that now:
`python -m venv env`

To activate the virtual environment:

 - On Unix-based OSs: `source env/bin/activate`
 - On Windows: `env\Scripts\activate`

You will be welcomed by `(env)` in front of your console line. To leave the virtual environment, type `exit` in the console.

### Install Required Libraries
To successfully create a working REST API we need some libraries! Libraries are pre-compiled code that allows developers to expand the functionality of their code past the pure language, in our case Python. We will be installing 4 libraries into our virtual environment.

These libraries are as follows:

 - [Request](https://pypi.org/project/requests/)
 - [Flask](https://pypi.org/project/Flask/)
 - [Python-dotenv](https://pypi.org/project/python-dotenv/)
 - [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

To install these into our virtual environment:

 1. Make sure your virtual environment is running.
 2. Run this command `pip install request flask python-dotenv beautifulsoup4`
 3. This will take some time but the libraries will be installed.

## We Are Now Ready to Start!
[Develop!](https://github.com/PackHacks/Python-Flask-Backend-Template/blob/main/backend/jobsearcher/api/DEV.md)
