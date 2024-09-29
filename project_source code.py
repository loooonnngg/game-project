from symbol import continue_stmt

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
def get_airport_information(): #fetching airport information from database, used in other functions
    airport_dict = {}
    cursor = connection.cursor()
    sql = (f"SELECT airport.ident, airport.NAME, airport.type, airport.latitude_deg, airport.longitude_deg, airport.iso_country, country.name,airport.continent "
           f"FROM country, airport "
           f"WHERE airport.iso_country = country.iso_country "
           f"having TYPE = 'medium_airport' OR TYPE = 'large_airport' "
           f"ORDER BY RAND() LIMIT 12;")
    cursor.execute(sql)
    output = cursor.fetchall()
    for i in range(12):
        airport_dict[i+1] = [output[i][0], output[i][1], output[i][2], output[i][3], output[i][4], output[i][5], output[i][6], output[i][7]]
    return airport_dict
def get_airport_distance(location1, location2): #getting distance between two point, with latitude and longitude as location1, and location 2
    first_airport = location1
    second_airport = location2
    return distance.distance(first_airport, second_airport).kilometers
def airport_list_continent_rename(airport_dict):
    list_airport=airport_dict
    for i in list_airport:
        if list_airport[i][7] == 'EU':
            list_airport[i][7]='Europe'
        elif list_airport[i][7] == 'NA':
            list_airport[i][7]='North America'
        elif list_airport[i][7] == 'SA':
            list_airport[i][7] ='South America'
        elif list_airport[i][7] == 'AF':
            list_airport[i][7] ='Africa'
        elif list_airport[i][7] == 'AN':
            list_airport[i][7] ='Antarctica'
        elif list_airport[i][7] == 'AS':
            list_airport[i][7] ='Asia'
        elif list_airport[i][7] == 'OC':
            list_airport[i][7] = 'Oceania/Australia'
        else:
            pass
    return list_airport
def points_calculation(co2_used,money_left_over,difficulty): #points calculation
    points = round((100000*difficulty/((co2_used + money_left_over*5)/2000)),2)
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
def choose_airport(airport_dict):
    while True:
        airport_input = int(input("choose the airport you want to go to using the number before each airports: "))
        if airport_input in airport_dict:
            new_position = airport_dict[airport_input]
            del airport_dict[airport_input]
            break
        else:
            print("Invalid input")
            continue
    return new_position
def flight_hint(current_location, airport_dict):
    compare_list = {}
    for i in airport_dict:
        start_airport = current_location[3], current_location[4]
        end_airport = airport_dict[i][3], airport_dict[i][4]
        distance = get_airport_distance(start_airport, end_airport)
        compare_list[i] = distance
    nearest_airport = min(compare_list, key=compare_list.get)
    return nearest_airport, airport_dict[nearest_airport]
def player_information():
    cursor = connection.cursor()
    player_fetch = (f"SELECT player.name,player.score,list_airport.airport_list "
           f"FROM player, list_airport "
           f"WHERE player.airport_seed=list_airport.list_seed ")
    cursor.execute(player_fetch)
    output = cursor.fetchall()
    if cursor.rowcount > 0:
        for i in range(cursor.rowcount):
            print(i+1,output[i])
    return output
#main program start here
player_position = ['EFHK', 'Helsinki Vantaa Airport', 'large_airport', 60.3172, 24.963301, 'FI', 'Finland', 'EU']
while True:
    print("What do you want to do:")
    print("1: Start a new game")
    print("2: View previous player")
    start_game_action = input("")
    if start_game_action == "1":
        airport_list = airport_list_continent_rename(get_airport_information())
        break
    elif start_game_action == "2":
        airport_dict = {}
        player_list = player_information()
        print("Do you want to start a game from previous player airport list??")
        print("1: yes")
        print("2: no ")
        action_confirm = input("")
        if action_confirm == "1":
            list_id = int(input("Which person's list do you want to use, select the number before the person: "))
            list_ident = player_list[list_id-1][2].split(",")
            cursor2 = connection.cursor()
            cursor2.execute(f"SELECT airport.ident, airport.NAME, airport.type, airport.latitude_deg, airport.longitude_deg, airport.iso_country, country.name,airport.continent "
                   f"FROM country, airport "
                   f"WHERE airport.iso_country = country.iso_country "
                   f"having airport.ident = '{list_ident[0]}' OR ident= '{list_ident[1]}' OR ident= '{list_ident[2]}' OR ident= '{list_ident[3]}' OR ident= '{list_ident[4]}' OR ident= '{list_ident[5]}' OR ident= '{list_ident[6]}' OR ident= '{list_ident[7]}' OR ident= '{list_ident[8]}' OR ident= '{list_ident[9]}' OR ident='{list_ident[10]}' OR ident= '{list_ident[11]}'"
                   f"order by airport.ident;")
            output2 = cursor2.fetchall()
            for i in range(12):
                airport_dict[i+1] = [output2[i][0], output2[i][1], output2[i][2], output2[i][3], output2[i][4], output2[i][5], output2[i][6], output2[i][7]]
            airport_list=airport_list_continent_rename(airport_dict)
            break
        elif action_confirm == "2":
            continue
print("")
print("You are a cancer patients who coincidentally met 2 other patient at the same hospital for their treatment. ")
print("Since all of you are in the process of curing your disease, everyone begin to have conversations with each "
      "other about their own situation and how they caught cancer. ")
print("After a brief conversation with each other, everyone realized that all three of them want to make the rest of "
      "their lives meaningful by travelling to places they always wanted to. ")
print("However, they are also aware that environmental pollution is the root cause of increasing cancer in people. ")
print("So, everyone produce an idea that they will try their best to limit their co2 consumption to the lowest while "
      "also travelling to as many places as possible within their budget.")
