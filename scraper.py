import urllib2
from bs4 import BeautifulSoup

def scrape_website():
    scrape_page = 'StackOverflow.com/jobs'
    page = urllib2.urlopen(scrape_page)
    soup = BeautifulSoup(page, 'html.parser')
    find_link = soup.find('a', attrs={'class': 'job-link'})
    parse_link = 
    find_python = soup.find('a', attrs={'class': 'post_tag job_link no_tag_menu'})
        if find_python == python:

            scrape_page = 