#!python3

'''
Create a program to iterate through the games and determine the win loss record 
for each time

Create a dictionary for each team and store their number of wins, games played,
goals for and goals against.  A dictionary template has been prepped for you to 
use, although you can probably build one faster using iteration or list comprehension

Note that in the list of "games", the first entry has been formatted nicely to help
you see what the contents of the entry is.  You can see that in the data for the
first game, BC played YT, and the game was a tie, 0-0
'''

teams = ['AB','BC','MN','SK','ON','QC','PE','NS','NB','NL','YT','NT','NU'] #a simple list
games = [ #a list of dictionaries
    {
        'home': 'BC', 
        'homeScore': 0, 
        'away': 'YT', 
        'awayScore': 0
    }, 
    #{'home': 'NU', 'homeScore': 2, 'away': 'NS', 'awayScore': 2}, {'home': 'PE', 'homeScore': 0, 'away': 'YT', 'awayScore': 2}, {'home': 'NU', 'homeScore': 1, 'away': 'YT', 'awayScore': 3}, {'home': 'NT', 'homeScore': 3, 'away': 'ON', 'awayScore': 1}, {'home': 'NU', 'homeScore': 2, 'away': 'ON', 'awayScore': 1}, {'home': 'BC', 'homeScore': 0, 'away': 'SK', 'awayScore': 3}, {'home': 'SK', 'homeScore': 2, 'away': 'NU', 'awayScore': 0}, {'home': 'MN', 'homeScore': 1, 'away': 'NS', 'awayScore': 3}, {'home': 'ON', 'homeScore': 0, 'away': 'AB', 'awayScore': 1}, {'home': 'MN', 'homeScore': 3, 'away': 'NU', 'awayScore': 2}, {'home': 'NB', 'homeScore': 0, 'away': 'NL', 'awayScore': 1}, {'home': 'BC', 'homeScore': 3, 'away': 'NT', 'awayScore': 2}, {'home': 'ON', 'homeScore': 1, 'away': 'NU', 'awayScore': 3}, {'home': 'NS', 'homeScore': 1, 'away': 'ON', 'awayScore': 1}, {'home': 'NL', 'homeScore': 3, 'away': 'BC', 'awayScore': 1}, {'home': 'NL', 'homeScore': 2, 'away': 'NT', 'awayScore': 1}, {'home': 'NU', 'homeScore': 2, 'away': 'AB', 'awayScore': 3}, {'home': 'MN', 'homeScore': 1, 'away': 'YT', 'awayScore': 1}, {'home': 'BC', 'homeScore': 1, 'away': 'PE', 'awayScore': 0}, {'home': 'QC', 'homeScore': 1, 'away': 'NL', 'awayScore': 0}, {'home': 'NL', 'homeScore': 1, 'away': 'NT', 'awayScore': 3}, {'home': 'BC', 'homeScore': 1, 'away': 'ON', 'awayScore': 0}, {'home': 'SK', 'homeScore': 0, 'away': 'AB', 'awayScore': 1}, {'home': 'YT', 'homeScore': 2, 'away': 'QC', 'awayScore': 2}, {'home': 'NT', 'homeScore': 2, 'away': 'NU', 'awayScore': 3}, {'home': 'NB', 'homeScore': 2, 'away': 'NT', 'awayScore': 2}, {'home': 'PE', 'homeScore': 2, 'away': 'BC', 'awayScore': 0}, {'home': 'PE', 'homeScore': 2, 'away': 'NB', 'awayScore': 0}, {'home': 'PE', 'homeScore': 0, 'away': 'YT', 'awayScore': 0}, {'home': 'NB', 'homeScore': 3, 'away': 'MN', 'awayScore': 2}, {'home': 'AB', 'homeScore': 0, 'away': 'NL', 'awayScore': 2}, {'home': 'QC', 'homeScore': 2, 'away': 'NL', 'awayScore': 1}, {'home': 'SK', 'homeScore': 0, 'away': 'MN', 'awayScore': 0}, {'home': 'QC', 'homeScore': 2, 'away': 'BC', 'awayScore': 3}, {'home': 'NU', 'homeScore': 2, 'away': 'AB', 'awayScore': 2}, {'home': 'NS', 'homeScore': 3, 'away': 'AB', 'awayScore': 3}, {'home': 'QC', 'homeScore': 1, 'away': 'NT', 'awayScore': 1}, {'home': 'SK', 'homeScore': 3, 'away': 'AB', 'awayScore': 0}, {'home': 'NL', 'homeScore': 3, 'away': 'QC', 'awayScore': 1}, {'home': 'NL', 'homeScore': 2, 'away': 'SK', 'awayScore': 1}, {'home': 'YT', 'homeScore': 1, 'away': 'BC', 'awayScore': 3}, {'home': 'NL', 'homeScore': 2, 'away': 'PE', 'awayScore': 2}, {'home': 'YT', 'homeScore': 1, 'away': 'NL', 'awayScore': 1}, {'home': 'NS', 'homeScore': 0, 'away': 'QC', 'awayScore': 1}, {'home': 'BC', 'homeScore': 1, 'away': 'NB', 'awayScore': 3}, {'home': 'NL', 'homeScore': 3, 'away': 'NU', 'awayScore': 1}, {'home': 'QC', 'homeScore': 0, 'away': 'SK', 'awayScore': 0}, {'home': 'NS', 'homeScore': 0, 'away': 'SK', 'awayScore': 0}, {'home': 'AB', 'homeScore': 1, 'away': 'NT', 'awayScore': 2}, {'home': 'YT', 'homeScore': 2, 'away': 'QC', 'awayScore': 2}, {'home': 'YT', 'homeScore': 1, 'away': 'NB', 'awayScore': 3}, {'home': 'NT', 'homeScore': 0, 'away': 'QC', 'awayScore': 2}, {'home': 'ON', 'homeScore': 2, 'away': 'BC', 'awayScore': 2}, {'home': 'BC', 'homeScore': 0, 'away': 'ON', 'awayScore': 1}, {'home': 'MN', 'homeScore': 1, 'away': 'ON', 'awayScore': 3}, {'home': 'SK', 'homeScore': 2, 'away': 'NU', 'awayScore': 1}, {'home': 'MN', 'homeScore': 3, 'away': 'PE', 'awayScore': 1}, {'home': 'NU', 'homeScore': 2, 'away': 'YT', 'awayScore': 3}, {'home': 'AB', 'homeScore': 0, 'away': 'NT', 'awayScore': 0}
    {
        'home': 'NU', 
        'homeScore': 2, 
        'away': 'NS', 
        'awayScore': 2
    },
    {
        'home': 'PE', 
        'homeScore': 0, 
        'away': 'YT', 
        'awayScore': 2
    },
    {
        'home': 'BC', 
        'homeScore': 0, 
        'away': 'MN', 
        'awayScore': 0
    },
    {
        'home': 'BC', 
        'homeScore': 2, 
        'away': 'SK', 
        'awayScore': 0
    },
    {
        'home': 'BC', 
        'homeScore': 1, 
        'away': 'ON', 
        'awayScore': 0
    },
    {
        'home': 'BC', 
        'homeScore': 0, 
        'away': 'QC', 
        'awayScore': 0
    },
    {
        'home': 'BC', 
        'homeScore': 0, 
        'away': 'PE', 
        'awayScore': 0
    },
    {
        'home': 'BC', 
        'homeScore': 3, 
        'away': 'NS', 
        'awayScore': 0
    },
    {
        'home': 'BC', 
        'homeScore': 0, 
        'away': 'NB', 
        'awayScore': 0
    },
    {
        'home': 'BC', 
        'homeScore': 4, 
        'away': 'NL', 
        'awayScore': 0
    },
    {
        'home': 'BC', 
        'homeScore': 0, 
        'away': 'YT', 
        'awayScore': 0
    },
    {
        'home': 'BC', 
        'homeScore': 5, 
        'away': 'NT', 
        'awayScore': 0
    },
    {
        'home': 'BC', 
        'homeScore': 0, 
        'away': 'NU', 
        'awayScore': 0
    },
    ]
