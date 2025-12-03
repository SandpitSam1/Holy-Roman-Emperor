import random

#some sort of strategy game where you fight people and grow your nation
#use armies, money, ect
#simple
#turn based
#set in the HRE? Become the emperor and unify germany?
#win by becoming emperor or conquering germany


#different actions to do in a turn:

#use army to...
#attack a country
#defend your country
#don't do anything (won't get killed)
#you can assign amounts of soldiers to these roles

#spend money on...
#army
#navy? (probs not)
#bribes

#use diplomats?
#improve relations with other countries (they might vote for you or not attack you)




#define all the variables

#-1 means that it hasn't been selected yet
player_country_id = -1

#names of all countries that exist in the game, list is a constant
countries = [
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
province_adj = [
    #Low Countries
    {"Holland" : [2, 3, 4]}, #0
    {"Friesland" : [0, 2, 8, 21]}, #1
    {"Utrecht" : [0, 1, 3, 21, 25]}, #2
    {"Breda" : [0, 2, 25, 26, 6, 4]}, #3
    {"Antwerpen" : [0, 3, 6, 5]}, #4
    {"Hainaut" : [4, 6]}, #5
    {"Liege" : [5, 4, 3, 26, 7]}, #6
    {"Luxemberg" : [6, 26, 28, 32]}, #7
    #Northern Germany
    {"Bremen" : [1, 21, 22, 9]}, #8
    {"Verden" : [8, 22, 16, 10]}, #9
    {"Holstein" : [9, 16, 11]}, #10
    {"Lübeck" : [10, 16, 12]}, #11
    {"Mecklenburg" : [11, 16, 20, 19, 18, 13]}, #12
    {"Vorpommern" : [12, 18, 14, 15]}, #13
    {"Stettin" : [13, 18, 17, 15]}, #14
    {"Hinterpommern" : [13, 14, 17]}, #15
    {"Luneburg" : [10, 11, 12, 20, 23, 22, 9]}, #16
    {"Neumark" : [15, 14, 18, 64, 67]}, #17
    {"Berlin" : [64, 19, 12, 13, 14, 17]}, #18
    {"Mittelmark" : [64, 54, 61, 20, 12, 18]}, #19
    {"Altmark" : [12, 19, 54, 23, 16]}, #20
    #West Germany
    {"Münster" : [1, 2, 25, 24, 22, 8]}, #21
    {"Hanover" : [8, 9, 16, 23, 24, 21]}, #22
    {"Brunswick" : [22, 16, 20, 54, 55, 29, 24]}, #23
    {"Westphalia" : [21, 22, 23, 29, 25]}, #24
    {"Cleve" : [2, 3, 26, 27, 29, 24, 21]}, #25
    {"Aachen" : [7, 6, 3, 25, 27, 28]}, #26
    {"Cologne" : [26, 25, 28]}, #27
    {"Trier" : [7, 26, 27, 25, 29, 30, 31, 32]}, #28
    {"Hesse" : [28, 25, 24, 23, 55, 56, 30]}, #29
    {"Mainz" : [28, 29, 56, 31, 57]}, #30
    {"Palatinate" : [32, 28, 30, 57, 33, 40, 41]}, #31
    #South Germany + Austria + Switzerland
    {"Lorraine" : [7, 28, 31, 33, 34, 39]}, #32
    {"Alsace" : [32, 31, 40, 39]}, #33
    {"Burgundy" : [32, 35, 36, 39]}, #34
    {"Geneva" : [34, 36, 37]}, #35
    {"Bern" : [35, 34, 39, 37]}, #36
    {"Zürich" : [35, 36, 39, 41, 42, 38]}, #37
    {"Chur" : [37, 42, 48]}, #38
    {"Sundgau" : [32, 34, 33, 40, 41, 37, 36]}, #39
    {"Baden" : [31, 39, 33, 41]}, #40
    {"Wurttemberg" : [39, 40, 31, 57, 37, 42, 43, 44]}, #41
    {"Bregenz" : [38, 37, 41, 43, 48]}, #42
    {"Augsburg" : [42, 41, 44, 46, 48]}, #43
    {"Ingolstadt" : [41, 42, 46, 45, 59, 58, 57]}, #44
    {"Landshut" : [47, 46, 44, 59, 63, 69, 53]}, #45
    {"Munich" : [43, 44, 45, 47, 48, 49]}, #46
    {"Salzburg" : [46, 49, 50, 53, 45]}, #47
    {"Tirol" : [38, 42, 43, 46, 49]}, #48
    {"Oberkarten" : [48, 46, 47, 50, 51]}, #49
    {"Graz" : [51, 49, 47, 53, 52]}, #50
    {"Slovenia" : [49, 50]}, #51
    {"Vienna" : [50, 53]}, #52
    {"Manhartsberg" : [50, 52, 47, 45, 69, 65]}, #53
    #East Germany + Bohemia
    {"Magdeburg" : [23, 20, 19, 61, 62, 55]}, #54
    {"Erfurt" : [23, 54, 62, 60, 58, 56, 29]}, #55
    {"Wurzburg" : [55, 57, 58, 29, 30]}, #56
    {"Ansbach" : [30, 31, 41, 44, 58, 56]}, #57
    {"Nürnburg" : [55, 60, 56, 57, 44, 45, 63]}, #58
    {"Oberpfalz" : [58, 44, 45, 63]}, #59
    {"Weimar" : [55, 62, 63, 59, 58]}, #60
    {"Mittenburg" : [62, 54, 19, 64]}, #61
    {"Saxony" : [55, 60, 54, 61, 64, 63]}, #62
    {"Erzgebirge" : [45, 59, 58, 60, 62, 64, 66, 69]}, #63
    {"Lusatia" : [63, 66, 67, 17, 18, 19, 61, 62]}, #64
    {"Moravia" : [53, 69, 66, 67, 68]}, #65
    {"Prague" : [69, 63, 64, 67, 65]}, #66
    {"Glogow" : [17, 64, 66, 65, 68]}, #67
    {"Opole" : [67, 65]}, #68
    {"Budejovice" : [63, 66, 65, 53, 45]}, #69
]

#province owners
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
]

#list of all countries and their data
#Data includes:
#country name
#manpower
#ducats
#army size
#provinces are handled in the provinces list
country_data = []
reset_country_data_list()


#indicates how many turns have passed, each turn is a month. Starts jan 1515 (well well well)
year = 1515
#0 = january, 11 = december
month = 0


#sets country_data to the starting values:
def reset_country_data_list():
    #resets country_data
    country_data = []
    #loops over each country
    for c in countries:
        #first adds the name
        data = [c]
        
        country_data.append(data)
        



#sets up a new game
def reset_game():
    pass
