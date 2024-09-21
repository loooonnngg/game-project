import mysql.connector
from geopy import distance
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'sql_password',
    database = 'flight_game',
    collation = 'utf8mb4_general_ci',
    autocommit = True
    ) #connection with database
def player_name(): #get player name
    name = input("What is your name? ")
    return name
def get_airport_information(): #fetching airport information from database, used in other functions
    cursor = connection.cursor()
    sql = (f"SELECT airport.ident, airport.NAME, airport.type, airport.latitude_deg, airport.longitude_deg, airport.iso_country, country.name,airport.continent "
           f"FROM country, airport "
           f"WHERE airport.iso_country = country.iso_country "
           f"and TYPE = 'medium_airport' OR TYPE = 'large_airport' "
           f"ORDER BY RAND() LIMIT 1;")
    cursor.execute(sql)
    output = cursor.fetchall()
    airport_information = output[0][0], output[0][1], output[0][2], output[0][3], output[0][4], output[0][5], output[0][6], output[0][7]
    return airport_information
def get_airport_distance(location1, location2): #getting distance between two point, with latitude and longitude as location1, and location 2
    first_airport = location1
    second_airport = location2
    return distance.distance(first_airport, second_airport).kilometers
def airport_list(airport_amount): #taking airport information and putting it in a dictionary, use get_airport_information()
    airport_dict = {}
    for i in range(airport_amount):
        airport_dict[i+1] = get_airport_information()
    return airport_dict
def choose_difficulty(): #taking difficulty and turn it into number
    print("Higher difficulty will give you less money to work with, but give more points at the end.")
    print("What difficulty would you like to choose? ")
    print("1: Easy")
    print("2: Medium")
    print("3: Hard")
    difficulty = input()
    return difficulty
def points_calculation(co2_used,fuel_consumed,money_left_over,difficulty): #points calculation
    points = int(10000/(((co2_used*0.25 + fuel_consumed*0.25 + money_left_over)*(1+difficulty/5))/2000))
    return points