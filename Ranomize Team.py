import random
import time

# Function will check to see if my name is in the player_list and find how FC Bayern has been entered and print that is my team.

def print_random_team(players, teams):
    """ Randomly assign players to the teams and pretty print results """
    # local copy of the lists. Now real lists are safe
    players = players[:]
    teams = teams[:]

    # results
    pairs = []

    # cheat
    print("Randomizing...")
    time.sleep(5)
    for team in teams:
        if team.lower() in pick_list:
            for player in players:
                if player.lower() in tom:
                    # reserve favorite team
                    pairs.append((player, team))
                    players.remove(player)
                    teams.remove(team)
                    # stop iterating over players (tom is found)
                    break
            # stop iteration over teams (Bayern is found)
            break

    # completely normal random
    # shuffle list of teams in place
    random.shuffle(teams)
    # combine them with players and add to results
    pairs.extend(zip(players, teams))

    # and print
    for name, team in pairs:
        print("%s will be %s" % (name, team))
# blank list variables set
player_list = []
team_list = []


# list of possible ways to write out my name or team I want to be be sure entered as lower case
pick_list = ["munich", "fc bayern", "bayern munich", "bayern"]
tom = ["tom", "levo", "tom l", "levin", "thomas levin", "thomas", "tommy"]


# adds players to list. a blank string will escape the loop
def add_players(list_of_players):
	player_name = input("Enter name of player " + str(len(list_of_players)+1) + "(press enter to finish): ")
	list_of_players.append(player_name)
	while player_name != "":
		player_name = input("Enter name of player " + str(len(list_of_players)+1) + "(press enter to finish): ")
		list_of_players.append(player_name)
	list_of_players.remove("")
	print("You have picked " + str(len(list_of_players)) + " players ")
	print(", ".join(list_of_players))
	print("\n")
	return list_of_players


# allows teams to be added. a blank string will escape the loop
def add_teams(list_of_teams):
	team = input("Enter name of team " + str(len(list_of_teams)+1) + "(press enter to finish): ")
	list_of_teams.append(team)
	while team != "":
		team = input("Enter name of team " + str(len(list_of_teams)+1) + "(press enter to finish): ")
		list_of_teams.append(team)
	list_of_teams.remove("")
	return list_of_teams


add_players(player_list)
add_teams(team_list)

# makes a check to see enough teams in the list for players wanting to play.
if len(player_list) <= len(team_list):
    print("You have picked " + str(len(team_list)) + " teams")
    print(", ".join(team_list))
    print("\n")
else:
    print("You have not picked enough teams, pick some more")
    add_teams(team_list)


print_random_team(player_list, team_list)
