import random
import numpy

def get_result(team1, team2, round_counter):
    matchup = [team1, team2]
    
    strength1 = calcStrength(team1, team2)
    #print(strength1)
    strength2 = calcStrength(team2, team1)
    #print(strength2)
    totalStrength = strength1 + strength2
    prob1 = strength1 / totalStrength
    prob2 = strength2 / totalStrength
    if prob1<0:
        print(team1.name)
    if prob2<0:
        print(team2.name)
    print(team1.name + ": " + str(prob1))
    return matchup[numpy.random.choice(numpy.arange(0,2), p=[prob1, prob2])]
    
    #round of 64
    if team1.seed == 1 and team2.seed == 16:
        return matchup[numpy.random.choice(numpy.arange(0,2), p=[0.9872, 0.0128])]
    elif team1.seed == 2 and team2.seed == 15:
        return matchup[numpy.random.choice(numpy.arange(0,2), p=[0.9295, 0.0705])]
    elif team1.seed == 3 and team2.seed == 14:
        return matchup[numpy.random.choice(numpy.arange(0,2), p=[0.8526, 0.1474])]
    elif team1.seed == 4 and team2.seed == 13:
        return matchup[numpy.random.choice(numpy.arange(0,2), p=[0.7885, 0.2115])]
    elif team1.seed == 5 and team2.seed == 12:
        return matchup[numpy.random.choice(numpy.arange(0,2), p=[0.6474, 0.3526])]
    elif team1.seed == 6 and team2.seed == 11:
        return matchup[numpy.random.choice(numpy.arange(0,2), p=[0.61, 0.39])]
    elif team1.seed == 7 and team2.seed == 10:
        return matchup[numpy.random.choice(numpy.arange(0,2), p=[0.61, 0.39])]
    elif team1.seed == 8 and team2.seed == 9:
        return matchup[numpy.random.choice(numpy.arange(0,2), p=[0.49, 0.51])]
    #round of 32
    elif team1.seed == 1 and (team2.seed == 8 or team2.seed == 9):
        return matchup[numpy.random.choice(numpy.arange(0,2), p=[0.86, 0.14])]
    elif team1.seed ==2 and (team2.seed == 7 or team2.seed == 10):
        return matchup[numpy.random.choice(numpy.arange(0,2), p=[0.67, 0.33])]
    elif team1.seed ==3 and (team2.seed == 6 or team2.seed == 11):
        return matchup[numpy.random.choice(numpy.arange(0,2), p=[0.61, 0.39])]
    else:
        '''
        elif abs(team1.seed - team2.seed) > 4:
            if team1.seed < team2.seed:
                return matchup[numpy.random.choice(numpy.arange(0,2), p=[0.75, 0.25])]
            return matchup[numpy.random.choice(numpy.arange(0,2), p=[0.25, 0.75])]
        '''
        #w.append(Team("Omaha", 15, 160, 1.8, 1.100, 59, 1.075, 277, -3.0, 203))
        strength1 = calcStrength(team1, team2)
        #print(strength1)
        strength2 = calcStrength(team2, team1)
        #print(strength2)
        totalStrength = strength1 + strength2
        prob1 = strength1 / totalStrength
        prob2 = strength2 / totalStrength
        if prob1<0:
            print(team1.name)
        if prob2<0:
            print(team2.name)
        print(team1.name + ": " + str(prob1))
        return matchup[numpy.random.choice(numpy.arange(0,2), p=[prob1, prob2])]
        
        
def calcStrength(team, opponent):
    # s.append(Team("Michigan",5, 23, 7.0, 1.072, 97, 0.975, 41, 12.4, 19))
    # s.append(Team("UC San Diego", 12, 35, 15.1, 1.131, 23, 0.912, 4, 0.2, 118))
    
    if team.sos > opponent.sos:
        strength = (50/team.net) + (team.avg_margin/5) + ((team.sos-opponent.sos)/1.5)
    else:
        strength = (50/team.net) + (team.avg_margin/5)
    
    if team.off_efficiency_rank <= 25 and team.off_efficiency_rank <= 25:
        strength += 5
    elif team.off_efficiency_rank <= 40 and team.off_efficiency_rank <= 40:
        strength +=3
    elif team.off_efficiency_rank <= 50 and team.off_efficiency_rank <= 50:
        strength +=1

    if team.three_point_percent >= .380:
        strength += 1
    elif team.three_point_percent >= .370:
        strength +=.75
    elif team.three_point_percent >= .360:
        strength +=.50
    elif team.three_point_percent >= .350:
        strength +=.25
    if team.three_point_percent < .320:
        strength -=.5
    
    
    if team.seed == 1:
        strength +=8
    if team.seed ==2:
        strength+=4
    
    return strength
    