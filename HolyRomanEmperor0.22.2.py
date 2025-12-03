import random

#Holy Roman Emperor, the game where you unify germany as any nation within the HRE!
#this is a turn based game where you decide how to use your troops and money to conquer germany
#before you get conquered by your neighbours

#TODO
#Get rid of some of the more brutal nesting atrocities
#add ai to non-player nations

#let the player disband armies even if they don't have enough money for armies
#tell the player how many idle armies they have when moving

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
    "Alsace", #31, Straßbourg had to be renamed as it is too hard to type
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
    ["Lubeck", [10, 16, 12]], #11
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
    ["Munster", [1, 2, 25, 24, 22, 8]], #21
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
    ["Zurich", [35, 36, 39, 41, 42, 38]], #37
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
    ["Nurnburg", [55, 60, 56, 57, 44, 45, 63]], #58
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

#amount of loans you can take before bankrupcy (loss) (doesn't apply to AI??)
LOAN_LIMIT = 5

#amount of territory each regiment can take
TERRITORY_CONQUERED_BY_REGIMENT = 100


#----------------------defining variables---------------------------

#-1 means that it hasn't been selected yet
player_country_id = -1

#how much territory each country has in each province from 1-1000.
#list of provinces and in those provinces is a list of countries, with the country data looking like country_id, territory
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


#function stolen from internet, checks if a value can be turned into an int
def can_be_made_int(s):
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True


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


#returns a list of the country_ids with the largest army, including any tied countries, moving to a given province_id
def find_largest_army(province_id):
    largest_armies = []
    largest_army = 0
    #finds the largest army
    for c in army_locations[province_id]:
        if c[1] > largest_army:
            largest_army = c[1]
    #adds each country with that many armies to the list
    for c in army_locations[province_id]:
        if c[1] == largest_army:
            largest_armies.append(c[0])
    
    return largest_armies


#returns a list of the country_ids with the largest army, including any tied countries, moving to a given province_id, 
#excluding country_id from calculations
def find_largest_army_excl(province_id, country_id):
    largest_armies = []
    largest_army = 0
    #finds the largest army
    for c in army_locations[province_id]:
        if c[1] > largest_army and not c[0] == country_id:
            largest_army = c[1]
    #adds each country with that many armies to the list
    for c in army_locations[province_id]:
        if c[1] == largest_army and not c[0] == country_id:
            largest_armies.append(c[0])
    
    return largest_armies


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


#returns the index of the territory of the province owner in the province_owners list of a given province, returns -1 if they don't own any
def find_country_territory_index(country_id, province_id):
    #loops over each country with territory in the province
    index = 0
    for c in province_owners[province_id]:
        #return the index if it is there
        if c[0] == country_id:
            return index
        index += 1
    #if it isnt there return -1 to signal it
    return -1


#returns the index of country_id's armies in the given province_id, returning -1 if they don't own any there
def find_country_army_index(country_id, province_id):
    #loops over every country with an army in the province
    pl_country_armies_index_in_prov = -1
    
    for i, c in enumerate(army_locations[province_id]):
        #if it finds the country_id in that list it takes a note of the index
        if c[0] == country_id:
            pl_country_armies_index_in_prov = i
    
    return pl_country_armies_index_in_prov


#returns a list of provinces that the given country has armies stationed in,
#with each province containing the province_id, and the amount of armies there
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


#returns the amount of armies a given country_id has in the given province_id, returns -1 if none found
def find_stationed_armies_in_province(country_id, province_id):
    #loops over each country with armies stationed there
    for c in army_locations[province_id]:
        if c[0] == country_id:
            return c[1]
    
    return -1


#returns the id of a named province (modified from internet solution)
def find_province_id(province_name):
    #enumerate turns the list into a list of tuples with an index and the original data in that spot
    for i, prov in enumerate(PROVINCE_ADJ):
        if prov[0] == province_name:
            return i
    return None


#moves a specified number of armies to a province
def move_armies_to_province(province_id, country_id, armies):
    global army_locations
    
    army_index = find_country_army_index(province_id, country_id)
    
    if army_index == -1:
        army_locations[province_id].append([country_id, armies])
    else:
        army_locations[province_id][army_index][1] += armies


#retracts orders from a specified number of armies to a province
def retract_armies_from_province(province_id, country_id, armies):
    global army_locations
    
    army_index = find_country_army_index(province_id, country_id)
    
    if army_index != -1:
        army_locations[province_id][army_index][1] -= armies
        #checks if there are now no more armies in that province and removes the section of the list if so
        if army_locations[province_id][army_index][1] < 1:
            army_locations[province_id].pop(army_index)


#returns the income for a given country_id
def calculate_income(country_id):
    province_count = find_province_count(country_id)
    #base of 1 tax, then 1.5 per province
    income = 1 + (province_count * 1.5)
    
    #hanseatic league is special
    if country_id == 11:
        #sets some coastal provinces in the north to be "important trade areas", so they are worth more to the hanseatic
        #specifically the northern coast of the HRE and Breda
        trade_significant_regions = list(range(16))
        for i in range(3):
            trade_significant_regions.pop(5)
        
        #goes over each province owned by hanseatic
        for p in find_owned_provinces(country_id):
            #if it's in trade_significant_regions, its worth another quarter ducat
            if p in trade_significant_regions:
                income += 0.25
    
    return income


#returns the expenses for a given country_id
def calculate_expenses(country_id):
    total_armies = country_data[player_country_id][2]
    province_count = find_province_count(player_country_id)
    forcelimit = calculate_forcelimit(player_country_id)
    amount_over_forcelimit = max(total_armies - forcelimit, 0)
    
    #army maintainance is 0.22 per regiment, and province maintainance is a high 0.5 ducats
    #if over forcelimit it works like eu4: (total_armies + amount_over_forcelimit) / forcelimit
    expenses = (total_armies * 0.22) * (total_armies + amount_over_forcelimit) / forcelimit
    expenses += (province_count * 0.5) #province maintainance is high to account for forts
    expenses = fix_float(expenses)
    
    return expenses


