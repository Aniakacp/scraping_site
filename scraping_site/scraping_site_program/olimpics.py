from bs4 import BeautifulSoup
import requests
import csv
from psycopg2 import connect

class Country:
    def __init__(self, name):
        self.name= name
        self.medals={'gold':0, 'silver':0, 'bronzer':0, 'NA':0}

class Olimpics:
    def __init__(self):
        self.country=None

    @staticmethod
    def clean_input(row):
        """
        Clean and sanitize the input so that it does not contain leading and trailing spaces
        """
        return [r.strip() for r in row]

    def get_data(self, file_name="/home/aniakacp/scraping_site/scraping_site_program/files/athlete_events.csv"):
        with open(file_name, "r") as f:
            country_list=[]
            medals_list=['Silver', 'Bronze', 'Gold', 'NA']
            lines = f.readlines()
            headers = lines[0].split(',')
            print(headers[9]) #year
            print(headers[11]) #medal
            print(headers[6]) #city

            for line in lines:
                if line != lines[0]:
                    arg = line.split(',')
                    if arg[6] not in country_list:
                        country_list.append(arg[6])

            for x in country_list:
                print(x)
        f.close()
    def save_to_DB(self):

        cnx = connect(host='localhost', port=5432, user='postgres', password='coderslab', database='athletes')
        cnx.autocommit = True
        cursor = cnx.cursor()
        for row in csv.reader("/home/aniakacp/scraping_site/scraping_site_program/files/athlete_events.csv"):
            cursor.execute(
                '')
        cnx.commit()
        cnx.close()


    def soup(self):
        r = requests.get('https://www.kaggle.com/mysarahmadbhat/120-years-of-olympic-history/version/1?select=athlete_events.csv')
        soup = BeautifulSoup(r.content, 'html5lib')
        print(soup.prettify())
        #if soup.find("div", {"id": "result-stats"}):
        #    print(soup.find("div", {"id": "result-stats"}))

if __name__ == "__main__":
    a = Olimpics()
    a.save_to_DB()

