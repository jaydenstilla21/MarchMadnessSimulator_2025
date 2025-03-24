class Team:
  def __init__(self, name, seed, net, avg_margin, off_efficiency, 
               off_efficiency_rank, def_efficiency, def_efficiency_rank, 
               sos, sos_rank, three_point_percent, three_point_percent_rank):
    self.name = name
    self.seed = seed
    self.net = net
    self.avg_margin = avg_margin
    self.off_efficiency = off_efficiency
    self.off_efficiency_rank = off_efficiency_rank
    self.def_efficiency = def_efficiency
    self.def_efficiency_rank = def_efficiency_rank
    self.sos = sos
    self.sos_rank = sos_rank
    self.three_point_percent = three_point_percent
    self.three_point_percent_rank = three_point_percent_rank
    
def create_south():
    s = []
    s.append(Team("Auburn",1, 2, 14.2, 1.182, 3, 0.981, 53, 16.4, 1, .368, 40))
    s.append(Team("Alabama State", 16, 274, 0, 1.014, 231, 1.017, 126, -6.9, 330, .329, 222))
    s.append(Team("Louisville",8, 24, 9.7, 1.112, 42, 0.975, 40, 10.1, 41, .330, 216))
    s.append(Team("Creighton", 9, 38, 5.7, 1.082, 81, 1.000, 86, 10.7, 36, .339, 177))
    s.append(Team("Michigan",5, 23, 7.0, 1.072, 97, 0.975, 41, 12.4, 19, .334, 195))
    s.append(Team("UC San Diego", 12, 35, 15.1, 1.131, 23, 0.912, 4, 0.2, 118, .365, 57))
    s.append(Team("Texas A&M",4, 18, 6.4, 1.058, 128, 0.968, 31, 13.1, 12, .311, 317))
    s.append(Team("Yale", 13, 72, 10.4, 1.148, 13, 1.000, 87, -0.1, 128, .385, 9))
    s.append(Team("Ole Miss",6, 28, 5.5, 1.076, 88, 1.000, 84, 12.8, 15, .341, 156))
    s.append(Team("North Carolina", 11, 36, 6.4, 1.113, 41, 1.025, 151, 11.7, 24, .353, 91))
    s.append(Team("Iowa State",3, 9, 12.3, 1.115, 40, 0.945, 14, 13.0, 13, .358, 68))
    s.append(Team("Lipscomb", 14, 84, 9.9, 1.130, 25, 0.986, 62, -2.3, 176, .367, 46))
    s.append(Team("Marquette",7, 26, 8.3, 1.092, 69, 0.973, 37, 11.6, 26, .325, 245))
    s.append(Team("New Mexico", 10, 42, 9.2, 1.059, 127, 0.937, 13, 6.1, 73, .341, 163))
    s.append(Team("Michigan State",2,11, 10.9, 1.102, 56, 0.948, 15, 12.4, 18, .308, 327))
    s.append(Team("Bryant", 15, 141, 5.8, 1.065, 113, 0.988, 65, -3.4, 225, .334, 198))
    return s
    
def create_east():
    e = []
    e.append(Team("Duke",1, 1, 20.8, 1.211, 1, 0.907, 3, 12.9, 14, .377, 20))
    e.append(Team("Mount St Marys", 16, 236, 0, 0.993, 278, 1.001, 88, -5.2, 288, .349, 122))
    e.append(Team("Mississippi State",8,34, 5.6, 1.106, 49, 1.028, 163, 12.0, 22, .314, 298))
    e.append(Team("Baylor", 9,30, 5.8, 1.107, 47, 1.021, 145, 13.4, 9, .347, 130))
    e.append(Team("Oregon",5,29, 5.3, 1.074, 92, 0.999, 83, 11.5, 28, .340, 170))
    e.append(Team("Liberty", 12,60, 9.6, 1.094, 66, 0.953, 19, 0.0, 122, .395, 5))
    e.append(Team("Arizona",4,12, 9.3, 1.126, 30, 0.998, 81, 14.6, 3, .324, 247))
    e.append(Team("Akron", 13,91, 8.1, 1.126, 32, 1.017, 129, -2.4, 178, .366, 49))
    e.append(Team("BYU",6, 25, 10.1, 1.143, 16, 1.000, 85, 11.6, 27, .371, 33))
    e.append(Team("VCU", 11, 31, 13.8, 1.117, 39, 0.914, 5, 3.5, 92, .335, 189))
    e.append(Team("Wisconsin",3, 15, 9.3, 1.131, 22, 0.999, 82, 12.4, 17, .349, 121))
    e.append(Team("Montana", 14, 143, 0.8, 1.089, 73, 1.078, 284, -2.8, 193, .365, 55))
    e.append(Team("Saint Mary's",7, 21, 12.0, 1.118, 38, 0.935, 11, 6.3, 71, .327, 230))
    e.append(Team("Vanderbilt", 10, 48, 4.8, 1.105, 53, 1.037, 175, 10.0, 43, .325, 239))
    e.append(Team("Alabama",2, 6, 9.7, 1.156, 9, 1.033, 170, 16.0, 2, .350, 114))
    e.append(Team("Robert Morris", 15, 139, 5.8, 1.074, 93, 0.993, 74, -4.1, 249, .349, 120))
    return e
    
