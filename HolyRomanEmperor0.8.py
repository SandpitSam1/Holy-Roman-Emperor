import random

#Holy Roman Emperor, the game where you unify germany as any nation within the HRE!
#this is a turn based game where you decide how to use your troops and money to conquer germany
#before you get conquered by your neighbours


#different actions to do in a turn:

#attack an enemy province
#defend one of your provinces
#you can assign amounts of soldiers to these roles
#buy more troops

#and after all actions of a turn have been completed things update:
#gain ducats from taxes and lose ducats from paying your army
#manpower is gained from levies and lost from reinforcing your armies
#the emperor takes levies as tribute from all duchies
#ownership of contested provinces is fought over


#misc thoughts
#give electorates a slight boost in either manpower (gives less to Austria???)
#give Hanseatic League a slight boost to income (make them one of the easy countries)




#----------------------defining constants---------------------------

#names of all countries that exist in the game, list is a constant
COUNTRIES = [
    #Emperor
    "Austria", #0
    
    #Electors
    "Bohemia", #1
    "Brandenburg", #2
    "Thuringia", #3
    "Cologne", #4
    "Palatinate", #5
    "Trier", #6
    "Mainz", #7
    
    #Duchies
    "Bavaria", #8
    "Switzerland", #9
    "Pomerania", #10
    "Hanseatic League", #11
    "Brunswick", #12
    "Ansbach", #13
    "Cleves", #14
    "Saxony", #15
    "Lorraine", #16
    "Münster", #17
    "Mecklenburg", #18
    "Wurttemberg", #19
    "Wurzburg", #20
    "Hesse", #21
    "Utrecht", #22
    "Friesland", #23
    "Liege", #24
    "Luneburg", #25
    "Verden", #26
    "Magdeburg", #27
    "Baden", #28
    "Augsburg", #29
    "Bregenz", #30
    "Straßbourg", #31
]