#returns the balace of income and expenses in a month for a given country_id
def calculate_balance(country_id):
    income = calculate_income(country_id)
    expenses = calculate_expenses(country_id)
    
    balance = income - expenses
    balance = fix_float(balance)
    
    return balance


#returns the amount of ducats needed to repay a loan for a given country_id
def calculate_loan_size(country_id):
    province_count = find_province_count(country_id)
    #7.5 ducats per province
    return round(province_count * 7.5)


#returns the max manpower for a given country_id
def calculate_max_manpower(country_id):
    province_count = find_province_count(country_id)
    #10k base, 1.5k per province
    max_manpower = 10000 + (1500 * province_count)
    #accounts for the emperor taking some levies
    if country_id == 0:
        max_manpower += (len(COUNTRIES) - 1) * 500
    #if you are stronger than the emperor you don't owe them crap
    elif province_count >= find_province_count(0):
        pass
    #electors contribute significantly less (not reflected in emperor gains, but this doesn't matter as it would be annoying to fix)
    elif 1 <= country_id <= 7:
        #the way I did this means that the bigger you are, the less levies you give as you are powerful enough to refuse them
        max_manpower -= round(250 / province_count)
    else:
        max_manpower -= 500
    
    return max_manpower


#returns the forcelimit for a given country_id
def calculate_forcelimit(country_id):
    #forcelimit is 6 at base, + 1.5 for each province
    return round(6 + (find_province_count(country_id) * 1.5))


#returns the manpower recovery speed for a given country_id
def calculate_manpower_recovery(country_id):
    max_manpower = calculate_max_manpower(country_id)
    #manpower recovery speed will replenish manpower from 0 to max in 10 years (adjust to less?), or add a minimum of 100.
    return max(round(max_manpower / 120), 100)


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
        #adds starting manpower, ducats, army, and loans, in that order
        
        #manpower is 10k at the start, with some random variance for flavour
        data.append(10000 + random.randrange(-1000, 1000))
        
        #ducats is 50 + two months of income (no expenses) with some random variance of max 0.3 ducats
        data.append(50 + calculate_income(c) - (random.randrange(-30, 30) / 100))
        
        #starting army is roughly 5/7ths of the force limit
        data.append(round(5/7 * calculate_forcelimit(c)))
        
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
    reset_army_locations_list()
    reset_country_data_list()
    
    year = 1515
    month = 0
    
    #flavour text that also describes your options, old text
    #print("There are a lot of options for countries to play as, and each country has a certain level of difficulty.")
    #print("")
    #print("For example, Austria is the Emperor of the Holy Roman Empire, so they are the most powerful, with widespread influence from Burgundy to Slovenia.")
    #print("There are also other powerful states such as the Electorates of the Kingdom of Bohemia and Brandenburg, and the powerful Duchies of Bavaria and Switzerland, who are also strong picks.")
    #print("")
    #print("If you want a bit more of a challenging game, you may also choose to play as the Electorate of Thuringia, the Duchy of Pomerania, or the Hanseatic League.")
    #print("If you would like a very challenging start, you could try the Electorates of Cologne or The Palatinate, or the Duchies of Brunswick, Ansbach, or Cleves.")
    #print("Any other country is an incredibly difficult start, so they are not recommended for anyone other than the most experienced of players.")
    #print("")
    #print("For a new player, it is recommened to play either Austria or Bohemia.")
    #print("Austria is the Emperor and the most powerful by far, but their territories are very spread out and may be difficult to defend, or be overwhelming to manage.")
    #print("The Kingdom Bohemia is far less powerful than Austria, but they are still much more powerful than any of the other countries as they are a Kingdom, and their territories are more connected than Austria's")
    #print("")
    #print("It should also be noted that Electorates give less levies to the Emperor, and the Hanseatic League also trades with northern provinces to make more money.")
    #print("")
    
    #new text
    print("There are lots of different countries to play as, each with their own difficulty.")
    print("Austria is the easiest and is recommened for new players, but Bohemia is also a good choice.")
    
    response = input("Would you like to see all the possible countries? (y/n): ")
    
    if response.lower() == "y":
        for i in COUNTRIES:
            print(i)
    elif response.title() in COUNTRIES:
        player_country_id = COUNTRIES.index(response.title())
        print("\n")
        return
    print("")
    
    #quick note to set things straight for ingame balance reasons; here are the true rankings with no fluff:
    #very easy = Austria
    #easy = bohemia, Brandenburg, Bavaria, Switzerland
    #moderate = Thuringia, Pomerania, Hanseatic League (if the others go up a tier then this tier merges with the next tier down)
    #hard = Cologne, Palatinate, Brunswick, Ansbach, Cleves
    #very hard = everyone else
    #impossible = anything that sticks out as a significantly harder start after testing, with liege, saxony, and maybe Wurttemberg, Bregenz and Augsburg on watchlists
    
    
    player_country_id = -1
    #ask the player which country they would like to play as
    response = input("Enter the name of the country you want to play as: ").title()
    while True:
        #if it is not a valid country then it tries again
        if response in COUNTRIES:
            player_country_id = COUNTRIES.index(response)
            break
        
        response = input("Invalid country, enter the name of a valid country: ").title()
    
    print("\n")
    


#------------------------game functions--------------------------

#executes a turn
def handle_turn():
    #states which turn it is
    print(f"------------------------------{MONTH_NAMES[month]} {str(year)}------------------------------")
    print("")
    #handle player inputs
    handle_player_input()
    #calculate ai decisions
    calculate_ai_decisions()
    #calculate what happens
    evaluate_turn()


