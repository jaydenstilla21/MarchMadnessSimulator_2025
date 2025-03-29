
def check_correct(south, east, midwest, west, champ_matchup, champion, round_counter):
    num_correct = 0
    espn_score = 0
    match round_counter:
        case 0:
            #south region round of 32
            if south[0].name == "Auburn":
                num_correct += 1
                espn_score += 10
            if south[1].name == "Creighton":
                num_correct += 1
                espn_score += 10
            if south[2].name == "Michigan":
                num_correct+=1
                espn_score += 10
            if south[3].name == "Texas A&M":
                num_correct+=1
                espn_score += 10
            if south[4].name == "Ole Miss":
                num_correct+=1
                espn_score += 10
            if south[5].name == "Iowa State":
                num_correct+=1
                espn_score += 10
            if south[6].name == "New Mexico":
                num_correct+=1
                espn_score += 10
            if south[7].name == "Michigan State":
                num_correct+=1
                espn_score += 10
                
            #east region round of 32    
            if east[0].name == "Duke":
                num_correct += 1
                espn_score += 10
            if east[1].name == "Baylor":
                num_correct += 1
                espn_score += 10
            if east[2].name == "Oregon":
                num_correct+=1
                espn_score += 10
            if east[3].name == "Arizona":
                num_correct+=1
                espn_score += 10
            if east[4].name == "BYU":
                num_correct+=1
                espn_score += 10
            if east[5].name == "Wisconsin":
                num_correct+=1
                espn_score += 10
            if east[6].name == "Saint Mary's":
                num_correct+=1
                espn_score += 10
            if east[7].name == "Alabama":
                num_correct+=1
                espn_score += 10
                
            #midwest region round of 32
            if midwest[0].name == "Houston":
                num_correct += 1
                espn_score += 10
            if midwest[1].name == "Gonzaga":
                num_correct += 1
                espn_score += 10
            if midwest[2].name == "McNeese":
                num_correct+=1
                espn_score += 10
            if midwest[3].name == "Purdue":
                num_correct+=1
                espn_score += 10
            if midwest[4].name == "Illinois":
                num_correct+=1
                espn_score += 10
            if midwest[5].name == "Kentucky":
                num_correct+=1
                espn_score += 10
            if midwest[6].name == "UCLA":
                num_correct+=1
                espn_score += 10
            if midwest[7].name == "Tennessee":
                num_correct+=1
                espn_score += 10
            
            #west region round of 32
            if west[0].name == "Florida":
                num_correct += 1
                espn_score += 10
            if west[1].name == "UConn":
                num_correct += 1
                espn_score += 10
            if west[2].name == "Colorado State":
                num_correct+=1
                espn_score += 10
            if west[3].name == "Maryland":
                num_correct+=1
                espn_score += 10
            if west[4].name == "Drake":
                num_correct+=1
                espn_score += 10
            if west[5].name == "Texas Tech":
                num_correct+=1
                espn_score += 10
            if west[6].name == "Arkansas":
                num_correct+=1
                espn_score += 10
            if west[7].name == "St. John's":
                num_correct+=1
                espn_score += 10
                
        case 1:
            #south region sweet 16
            if south[0].name == "Auburn":
                num_correct += 1
                espn_score += 20
            if south[1].name == "Michigan":
                num_correct+=1
                espn_score += 20
            if south[2].name == "Ole Miss":
                num_correct+=1
                espn_score += 20
            if south[3].name == "Michigan State":
                num_correct+=1
                espn_score += 20
                
            #east region sweet 16
            if east[0].name == "Duke":
                num_correct += 1
                espn_score += 20
            if east[1].name == "Arizona":
                num_correct += 1
                espn_score += 20
            if east[2].name == "BYU":
                num_correct+=1
                espn_score += 20
            if east[3].name == "Alabama":
                num_correct+=1
                espn_score += 20
                
            #midwest region sweet 16
            if midwest[0].name == "Houston":
                num_correct += 1
                espn_score += 20
            if midwest[1].name == "Purdue":
                num_correct += 1
                espn_score += 20
            if midwest[2].name == "Kentucky":
                num_correct+=1
                espn_score += 20
            if midwest[3].name == "Tennessee":
                num_correct+=1
                espn_score += 20
            
            #west region sweet 16    
            if west[0].name == "Florida":
                num_correct += 1
                espn_score += 20
            if west[1].name == "Maryland":
                num_correct += 1
                espn_score += 20
            if west[2].name == "Texas Tech":
                num_correct+=1
                espn_score += 20
            if west[3].name == "Arkansas":
                num_correct+=1
                espn_score += 20
        
        case 2:
            #south region elite 8
            if south[0].name == "Auburn":
                num_correct += 1
                espn_score += 40
            if south[1].name == "Michigan State":
                num_correct += 1
                espn_score += 40
            
            #east region elite 8
            if east[0].name == "Duke":
                num_correct += 1
                espn_score += 40
            if east[1].name == "Alabama":
                num_correct +=1
                espn_score += 40
            
            #midwest region elite 8
            if midwest[0].name == "Houston":
                num_correct +=1
                espn_score += 40
            if midwest[1].name == "Tennessee":
                num_correct +=1
                espn_score += 40
                
            #west region elite 8
            if west[0].name == "Florida":
                num_correct +=1
                espn_score += 40
            if west[1].name == "Texas Tech":
                num_correct +=1
                espn_score += 40
          
        case 3:
            #south region final four
            if south[0].name == "San Diego State":
                num_correct += 1
                espn_score += 80
            
            #east region elite 8
            if east[0].name == "Florida Atlantic":
                num_correct += 1
                espn_score += 80
            
            #midwest region elite 8
            if midwest[0].name == "Miami":
                num_correct +=1
                espn_score += 80
                
            #west region elite 8
            if west[0].name == "Uconn":
                num_correct +=1
                espn_score += 80
        case 4:
            if champ_matchup[1].name == "Uconn":
                print("hh")
                num_correct +=1
                espn_score+=160
            if champ_matchup[0].name == "San Diego State":
                print("hh")
                num_correct +=1
                espn_score+=160
        case 5:
            if champion.name == "Uconn":
                num_correct+=1
                espn_score +=320
    return num_correct