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




#----------------------defining constants---------------------------

#names of all countries that exist in the game, list is a constant
COUNTRIES = [
    #Emperor
    "Austria", #0
    
    #Electors
    "Bohemia", #1
    "Brandenburg", #2
    "Thuringia", #3
    "Colonge", #4
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
    "Munster", #17
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
        
        #ducats is 50 + two months of income with some random variance
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
    print("\n")
    #loops decisions until the player is done choosing what to do
    options_selected = False
    while not options_selected:
        display_stats()
        delete = input()
    

#display stats of the player country
def display_stats():
    display_army_info()
    display_economic_info()
    display_province_info()
 

#display army information
def display_army_info():
    print("Army Information:")
    total_armies = country_data[player_country_id][2]
    #finds out how many armies have already moved
    moved_armies = find_stationed_armies_count(player_country_id)
    #and then how many haven't
    idle_armies = total_armies - moved_armies
    
    #mentions how many armies the player has left to move
    print(COUNTRIES[player_country_id] + " has " + str(total_armies) + " armies.")
    #mentions where moved armies have gone to, if they have any already
    if moved_armies > 0:
        #gets all of the moved armies' locations
        moved_armies_locations = find_stationed_armies(player_country_id)
        
        #changes the text depending on how many of these armies have moved so far
        if moved_armies == total_armies:
            print("You have moved all of your armies, and they are stationed in these provinces:")
        else:
            print("You have moved some of your armies, and they are stationed in these provinces:")
        
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
    print("")


#display economic information
def display_economic_info():
    print("Economic information:")
    #finds player's ducat and loan count
    ducats = country_data[player_country_id][1]
    loans = country_data[player_country_id][3]
    
    province_count = find_province_count(player_country_id)
    
    #calculates player's income
    income = 1 + (province_count * 1.5)
    
    print(COUNTRIES[player_country_id] + " has " + str(ducats) + " ducats.")
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
    
    print(COUNTRIES[player_country_id] + " has " + str(len(owned_provinces)) + " provinces.")
    if len(owned_provinces) > 1:
        print("The provinces " + COUNTRIES[player_country_id] + " owns are:")
    else:
        print("The province " + COUNTRIES[player_country_id] + " owns is:")
    
    for p in owned_provinces:
        print(PROVINCE_ADJ[p][0])


#----------------------testing functions-------------------------

#makes sure all lists are set up correctly
def test_lists():
    print(province_owners)
    print("")
    print(country_data)


#---------------------------game body-----------------------------

reset_game()

handle_turn()











