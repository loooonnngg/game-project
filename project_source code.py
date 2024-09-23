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
    airport_dict = {}
    cursor = connection.cursor()
    sql = (f"SELECT airport.ident, airport.NAME, airport.type, airport.latitude_deg, airport.longitude_deg, airport.iso_country, country.name,airport.continent "
           f"FROM country, airport "
           f"WHERE airport.iso_country = country.iso_country "
           f"having TYPE = 'medium_airport' OR TYPE = 'large_airport' "
           f"ORDER BY RAND() LIMIT 11;")
    cursor.execute(sql)
    output = cursor.fetchall()
    for i in range(11):
        airport_dict[i+1] = output[i][0], output[i][1], output[i][2], output[i][3], output[i][4], output[i][5], output[i][6], output[i][7]
    return airport_dict
def get_airport_distance(location1, location2): #getting distance between two point, with latitude and longitude as location1, and location 2
    first_airport = location1
    second_airport = location2
    return distance.distance(first_airport, second_airport).kilometers
def airport_list(airport_amount): #taking airport information and putting it in a dictionary, use get_airport_information()
    airport_dict = {}
    for i in range(airport_amount):
        airport_dict[i+1] = get_airport_information()
    return airport_dict
def points_calculation(co2_used,fuel_consumed,money_left_over,difficulty): #points calculation
    points = int(10000/(((co2_used*0.25 + fuel_consumed*0.25 + money_left_over)*(1+difficulty/5))/2000))
    return points
def play_action(): #take player action each turn
    print("What would you like to do? ")
    print("1: select airport to go to")
    print("2: use your money")
    print("3: use a hint")
    action_input=input(str())
    if action_input == "1" or action_input == "2" or action_input == "3":
        return action_input
    else:
        print("Invalid input")
        return play_action()
#main program start here
print("You are a cancer patients who coincidentally met 2 other patient at the same hospital for their treatment. ")
print("Since all of you are in the process of curing your disease, everyone begin to have conversations with each other about their own situation and how they caught cancer. ")
print("After a brief conversation with each other, everyone realized that all three of them want to make the rest of their lives meaningful by travelling to places they always wanted to. ")
print("However, they are also aware that environmental pollution is the root cause of increasing cancer in people. ")
print("So, everyone produce an idea that they will try their best to limit their co2 consumption to the lowest while also travelling to as many places as possible within their budget.")
print("")
print("Everyone have different budget, who do you want to play as?")
print("Higher difficulty will give you less money to work with, but give more points at the end.")
while True:
    print("What difficulty would you like to choose? ")
    print("1: Henderson(Easy)")
    print("2: Rosaline(Medium)")
    print("3: Josh(Hard)")
    difficulty_input=input(str())
    if difficulty_input=="1":
        money_multiply=3
        break
    elif difficulty_input=="2":
        money_multiply=2
        break
    elif difficulty_input=="3":
        money_multiply=1
        break
    else:
        print("Invalid input")
print("List of airport you need to travel to are:")
airport_list = get_airport_information()
for i in airport_list:
    print(airport_list[i])
player_money = 1000*money_multiply
print("")
print("You will be starting from")
print("('EFHK', 'Helsinki Vantaa Airport', 'large_airport', 60.3172, 24.963301, 'FI', 'Finland', 'EU')")
print("")
print(f"And you have {player_money}$ to spend, along with 3500L of fuel to use  (An average plane uses 3.5L of fuel and emit 10kg of CO2 /100km per passenger)") #information taken from https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft and https://www.carbonindependent.org/22.html
print("You can use your money to buy more fuel for your travel. ")
print("Gain hints of which airport is the closest and is the most efficient to travel to.")
print("Or used to increase your score at the end")
