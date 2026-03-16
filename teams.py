class Team:
  def __init__(self, name="Unknown", seed=0, net=0, avg_margin=0.0, off_efficiency=0.0, 
               off_efficiency_rank=0, def_efficiency=0.0, def_efficiency_rank=0, 
               sos=0.0, sos_rank=0, three_point_percent=0.0, three_point_percent_rank=0):
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

#South Teams
Florida = Team("Florida",1, 4, 14.8, 1.171, 18, 0.981, 53, 16.4, 1, .368, 40)
Lehigh = Team("Lehigh / Prairie View", 16, 275, 0, 1.033, 232, 1.017, 126, -6.9, 330, .329, 222)
Clemson = Team("Clemson",8, 34, 7.4, 1.103, 87, 0.975, 40, 10.1, 41, .330, 216)
Iowa = Team("Iowa", 9, 27, 9.2, 1.160, 29, 1.000, 86, 10.7, 36, .339, 177)
Vanderbilt = Team("Vanderbilt",5, 13, 11.1, 1.180, 11, 0.975, 41, 12.4, 19, .334, 195)
McNeese = Team("McNeese", 12, 56, 9.8, 1.111, 75, 0.912, 4, 0.2, 118, .365, 57)
Nebraska = Team("Nebraska",4, 14, 11.1, 1.119, 64, 0.968, 31, 13.1, 12, .311, 317)
Troy = Team("Troy", 13, 125, 3.8, 1.092, 105, 1.000, 87, -0.1, 128, .385, 9)
NorthCarolina = Team("North Carolina",6, 24, 8.5, 1.127, 58, 1.000, 84, 12.8, 15, .341, 156)
Vcu = Team("VCU", 11, 43, 10.1, 1.146, 43, 1.025, 151, 11.7, 24, .353, 91)
Illinois = Team("Illinois",3, 8, 14.6, 1.232, 1, 0.945, 14, 13.0, 13, .358, 68)
Penn = Team("Penn", 14, 139, 1.2, 1.050, 198, 0.986, 62, -2.3, 176, .367, 46)
SaintMarys = Team("Saint Mary's",7, 22, 12.3, 1.143, 45, 0.973, 37, 11.6, 26, .325, 245)
TexasAM = Team("Texas A&M", 10, 44, 8.2, 1.155, 33, 0.937, 13, 6.1, 73, .341, 163)
Houston = Team("Houston",2, 5, 14.3, 1.148, 42, 0.948, 15, 12.4, 18, .308, 327)
Idaho = Team("Idaho", 15, 145, 2.7, 1.073, 142, 0.988, 65, -3.4, 225, .334, 198)

#East Teams
Duke = Team("Duke",1, 1, 19.1, 1.198, 4, 0.907, 3, 12.9, 14, .377, 20)
Siena = Team("Siena", 16, 183, 4.9, 1.071, 145, 1.001, 88, -5.2, 288, .349, 122)
OhioState = Team("Ohio State",8,29, 7.0, 1.158, 32, 1.028, 163, 12.0, 22, .314, 298)
Tcu = Team("TCU", 9,39, 6.2, 1.083, 121, 1.021, 145, 13.4, 9, .347, 130)
StJohns = Team("St. John's",5,16, 11.6, 1.110, 76, 0.999, 83, 11.5, 28, .340, 170)
NorthernIowa = Team("Northern Iowa", 12, 72, 7.0, 1.058, 173, 0.953, 19, 0.0, 122, .395, 5)
Kansas = Team("Kansas",4, 21, 6.2, 1.074, 135, 0.998, 81, 14.6, 3, .324, 247)
CalBaptist = Team("Cal Baptist", 13,98, 5.5, 1.044, 211, 1.017, 129, -2.4, 178, .366, 49)
Louisville = Team("Louisville",6, 17, 12.6, 1.171, 19, 1.000, 85, 11.6, 27, .371, 33)
SouthFlorida = Team("South Florida", 11, 45, 10.7, 1.128, 56, 0.914, 5, 3.5, 92, .335, 189)
MichiganState = Team("Michigan State",3, 11, 10.5, 1.148, 40, 0.999, 82, 12.4, 17, .349, 121)
NorthDakotaState = Team("North Dakota State", 14, 114, 8.3, 1.120, 63, 1.078, 284, -2.8, 193, .365, 55)
Ucla = Team("UCLA",7, 30, 6.7, 1.144, 44, 0.935, 11, 6.3, 71, .327, 230)
Ucf = Team("UCF", 10, 51, 2.5, 1.113, 74, 1.037, 175, 10.0, 43, .325, 239)
UConn = Team("UConn",2, 10, 12.4, 1.134, 50, 1.033, 170, 16.0, 2, .350, 114)
Furman = Team("Furman", 15, 186, 2.9, 1.091, 110, 0.993, 74, -4.1, 249, .349, 120)

