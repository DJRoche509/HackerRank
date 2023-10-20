'''
Use the HTTP GET method to retrieve information from a database of food outlets. Query https://jsonmock.hackerrank.com/api/food_outlets?city=<city> 
to find all the records for a city. The query result is paginated. To access additional pages, append &page={num} to the URL where num is the page number.

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

Given the city name as city and minimum vote count as votes, filter the result by city name. Find the outlet with the highest rating and whose vote count 
is greater than or equal to the required minimum votes. In case, of a tie in the rating, return the one with the maximum vote count.
'''


import requests

def finestFoodOutlet(city, votes):
    url = f"https://jsonmock.hackerrank.com/api/food_outlets?city={city}"
    response = requests.get(url)
    data = response.json()

    total_pages = data["total_pages"]
    outlets = []

    for page in range(1, total_pages + 1):
        url = f"https://jsonmock.hackerrank.com/api/food_outlets?city={city}&page={page}"
        response = requests.get(url)
        data = response.json()

        for outlet in data["data"]:
            if outlet["user_rating"]["votes"] >= votes:
                outlets.append(outlet)

    if not outlets:
        return 'No matching Outlet Found'

    finest_outlet = max(outlets, key=lambda o: (o["user_rating"]["average_rating"], o["user_rating"]["votes"]))['name']
    return finest_outlet

# Example usage
city = "Seattle"
minimum_votes = 100
result = finestFoodOutlet(city, minimum_votes)
print(result)
# Expected: "Cafe Juanita"