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

#names of countries you can play
availiable_countries = []
#names of all countries that exist in the game
countries = [
    "Austria",
    "Bohemia",
    "Switzerland",
    "Brandenburg",
    "Saxony",
    "Bavaria",
    "Pomerania",
    "Colonge",
    "Trier",
    "Palatinate",
    "Mainz",
    "Savoy",
    "Milan",
    "Genoa",
]
#list of all countries and their data
#Data includes:
#country name
#country id
#country territory
#manpower
#ducats
#army size
#whether they are a player or not

country_data = []

#indicates how many turns have passed, each turn is a month. Starts jan 1515 (well well well)
year = 1515
#0 = january, 11 = december
month = 0



#sets up a new game
def reset_game():
    pass

    
    