teamData = { #a nested dictionary contains a key (team), and a value, which is a dictionary of a game data 
    
    'AB' : {
        'gamesPlayed' : 0,
        'wins' : 0,
        'losses' : 0,
        'ties' : 0,
        'goalsFor' : 0,
        'goalsAgainst' : 0
    },
    'BC' : {},
    'MN' : {},'SK' : {},'ON' : {},'QC' : {},'PE' : {},'NS' : {},'NB' : {},'NL' : {},'YT' : {},'NT' : {},'NU' : {}
}

#def main(): 
for team in teams: #iterate each team, then nest iterate each game
        gamesPlayed = 0
        wins = 0
        losses = 0
        ties = 0
        goalsFor = 0
        goalsAgainst = 0
        #print (team)
        for game in games: #iterate each game for this team
             
            if (game['home'] == team ) :
                 
                if (game['homeScore'] > game['awayScore']):
                    wins = wins + 1
                if (game['homeScore'] < game['awayScore']):  
                    losses = losses +1
                goalsFor = game['homeScore'] + 1    
                gamesPlayed = gamesPlayed + 1  
               
                
                
            if (game['away'] == team ) :
                if (game['homeScore'] < game['awayScore']):
                    wins = wins + 1
                if (game['homeScore'] > game['awayScore']):  
                    losses = losses + 1
                goalsAgainst = game['awayScore'] + 1    
                gamesPlayed = gamesPlayed + 1
                
            
                
            dict_for_this_team = {} # build up dictionay for this team
            dict_for_this_team["gamesPlayed"] = gamesPlayed  #key value pair
            dict_for_this_team["wins"] = wins #key value pair
            dict_for_this_team["losses"] = losses #key value pair
            dict_for_this_team["ties"] = ties #key value pair
            dict_for_this_team["goalsFor"] = goalsFor #key value pair
            dict_for_this_team["goalsAgainst"] = goalsAgainst #key value pair
           
         
         
        # actual append to the list of dictionaries that we are building.
        teamData[team].update(dict_for_this_team)
       
        
    
def tests():
    assert teamData['BC']['gamesPlayed'] == 12
    assert teamData['BC']['wins'] == 5 
    
if __name__ == "__main__":
    tests()    



