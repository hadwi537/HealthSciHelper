import requests
from html.parser import HTMLParser
import pandas as pd
from bs4 import BeautifulSoup
from pprint import pprint

# This will end up on a vm at some point

subject_to_html = dict()

class OtagoHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if (len(attrs) > 1):
            if (attrs[1][0] == 'title'):
                #should use the hanmdle data method
                subject_to_html[attrs[1][1]] = attrs[0][1]
        
    def handle_endtag(self, tag):
        # print("Encountered an end tag :", tag)
        pass 

    def handle_data(self, data):
        # print("Encountered some data  :", data)
        pass

parser = OtagoHTMLParser()

A_Z_papers = requests.get('https://www.otago.ac.nz/courses/subjects/a-z/')
response = A_Z_papers.text

parser.feed(response)

class Paper:
    '''
    The addition of a paper descirption would be a good idea
    '''

    def __init__(self, paper_code, year, title, points, teaching_period, subject, prerequistes = "none", more_info='None'):
        self.paper_code = paper_code
        self.year = year
        self.title = title
        self.points = points
        self.teaching_period = teaching_period
        self.subject = subject
        self.prerequistes = prerequistes
        self.more_info = more_info

    def __repr__(self):
        return str(self.__dict__)


def get_dl(soup):
    keys, values = [], []
    for dl in soup.findAll("dl"):
        for dt in dl.findAll("dt"):
            keys.append(dt.text.strip())
        for dd in dl.findAll("dd"):
            values.append(dd.text.strip())
    return dict(zip(keys, values))


subject_paperInfo = dict()
paper_dict = dict()
for subject in subject_to_html.keys(): #tABLES ARE options for degree + all papers
    search = "http://www.otago.ac.nz" + subject_to_html[subject]
    paperHTML =  requests.get(search)

    papers = None
    paper_search_defualt = "https://www.otago.ac.nz/courses/papers/index.html?papercode="
    try:
        list_of_df = pd.read_html(search)
        table_num = len(list_of_df) #include if more than n tables 
        if (table_num > 5): #vauge cutoff point for little v small subjects
            papers = list_of_df[table_num-1]
            papers.columns = [c.replace(' ', '_') for c in papers.columns]
            for row in papers.itertuples():
                search  = paper_search_defualt + row.Paper_code
                paperPage = requests.get(search)
                soup = BeautifulSoup(paperPage.content, "html.parser")
                dl_dict = get_dl(soup)

                prereq = "none"
                try:
                    prereq = dl_dict["Prerequisite"]
                except:
                    pass

                paper_dict[row.Paper_code] = Paper(row.Paper_code, row.Year, row.Title, row.Points,
                row.Teaching_period, subject, prereq, dl_dict)

    except Exception as e:
        print("An exception has occured")
        print(e)

pprint(paper_dict)
df = pd.DataFrame([paper_dict])
df.to_csv('paper_dict.csv')