#province names and adjacencies, constant
PROVINCE_ADJ = [
    #Low Countries
    ["Holland", [2, 3, 4]], #0
    ["Friesland", [0, 2, 8, 21]], #1
    ["Utrecht", [0, 1, 3, 21, 25]], #2
    ["Breda", [0, 2, 25, 26, 6, 4]], #3
    ["Antwerpen", [0, 3, 6, 5]], #4
    ["Hainaut", [4, 6]], #5
    ["Liege", [5, 4, 3, 26, 7]], #6
    ["Luxemberg", [6, 26, 28, 32]], #7
    #Northern Germany
    ["Bremen", [1, 21, 22, 9]], #8
    ["Verden", [8, 22, 16, 10]], #9
    ["Holstein", [9, 16, 11]], #10
    ["Lübeck", [10, 16, 12]], #11
    ["Mecklenburg", [11, 16, 20, 19, 18, 13]], #12
    ["Vorpommern", [12, 18, 14, 15]], #13
    ["Stettin", [13, 18, 17, 15]], #14
    ["Hinterpommern", [13, 14, 17]], #15
    ["Luneburg", [10, 11, 12, 20, 23, 22, 9]], #16
    ["Neumark", [15, 14, 18, 64, 67]], #17
    ["Berlin", [64, 19, 12, 13, 14, 17]], #18
    ["Mittelmark", [64, 54, 61, 20, 12, 18]], #19
    ["Altmark", [12, 19, 54, 23, 16]], #20
    #West Germany
    ["Münster", [1, 2, 25, 24, 22, 8]], #21
    ["Hanover", [8, 9, 16, 23, 24, 21]], #22
    ["Brunswick", [22, 16, 20, 54, 55, 29, 24]], #23
    ["Westphalia", [21, 22, 23, 29, 25]], #24
    ["Cleve", [2, 3, 26, 27, 29, 24, 21]], #25
    ["Aachen", [7, 6, 3, 25, 27, 28]], #26
    ["Cologne", [26, 25, 28]], #27
    ["Trier", [7, 26, 27, 25, 29, 30, 31, 32]], #28
    ["Hesse", [28, 25, 24, 23, 55, 56, 30]], #29
    ["Mainz", [28, 29, 56, 31, 57]], #30
    ["Palatinate", [32, 28, 30, 57, 33, 40, 41]], #31
    #South Germany + Austria + Switzerland
    ["Lorraine", [7, 28, 31, 33, 34, 39]], #32
    ["Alsace", [32, 31, 40, 39]], #33
    ["Burgundy", [32, 35, 36, 39]], #34
    ["Geneva", [34, 36, 37]], #35
    ["Bern", [35, 34, 39, 37]], #36
    ["Zürich", [35, 36, 39, 41, 42, 38]], #37
    ["Chur", [37, 42, 48]], #38
    ["Sundgau", [32, 34, 33, 40, 41, 37, 36]], #39
    ["Baden", [31, 39, 33, 41]], #40
    ["Wurttemberg", [39, 40, 31, 57, 37, 42, 43, 44]], #41
    ["Bregenz", [38, 37, 41, 43, 48]], #42
    ["Augsburg", [42, 41, 44, 46, 48]], #43
    ["Ingolstadt", [41, 42, 46, 45, 59, 58, 57]], #44
    ["Landshut", [47, 46, 44, 59, 63, 69, 53]], #45
    ["Munich", [43, 44, 45, 47, 48, 49]], #46
    ["Salzburg", [46, 49, 50, 53, 45]], #47
    ["Tirol", [38, 42, 43, 46, 49]], #48
    ["Oberkarten", [48, 46, 47, 50, 51]], #49
    ["Graz", [51, 49, 47, 53, 52]], #50
    ["Slovenia", [49, 50]], #51
    ["Vienna", [50, 53]], #52
    ["Manhartsberg", [50, 52, 47, 45, 69, 65]], #53
    #East Germany + Bohemia
    ["Magdeburg", [23, 20, 19, 61, 62, 55]], #54
    ["Erfurt", [23, 54, 62, 60, 58, 56, 29]], #55
    ["Wurzburg", [55, 57, 58, 29, 30]], #56
    ["Ansbach", [30, 31, 41, 44, 58, 56]], #57
    ["Nürnburg", [55, 60, 56, 57, 44, 45, 63]], #58
    ["Oberpfalz", [58, 44, 45, 63]], #59
    ["Weimar", [55, 62, 63, 59, 58]], #60
    ["Mittenburg", [62, 54, 19, 64]], #61
    ["Saxony", [55, 60, 54, 61, 64, 63]], #62
    ["Erzgebirge", [45, 59, 58, 60, 62, 64, 66, 69]], #63
    ["Lusatia", [63, 66, 67, 17, 18, 19, 61, 62]], #64
    ["Moravia", [53, 69, 66, 67, 68]], #65
    ["Prague", [69, 63, 64, 67, 65]], #66
    ["Glogow", [17, 64, 66, 65, 68]], #67
    ["Opole", [67, 65]], #68
    ["Budejovice", [63, 66, 65, 53, 45]], #69
]

#a list of months of the year
MONTH_NAMES = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


#----------------------defining variables---------------------------

#-1 means that it hasn't been selected yet
player_country_id = -1

#province owners
province_owners = []

#the provinces armies are in
#is a list of all provinces, and in the provinces is a list of countries, 
#with each country specifying its id and how many armies stationed there
army_locations = []

#list of all countries and their data
#Data includes:
#manpower
#ducats
#army size
country_data = []

#indicates how many turns have passed, each turn is a month. Starts jan 1515
year = 1515
#0 = january, 11 = december
month = 0


#--------------------------functions----------------------------

#----------------------general functions------------------------

#stolen code for a useful ordinal creator
def make_ordinal(n):
    #makes sure n is an integer
    n = int(n)
    #checks if n's last two didgets are between 11 and 13, as they use th instead of anything fancier
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        #defines a list of ordinals for numbers 0-4
        suffix = ['th', 'st', 'nd', 'rd', 'th']
        #finds the first didget of n and turns anything above 4 into 4, then uses the chopped version of n
        #to find the correct item of the list needed
        #"how did I not think of this" ahh solution
        suffix = suffix[min(n % 10, 4)]
    #returns the string needed
    return str(n) + suffix


#returns the same value, but floating point imprecision is fixed to 2dp
def fix_float(float_num):
    return round(float_num, 2)


#--------------------functions to find data---------------------

#returns how many provinces country with id country_id has
def find_province_count(country_id):
    province_count = 0
    #loops over every province in the list
    for p in province_owners:
        #checks if the country owns the province
        if country_owns_province(p, country_id):
            province_count += 1
    
    return province_count
  