print("")
player_name=input("What name do you want to be saved as?: ")
print("Everyone have different budget, who do you want to play as?")
print("Higher difficulty will give you less money to work with, but give more points at the end.")
while True:
    print("What difficulty would you like to choose? ")
    print("1: Henderson(Easy)")
    print("2: Rosaline(Medium)")
    print("3: Josh(Hard)")
    difficulty_input=int(input())
    if difficulty_input==1:
        money_multiply=3
        break
    elif difficulty_input==2:
        money_multiply=2
        break
    elif difficulty_input==3:
        money_multiply=1
        break
    else:
        print("Invalid input")
player_money = 1000*money_multiply
player_fuel = 1000
player_co2 = 0
player_hint = 3
print("")
print("You will be starting from")
print(player_position[0],',', player_position[1],',',player_position[6],',',player_position[7])
print("")
print(f"You have {player_money}$ to spend, along with {player_fuel}L of fuel to use (An average plane uses 3.5L of fuel and emit 10kg of CO2 /100km per passenger)") #information taken from https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft and https://www.carbonindependent.org/22.html
print(f"Along with hints {player_hint} to know which airport is the closest to travel to")
print("You can use your money to buy more fuel for your travel. ")
print("Gain hints of which airport is the closest and is the most efficient to travel to.")
print("Or used to increase your score at the end")
airport_save = []
for airport in airport_list:
    airport_save.append(airport_list[airport][0])
airport_save.sort()
airport_save = ",".join(airport_save)
player_action = None
counter=0
while len(airport_list) > 0:
    if player_fuel < 0:
        print("Game over, You ran out of fuel")
        break
    print('List of airport left to visit are:')
    for i in airport_list:
        print(i,',', airport_list[i][0],',', airport_list[i][1],',', airport_list[i][6],',', airport_list[i][7])
    print(f"You have {round(player_money, 1)}$")
    print(round(player_fuel,1),"L of fuel")
    print(f"And {player_hint} hints")
    player_action = play_action()
    if player_action == "1":
        original_position = [player_position[3],player_position[4]]
        player_position = choose_airport(airport_list)
        new_position = [player_position[3],player_position[4]]
        distance_travelled = round(get_airport_distance(original_position,new_position),1)
        player_fuel-=round(distance_travelled*3.5/100, 1)
        player_co2+=round(distance_travelled/10, 1)
        print(f'You travelled {distance_travelled} km')
        print(f'You used {round(distance_travelled*3.5/100, 1)}L of fuel, and have {round(player_fuel,1)}L of fuel left.')
        print(f'While emitting {round(distance_travelled/10, 1)} kg of CO2, you have emitted a total of {round(player_co2,1)}Kg of CO2.')
        print('You are now at',player_position[0],',', player_position[1],',',player_position[6],',',player_position[7])
        print('')
    if player_action == "2":
        while True:
            print("What do you want to do with your money")
            print("1: buy more fuel(300L/500$)")
            print("2: buy more hints(1 hints/200$)")
            print("3: cancel")
            money_action = input(str())
            if money_action == "1":
                if player_money >= 500:
                    print("You have bought 300L of fuel for 500$")
                    player_fuel+=200
                    player_money-=500
                    break
                else:
                    print("You dont have enough money to buy this")
                    continue
            elif money_action == "2":
                if player_money >= 200:
                    print("You have bought another hint for 200$")
                    player_hint+=1
                    player_money-=200
                    break
                else:
                    print("You dont have enough money to buy this")
                    continue
            elif money_action == "3":
                break
            else:
                print("Invalid input")
    if player_action == "3":
        if player_hint > 0:
            player_hint-=1
            nearest_airport = flight_hint(player_position,airport_list)
            print(f"The nearest airport is {nearest_airport[0]} {nearest_airport[1][0]}, {nearest_airport[1][1]}, {nearest_airport[1][6]}, {nearest_airport[1][7]}")
            print("Do you want to travel to this airport")
            print("1: Yes")
            print("2: No")
            confirm_action = input()
            if confirm_action == "1":
                original_position = [player_position[3], player_position[4]]
                player_position = nearest_airport[1]
                new_position = [player_position[3], player_position[4]]
                distance_travelled = round(get_airport_distance(original_position, new_position), 1)
                player_fuel -= round(distance_travelled * 3.5 / 100, 1)
                player_co2 += round(distance_travelled / 10, 1)
                del airport_list[nearest_airport[0]]
                print(f'You travelled {distance_travelled} km')
                print(f'You used {round(distance_travelled * 3.5 / 100, 1)}L of fuel, and have {round(player_fuel,1)}L of fuel left.')
                print(f'While emitting {round(distance_travelled / 10, 1)} kg of CO2, you have emitted a total of {round(player_co2,1)}Kg of CO2.')
                print('You are now at', player_position[0], ',', player_position[1], ',', player_position[6], ',',player_position[7])
                print('')
            elif confirm_action == "2":
                continue
        else:
            print("You don't have any hints left")
            continue
    counter+=1
    if counter % 3 == 0:
        player_fuel+= 400
        print("You have gained a free 400L refuel for travelling to 3 new airports")
player_score = points_calculation(player_co2,player_money,difficulty_input)
print(f"You have finished your journey and have {player_score} points")
cursor = connection.cursor()
sql_save = (f"INSERT INTO list_airport (airport_list) VALUES ('{airport_save}');"
            f"INSERT INTO player (NAME,score,airport_seed) VALUES ('{player_name}',{player_score},LAST_INSERT_ID());")
cursor.execute(sql_save)