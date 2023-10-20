'''
TOTAL VOTES

A restaurant rating application collects ratings or votes from its users and stores them in a database. They want to allow users to retrieve 
the total vote count for restaurants in a city. Implement a function, getVoteCount. Given a city name and the estimated cost for the outlet, 
make a GET request to the API at https://jsonmock.hackerrank.com/api/food_outlets?city=<cityName>&estimated_cost=<estimatedCost> wheren and 
are the parameters passed to the function.


The response is a Json object with the following 5 fields:

1. page: The current pahe of the results.
2. per_page: The maximum number of results returned per page. (Number)
3. total: The total number results. (Number)
4. total_pages: The total number of pages with results. (Number)
5. data: Either an empty array or an array with a single object that contains the food outlets' records.


In data, each food outlet has the following schema:

1. id: outlet id (Number)
2. name: The name of the outlet (String)
3. city: The city in which the outlet is located (String)
4. estimated_cost: The estimated cost of the food in the particular outlet (Number).
5. user_rating: An object containing the user ratings for theoutlet (Number). The object has the following schema:
     a) average_ rating: The average user rating for the outlet (Number)
     b) votes: The number of people who voted for the oulet (Number)

     
If there are no matching records returned, the data array will be empty. In that cases, the getVoteCount function should return -1.

An example of a food outlet record is as follows:
{
    "id": 41,
    "city": "Seattle",
    "name": "Cafe Juanita",
    "estimated_cost": 160,
    "user_rating": { 
        "average_rating": 4.9,
        "votes": 16203
    }
}

Use the votes property of rach outlet to calculate the total vote count of all the matching outlets.


Function Description
Complete the getVoteCount function in the editor below.

getVoteCount has the following parameters:

    cityName: The city to query. (String)
    estimatedCost: The cost to query. (Integer)

    
Returns
Integer: the sum of votes for matching outlets or -1.

Constraints
No query will return more than 10 records.

Sample Cases
    1. Sample Case 0
        Input: "Seattle", 110
        Output: 2116
        Explanation: First a call is made to API https://jsonmock.hackerrank.com/api/food_outlets?city=Seattle&estimated_cost=110 tp fetch the only 
        matching outlet. The sum of votes is calculated and returned.

    2. Sample Case 1
        Input: "Delaware", 150
        Output: -1
        Explanation: An API call is made to https://jsonmock.hackerrank.com/api/food_outlets?city=Delaware&estimated_cost=150 tp fetch the only matching 
        outlet. The sum of votes is calculated and returned.
'''
import requests

def getVoteCount(cityName, estimatedCost):
    url = f"https://jsonmock.hackerrank.com/api/food_outlets?city={cityName}&estimated_cost={estimatedCost}"
    response = requests.get(url)
    data = response.json()
    
    if not data['data']:
        return -1

    outlets = data['data']
    
    totalVotes = sum( outlet['user_rating']['votes'] for outlet in outlets)

    return totalVotes



samples = [('Seattle', 110),('Delaware', 150) ,('Miami', 120),('Miami', 110),('Omaha', 60),('Dallas', 70),('Dallas', 100),('Denver', 200),('Houston', 350)]

for city, cost in samples:
    print(getVoteCount(city, cost))

# Expecting Values: 
# 2116
# -1
# 3682
# 1770
# 5078
# 1592
# -1
# -1
# 732