#returns the country(id) with the most territory in a province and how much territory they have in it
def country_province_owner(province):
    #id of the country with the most territory
    country_with_most = -1
    #the amount of territory the country with the most has
    most_country_territory = 0
    
    #checks every country with territory there if they have the most in there
    for c in province:
        if c[1] > most_country_territory:
            country_with_most = c[0]
            most_country_territory = c[1]
    
    return [country_with_most, most_country_territory]


#returns true if country_id has the most territory in the province given, false otherwise
def country_owns_province(province, country_id):
    #finds which country is the owner of the province
    province_owner = country_province_owner(province)
    
    #checks if the country we are checking for is the owner
    if province_owner[0] == country_id:
        return True
    else:
        return False


#returns the owner of a given province(id)
def find_province_owner(province_id):
    #gets the owner of the province
    province = province_owners[province_id]
    province_owner = country_province_owner(province)
    #returns the country id
    return province_owner[0]


#returns a list of country ids and their corresponding province ids from a list of province ids 
#(assigns the owners to a list of provinces)
#the order is country(id), province(id)
def find_province_owners(province_ids):
    provinces_and_owners = []
    #loops over each province
    for p in province_ids:
        owner = find_province_owner(p)
        provinces_and_owners.append([owner, p])
    
    return provinces_and_owners


#returns a list of province ids owned by country_id
def find_owned_provinces(country_id):
    provinces_owned = []
    province_id = 0
    
    #loops over every province
    for p in province_owners:
        #adds province id to the list if the country owns it
        if country_owns_province(p, country_id):
            provinces_owned.append(province_id)
        
        #updates the province id
        province_id += 1
    
    return provinces_owned


#returns a list of province ids owned by country_id, from a given list of province ids and owners
def find_owned_provinces_from_set(country_id, country_and_prov_ids):
    owned_provinces = []
    
    #goes over each province
    for p in country_and_prov_ids:
        #if the country owns the province, the province id is put in a list
        if p[0] == country_id:
            owned_provinces.append(p[1])
    
    return owned_provinces


#returns a list of province ids bordering country_id's provinces
def find_bordering_provinces(country_id):
    country = find_owned_provinces(country_id)
    bordering_provinces = []
    
    #loops over every province in the country
    for p in country:
        #loops over every adjacent province to the province in the country
        for a in PROVINCE_ADJ[p][1]:
            #if it is not already in the list or it is in the country already, it's added
            if not a in bordering_provinces and not a in country:
                bordering_provinces.append(a)
    
    return bordering_provinces


#returns a list of country ids that own at least one province adjacent to country_id's provinces
def find_bordering_countries(country_id):
    bordering_provinces = find_bordering_provinces(country_id)
    bordering_countries = []
    
    #loops over every bordering province
    for p in bordering_provinces:
        #finds the owner of the province
        owner = find_province_owner(p)
        #if they aren't in the list already, they are added
        if not owner in bordering_countries:
            bordering_countries.append(owner)
    
    return bordering_countries


#returns a list of provinces that the given country has armies stationed in
def find_stationed_armies(country_id):
    provinces = []
    province_id = 0
    #loops over every province in army_locations
    for p in army_locations:
        #loops over every country with armies stationed/moving there
        for c in p:
            #checks if the country is the one we are checking for
            if c[0] == country_id:
                #adds the province id and the soldier count to the list of provinces with armies
                provinces.append([province_id, c[1]])
        
        #increases the province_id counter
        province_id += 1
            
    return provinces


#returns the number of armies that the given country has stationed
def find_stationed_armies_count(country_id):
    #finds all the provinces where the country has armies stationed
    provinces_with_armies = find_stationed_armies(country_id)
    stationed_armies = 0
    #loops over each one and adds up all the armies
    for p in provinces_with_armies:
        stationed_armies += p[1]
    
    return stationed_armies


#--------------------value setup functions----------------------