#makes all the NPC nations take their turns
def calculate_ai_decisions():
    for country_id, country in enumerate(COUNTRIES):
        if country_id == player_country_id:
            continue
        if find_province_count(country_id) < 1:
            continue
        print(country)
        print(str(country_data[country_id][2]))
        ai_train_armies(country_id)
        print(str(country_data[country_id][2]))
        ai_move_armies(country_id)


#
def ai_train_armies(country_id):
    global country_data
    
    ducats = country_data[country_id][1]
    manpower = country_data[country_id][0]
    total_armies = country_data[country_id][2]
    balance = calculate_balance(country_id)
    forcelimit = calculate_forcelimit(country_id)
    
    #make decision
    armies_to_train = 0
    decision_reached = False
    while not decision_reached:
        #if it can't afford to lose money for 5 turns...
        if balance < 0 and ducats + (balance * 5) < 0:
            #it sees if the amount of armies disbanding can counterract it
            if ducats + (5 * (balance + (-0.22 * armies_to_train))) < 0:
                #if not it disbands another
                armies_to_train -= 1
            else:
                decision_reached = True
        #if it can train another army and has the spare income to afford the upkeep it does
        elif 10 * armies_to_train + 1 < ducats and 1000 * armies_to_train + 1 < manpower and 0.22 * armies_to_train + 1 < balance:
            armies_to_train += 1
        else:
            decision_reached = True
        
        
    #makes payment for the training/disbanding
    if armies_to_train < 0:
        #gives a refund of 250 manpower
        country_data[country_id][0] += 250 * armies_to_train
    else:
        country_data[country_id][0] -= 1000 * armies_to_train
        country_data[country_id][1] = fix_float(ducats - (10 * armies_to_train))
    
    #changes the amount of armies they have
    country_data[country_id][2] += armies_to_train


#TODO
def ai_move_armies():
    pass


#takes all the army orders and figures out what happens, then also updates other things
def evaluate_turn():
    #deals with armies attacking eachother
    evaluate_army_orders()
    #deals with other variables that change each month
    evaluate_end_of_turn()


#calculates how much money and manpower each country gets and returns how many loans the player took
def handle_income_and_manpower():
    global country_data
    
    player_loans_taken = 0
    country_id = 0
    for country_info in country_data:
        country_info[0] += calculate_manpower_recovery(country_id)
        country_info[1] += calculate_balance(country_id)
        country_info[1] = fix_float(country_info[1])
        #checks if loans need to be taken
        if country_info[1] < 0:
            while country_info[1] < 0:
                country_info[1] += calculate_loan_size(country_id)
                country_info[3] += 1
                if player_country_id == country_id:
                    player_loans_taken += 1
        country_id += 1
    return player_loans_taken


#deals with variables that change each month and other end of turn shenanigans
def evaluate_end_of_turn():
    global end_game
    global country_data
    global month
    global year
    
    #calculates how much money and manpower each country gets and returns how many loans the player took
    player_loans_taken = handle_income_and_manpower()
     
    reset_army_locations_list()
    
    #check if the player has too many loans
    if country_data[player_country_id][3] >= LOAN_LIMIT:
        end_game = True
        print(f"You were forced to take too many loans, so {COUNTRIES[player_country_id]} went bankrupt and got annexed by your more powerful and economically responsible neighbours.")
        return
    elif player_loans_taken > 0:
        print(f"You have taken {str(player_loans_taken)} loans due losing too much money.")
    
    country_id = 0
    #deal with non-player bankrupt nations
    for c in country_data:
        if c[3] >= LOAN_LIMIT and country_id != player_country_id:
            #deletes all their armies as punishment
            c[2] = 0
        country_id += 1
    
    #change the month and year if necessary year
    month += 1
    if month >= 12:
        month = 0
        year += 1


#deals with army movement and territory gain/loss
def evaluate_army_orders():
    global army_locations
    global country_data
    global province_owners
    #loop over each province
    for province_id, p in enumerate(army_locations):
        #if there are no armies, then nothing changes or happens 
        if len(p) == 0:
            #move onto the next province
            continue
        #check whether the owner of the province is defending themselves
        province_owner = find_province_owner(province_id)
        owner_army_index = find_country_army_index(province_owner, province_id)
        owner_territory_index = find_country_territory_index(province_owner, province_id)
        
        #if they are defending themselves then resolve that
        if owner_army_index != -1:
            countries_with_largest_army = find_largest_army_excl(province_id, owner_army_index)
            #each enemy army fights the defending owner army until the owner armies are destroyed or 
            #each enemy army has fought the owner army once
            for a in range(len(p)):
                #can't fight itself
                if a == owner_army_index:
                    continue
                #does a battle between the attacker and the owner
                evaluate_battle(province_id, p[a][0], p[owner_army_index][0])
                #checks if the owner has any armies left
                owner_army_index = find_country_army_index(province_owner, province_id)
                #if not the loop exits early, and if so then the index is updated and the next battle happens
                if owner_army_index == -1:
                    break
            #if the owner still has armies
            if owner_army_index != -1:
                #they keep the territory and nothing else happens
                continue #move to next province after resolution
        
        #now the province is guarenteed not to have any defenders, so it just becomes a scramble for the remaining armies
        
        #double checking they are not defending themselves
        if owner_army_index == -1:
            #if there is just one attacker...
            if len(p) == 1:
                #...the attacker just takes some of the owner's territory there
                calculate_territory_taken(province_id, province_owner, p[0][0], 0, p[0][1])
                #move to next province
                continue
            #otherwise the largest army takes the province, with ties broken by a battle.
            #finds a list of countries with the largest army in the province, including ties
            countries_with_largest_army = find_largest_army(province_id)
            #if there is no tie, there is no battle and the small armies go home unscathed
            #otherwise the tieing countries have to decide a victor
            if len(countries_with_largest_army) > 1:
                #they do battles until there is only one army
                while len(countries_with_largest_army) > 1:
                    evaluate_battle(province_id, countries_with_largest_army[0], countries_with_largest_army[1])
                    countries_with_largest_army = find_largest_army(province_id)
            
            #once there is a clear winner, that winner takes some territory from the owner
            calculate_territory_taken(province_id, province_owner, countries_with_largest_army[0], 0, p[countries_with_largest_army[0]][1])
            continue #move to next province after resolution
        
        #hopefully all conflicts are resolved by now, move to the next province


