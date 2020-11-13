# Web Scraper

This web scraper is created using Beautiful Soup. A csv file is the result after requesting information from a url, creating a soup object, parsing through HTML elements, separating information by type and creating a dataframe. A dataframe is then converted to a CSV and exported.

## Installation Setup

These requirements may already be satified on your machine, but if not, open terminal and install:
`pip3 install pandas`
`pip3 install beautifulsoup4`
`pip3 install requests`

## Troubleshooting

When importing packages beautiful soup should be imported as `from bs4 import BeautifulSoup`. The import statement may not be recognized. DON'T PANIC. Go into the settings of your text editor, click Settings (Preferences on a Mac) and go to Python Interpreter. There should be an option for beautifulsoup4 click that and press OK. If there is still some issue, install a virtual enviroment with `pip3 install virtualenv` and test the install `virtualenv --version`. Then create a virtual enviroment `virtualenv name_of_directory`.

<https://github.com/ryreadme/web-scraper/blob/master/Settings_Preferences.png>
<https://github.com/ryreadme/web-scraper/blob/master/Python_Interpreter.png>

## Technologies Used

Text Editor: PyCharm
Packages:

1. Python
2. Pandas
3. Requests
4. Beautiful Soup

<https://github.com/ryreadme/web-scraper/blob/master/applications.csv>
