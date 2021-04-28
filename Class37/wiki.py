
from bs4 import BeautifulSoup
import requests
import urllib

def main():
    
#     wikipedia("https://en.wikipedia.org/wiki/Hamilton_College")
#     wikipedia("https://en.wikipedia.org/wiki/Science")
    wikipedia("https://en.wikipedia.org/wiki/Epistemology")
    
#     test = "This string (has parentheses) and no longer (has parentheses)."
#     
#     test2 = "This string (has (nested (parentheses) and it) might cause) trouble."
#     print(remove_parentheses(test2))
    
    
    
def remove_parentheses(string):
    """Removes parentheses from the string and everything between them."""
    
    new_string = ""
    opened_parentheses = 0
    
    for char in string:
        if char == "(":
            opened_parentheses += 1
            
        elif char == ")":
            opened_parentheses -= 1
        
        elif opened_parentheses == 0:
            new_string += char
            
    return new_string
    
    

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
        
        ## Find all of the paragraphs, and then go through them
        ## to find the first one that has a link in it.
        paragraphs = html.find_all("p")
        
        link_found = False
        
        for para in paragraphs:

            ## We want to find any parentheses that are in this paragraph
            ## and remove them.
            para_string = str(para)
            para_str_without_parentheses = remove_parentheses(para_string)
            
            ## Turn the string of HTML back into a BeautifulSoup object, so we
            ## can find the link in it.
            para = BeautifulSoup(para_str_without_parentheses, "html.parser")

            ## Find the first link in <p>
            ## JUST KIDDING: Find all links, and then look for the first one
            ## that starts with /wiki/
            all_links = para.find_all("a")
            
            for link in all_links:
                
                # get the link's href
                href = link["href"]
            
                if href.startswith("/wiki/"):
                
                    url = urllib.parse.urljoin(url, href)
                    
    #                 print("First link's text", first_link.text)
                    
                    print(url)
                    
                    ## A switch to tell us if we found a link
                    link_found = True
                    
                    ## break - this immediately ends the loop you are currently in
                    break
            
            ### This checks if our inner loop found a link, and if so, breaks out of
            ### paragraph loop
            if link_found:
                break
                
                
                
        
        
        
    
    
    
    
    


main()