#calculates how much territory to take from the defender of an attack
def calculate_territory_taken(province_id, defender_country_id, attacker_country_id, defending_armies, attacking_armies):
    global province_owners
    army_difference = attacking_armies - defending_armies
    if army_difference <= 0:
        return 0
    attacker_territory_index = find_country_territory_index(attacker_country_id, province_id)
    defender_territory_index = find_country_territory_index(defender_country_id, province_id)
    
    old_defender_territory = province_owners[province_id][defender_territory_index][1]
    
    province_owners[province_id][defender_territory_index][1] -= army_difference * TERRITORY_CONQUERED_BY_REGIMENT
    if province_owners[province_id][defender_territory_index][1] <= 0:
        province_owners[province_id].pop(defender_territory_index)
        
    if army_difference * TERRITORY_CONQUERED_BY_REGIMENT > old_defender_territory:
        territory_taken = old_defender_territory
    else:
        territory_taken = army_difference * TERRITORY_CONQUERED_BY_REGIMENT# + random.randrange(-5, 5) (maybe add random variation?)
    
    if attacker_territory_index == -1:
        province_owners[province_id].append([attacker_country_id, territory_taken])
    else:
        province_owners[province_id][attacker_territory_index][1] += territory_taken


#calculates the outcome of a battle and then updates province information and country data accordingly
def evaluate_battle(province_id, country_1, country_2):
    army_1 = find_stationed_armies_in_province(country_1, province_id)
    army_2 = find_stationed_armies_in_province(country_2, province_id)
    
    #if army_difference is positive then army 1 is bigger, otherwise army 2 is bigger.
    #the larger the difference, the more crushing the defeat
    army_difference = army_1 - army_2
    
    #each army takes casualties
    #the amount of casualties is 1 each for a draw, and if one army is larger then they take less and the other takes exponentially more
    #if the bottom of the fraction is 1 or less, then the whole army is destroyed.
    if army_1 + army_difference <= 1:
        new_army_1 = 0
    else:
        new_army_1 = army_1
        #include a bit of random variance
        new_army_1 -= round(army_1 / (army_1 + army_difference + (random.randrange(0, 10) / 10)))
    
    if army_2 - army_difference <= 1:
        new_army_2 = 0
    else:
        new_army_2 = army_2
        #variance
        new_army_2 -= round(army_2 / (army_2 - army_difference + (random.randrange(0, 10) / 10)))
    
    #finds where the countries' armies are
    army_1_index = find_country_army_index(country_1, province_id)
    army_2_index = find_country_army_index(country_2, province_id)
    
    #then updates the armies at that location
    army_locations[province_id][army_1_index][1] = new_army_1
    army_locations[province_id][army_2_index][1] = new_army_2
    
    #updates the country stats to reflect the new army size
    country_data[country_1][2] -= army_1 - new_army_1 #changes the army size by the difference of the starting army and the current army size
    country_data[country_2][2] -= army_2 - new_army_2 


#handles the player inputs in a turn
def handle_player_input():
    global end_game
    
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
            train_armies_menu()
        elif decision == 4:
            all_options_selected = confirm_orders_menu()
        elif decision == 5:
            u_sure = input("Are you sure you want to end the game? (y/n): ").lower()
            if u_sure == "y":
                all_options_selected = True
                end_game = True


#ui to confirm the orders you placed after selecting that you want to end the turn
#returns whether all options selected
def confirm_orders_menu():
    global all_options_selected
    
    total_armies = country_data[player_country_id][2]
    #finds out how many armies have already moved
    moved_armies = find_stationed_armies_count(player_country_id)
    #and then how many haven't
    idle_armies = total_armies - moved_armies
    
    if idle_armies > 0:
        prov_to_move_to = find_owned_provinces(player_country_id)[0]
        print(f"You have some armies that have not moved yet. Do you want to have them all guard the province of {PROVINCE_ADJ[prov_to_move_to][0]} or do you want go back?")
        #idiot proofs the question
        decision = input(f"Enter 1 to move them all to {PROVINCE_ADJ[prov_to_move_to][0]}, 2 to go back to the option select: ")
        while not (decision == "1" or decision == "2"):
            decision = input("Please enter a 1 or a 2: ")
        
        decision = int(decision)
        
        #if they choose to move there
        if decision == 1:
            move_armies_to_province(prov_to_move_to, player_country_id, idle_armies)
            print("")
        else:
            #otherwise go back to option select
            print("")
            return False
    
    #then ask if the player is sure they are done
    decision = input("Are you sure you are ready to end the turn and go to the next? (y/n): ").lower()
    print("")
    if decision == "y":
        return True


