'''
Created on 11/05/2018

@author: jruiz
'''

from countries import country_list

def cities_population():
    """
    Define a Dictionary, population
    that provides information 
    on the world's largest cities.
    The key is the name of a city
    (a string), and the associated 
    value is its population in
    millions of people
    """
    #===========================================================================
    # Key         |   Value
    # Shanghai    |    17.8
    # Istanbul    |    13.3
    # Karachi     |    13.0
    # Mumbai      |    12.5
    #===========================================================================
    population = dict()
    population['Shanghai'] = 17.5
    population['Istanbul'] = 13.3
    population['Karachi'] = 13.0
    population['Mumbai'] = 12.5
    return population

def visitors():
    '''
    Create a dict, country_counts, whose keys are country names, and whose 
    values are the number of times the country occurs in the countries list. 
    '''
    country_counts = {}
    for country in country_list:
    #todo: insert countries into the country_count dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1
    return country_counts
    
def prolific_year():
    Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}
    
    years = {}

    for album_title in Beatles_Discography:
        print("title: {}, year: {}".format(album_title, 
                                           Beatles_Discography[album_title]))
        if Beatles_Discography[album_title] in years:
            years[Beatles_Discography[album_title]] += 1
        else:
            
            print(years.get(Beatles_Discography[album_title],
                             '--'))
            years[Beatles_Discography[album_title]] = 1 
        
    prolific = sorted(years.items(),
                       key = lambda pair: pair[-1],
                       reverse = True)
    max_years =[]
    max = 0
    print("Year\tAlbums produced")
    for year, albums in prolific:
        print("{}\t{}".format(year, albums))
        if albums > max:
            max = albums
            if year not in max_years:
                max_years.append(year)
    return max_years
            
    
# For this quiz, write a function total_takings that calculates the sum of 
# takings from every circus in the year. Here's a sample input for this function:

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

def total_takings(d):
    takings = 0
    for key in d.keys():
        takings += sum(d[key])
    return takings

if __name__ == '__main__':
    print(cities_population())
    print(visitors())
    print(prolific_year())
    print(total_takings(monthly_takings))