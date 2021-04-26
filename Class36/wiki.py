
from bs4 import BeautifulSoup
import requests
import urllib

def main():
    
    wikipedia("https://en.wikipedia.org/wiki/Hamilton_College")
    

def wikipedia(url):
    """Replicates the process of clicking the first link in each
    Wikipedia article until it gets to Philosophy."""
    
    MAX_PAGES = 20
    
    print(url)
    
    # Loop until either we get to Philosophy or reach MAX_PAGES
    for i in range(MAX_PAGES):
        
        source_code = requests.get(url).text
        html = BeautifulSoup(source_code, "html.parser")
        
        ## Find the first <p> tag
        
        ## NEXT TIME: Find all of the paragraphs, and then go through them
        ## to find the first one that has a link in it.
        
        first_paragraph = html.find("p")
#         print(first_paragraph.text)

        ## Find the first link in <p>
        first_link = first_paragraph.find("a")
        
        ## This link is a root relative link (links that start with /)
#         print(first_link)
        relative_link = first_link["href"]
        
        url = urllib.parse.urljoin(url, relative_link)
        
        print(url)
        
        
        
    
    
    
    
    


main()