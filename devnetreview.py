 
"""
 Best Picture Nominees
- Minari
- Sound of Metal
- Mank
- Promising Young Woman
- The Father
- Judas and the Black Messiah
- The Trial of the Chigago 7
- Nomadland
For each movie, obtain:
- Year
- Rating
- Director(s)
- Plot
- Cast (top 5)
- Genre
Create a pretty table and store the output in a file called output.txt
Post the source code and the output file in your github.
Share the link with sarifern@cisco.com
The first submission of each category (begineer, intermediate, advanced) will get a price. 
"""

import requests
import json
from prettytable import PrettyTable

#Define the URL
omdbAPIURL = 'http://www.omdbapi.com/?t='
omdbAPIKey = 'd54429ee'

#Define the titles
nominees = ['Minari', 'Sound of Metal', 'Mank', 'Promising Young Woman', 'The Father', 'Judas and the Black Messiah', 'The Trial of the Chicago 7', 'Nomadland']

#Define the dict
table = []

for nom in nominees:
    term = nom.replace(' ', '+')
    url = omdbAPIURL + term + '&apikey=' + omdbAPIKey
    response = requests.get(url)
    data = response.json()

    """
    nomineeAns = {
        'Title': data['Title'],
        'Year': data['Year'],
        'Rating': data['imdbRating'],
        'Director': data['Director'],
        'Plot': data['Plot'],
        'Cast': data['Actors'],
        'Genre': data['Genre']
    }
    """

    nomineeAns = [
        data['Title'],
        data['Year'],
        data['imdbRating'],
        data['Director'],
        data['Plot'],
        data['Actors'],
        data['Genre']
    ]
    
    table.append(nomineeAns)

headers = ['Title', 'Year', 'Rating', 'Director', 'Plot', 'Cast', 'Genre']

ptable = PrettyTable()
ptable.field_names = headers
ptable.add_rows(table)

with open('output.txt', 'w') as file:
    file.truncate(0)
    file.write(ptable.get_string())





