# author: @ryreadme
# Linkedin Job Scraper

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Linkedin url
url = 'https://www.linkedin.com/jobs/search?keywords=Junior%20Software%20Engineer' \
      '&location=Toronto%2C%20Ontario%2C%20Canada&geoId=100025096' \
      '&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0'

# gets the page
page = requests.get(url)

# create a beautiful soup object and returns the html of the entire page
soup = BeautifulSoup(page.content, 'html.parser')

# gets all the job listings in the search
jobs = soup.find_all('li', class_='result-card job-result-card result-card--with-hover-state')

# parses through the jobs to extract the text from the elements
for job in jobs:
    title = job.find('h3', class_='result-card__title job-result-card__title').get_text().strip()
    company = job.find('h4', class_='result-card__subtitle job-result-card__subtitle').get_text().strip()
    location = job.find('span', class_='job-result-card__location').get_text().strip()
    link = job.find('a')['href']
    print(title)
    print(company)
    print(location)
    print(link + '\n')

# extracting the data by type to place in a dataframe
job_titles = [job.find('h3', class_='result-card__title job-result-card__title').get_text().strip() for job in jobs]
job_companies = [job.find('h4', class_='result-card__subtitle job-result-card__subtitle').get_text().strip() for job in jobs]
job_locations = [job.find('span', class_='job-result-card__location').get_text().strip() for job in jobs]
job_links = [job.find('a')['href'] for job in jobs]

# crete the data frame creating columns by type of data
job_applications = pd.DataFrame(
    {
        'Title': job_titles,
        'Company': job_companies,
        'Location': job_locations,
        'Link': job_links
    })

# create and name csv file
job_applications.to_csv('applications.csv')

# Resources:
# Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# find_all by class: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class
