import csv

from bs4 import BeautifulSoup
from googlesearch import search
import os

import requests

class ScrapingText:
    def __init__(self):
       self.keywords=[]

    @staticmethod
    def clean_input(row):
        """
        Clean and sanitize the input so that it does not contain leading and trailing spaces
        """
        return [r.strip() for r in row]

    def get_data(self, file_name="/home/aniakacp/scraping_site/scraping_site_program/files/keywords.text"):

        with open(file_name, newline="") as _file:
            reader = csv.reader(
                _file,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_ALL,
                skipinitialspace=True,
            )
            lines = _file.readlines()
            self.headers= lines[0].split(', ' '')


    def read_file(self, file_name="/home/aniakacp/scraping_site/scraping_site_program/files/keywords.txt"):
        """
            Fetch the data from the given txt file and construct the list of Student objects
        """
        with open(file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                arg= line.split(',')
                self.keywords= self.clean_input(arg)
        f.close()
        return self.keywords

    def search_site(self, keywords):
        response= requests.get('http://www.google.com/search?start=0&num=10&q=red+sox&cr=countryCA')
        return response.request

    def create_file(self, filename):
        if not os.path.exists(filename):
            open(filename, 'w').close()

    def googleSearch(self, keywords=None, file_name="/home/aniakacp/scraping_site/scraping_site_program/files/results.csv"):
        link = 'https://www.searchenginejournal.com/'
        for keyword in self.keywords:
            filename= f"/home/aniakacp/scraping_site/scraping_site_program/files/{keyword}.txt"
            self.create_file(filename= filename)
            for j in search(query = '?q=https://www.searchenginejournal.com/&q=screaming+frog', tld="co.in", num=10, stop=10, pause=2, extra_params= {'filter': link}):
                with open(filename, "a") as f:
                    if j.startswith('https://www.searchenginejournal.com/'):
                        f.writelines(f'{j}/\n')
                    else:
                        f.writelines('')
                f.close()


    def check(self):
        URL = "https://www.google.com/search?q=https://www.searchenginejournal.com/&q=screaming+frog"
        r = requests.get(URL)
        print(r.content)

    def soup(self):
        r = requests.get('https://www.google.com/search?q=https://www.searchenginejournal.com/&q=screaming+frog')
        soup = BeautifulSoup(r.content, 'html5lib')
        print(soup.prettify())
        if soup.find("div", {"id": "result-stats"}):
            print(soup.find("div", {"id": "result-stats"}))

if __name__ == "__main__":
    a = ScrapingText()
    a.read_file()
  #  a.googleSearch()
    a.soup()