#ui for army training
def train_armies_menu():
    global country_data
    
    stop_training_armies = False
    while not stop_training_armies:
        #displays some important stats
        ducats = country_data[player_country_id][1]
        manpower = country_data[player_country_id][0]
        total_armies = country_data[player_country_id][2]
        balance = calculate_balance(player_country_id)
        forcelimit = calculate_forcelimit(player_country_id)
        
        print(f"{COUNTRIES[player_country_id]} has {str(ducats)} ducats.")
        print(f"{COUNTRIES[player_country_id]} has a total balance of {str(balance)} ducats per month.")
        if total_armies == 1:
            print(f"{COUNTRIES[player_country_id]} has {str(total_armies)} army.")
        else:
            print(f"{COUNTRIES[player_country_id]} has {str(total_armies)} armies.")
        print(f"{COUNTRIES[player_country_id]} has a forcelimit of {str(forcelimit)} armies before their armies become more expensive.")
        print(f"{COUNTRIES[player_country_id]} has {str(manpower)} manpower.")
        print("")
        
        print("Armies cost 10 ducats and 1000 manpower to build.")
        print("Disbanding armies refunds you 250 manpower.")
        print("")
        
        #stop the training if the player cannot train any due to lack of resources
        if ducats < 10:
            print("You cannot train anymore armies due to lack of funds, as armies cost 10 ducats to train.")
            stop_training_armies = True
            break
        if manpower < 1000:
            print("You cannot train anymore armies due to lack of manpower, as armies cost 1000 manpower to train.")
            stop_training_armies = True
            break
        
        
        moved_armies = find_stationed_armies_count(player_country_id)
        idle_armies = total_armies - moved_armies
        
        #ask how many
        armies_to_train = input("How many armies would you like to train? (You can enter a negative number to disband existing armies): ")
        
        if armies_to_train.lower() == "cancel":
            print("Cancelling training armies, returning to menu...")
            stop_training_armies = True
            break
        
        #checks if the answer is a valid one in a special way to make sure that there are no errors with doing int() on invalid strings
        valid_answer = True
        if not can_be_made_int(armies_to_train):
            valid_answer = False
        elif (int(armies_to_train) * 10) > ducats or (int(armies_to_train) * 1000) > manpower or armies_to_train == "0" or int(armies_to_train) < -idle_armies:
            valid_answer = False
            
        #check for an unreasonable amount of weird responses
        while not valid_answer:
            #checks for a darwin award
            if not can_be_made_int(armies_to_train):
                armies_to_train = input("Please input a valid NUMBER: ")
            else:
                armies_to_train = int(armies_to_train)
                
                if (armies_to_train * 10) > ducats:
                    armies_to_train = input("You don't have enough ducats to train that many troops, please input a valid number: ")
                elif (armies_to_train * 1000):
                    armies_to_train = input("You don't have enough manpower to train that many troops, please input a valid number: ")
                elif armies_to_train < -idle_armies:
                    armies_to_train = input("You are trying to disband more troops than you have idle troops availiable to disband, please input a valid number: ")
                else:
                    armies_to_train = input("Please input a valid number: ")
            
            #checks if the answer is a valid one
            valid_answer = True
            if not can_be_made_int(armies_to_train) and armies_to_train.lower() != "cancel":
                valid_answer = False
            elif armies_to_train.lower() == "cancel":
                pass
            elif (int(armies_to_train) * 10) > ducats or (int(armies_to_train) * 1000) > manpower or armies_to_train == "0" or int(armies_to_train) < -idle_armies:
                valid_answer = False
        
        
        if armies_to_train.lower() == "cancel":
            print("Cancelling training armies, returning to menu...")
            stop_training_armies = True
            break
        
        armies_to_train = int(armies_to_train)
        
        #makes payment for the training/disbanding
        if armies_to_train < 0:
            #gives a refund of 250 manpower
            country_data[player_country_id][0] += 250 * armies_to_train
        else:
            country_data[player_country_id][0] -= 1000 * armies_to_train
            country_data[player_country_id][1] = fix_float(country_data[player_country_id][1] - (10 * armies_to_train))
        
        #changes the amount of armies they have
        country_data[player_country_id][2] += armies_to_train
        
        print("Do you want to stop training armies or continue?")
        stop_training_decision = input("Enter 1 to stop, 2 to continue: ")
        if stop_training_decision != "2":
            stop_training_armies = True
        else:
            print("")
    print("")


