#Abruptly Goblins Codecademy Project
#Things to add: 



#Empty list as holder
from itertools import count


gamers = []

#Function to add gamers into the list with their name and available days of the week
def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        if gamer["name"] in gamers:
            print("Gamer already exists in our database")
        else:
            gamers_list.append(gamer)
    else:
        print("Needs more information")
    return


#1st method input required to add a new memeber
kimberly = {
    "name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]
}
#Using the function to add said gamer
add_gamer(kimberly, gamers)
#gamers.clear()
#used to clear the 

#2nd Input method
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
i = 1
for gamer in gamers:
    print(str(i))
    print(gamer)
    i += 1

#Function that outputs number value for each day of the week
def build_daily_frequency_table():
    return {
        "Monday":    0,
        "Tuesday":   0,
        "Wednesday": 0,
        "Thursday":  0,
        "Friday":    0,
        "Saturday":  0,
        "Sunday":    0
    }
count_availability = build_daily_frequency_table()

#Iterates through all gamers and then their available days to add it to the day count
def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer["availability"]:
            available_frequency[day] += 1


#Takes gamer and weekdays list to add the amount onto the list and the prints it
calculate_availability(gamers, count_availability)
print(count_availability)


#Function to find the best available night
def find_best_night(available_table):
    best_availability = 0
    for day, availability in available_table.items():
        if availability > best_availability:
            best_day = day
            best_availability = availability
    return best_day


game_night = find_best_night(count_availability)
print(game_night)

#Text
def available_on_night(gamers_list, day):
    return [gamer for gamer in gamers_list if day in gamer["availability"]]

attending_game_night = available_on_night(gamers, game_night)
print(attending_game_night)



#Email Function and text
form_email = """
Dear {name},
We are happy to invite you to our special gaming night on {day_of_week}, where
we plan to play some {game}!

Yours kindly, 
the Sorcery Society
"""

def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name = gamer["name"], day_of_week = day, game = game))

send_email(attending_game_night, game_night, "Abruptly Goblins")


#A way to invide all the other people who couldn't attend on the most favorable day
unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer["availability"]]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)

available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins")

