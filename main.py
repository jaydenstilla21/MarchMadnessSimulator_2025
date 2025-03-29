from teams import *
from result import *
from check_accuracy import *
from espn_score import *
import random
import numpy

'''
south = create_south()
east = create_east()
midwest = create_midwest()
west = create_west()
final_four = []
'''

def most_common(lst):
    return max(set(lst), key=lst.count)

def create_champs_dict(champs_list, num_sims):
    champ_list_unique = set(champs_list)
    champs_dict = {}
    for team in champ_list_unique:
        #champ_percent = int(100 * (champs_list.count(team) / num_sims))
        champs_dict[team] = champs_list.count(team)
    return champs_dict

def sim_round(region, round_counter):
    next_round = []
    for i in range(0,len(region)-1,2):
        team1 = region[i]
        team2 = region[i+1]
        matchup_list = [team1, team2]
        winner = get_result(team1, team2, round_counter)
        next_round.append(winner)
        matchup_list.remove(winner)
    round_counter = round_counter +1
    return next_round
    
    
def sim_round_loud(region, round_counter):
    match round_counter:
        case 0:
            print("ROUND OF 64")
        case 1:
            print("ROUND OF 32")
        case 2:
            print("SWEET SIXTEEN")
        case 3:
            print("ELITE EIGHT")
        case 4:
            print("FINAL FOUR")
        case _:
            pass
    next_round = []
    for i in range(0,len(region)-1,2):
        team1 = region[i]
        team2 = region[i+1]
        matchup_list = [team1, team2]
        winner = get_result(team1, team2, round_counter)
        next_round.append(winner)
        matchup_list.remove(winner)
        
        if winner.seed > matchup_list[0].seed:
            print(winner.name + " beats " + matchup_list[0].name + " (upset)")
        else:
            print(winner.name + " beats " + matchup_list[0].name)
        
    round_counter = round_counter +1
    print()
    return next_round
    
correct_list = []
champs_list = []
champ_matchup = []
champion = Team("x" ,1,1, 10.0, 0.0, 0, 0.0, 0, 0.0, 0, .000, 0 )
espn_score_list = []

round_selector = int(input("Enter round you want to start at: "))

num_sims = int(input("Enter number of simulations: "))
for q in range(0,num_sims):
    if round_selector == 3:
        south = create_south_elite8()
        east = create_east_elite8()
        midwest = create_midwest_elite8()
        west = create_west_elite8()
    else:
        south = create_south()
        east = create_east()
        midwest = create_midwest()
        west = create_west()

    #round_counter = 0
    round_counter = round_selector
    num_correct = 0
    espn_score = 0
    while len(south) > 1:
        if num_sims == 1:
            south = sim_round_loud(south, round_counter)
            east = sim_round_loud(east, 5)
            midwest = sim_round_loud(midwest, 5)
            west = sim_round_loud(west, 5)
        else:
            south = sim_round(south, round_counter)
            east = sim_round(east, 5)
            midwest = sim_round(midwest, 5)
            west = sim_round(west, 5)
        if round_counter <=2:
            num_correct += check_correct(south, east, midwest, west, champ_matchup, champion, round_counter)
        espn_score += get_espn_score(south, east, midwest, west, round_counter)
        round_counter = round_counter+1
        if len(south)==1:
            final_four = [south[0], west[0], east[0], midwest[0]]
            if num_sims == 1:
                final_four = sim_round_loud(final_four, round_counter)
                num_correct += check_correct(south, east, midwest, west, final_four, champion, 4)
                final_four = sim_round_loud(final_four, 5)
                num_correct += check_correct(south, east, midwest, west, champ_matchup, final_four[0], 5)
            else:
                final_four = sim_round(final_four, round_counter)
                final_four = sim_round(final_four, 5)
       
    champion = final_four[0]
    #num_correct = int(round(100 * round(num_correct/60, 2), 0))
    num_correct = int(round(100 * round(num_correct/56, 2), 0))
    
    correct_list.append(num_correct)
    champs_list.append(champion.name)
    espn_score_list.append(espn_score)
    print(champion.name + " has won the national championship as the " + str(champion.seed) + " seed!")
    #print("The percent of games correctly predicted is " + str(num_correct) + "%")

correct_avg = int(round(sum(correct_list)/len(correct_list), 0))
espn_score_avg = int(round((sum(espn_score_list)/len(espn_score_list))/10)) * 10
#most_champs = most_common(champs_list)
#num_most_champs = champs_list.count(most_champs)
#most_champs_percent = int(100*(num_most_champs/num_sims))

champs_dict = create_champs_dict(champs_list, num_sims)


#print("Out of " + str(num_sims) + " simulations the highest ESPN Tournament Challenge Score was " + str(max(espn_score_list)))
#print("Out of " + str(num_sims) + " simulations the average ESPN Tournament Challenge Score was " + str(espn_score_avg))
print("Out of " + str(num_sims) + " simulations the highest percent of games correct in a single bracket was "\
+ str(max(correct_list)) + "%")
#print("Out of " + str(num_sims) + " simulations the average percent of game correct was " + str(correct_avg) + "%")
for key, value in sorted(champs_dict.items(), key=lambda item: item[1]):
    print(f"{key}: {value}")
#print("Out of " + str(num_sims) + " simulations the most common national champion was " + str(most_champs) + " (" + str(most_champs_percent) + "%)")

    