#sets province_owners to the starting values:
def reset_province_owners_list():
    global province_owners
    province_owners = [
        [[0, 1000]], #province 0 (Holland), owner austria 100.0%
        [[23, 1000]],
        [[22, 1000]],
        [[0, 1000]],
        [[0, 1000]],
        [[0, 1000]],
        [[24, 1000]],
        [[0, 1000]],
        
        [[11, 1000]],
        [[26, 1000]],
        [[11, 1000]],
        [[11, 1000]],
        [[18, 1000]],
        [[10, 1000]],
        [[10, 1000]],
        [[10, 1000]],
        [[25, 1000]],
        [[2, 1000]],
        [[2, 1000]],
        [[2, 1000]],
        [[2, 1000]],
        
        [[17, 1000]],
        [[12, 1000]],
        [[12, 1000]],
        [[4, 1000]],
        [[14, 1000]],
        [[14, 1000]],
        [[4, 1000]],
        [[6, 1000]],
        [[21, 1000]],
        [[7, 1000]],
        [[5, 1000]],
        
        [[16, 1000]],
        [[31, 1000]],
        [[0, 1000]],
        [[9, 1000]],
        [[9, 1000]],
        [[9, 1000]],
        [[9, 1000]],
        [[0, 1000]],
        [[28, 1000]],
        [[19, 1000]],
        [[30, 1000]],
        [[29, 1000]],
        [[8, 1000]],
        [[8, 1000]],
        [[8, 1000]],
        [[8, 1000]],
        [[0, 1000]],
        [[0, 1000]],
        [[0, 1000]],
        [[0, 1000]],
        [[0, 1000]],
        [[0, 1000]],
        
        [[27, 1000]],
        [[3, 1000]],
        [[20, 1000]],
        [[13, 1000]],
        [[13, 1000]],
        [[5, 1000]],
        [[3, 1000]],
        [[3, 1000]],
        [[15, 1000]],
        [[1, 1000]],
        [[1, 1000]],
        [[1, 1000]],
        [[1, 1000]],
        [[1, 1000]],
        [[1, 1000]],
        [[1, 1000]],
    ]
    

#sets country_data to the starting values:
def reset_country_data_list():
    #resets country_data
    global country_data
    country_data = []
    #loops over each country
    for c in range(0, len(COUNTRIES)):
        #makes an empty list for the data
        data = []
        #adds starting manpower, ducats and army, in that order
        
        #manpower is 10k at the start, with some random variance for flavour
        data.append(10000 + random.randrange(-1000, 1000))
        
        #ducats is 50 + two months of income (no expenses) with some random variance
        data.append(50 + (1 + (find_province_count(c) * ((15 + random.randrange(-3, 3)) / 10))))
        
        #starting army is roughly 5/7ths of the force limit
        data.append(round(5/7 * round(6 + (find_province_count(c) * 1.5))))
        
        #countries start with no loans
        data.append(0)
        
        country_data.append(data)


#resets army_locations with empty lists for each province
def reset_army_locations_list():
    global army_locations
    army_locations = []
    for p in PROVINCE_ADJ:
        army_locations.append([])


#sets up a new game by reseting all variables
def reset_game():
    global player_country_id
    global year
    global month
    
    reset_province_owners_list()
    reset_country_data_list()
    
    year = 1515
    month = 0
    
    #flavour text that also describes your options
    print("There are a lot of options for countries to play as, and each country has a certain level of difficulty.")
    print("For example, Austria is the Emperor of the Holy Roman Empire, so they are the most powerful, with widespread influence from Burgundy to Slovenia.")
    print("There are also other powerful states such as the Electorates of the Kingdom of Bohemia and Brandenburg, and the powerful Duchies of Bavaria and Switzerland, who are also strong picks.")
    print("If you want a bit more of a challenging game, you may also choose to play as the Electorate of Thuringia, or the Duchies of Pomerania or the Hanseatic League.")
    print("If you would like a very challenging start, you could try the Electorates of Cologne or The Palatinate, or the Duchies of Brunswick, Ansbach, or Cleves.")
    print("Any other country is an incredibly difficult start, so they are not recommended for anyone other than the most experienced of players.")
    
    print("For a new player, it is recommened to play either Austria or Bohemia.")
    print("Austria is the Emperor and the most powerful by far, but their territories are very spread out and may be difficult to defend, or be overwhelming to manage.")
    print("The Kingdom Bohemia is far less powerful than Austria, but they are still much more powerful than any of the other countries as they are a Kingdom, and their territories are more connected than Austria's")
    
    if input("Would you like to see all the possible countries? (y/n)").lower() == "y":
        for i in COUNTRIES:
            print(i)
    
    #quick note to set things straight for ingame balance reasons; here are the true rankings with no fluff:
    #very easy = Austria
    #easy = bohemia, Brandenburg, Bavaria, Switzerland, maybe Hanseatic if they get the money buff, maybe Thuringia if the Electorates get a buff
    #moderate = Thuringia, Pomerania, Hanseatic League (if the others go up a tier then this tier merges with the next tier down)
    #hard = Cologne, Palatinate, Brunswick, Ansbach, Cleves
    #very hard = everyone else
    #impossible = anything that sticks out as a significantly harder start after testing, with liege, saxony, and maybe Wurttemberg, Bregenz and Augsburg on watchlists
    
    
    
    player_country_id = -1
    #ask the player which country they would like to play as
    response = input("Enter the name of the country you want to play as: ").capitalize()
    while True:
        #if it is not a valid country then it tries again
        if response in COUNTRIES:
            player_country_id = COUNTRIES.index(response)
            break
        
        response = input("Invalid country, enter the name of a valid country: ").capitalize()
    
    print("")
    


