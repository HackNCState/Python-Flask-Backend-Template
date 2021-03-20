# Lets Start Developing!

We are going to make the simple Flask backend first before wrapping the scrapping function in.

## Starting with Flask

Create a file *api.py* by right-clicking -> New File (in Visual Studio Code).

In *api.py* we need Flask, request, and jsonify from the flask library. To do this, copy over the import <br>`from flask import Flask, request, jsonify` <br>from the cloned template repo.

Return twice then add <br> `app = Flask(__name__)` <br> The `__name__` variable is set by Python and is the module name, in this case *api*. Our module name is passed into the Flask constructor to describe the name of the application from the [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask).

Return twice then add <br> `@app.route('/retrieveJobs', methods=['GET'])` <br> This block of code adds the GET routing at the API endpoint `/retrieveJobs`. This means that if we were to test this backend with a utility like Postman, we would submit the GET HTTP request from 127.0.0.1:5000/retrieveJobs. **I will cover how to do this live in the workshop**

Return once then add a function with any name that will run when the api endpoint is called. In my case I used `getJobs()`. Any code in this function block will now run once the api endpoint is called.

We now need to create a list. Here I called it `data = []` but you can really call it anything! This list is what we are going to "jsonify" shortly to return to the caller of the API.

Return once.

In my template I included an if statement to get to make sure the  requesting method is `GET` even though that is the only requesting method that is routed for. However, if you are creating your own backends (away from this workshop) you can entertain many request types (`GET` `POST` `PUT` `DELETE` for example) from one endpoint. This isn't really the best design but it can be done. This if statement ensures that the `GET` method is the only one we are wanting to provide functionality for at this time.

Return once.

We now have to set the `data` variable to the the value provided in the template: <br>
`[dict(id='1', name='max', email='max@gmail.com')]` <br>
This is a testing dictionary. We will change this as soon as we know everything you've set up works!

Return once.

We are now going to create a variable `response` that will be set to the `jsonify(data)`. This creates a JSON object from the data dictionary list and places it into the `response` variable. With this variable, we are also going to set the `.status_code` for the `response` variable to 202 (the HTTP status for `Accepted`). This response code will be passed with the JSON information to the caller to notify them that the action they took was accepted. There are a slew of HTTP status numbers you can use here, I just chose 202 for simplicity.

Return once.

Lastly we are going to return the `response` variable to the caller!

Congradulations! You've just created your first API. Admittedly, it doesn't do much yet, but we will change that shortly!

## Writing the Indeed.com Webscraper
Create a file *indeedScraper.py* by right-clicking -> New File (in Visual Studio Code).

In *indeedScraper.py* we need to import requests <br> `import requests` <br> We also need BeautifulSoup from bs4 <br> `from bs4 import BeautifulSoup`

The way I write web scrapers is a three function design strategy. I usually do an `extract` function, a `transform` function, and the caller function, which in this case is `getList`. We will break these down below.

### The `extract` Function
This extract function extracts the html webpage from the url we are giving it and returning it ot eh caller (using request and BeautifulSoup).

We first have to study the webpage we are wanting to scrape. We are using Indeed.com for this scraping, so navigate to where you want on that site. The url we are using for scraping is <br> `https://www.indeed.com/jobs?q=Software+Engineer&l=Raleigh%2C+NC&radius=50` which is a job search for "Software Engineering" within 50 miles from "Raleigh, NC". You can search for anything you want here, but the url above is what I will be using.

Back to the function! The first thing we need to do is create a headers variable, which is structured like: <br> `headers = {'User-Agent': ''}` <br> You will need to find your user agent on your own. You can do this by searching "my user agent" in your preferred search engine. <br> Mine looked something like this: <br> `'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'`  <br> Place this string in the headers variable like: <br> `{'User-Agent': 'my user agent'}`

Return once.

Now place the url we found into a `url` variable. Make sure to place the letter f in front of your string so that you can add some formating to the string with the parameter `(pageNum)` to the extract function. I will talk about this during the live workshop.

Return once.

Now, we are going to create another variable, `r`, which is where we are going to place the request response. Please enter: <br> `requests.get(url, headers)` to be set equal to the variable you just created. This is the HTTP GET request call that pulls all the website data from the url into the script and places it into the `r` var.

Return once.

Now, we are going to create another variable, `soup`, which is where we are going to place the BeautifulSoup constructor response. Please enter: <br> `BeautifulSoup(r.content, 'html.parse')` to be set equal to the variable you just created. This is where we call the BeautifulSoup library for parsing the content from the webpage. Invoking `.content` on the request gives us the bytes that we can parse. We are parsing the webpage's html so we are going to user `'html.parser'`, but we could've also used `'xml.parser'` if we were parsing xml content. BeautifulSoup returns the html content parsed from the request.

Return once.

Return the `soup` variable you created and now that function is done!

### The `transform` Function
This transform function pulls the information from the html content extracted by the `extract` function. We pull all the information we want from the html here and add a job dictionary to a jobList list.

We first have to study the webpage we are wanting to scrape. We are using Indeed.com for this scraping, so navigate to where you want on that site. The url we are using for scraping is <br> `https://www.indeed.com/jobs?q=Software+Engineer&l=Raleigh%2C+NC&radius=50` which is a job search for "Software Engineering" within 50 miles from "Raleigh, NC". You can search for anything you want here, but the url above is what I will be using. At this portion of the webpage investagtion we are looking for the html blocks that we can pull information  from. 

