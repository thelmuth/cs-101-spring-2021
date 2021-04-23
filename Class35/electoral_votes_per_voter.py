"""
Finds the number of electoral college votes per state, and then
finds the population of each state, in order to compute the people per
electoral college vote per state.

Make a nice plot using matplotlib
"""

from bs4 import BeautifulSoup
import requests

def main():
    electoral_votes = scrape_electoral_votes()
    
#     print(electoral_votes)
    
    population = scrape_population()
    
    print(population)
    
    
def scrape_population():
    """Returns a dictionary of populations of each state scraped from Wikipedia."""
    
    url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
    source_code = requests.get(url).text
    html = BeautifulSoup(source_code, "html.parser")
    
    first_table = html.find("table")
    
#     print(first_table.find("caption"))
    
    rows = first_table.find_all("tr")
    rows = rows[2:]
    
    for row in rows:
        
        th = row.find("th")
        state = th.text.strip()
        
        if state[-1] == "]":
            state = state[:-3]
            
        cells = row.find_all("td")
        
        population_string = cells[-8].text.strip()
        population = int(remove_commas(population_string))
        
        print(state, population)
    
    
def remove_commas(string_version_of_integer):
    """Removes the commas from this string."""
    
    new_string = ""
    for char in string_version_of_integer:
        if char != ",":
            new_string += char
            
    return new_string
    

def scrape_electoral_votes():
    """Returns a dictionary of the electoral college votes for each state."""
    
    url = "https://www.britannica.com/topic/United-States-Electoral-College-Votes-by-State-1787124"
    
    ### get returns the data from the url.
    ### .text gives us the actual source code
    source_code = requests.get(url).text
    
    ### creates a BeautifulSoup object, which stores all of the data about the HTML
    html = BeautifulSoup(source_code, "html.parser")

    electoral_votes = {}
    
    ### This finds the _first_ table in the page
    table = html.find("table")
    
    ### Find all table rows in the source code
    ### This returns a list of new BeautifulSoup objects, so we can look through the
    ### list and find other things within it.
    rows = table.find_all("tr")

    ### Iterate through the list of table rows:
    for row in rows:
        
        ## Find all td elements within a row
        cells = row.find_all("td")
        
        # Make sure row has some td cells
        if cells != []:
#             print(cells[0].text)
#             print(cells[1].text)
#             print(cells[2].text)
#             print(cells[3].text)
        
            ## Fill our dictionary with the data we've scraped
            electoral_votes[cells[0].text] = int(cells[1].text)
            
            if cells[2].text != "":
                electoral_votes[cells[2].text] = int(cells[3].text)
        

    return electoral_votes
        


main()