#------------------------game functions--------------------------

#executes a turn
def handle_turn():
    #handle player inputs
    handle_player_input()
    #calculate ai decisions
    
    #calculate what happens
    
    pass


#handles the player inputs in a turn
def handle_player_input():
    #states which turn it is
    print("It is " + MONTH_NAMES[month] + " " + str(year) + ", and your country, " + COUNTRIES[player_country_id] + ", has many decisions to make.")
    print("")
    display_general_info()
    #loops decisions until the player is done choosing what to do
    all_options_selected = False
    while not all_options_selected:
        #gets the player's decision
        decision = get_player_option_select()
        #acts upon it
        if decision == 1:
            display_stats()
        elif decision == 2:
            move_armies_menu()
        elif decision == 3:
            pass


#the ui for moving armies
def move_armies_menu():
    pass


#asks the player to enter a number to show what they want to do, returns their response
def get_player_option_select():
    #ask player what they want to do
        print("Enter a 1 if you want to see more information about your nation")
        print("Enter a 2 if you want to move armies")
        print("Enter a 3 if you want to train new armies")
        decision = int(input())
        print("")
        return decision


#display stats of the player country
def display_stats():
    display_army_info(False)
    display_bordering_country_info()
    display_economic_info()
    display_province_info()
    display_leaderboard_info()


#shows the top 5 powers in the HRE
def display_leaderboard_info():
    print("Top Countries by Provinces:")
    
    #makes a list of every country and how many provinces they have
    countries_prov_count = []
    for c in range(0, len(COUNTRIES)):
        countries_prov_count.append([c, find_province_count(c)])
    
    #gets the sorted list of countries by province count, with first at the top and last at the bottom.
    #ties broken by the country_id, putting the emperor and electors above duchies, and then ordering by starting territories, then vibes.
    #it orders first by the negative value of provinces, and the ascending order becomes descending this way
    power_rankings = sorted(countries_prov_count, key = lambda x : (-x[1], x[0]))
    
    #makes a top 5 by cutting off all but the first 5 values
    top_5_countries = power_rankings[:5]
    
    place = 1
    for c in top_5_countries:
        print(make_ordinal(place) + " place: " + COUNTRIES[c[0]] + ", with " + str(c[1]) + " provinces.")
        place += 1
    
    #finds out what ranking the player got
    player_ranking = power_rankings.index([player_country_id, find_province_count(player_country_id)])
    
    #if they aren't on the leaderboard (skill issue icl), then they get mentioned at the bottom
    if player_ranking > 4:
        if power_rankings[player_ranking][1] == 1:
            print("Your country, " + COUNTRIES[player_country_id] + ", got " + make_ordinal(player_ranking + 1) + ", with " + str(power_rankings[player_ranking][1]) + " province.")
        else:
            print("Your country, " + COUNTRIES[player_country_id] + ", got " + make_ordinal(player_ranking + 1) + ", with " + str(power_rankings[player_ranking][1]) + " provinces.")
    
    print("")