#the ui for moving armies
def move_armies_menu():
    #dont forget this (imagine if this saves me in the future)
    global army_locations
    
    stop_moving_armies = False
    while not stop_moving_armies:
        #only displays how many armies you have and where they have moved to if they have moved
        display_army_info(True)
        #display possible provinces to move to
        display_valid_army_target_info()
        
        total_armies = country_data[player_country_id][2]
        #finds out how many armies have already moved
        moved_armies = find_stationed_armies_count(player_country_id)
        #and then how many haven't
        idle_armies = total_armies - moved_armies
        
        move_or_retract = 0 #1 = move, 2 = retract, 0 for unset
        quantity_affected = 0 #how many armies will be moved or retracted from a province
        province_affected = -1 #province id of the affected province, -1 means unset
        
        #asks whether you want to move to places with unstationed armies or whether you want to retract an order
        #removes options depending on the situation
        if idle_armies > 0 and moved_armies > 0:
            #if either is allowed then it asks
            print("Do you want to move armies that haven't moved or retract orders from armies who you have already given orders?")
            move_or_retract = input("Enter 1 to move, 2 to retract: ")
            while not (move_or_retract == "1" or move_or_retract == "2" or move_or_retract.lower() == "cancel"):
                move_or_retract = input("Please enter a 1 or a 2: ")
            
            if move_or_retract.lower() == "cancel":
                print("Canceling movement ordering, returning to menu...")
                stop_moving_armies = True
                break
            
            move_or_retract = int(move_or_retract)
        elif idle_armies == 0:
            #if you have moved all your armies then you have to confirm that you still want to order (remove if it gets annoying)
            print("You have already given all of your armies orders. Would you like to retract some of these orders or stop managing army movement?")
            stop_moving_decision = input("Enter 1 to stop, 2 to retract: ").lower()
            if stop_moving_decision != "2":
                stop_moving_armies = True
                break
            #as you have one option it makes the decision for you
            move_or_retract = 2
        else:
            #if you haven't moved anything yet the game just continues
            move_or_retract = 1
        
        
        #asks which province to move to or retract a move from
        if move_or_retract == 1:
            province_move_decision = input("Which province do you want to move to: ").title()
        else:
            province_move_decision = input("Which province do you want to retract a move from: ").title()
        
        if province_move_decision.lower() == "cancel":
                print("Canceling movement ordering, returning to menu...")
                stop_moving_armies = True
                break
        
        #finds all the neighbouring provinces and who owns them
        unsort_neighbour_provinces = find_province_owners(find_bordering_provinces(player_country_id))
        #finds all the provinces the player owns
        owned_provinces = find_owned_provinces(player_country_id)
        
        #sorts neighbour_provinces to be ordered by country_id
        unsort_neighbour_provinces.sort(key = lambda sortby: sortby[0])
        #puts it in the right data format
        neighbour_provinces = []
        for p in unsort_neighbour_provinces:
            neighbour_provinces.append(p[1])
        
        #creates one big list of all the availiable movement provinces
        availiable_provinces = owned_provinces + neighbour_provinces
        
        #find all availiable retractions
        provinces_stationed_in = find_stationed_armies(player_country_id)
        #makes a new list which is just the province_ids and not also the army count
        province_ids_stationed_in = []
        for p in provinces_stationed_in:
            province_ids_stationed_in.append(p[0])
        
        #check if they're using a shortcut 
        if can_be_made_int(province_move_decision):
            if int(province_move_decision) <= (len(availiable_provinces) + 1) and int(province_move_decision) > 0:
                province_move_decision = availiable_provinces[int(province_move_decision) - 1]
        else:
            #otherwise turns the name into an id
            province_move_decision = find_province_id(province_move_decision)
        
        
        #makes sure it works properly
        while province_move_decision == None or (move_or_retract == 1 and not province_move_decision in availiable_provinces) or (move_or_retract == 2 and not province_move_decision in province_ids_stationed_in):
            #if the province doesn't exist
            if province_move_decision == None:
                province_move_decision = input("Invalid province name, please enter the name of a valid province: ").title()
            #if it's an invalid move
            elif move_or_retract == 1 and not province_move_decision in availiable_provinces:
                province_move_decision = input("You cannot move an army there, please enter the name of a valid province: ").title()
            #if there would be no armies to remove from that province
            elif move_or_retract == 2 and not province_move_decision in province_ids_stationed_in:
                province_move_decision = input("There are no armies you can retract from this province, please enter the name of a valid province: ").title()
            #just in case something else slips through the cracks
            else:
                province_move_decision = input("Invalid province, please enter the name of a valid province: ").title()
            
            if province_move_decision.lower() == "cancel":
                print("Canceling movement ordering, returning to menu...")
                stop_moving_armies = True
                break
            
            #check if they're using a shortcut 
            if can_be_made_int(province_move_decision):
                if int(province_move_decision) < len(availiable_provinces) and int(province_move_decision) < 0:
                    province_move_decision = availiable_provinces[int(province_move_decision)]
            else:
                #otherwise turns the name into an id
                province_move_decision = find_province_id(province_move_decision)
                
            #if cancel was selected, then the the loop is broken
            if stop_moving_armies:
                break
            
        
        province_affected = province_move_decision
        
        
        #asks how many you want to move There
        #if you are moving then it only lets you pick how many if you have more than one
        if move_or_retract == 1:
            if idle_armies == 1:
                quantity_affected = 1
            else:
                quantity_affected = input("How many of your armies would you like to move there: ")
                
                valid_answer = True
                if quantity_affected.lower() == "cancel":
                    pass
                elif not can_be_made_int(quantity_affected):
                    valid_answer = False
                elif int(quantity_affected) > idle_armies or int(quantity_affected) < 1:
                    valid_answer = False
                #makes sure there is no trickery
                while not valid_answer:
                    if not can_be_made_int(quantity_affected):
                        quantity_affected = input("Please input a valid NUMBER: ")
                    elif int(quantity_affected) > idle_armies:
                        quantity_affected = input("You do not have enough armies, please input a valid number: ")
                    else:
                        quantity_affected = input("Please input a valid number: ")
                    
                    valid_answer = True
                    if quantity_affected.lower() == "cancel":
                        pass
                    elif not can_be_made_int(quantity_affected):
                        valid_answer = False
                    elif int(quantity_affected) > idle_armies or int(quantity_affected) < 1:
                        valid_answer = False
                    
        else:
            #otherwise you get to pick if there is more than one army in that province
            #finds how many armies are in the province
            for p in provinces_stationed_in:
                if province_affected == p[0]:
                    armies_stationed = p[1]
                    break
            
            if armies_stationed > 1:
                quantity_affected = input("How many armies would you like to retract the order to move here from: ")
                
                valid_answer = True
                if quantity_affected.lower() == "cancel":
                    pass
                elif not can_be_made_int(quantity_affected):
                    valid_answer = False
                elif int(quantity_affected) > armies_stationed or int(quantity_affected) < 1:
                    valid_answer = False
                #trickery prevention
                while not valid_answer:
                    if not can_be_made_int(quantity_affected):
                        quantity_affected = input("Please input a valid NUMBER: ")
                    elif int(quantity_affected) > armies_stationed:
                        quantity_affected = input("There are not enough armies there to retract, please input a valid number: ")
                    else:
                        quantity_affected = input("Please input a valid number: ")
                    
                    valid_answer = True
                    if quantity_affected.lower() == "cancel":
                        pass
                    elif not can_be_made_int(quantity_affected):
                        valid_answer = False
                    elif int(quantity_affected) > armies_stationed or int(quantity_affected) < 1:
                        valid_answer = False
            else:
                #if there is only one then only one can be retracted
                quantity_affected = 1
        
        #checks whether this is a string
        if isinstance(quantity_affected, str):
            #if so check
            if quantity_affected.lower() == "cancel":
                print("Canceling movement ordering, returning to menu...")
                stop_moving_armies = True
                break
        
        quantity_affected = int(quantity_affected)
        
        if move_or_retract == 1:
            move_armies_to_province(province_affected, player_country_id, quantity_affected)
        else:
            retract_armies_from_province(province_affected, player_country_id, quantity_affected)
        
        print("")
        #reassures the player that the move was succesfull if it was, and warns the player if I'm bad at coding
        message = "Your "
        if quantity_affected == 1:
            message += "army has been succesfully "
        else:
            message += "armies have been succesfully "
        if move_or_retract == 1:
            message += "moved."
        else:
            message += "retracted."
        print(message)
        
        print("")
        
        #asks if you want to exit out of the loop
        print("Do you want to stop ordering armies or continue?")
        stop_moving_decision = input("Enter 1 to stop, 2 to continue: ")
        if stop_moving_decision == "1":
            stop_moving_armies = True
        else:
            print("")
    print("")