#Midwest Teams
Michigan = Team("Michigan",1, 2, 17.6, 1.183, 8, 0.891, 1, 14.3, 5, .398, 4)
Howard = Team("Howard / UMBC", 16, 203, 7.2, 1.045, 204, 0.975, 39, -7.4, 338, .340, 167)
Georgia = Team("Georgia",8, 33, 10.7, 1.173, 16, 0.950, 17, 8.7, 58, .344, 146)
SaintLouis = Team("Saint Louis", 9, 31, 15.8, 1.177, 15, 0.984, 59, 11.5, 29, .335, 193)
TexasTech = Team("Texas Tech",5, 19, 7.8, 1.154, 34, 0.966, 28, 8.9, 54, .372, 31)
Akron = Team("Akron", 12, 54, 12.4, 1.192, 5, 0.952, 18, -0.9, 145, .356, 77)
Alabama = Team("Alabama",4, 18, 8.3, 1.188, 6, 1.049, 209, 13.1, 11, .385, 10)
Hofstra = Team("Hofstra", 13, 88, 6.9, 1.099, 95, 1.022, 148, -3.1, 209, .366, 51)
Tennessee = Team("Tennessee",6, 20, 10.1, 1.137, 49, 1.001, 90, 13.3, 10, .311, 316)
Smu = Team("SMU / Miami (OH)", 11, 37, 6.6, 1.148, 41, 0.991, 70, 9.5, 50, .388, 6)
Virginia = Team("Virginia",3, 12, 12.2, 1.159, 30, 1.046, 201, 14.2, 7, .374, 25)
WrightState = Team("Wright State", 14, 127, 4.6, 1.127, 57, 0.961, 22, -1.0, 149, .303, 339)
Kentucky = Team("Kentucky",7, 28, 6.9, 1.131, 53, 0.970, 33, 11.8, 23, .352, 100)
SantaClara = Team("Santa Clara", 10, 40, 9.8, 1.164, 24, 1.018, 132, 5.4, 83, .358, 69)
IowaState = Team("Iowa State",2, 6, 16.6, 1.173, 17, 0.932, 9, 14.6, 4, .340, 166)
TennesseeState = Team("Tennessee State", 15, 172, 4.1, 1.072, 144, 1.059, 238, -1.0, 148, .345, 138)

#West Teams
Arizona = Team("Arizona",1, 3, 17.4, 1.179, 12, 0.955, 20, 14.3, 6, .355, 84)
LongIsland = Team("Long Island", 16, 198, 3.0, 1.058, 175, 1.021, 146, -4.6, 273, .313, 306)
Villanova = Team("Villanova",8, 35, 6.4, 1.117, 69, 1.011, 107, 10.5, 37, .354, 88)
UtahState = Team("Utah State", 9, 26, 10.8, 1.160, 28, 1.049, 207, 11.4, 30, .370, 35)
Wisconsin = Team("Wisconsin",5, 25, 7.1, 1.163, 26, 0.992, 72, 6.1, 75, .380, 17)
HighPoint = Team("High Point", 12, 75, 14.6, 1.181, 9, 0.981, 54, 5.8, 79, .366, 52)
Arkansas = Team("Arkansas",4, 15, 9.9, 1.199, 29, 0.924, 6, 11.7, 25, .372, 29)
Hawaii = Team("Hawaii", 13, 101, 8.4, 1.057, 178, 0.935, 12, -1.1, 152, .316, 285)
Byu = Team("BYU",6, 23, 8.6, 1.178, 5, 1.154, 35, 12.0, 20, .370, 36)
NCState = Team("NC State / Texas", 11, 36, 7.2, 1.169, 21, 0.965, 26, 0.7, 111, .350, 110)
Gonzaga = Team("Gonzaga",3, 7, 19.1, 1.179, 13, 0.979, 50, 12.5, 16, .379, 19)
KennesawState = Team("Kennesaw State", 14, 155, 2.1, 1.076, 134, 1.020, 143, -2.8, 196, .330, 212)
MiamiFL = Team("Miami (FL)",7, 32, 10.8, 1.153, 36, 0.967, 30, 13.7, 8, .352, 102)
Missouri = Team("Missouri", 10, 58, 4.3, 1.125, 59, 0.984, 60, 11.1, 33, .333, 201)
Purdue = Team("Purdue",2, 9, 11.5, 1.224, 2, 0.895, 2, 10.2, 39, .304, 338)
Queens = Team("Queens", 15, 189, 1.7, 1.161, 27, 1.075, 277, -3.0, 203, .367, 44)

    
def create_south():
    s = []
    s.append(Florida)
    s.append(Lehigh)
    s.append(Clemson)
    s.append(Iowa)
    s.append(Vanderbilt)
    s.append(McNeese)
    s.append(Nebraska)
    s.append(Troy)
    s.append(NorthCarolina)
    s.append(Vcu)
    s.append(Illinois)
    s.append(Penn)
    s.append(SaintMarys)
    s.append(TexasAM)
    s.append(Houston)
    s.append(Idaho)
    return s
    