def create_midwest():
    mw = []
    mw.append(Team("Houston",1, 3, 15.7, 1.131, 24, 0.891, 1, 14.3, 5, .398, 4))
    mw.append(Team("SIUE", 16, 216, 2.6, 1.013, 237, 0.975, 39, -7.4, 338, .340, 167))
    mw.append(Team("Gonzaga",8, 8, 17.0, 1.181, 4, 0.950, 17, 8.7, 58, .344, 146))
    mw.append(Team("Georgia", 9, 33, 6.3, 1.073, 95, 0.984, 59, 11.5, 29, .335, 193))
    mw.append(Team("Clemson",5, 22, 10.7, 1.123, 34, 0.966, 28, 8.9, 54, .372, 31))
    mw.append(Team("McNeese", 12, 58, 11.2, 1.118, 37, 0.952, 18, -0.9, 145, .356, 77))
    mw.append(Team("Purdue",4, 19, 6.8, 1.150, 12, 1.049, 209, 13.1, 11, .385, 10))
    mw.append(Team("High Point", 13, 82, 11.2, 1.184, 2, 1.022, 148, -3.1, 209, .366, 51))
    mw.append(Team("Illinois",6, 17, 9.2, 1.125, 33, 1.001, 90, 13.3, 10, .311, 316))
    mw.append(Team("Xavier", 11, 45, 7.2, 1.091, 70, 0.991, 70, 9.5, 50, .388, 6))
    mw.append(Team("Kentucky",3, 14, 7.4, 1.146, 15, 1.046, 201, 14.2, 7, .374, 25))
    mw.append(Team("Troy", 14, 99, 6.5, 1.055, 134, 0.961, 22, -1.0, 149, .303, 339))
    mw.append(Team("UCLA",7, 27, 9.0, 1.103, 54, 0.970, 33, 11.8, 23, .352, 100))
    mw.append(Team("Utah State", 10, 37, 9.3, 1.152, 10, 1.018, 132, 5.4, 83, .358, 69))
    mw.append(Team("Tennessee",2, 5, 11.7, 1.106, 50, 0.932, 9, 14.6, 4, .340, 166))
    mw.append(Team("Wofford", 15, 131, 2.8, 1.100, 58, 1.059, 238, -1.0, 148, .345, 138))
    return mw
    
def create_west():
    w = []
    w.append(Team("Florida",1, 4, 16.2, 1.178, 6, 0.955, 20, 14.3, 6, .355, 84))
    w.append(Team("Norfolk State", 16, 183, 3.9, 1.077, 87, 1.021, 146, -4.6, 273, .313, 306))
    w.append(Team("UConn",8, 32, 9.4, 1.150, 11, 1.011, 107, 10.5, 37, .354, 88))
    w.append(Team("Oklahoma", 9, 43, 4.0, 1.105, 52, 1.049, 207, 11.4, 30, .370, 35))
    w.append(Team("Memphis",5, 49, 6.9, 1.085, 76, 0.992, 72, 6.1, 75, .380, 17))
    w.append(Team("Colorado State", 12, 47, 8.1, 1.101, 57, 0.981, 54, 5.8, 79, .366, 52))
    w.append(Team("Maryland",4, 10, 14.7, 1.127, 29, 0.924, 6, 11.7, 25, .372, 29))
    w.append(Team("Grand Canyon", 13, 92, 8.8, 1.054, 137, 0.935, 12, -1.1, 152, .316, 285))
    w.append(Team("Missouri",6, 16, 10.6, 1.178, 5, 1.030, 165, 12.0, 20, .370, 36))
    w.append(Team("Drake", 11, 56, 9.0, 1.110, 44, 0.965, 26, 0.7, 111, .350, 110))
    w.append(Team("Texas Tech",3, 7, 13.3, 1.172, 7, 0.979, 50, 12.5, 16, .379, 19))
    w.append(Team("UNC Wilmington", 14, 102, 6.8, 1.120, 36, 1.020, 143, -2.8, 196, .330, 212))
    w.append(Team("Kansas",7, 20, 6.9, 1.064, 114, 0.967, 30, 13.7, 8, .352, 102))
    w.append(Team("Arkansas", 10, 40, 5.5, 1.060, 123, 0.984, 60, 11.1, 33, .333, 201))
    w.append(Team("St. John's",2, 13, 12.8, 1.069, 107, 0.895, 2, 10.2, 39, .304, 338))
    w.append(Team("Omaha", 15, 160, 1.8, 1.100, 59, 1.075, 277, -3.0, 203, .367, 44))
    return w
    
    