#asks the player to enter a number to show what they want to do, returns their response
def get_player_option_select():
    #ask player what they want to do
        print("Enter a 1 if you want to see more information about your nation.")
        print("Enter a 2 if you want to move armies or retract moves you have already made.")
        print("Enter a 3 if you want to train new armies or disband existing armies.")
        print("Enter a 4 if you want to confirm your orders for the turn and proceed to the next.")
        print("Enter a 5 if you want to exit this game and start a new one.")
        decision = input()
        while not can_be_made_int(decision) or int(decision) < 1 or int(decision) > 5:
            decision = input("Enter a valid number: ")
        decision = int(decision)
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
        print(f"{make_ordinal(place)} place: {COUNTRIES[c[0]]}, with {str(c[1])} provinces.")
        place += 1
    
    #finds out what ranking the player got
    player_ranking = power_rankings.index([player_country_id, find_province_count(player_country_id)])
    
    #if they aren't on the leaderboard (skill issue icl), then they get mentioned at the bottom
    if player_ranking > 4:
        if power_rankings[player_ranking][1] == 1:
            print(f"Your country, {COUNTRIES[player_country_id]}, got {make_ordinal(player_ranking + 1)}, with {str(power_rankings[player_ranking][1])} province.")
        else:
            print(f"Your country, {COUNTRIES[player_country_id]}, got {make_ordinal(player_ranking + 1)}, with {str(power_rankings[player_ranking][1])} provinces.")
    
    print("")


#self explanatory
def display_bordering_country_info():
    print("Neighboring Country Information:")
    
    neighbours = find_bordering_countries(player_country_id)
    #gets the provinces bordering the country and also who owns each of them
    neighbour_provinces = find_province_owners(find_bordering_provinces(player_country_id))
    
    print(f"{COUNTRIES[player_country_id]} has {str(len(neighbours))} neighbouring countries. They are:")
    
    #goes over each country and gives info on them
    for c in neighbours:
        message = ""
        provinces = find_province_count(c)
        message += f"{COUNTRIES[c]}, who has {str(provinces)}"
        
        #handling plurality
        if provinces == 1:
            message += " province, "
        else:
            message += " provinces, "
        
        #find the provinces that they own that border the player country
        owned_provinces = find_owned_provinces_from_set(c, neighbour_provinces)
        
        #handling plurality
        
        if len(owned_provinces) == provinces:
            if len(owned_provinces) == 1:
                message += "and it borders "
            else:
                message += "all of which border "
        else:
            if len(owned_provinces) == 1:
                message += f"{str(len(owned_provinces))} of which borders "
            else:
                message += f"{str(len(owned_provinces))} of which border "
        
        message += f"{COUNTRIES[player_country_id]}: "
        
        
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


#displays the provinces the player owns and the provinces that are adjacent and who owns them
def display_valid_army_target_info():
    print("Availiable Provinces to Move to:")
    
    #finds all the neighbouring provinces and who owns them
    neighbour_provinces = find_province_owners(find_bordering_provinces(player_country_id))
    #finds all the provinces the player owns
    unstruct_owned_provinces = find_owned_provinces(player_country_id)
    #turns it into the right data format: [country_id, province_id]
    owned_provinces = []
    for p in unstruct_owned_provinces:
        owned_provinces.append([player_country_id, p])
    
    #sorts neighbour_provinces to be ordered by country_id
    neighbour_provinces.sort(key = lambda sortby: sortby[0])
    
    #creates one big list of all the availiable movement provinces
    availiable_provinces = owned_provinces + neighbour_provinces
    
    for i, p in enumerate(availiable_provinces):
        print(f"{i + 1}: {PROVINCE_ADJ[p[1]][0]}, owned by {COUNTRIES[p[0]]}.")
    
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
        print(f"{COUNTRIES[player_country_id]} has {str(total_armies)} army.")
    else:
        print(f"{COUNTRIES[player_country_id]} has {str(total_armies)} armies.")
    
    #mentions where moved armies have gone to, if they have any already
    if moved_armies > 0:
        #gets all of the moved armies' locations
        moved_armies_locations = find_stationed_armies(player_country_id)
        
        #changes the text depending on how many of these armies have moved so far
        if moved_armies == total_armies:
            print(f"{COUNTRIES[player_country_id]} have moved all of your armies, and they are moving to these provinces:")
        else:
            print(f"{COUNTRIES[player_country_id]} have moved {moved_armies} of your armies, and they are moving to these provinces:")
        
        #loops over each province to describe where they have gone
        for p in moved_armies_locations:
            message = str(p[1])
            #checks how many armies are in the province to see if it is plural
            if p[1] > 1:
                message += " armies are "
            else:
                message += " army is "
            
            #checks if the country owns the province the army is stationed in
            if country_owns_province(province_owners[p[0]], player_country_id):
                #if so then say that the army(s) is guarding the province
                message += "defending "
            else:
                #otherwise they are attacking
                message += "attacking "
            
            #adds on the name of the province
            message += f"{PROVINCE_ADJ[p[0]][0]}."
            
            #finally prints the built message
            print(message)
                
            
    else:
        print("None of these armies have moved yet.")
    
    #checks if only army info should be shown
    if just_armies:
        print("")
        return
    
    #forcelimit
    forcelimit = calculate_forcelimit(player_country_id)
    
    print(f"{COUNTRIES[player_country_id]} has a forcelimit of {str(forcelimit)} armies before their armies become more expensive.")
    
    #manpower
    manpower = country_data[player_country_id][0]
    
    max_manpower = calculate_max_manpower(player_country_id)
    
    #values taken straight from the wiki
    manpower_recovery = calculate_manpower_recovery(player_country_id)
    
    print(f"{COUNTRIES[player_country_id]} has {str(manpower)} manpower.")
    print(f"{COUNTRIES[player_country_id]} cannot have more than {str(max_manpower)} manpower in reserves.")
    print(f"{COUNTRIES[player_country_id]} recovers {str(manpower_recovery)} manpower in a month.")
    
    
    
    print("")