def create_east():
    e = []
    e.append(Duke)
    e.append(Siena)
    e.append(OhioState)
    e.append(Tcu)
    e.append(StJohns)
    e.append(NorthernIowa)
    e.append(Kansas)
    e.append(CalBaptist)
    e.append(Louisville)
    e.append(SouthFlorida)
    e.append(MichiganState)
    e.append(NorthDakotaState)
    e.append(Ucla)
    e.append(Ucf)
    e.append(UConn)
    e.append(Furman)
    return e
    
def create_midwest():
    mw = []
    mw.append(Michigan)
    mw.append(Howard)
    mw.append(Georgia)
    mw.append(SaintLouis)
    mw.append(TexasTech)
    mw.append(Akron)
    mw.append(Alabama)
    mw.append(Hofstra)
    mw.append(Tennessee)
    mw.append(Smu)
    mw.append(Virginia)
    mw.append(WrightState)
    mw.append(Kentucky)
    mw.append(SantaClara)
    mw.append(IowaState)
    mw.append(TennesseeState)
    return mw
    
def create_west():
    w = []
    w.append(Arizona)
    w.append(LongIsland)
    w.append(Villanova)
    w.append(UtahState)
    w.append(Wisconsin)
    w.append(HighPoint)
    w.append(Arkansas)
    w.append(Hawaii)
    w.append(Byu)
    w.append(NCState)
    w.append(Gonzaga)
    w.append(KennesawState)
    w.append(MiamiFL)
    w.append(Missouri)
    w.append(Purdue)
    w.append(Queens)
    return w

# def create_south_round32():
#    s = []
#    s.append(Auburn)
#    s.append(Creighton)
#    s.append(Michigan)
#    s.append(TexasAM)
#    s.append(MichiganState)
#    s.append(NewMexico)
#    s.append(OleMiss)
#    s.append(IowaState)
#    return s

# def create_east_round32():
#    e = []
#    e.append(Duke)
#    e.append(Baylor)
#    e.append(Arizona)
#    e.append(Oregon)
#    e.append(Alabama)
#    e.append(SaintMarys)
#    e.append(Wisconsin)
#    e.append(Byu)
#    return e

# def create_midwest_round32():
#    mw = []
#    mw.append(Houston)
#    mw.append(Gonzaga)
#    mw.append(Purdue)
#    mw.append(McNeese)
#    mw.append(Tennessee)
#    mw.append(Ucla)
#    mw.append(Kentucky)
#    mw.append(Illinois)
#    return mw

# def create_west_round32():
#     w = []
#     w.append(Florida)
#     w.append(UConn)
#     w.append(Maryland)
#     w.append(ColoradoState)
#     w.append(StJohns)
#     w.append(Arkansas)
#     w.append(TexasTech)
#     w.append(Drake)
#     return w

# def create_south_sweet16():
#    s = []
#    s.append(Auburn)
#    s.append(Michigan)
#    s.append(MichiganState)
#    s.append(OleMiss)
#    return s

# def create_east_sweet16():
#    e = []
#    e.append(Duke)
#    e.append(Arizona)
#    e.append(Alabama)
#    e.append(Byu)
#    return e

# def create_midwest_sweet16():
#    mw = []
#    mw.append(Houston)
#    mw.append(Purdue)
#    mw.append(Tennessee)
#    mw.append(Kentucky)
#    return mw

# def create_west_sweet16():
#     w = []
#     w.append(Florida)
#     w.append(Maryland)
#     w.append(Arkansas)
#     w.append(TexasTech)
#     return w
    
# def create_south_elite8():
#    s = []
#    s.append(Auburn)
#    s.append(MichiganState)
#    return s

# def create_east_elite8():
#    e = []
#    e.append(Duke)
#    e.append(Alabama)
#    return e

# def create_midwest_elite8():
#    mw = []
#    mw.append(Houston)
#    mw.append(Tennessee)
#    return mw

# def create_west_elite8():
#     w = []
#     w.append(Florida)
#     w.append(TexasTech)
#     return w

# def create_south_final4():
#    s = []
#    s.append(Auburn)
#    return s

# def create_east_final4():
#    e = []
#    e.append(Duke)
#    return e

# def create_midwest_final4():
#    mw = []
#    mw.append(Houston)
#    return mw

# def create_west_final4():
#     w = []
#     w.append(Florida)
#     return w

# def create_champ_game():
#     list = []
#     list.append(Florida)
#     list.append(Houston)
#     return list