#self explanatory
def display_bordering_country_info():
    print("Neighboring Country Information:")
    
    neighbours = find_bordering_countries(player_country_id)
    #gets the provinces bordering the country and also who owns each of them
    neighbour_provinces = find_province_owners(find_bordering_provinces(player_country_id))
    
    print(COUNTRIES[player_country_id] + " has " + str(len(neighbours)) + " neighbouring countries. They are:")
    
    #goes over each country and gives info on them
    for c in neighbours:
        message = ""
        provinces = find_province_count(c)
        message += COUNTRIES[c] + ", who has " + str(provinces)
        
        #handling plurality
        if provinces == 1:
            message += " province, "
        else:
            message += " provinces, "
        
        #find the provinces that they own that border the player country
        owned_provinces = find_owned_provinces_from_set(c, neighbour_provinces)
        
        #handling plurality
        if len(owned_provinces) == 1:
            message += "and it borders "
        elif len(owned_provinces) == provinces:
            message += "all of which border "
        else:
            message += str(len(owned_provinces)) + " of which border "
        
        message += COUNTRIES[player_country_id] + ": "
        
        
        #loops over each province to name it individually
        index = 0
        for p in owned_provinces:
            #names it
            message += PROVINCE_ADJ[p][0]
            
            #makes the listed names grammatical
            if index + 2 == len(owned_provinces):
                if len(owned_provinces) == 2:
                    message += " and "
                else:
                    message += ", and "
            elif index + 1 == len(owned_provinces):
                message += "."
            else:
                message += ", "
            
            index += 1
        
        #finally prints the message about the country
        print(message)
    
    print("")


#display army information, input is for whether only army info should be shown or all of it
def display_army_info(just_armies):
    print("Army Information:")
    total_armies = country_data[player_country_id][2]
    #finds out how many armies have already moved
    moved_armies = find_stationed_armies_count(player_country_id)
    #and then how many haven't
    idle_armies = total_armies - moved_armies
    
    #mentions how many armies the player has
    if total_armies == 1:
        print(COUNTRIES[player_country_id] + " has " + str(total_armies) + " army.")
    else:
        print(COUNTRIES[player_country_id] + " has " + str(total_armies) + " armies.")
    
    #mentions where moved armies have gone to, if they have any already
    if moved_armies > 0:
        #gets all of the moved armies' locations
        moved_armies_locations = find_stationed_armies(player_country_id)
        
        #changes the text depending on how many of these armies have moved so far
        if moved_armies == total_armies:
            print(COUNTRIES[player_country_id] + " have moved all of your armies, and they are moving to these provinces:")
        else:
            print(COUNTRIES[player_country_id] + " have moved some of your armies, and they are moving to these provinces:")
        
        #loops over each province to describe where they have gone
        for p in moved_armies_locations:
            message = str(p[1])
            #checks how many armies are in the province to see if it is plural
            if p[1] > 1:
                message += " armies are "
            else:
                message += " army is "
            
            #checks if the country owns the province the army is stationed in
            if country_owns_province(province_owners[p[0]]):
                #if so then say that the army(s) is guarding the province
                message += "defending "
            else:
                #otherwise they are attacking
                message += "attacking "
            
            #adds on the name of the province
            message += PROVINCE_ADJ[p[0]][0] + "."
            
            #finally prints the built message
            print(message)
                
            
    else:
        print("None of these armies have moved yet.")
    
    #checks if only army info should be shown
    if just_armies:
        print("")
        return
    
    #manpower
    manpower = country_data[player_country_id][0]
    
    #calculates max manpower
    province_count = find_province_count(player_country_id)
    max_manpower = 10000 + (1500 * province_count)
    #accounts for the emperor taking some levies
    if player_country_id == 0:
        max_manpower += (len(COUNTRIES) - 1) * 500
    else:
        max_manpower -= 500
    
    #values taken straight from the wiki
    manpower_recovery = max(round(max_manpower / 120), 100)
    
    print(COUNTRIES[player_country_id] + " has " + str(manpower) + " manpower.")
    print(COUNTRIES[player_country_id] + " cannot have more than " + str(max_manpower) + " manpower in reserves.")
    print(COUNTRIES[player_country_id] + " recovers " + str(manpower_recovery) + " manpower in a month.")
    
    
    
    print("")


