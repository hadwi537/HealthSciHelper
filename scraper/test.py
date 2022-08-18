import requests
from html.parser import HTMLParser

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

subject_to_html

for paper in subject_to_html.keys():
    search = "http://www.otago.ac.nz" + subject_to_html[paper]
    paperHTML =  requests.get(search)
