
def get_espn_score(south, east, midwest, west, round_counter):
    num_correct = 0
    espn_score = 0
    match round_counter:
        case 0:
            #south region round of 32
            if south[0].name == "Alabama":
                espn_score += 10
            if south[1].name == "Maryland":
                espn_score += 10
            if south[2].name == "San Diego State":
                espn_score += 10
            if south[3].name == "Furman":
                espn_score += 10
            if south[4].name == "Creighton":
                espn_score += 10
            if south[5].name == "Baylor":
                espn_score += 10
            if south[6].name == "Missouri":
                espn_score += 10
            if south[7].name == "Princeton":
                num_correct+=1
                espn_score += 10
                
            #east region round of 32    
            if east[0].name == "Fairleigh Dickinson":
                espn_score += 10
            if east[1].name == "Florida Atlantic":
                espn_score += 10
            if east[2].name == "Duke":
                espn_score += 10
            if east[3].name == "Tennessee":
                espn_score += 10
            if east[4].name == "Kentucky":
                espn_score += 10
            if east[5].name == "Kansas State":
                espn_score += 10
            if east[6].name == "Michigan State":
                espn_score += 10
            if east[7].name == "Marquette":
                espn_score += 10
                
            #midwest region round of 32
            if midwest[0].name == "Houston":
                espn_score += 10
            if midwest[1].name == "Auburn":
                espn_score += 10
            if midwest[2].name == "Miami":
                espn_score += 10
            if midwest[3].name == "Indiana":
                espn_score += 10
            if midwest[4].name == "Pittsburgh":
                espn_score += 10
            if midwest[5].name == "Xavier":
                espn_score += 10
            if midwest[6].name == "Penn State":
                espn_score += 10
            if midwest[7].name == "Texas":
                espn_score += 10
            
            #west region round of 32
            if west[0].name == "Kansas":
                espn_score += 10
            if west[1].name == "Arkansas":
                espn_score += 10
            if west[2].name == "Saint Mary's":
                espn_score += 10
            if west[3].name == "UConn":
                espn_score += 10
            if west[4].name == "TCU":
                espn_score += 10
            if west[5].name == "Gonzaga":
                espn_score += 10
            if west[6].name == "Northwestern":
                espn_score += 10
            if west[7].name == "UCLA":
                espn_score += 10
                
        case 1:
            #south region sweet 16
            if south[0].name == "Alabama":
                espn_score += 20
            if south[1].name == "San Diego State":
                espn_score += 20
            if south[2].name == "Creighton":
                espn_score += 20
            if south[3].name == "Princeton":
                espn_score += 20
                
            #east region sweet 16
            if east[0].name == "Florida Atlantic":
                espn_score += 20
            if east[1].name == "Tennessee":
                espn_score += 20
            if east[2].name == "Kansas State":
                espn_score += 20
            if east[3].name == "Michigan State":
                espn_score += 20
                
            #midwest region sweet 16
            if midwest[0].name == "Houston":
                espn_score += 20
            if midwest[1].name == "Miami":
                espn_score += 20
            if midwest[2].name == "Xavier":
                espn_score += 20
            if midwest[3].name == "Texas":
                espn_score += 20
            
            #west region sweet 16    
            if west[0].name == "Arkansas":
                espn_score += 20
            if west[1].name == "UConn":
                espn_score += 20
            if west[2].name == "Gonzaga":
                espn_score += 20
            if west[3].name == "UCLA":
                espn_score += 20
        case 2:
            #east region elite 8
            if east[0].name == "Florida Atlantic":
                espn_score += 40
            if east[1].name == "Kansas State":
                espn_score += 40
            
            #west region elite 8
            if west[0].name == "UConn":
                espn_score += 40
            if west[1].name == "Gonzaga":
                espn_score += 40
            
            #midwest region elite 8
            if midwest[0].name == "Miami":
                espn_score += 40
            if midwest[1].name == "Texas":
                espn_score += 40
            
            #south region elite 8
            if south[0].name == "San Diego State":
                espn_score += 40
            if south[1].name == "Creighton":
                espn_score += 40
            
    return espn_score