Indeed structures its job information into divs named 'jobsearch-SerpJobCard'. We will show you how to find this div while on the Indeed Job Search page and where to find the others below. For this, we are finding all the job search cards by div from the soup by invoking `find_all` on the soup parameter. For Indeed, this should return a list (of len 15) of cards that we can further search through.

Return once.

Now, we are going to create a variable I called `allDivs` and set it equal to this block of code: <br> `soup.find_all('div', class_ =  'jobsearch-SerpJobCard')` <br> This block of code finds all instances of the class `'jobsearch-SerpJobCard'` and returns a list of these instances from the soup.

Return once.

We are now going to loop through the list we just created with a for-each loop. To do this place: <br> `for item in allDivs` to do this. <br> All the code in this for loop will  be where we parse the most specific blocks of the job cards.

Return once.

Investigating the Indeed webpage, we can see that the title is held within the first `'a'` block. We find the first instance of `'a'` in the card and get the striped text. This text is the title of the job we are scraping for, thus, we place it into the title var. We invoke `find` instead of find_all because we don't want a list of all 'a' blocks. To do this, we need to create a new variable: `title` and set it equal to: <br> `item.find('a').text.strip()`

Return once.

Investigating the Indeed webpage, we can see that the name of the company is held within the first `'span'` field in the class `'company'`. We invoke find here with `'span'`, looking in the `class_` `'company'` to get the text, which is the stripped then assigned to the company var. To do this, we need to create a new variable: `company` and set it equal to: <br> `item.find('span', class_ = 'company').text.strip()`

Return once.

Indeed doesn't force employers to add the salary to the job posting, but if they do, we want to catch it. We do this by placing our find block in a `try except` block. Find a posting that has a salary and investigate it like we did for the previous two fields. The salary is held within the first `'span'` field in the class `'salaryText'`. We invoke find here with `'span'`, looking in the `class_` `'salaryText'` to get the text. If it exists, it is stripped then assigned to the salaray var. If it doesn't exist then set the salary var to be empty (`''`). To do this, we need to create a new variable: `salary` and set it equal to: <br> `item.find('span', class_ = 'salaryText').text.strip()` <br> This is place in the `try execpt` block.

Return once.

Investigating the Indeed webpage, we can see that the job summary of the listing is held within the the first div in the class `'summary'`. We invoke find here with `'div'`, looking in the `class_` `'summary'` to get the text, which is then stripped. While developing this system the summary appeared to have a lot of unneeded new line characters, so I replaced the new line character with the `''` character by invoking `replace`. To do this, we need to create a new variable: `summary` and set it equal to: <br> `item.find('div', class_ = 'summary').text.strip().replace('\n', '')`

Return once.

We are now done with getting all the information! All we need to do now is build the `job` dictionary with all the information and `append` that dictionary to the `jobList` that we will create in the next function. Follow the structure below to create the dictionary: <br> `job = { 'title': title, 'company': company, 'salary': salary, 'summary': summary }` 
With the dictionary created, append to the `jobList` list like: `jobList.append(job)`.

Return the jobList and **MAKE SURE IT'S OUTSIDE THE FOUR EACH LOOP OR YOU WILL ONLY BE ABLE TO SCRAPE ONE JOB**

Congrats! We only have one more function then this file will be done!

### The `getList` Function
This getList function is the front facing function for this file. This function is called by the Flask endpoint to get the full list of job dictionaries.

Return once.

We need to create the `jobList` variable to be used in the `transform` function.

Return once.

Now, we just need to loop through however many jobs we want with a `for each` loop. Indeed handles pages in groups of 10s by the url but there are 15 jobs on each page. This for loop gets a certain number of pages. You can increase the middle value by 10 to get 15 more jobs. `range` here is used to do the `for each` loop so that we can pass the page number to the `extract` function. `range(0, 50, 10)` returns a list of 0, 10, 20, 30, 40, and 50 that the loop loops through.

Return once.

Now we need a caller to the `extract` function. With the `for each` loop we can pass in the page number to the extract function and use the `soup` content. To do this, use: `content = extract(pageNumber)`

Return once.

Pass the `content` variable to the `transform` function. To do this, use: `transform(jobList, content)`.

And we're done! All we have to do is return the jobList for the getList function and your webscraper is fully functional!!

## Finishing Up the Flask Implementation!
In *api.py* we need to add some more imports to fully implement the code base we just wrote! To do this, enter: `from indeedScraper import getList` &<br> `from flask_cors import CORS` under the original `from flask import Flask, request, jsonify` import.

Under the original `app = Flask(__name__)` we are going to add the CORS specifications for this API to work well with the React frontend. To do this, all we have to do is invoke the CORS constructor with the original app object with `CORS(app)`. If you have questions about CORS, check [this](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) link out.

The last thing we need to edit from the original *api.py* is the assigning to the `data` variable. Currently, we just created an example dictionary list, but now all we have to do is call the `getList()` function that we imported from the *indeedScraper.py* that we wrote!

Everything else stays the same!!

THE BACKEND IS DONE! CONGRADULATIONS!!

We are going to do some live testing during the workshop with Postman.