#display economic information
def display_economic_info():
    print("Economic information:")
    #finds player's ducat and loan count
    ducats = country_data[player_country_id][1]
    loans = country_data[player_country_id][3]
    
    total_armies = country_data[player_country_id][2]
    province_count = find_province_count(player_country_id)
    
    #calculates player's income, expenses and balance
    income = 1 + (province_count * 1.5)
    
    expenses = (total_armies * 0.22) + (province_count * 0.5) #province maintainance is high to account for forts
    expenses = fix_float(expenses)
    
    balance = income - expenses
    balance = fix_float(balance)
    
    print(COUNTRIES[player_country_id] + " has " + str(ducats) + " ducats.")
    print(COUNTRIES[player_country_id] + " has an income of " + str(income) + " ducats per month from province taxes.")
    print(COUNTRIES[player_country_id] + " spends " + str(expenses) + " ducats per month on maintaining their armies and provinces.")
    print(COUNTRIES[player_country_id] + " has a total balance of " + str(balance) + " ducats per month.")
    
    #checks if you have no loans, and changes the statment accordingly
    if loans < 1:
        print(COUNTRIES[player_country_id] + " has no loans.")
    else:
        print(COUNTRIES[player_country_id] + " has " + str(loans) + " loans.")
        
        #tells you how much you need to pay to pay them off
        loan_size = round(province_count * 7.5)
        debt = loan_size * loans
        months_to_repay = round(debt / income)
        print("You need to pay " + str(loan_size) + " ducats per loan, and with a total debt of " + str(debt) + " you would need " + str(months_to_repay) + " months of income to repay it all.")
        
        #bankrupcy warning
        if loans > 3:
            print("You are approaching the loan limit of 5, if you exceed this limit you will go bankrupt and lose.")
    
    print("")


#display province information
def display_province_info():
    print("Province information:")
    #get all owned provinces
    owned_provinces = find_owned_provinces(player_country_id)
    
    #I hate plurals
    if len(owned_provinces) > 1:
        print(COUNTRIES[player_country_id] + " has " + str(len(owned_provinces)) + " provinces.")
        print("The provinces " + COUNTRIES[player_country_id] + " owns are:")
    else:
        print(COUNTRIES[player_country_id] + " has " + str(len(owned_provinces)) + " province.")
        print("The province " + COUNTRIES[player_country_id] + " owns is:")
    
    for p in owned_provinces:
        print(PROVINCE_ADJ[p][0])
    
    print("")


#display general information, e.g. non specifics but just an overview
def display_general_info():
    print("Overview of " + COUNTRIES[player_country_id] + "'s situation:")
    
    #calculate variables
    total_armies = country_data[player_country_id][2]
    
    ducats = country_data[player_country_id][1]
    
    province_count = find_province_count(player_country_id)
    
    manpower = country_data[player_country_id][0]
    
    income = 1 + (province_count * 1.5)
    expenses = (total_armies * 0.22) + (province_count * 0.5) #province maintainance is high to account for forts
    expenses = fix_float(expenses)
    balance = income - expenses
    balance = fix_float(balance)
    
    #plurality
    if province_count == 1:
        print(COUNTRIES[player_country_id] + " has " + str(province_count) + " province.")
    else:
        print(COUNTRIES[player_country_id] + " has " + str(province_count) + " provinces.")
    
    print(COUNTRIES[player_country_id] + " has " + str(ducats) + " ducats.")
    print(COUNTRIES[player_country_id] + " has a total balance of " + str(balance) + " ducats per month.")
    #plurality
    if total_armies == 1:
        print(COUNTRIES[player_country_id] + " has " + str(total_armies) + " army.")
    else:
        print(COUNTRIES[player_country_id] + " has " + str(total_armies) + " armies.")
    print(COUNTRIES[player_country_id] + " has " + str(manpower) + " manpower.")
    print("")


#----------------------testing functions-------------------------

#makes sure all lists are set up correctly
def test_lists():
    print(province_owners)
    print("")
    print(country_data)


#---------------------------game body-----------------------------

#intro text
print("Welcome to Holy Roman Emperor, the game where you have to try and unite Germany!")
print("This is a game of strategy and conquest, where you start as a nation within the Holy Roman Empire in the year 1515, and you try and lead your nation to glory.")
print("Speaking of nations, you should probably pick a country to start as.")

reset_game()

handle_turn()