#display economic information
def display_economic_info():
    print("Economic information:")
    #finds player's ducat and loan count
    ducats = country_data[player_country_id][1]
    loans = country_data[player_country_id][3]
    
    #calculates player's income, expenses and balance
    income = calculate_income(player_country_id)
    expenses = calculate_expenses(player_country_id)
    balance = calculate_balance(player_country_id)
    
    print(f"{COUNTRIES[player_country_id]} has {str(ducats)} ducats.")
    print(f"{COUNTRIES[player_country_id]} has an income of {str(income)} ducats per month from province taxes.")
    print(f"{COUNTRIES[player_country_id]} spends {str(expenses)} ducats per month on maintaining their armies and provinces.")
    print(f"{COUNTRIES[player_country_id]} has a total balance of {str(balance)} ducats per month.")
    
    #checks if you have no loans, and changes the statment accordingly
    if loans < 1:
        print(f"{COUNTRIES[player_country_id]} has no loans.")
    else:
        print(f"{COUNTRIES[player_country_id]} has {str(loans)} loans.")
        
        #tells you how much you need to pay to pay them off
        loan_size = calculate_loan_size(player_country_id)
        debt = loan_size * loans
        months_to_repay = round(debt / income)
        print(f"You need to pay {str(loan_size)} ducats per loan, and with a total debt of {str(debt)} you would need {str(months_to_repay)} months of income to repay it all.")
        
        #bankrupcy warning
        if loans > LOAN_LIMIT - 2:
            print(f"You are approaching the loan limit of {str(LOAN_LIMIT)}, if you exceed this limit you will go bankrupt and lose.")
    
    print("")


#display province information
def display_province_info():
    print("Province information:")
    #get all owned provinces
    owned_provinces = find_owned_provinces(player_country_id)
    
    #I hate plurals
    if len(owned_provinces) > 1:
        print(f"{COUNTRIES[player_country_id]} has {str(len(owned_provinces))} provinces.")
        print(f"The provinces {COUNTRIES[player_country_id]} owns are:")
    else:
        print(f"{COUNTRIES[player_country_id]} has {str(len(owned_provinces))} province.")
        print(f"The province {COUNTRIES[player_country_id]} owns is:")
    
    for p in owned_provinces:
        print(PROVINCE_ADJ[p][0])
    
    print("")


#display general information, e.g. non specifics but just an overview
def display_general_info():
    print(f"Overview of {COUNTRIES[player_country_id]}'s situation:")
    
    #calculate variables
    total_armies = country_data[player_country_id][2]
    ducats = country_data[player_country_id][1]
    province_count = find_province_count(player_country_id)
    manpower = country_data[player_country_id][0]
    balance = calculate_balance(player_country_id)
    
    #plurality
    if province_count == 1:
        print(f"{COUNTRIES[player_country_id]} has {str(province_count)} province.")
    else:
        print(f"{COUNTRIES[player_country_id]} has {str(province_count)} provinces.")
    
    print(f"{COUNTRIES[player_country_id]} has {str(ducats)} ducats.")
    print(f"{COUNTRIES[player_country_id]} has a total balance of {str(balance)} ducats per month.")
    #plurality
    if total_armies == 1:
        print(f"{COUNTRIES[player_country_id]} has {str(total_armies)} army.")
    else:
        print(f"{COUNTRIES[player_country_id]} has {str(total_armies)} armies.")
    print(f"{COUNTRIES[player_country_id]} has {str(manpower)} manpower.")
    print("")


#---------------------------game body-----------------------------

#intro text
print("Welcome to Holy Roman Emperor, the game where you have to try and unite Germany!")
print("This is a game of strategy and conquest, where you start as a nation within the Holy Roman Empire in the year 1515, and you try and lead your nation to glory.")
print("")
print("Speaking of nations, you should probably pick a country to start as.")
print("")

#main loop that allows the game to be reset
while True:
    end_game = False
    reset_game()
    #main game loop
    while True:
        #i wonder what this does
        handle_turn()
        #if the game has been aborted it will restart it
        if end_game == True:
            print("Ending this game, starting a new one...\n\n")
            print("------------------------------New Game-----------------------------------")
            print("")
            print("You now need to pick a country to play as. It can be the same one or a different one to your last game.\n")
            break






