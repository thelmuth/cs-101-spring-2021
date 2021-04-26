"""
Finds the number of electoral college votes per state, and then
finds the population of each state, in order to compute the people per
electoral college vote per state.

Make a nice plot using matplotlib
"""

from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

def main():
    electoral_votes = scrape_electoral_votes()
    
#     print(electoral_votes)
    
    population = scrape_population()
    
#     print(population)
    
    ### matplotlib wants:
    ### x values = ["Alabama", "Alaska", ...]
    ### y values = [people / electoral vote for each state]

    states = list(electoral_votes.keys())
    states.sort()
    
#     print(states)
#     print(type(states))

    people_per_electoral_vote = []
    for state in states:
        pop = population[state]
        votes = electoral_votes[state]
        
        pop_per_vote = pop / votes
        
        people_per_electoral_vote.append(pop_per_vote)
        
#     print(people_per_electoral_vote)
    
    plt.bar(states, people_per_electoral_vote)
    plt.xticks(rotation=90)
    plt.ylabel("People per electoral college vote")
    plt.show()
    
    
def scrape_population():
    """Returns a dictionary of populations of each state scraped from Wikipedia."""
    
    url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
    source_code = requests.get(url).text
    html = BeautifulSoup(source_code, "html.parser")
    
    first_table = html.find("table")
    
#     print(first_table.find("caption"))
    
    rows = first_table.find_all("tr")
    rows = rows[2:]
    
    population_by_state = {}
    
    for row in rows:
        
        th = row.find("th")
        state = th.text.strip()
        
        if state[-1] == "]":
            state = state[:-3]
            
        cells = row.find_all("td")
        
        population_string = cells[-8].text.strip()
        population = int(remove_commas(population_string))
        
#         print(state, population)

        population_by_state[state] = population
        
    ## Need to separately deal with DC
    tables = html.find_all("table")
    dc_table = tables[1]
    
    dc_cells = dc_table.find_all("td")
    pop_cell = dc_cells[2]
    dc_pop = int(remove_commas(pop_cell.text))
    population_by_state["District of Columbia"] = dc_pop
        
    return population_by_state
    
    
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