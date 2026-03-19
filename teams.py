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
Florida = Team("Florida",1, 4, 14.8, 1.171, 18, 0.972, 26, 15.5, 3, .308, 324)
PrarieViewAM = Team("Prairie View A&M", 16, 300, 0, 1.014, 272, 1.052, 162, -9.2, 354, .332, 220)
Clemson = Team("Clemson",8, 34, 7.4, 1.103, 87, 0.993, 40, 10.4, 39, .341, 169)
Iowa = Team("Iowa", 9, 27, 9.2, 1.160, 29, 1.017, 80, 11.9, 26, .357, 74)
Vanderbilt = Team("Vanderbilt",5, 13, 11.1, 1.180, 11, 1.028, 95, 13.6, 16, .355, 90)
McNeese = Team("McNeese", 12, 56, 9.8, 1.111, 75, 0.969, 24, -0.1, 128, .365, 57)
Nebraska = Team("Nebraska",4, 14, 11.1, 1.119, 64, 0.959, 17, 12.5, 23, .316, 299)
Troy = Team("Troy", 13, 125, 3.8, 1.092, 105, 1.039, 125, -1.8, 170, .332, 219)
NorthCarolina = Team("North Carolina",6, 24, 8.5, 1.127, 58, 1.007, 65, 11.3, 31, .345, 153)
Vcu = Team("VCU", 11, 43, 10.1, 1.146, 43, 1.004, 61, 5.0, 85, .367, 35)
Illinois = Team("Illinois",3, 8, 14.6, 1.232, 1, 1.019, 81, 14.4, 8, .347, 140)
Penn = Team("Penn", 14, 139, 1.2, 1.050, 198, 1.033, 104, -0.5, 137, .387, 11)
SaintMarys = Team("Saint Mary's",7, 22, 12.3, 1.143, 45, 0.961, 18, 6.1, 82, .386, 13)
TexasAM = Team("Texas A&M", 10, 44, 8.2, 1.155, 33, 1.047, 152, 10.8, 35, .362, 46)
Houston = Team("Houston",2, 5, 14.3, 1.148, 42, 0.935, 4, 14.5, 7, .349, 127)
Idaho = Team("Idaho", 15, 145, 2.7, 1.073, 142, 1.036, 114, -2.8, 202, .345, 148)

#East Teams
Duke = Team("Duke",1, 1, 19.1, 1.198, 4, 0.919, 2, 15.2, 4, .351, 111)
Siena = Team("Siena", 16, 183, 4.9, 1.071, 145, 0.997, 50, -5.1, 273, .304, 334)
OhioState = Team("Ohio State",8,29, 7.0, 1.158, 32, 1.056, 174, 12.8, 21, .360, 58)
Tcu = Team("TCU", 9,39, 6.2, 1.083, 121, 0.996, 47, 10.3, 41, .331, 224)
StJohns = Team("St. John's",5,16, 11.6, 1.110, 76, 0.952, 13, 11.5, 27, .332, 215)
NorthernIowa = Team("Northern Iowa", 12, 72, 7.0, 1.058, 173, 1.8, 103, 0.0, 122, .349, 128)
Kansas = Team("Kansas",4, 21, 6.2, 1.074, 135, 0.985, 35, 14.3, 9, .350, 124)
CalBaptist = Team("Cal Baptist", 13,98, 5.5, 1.044, 211, 0.966, 21, -1.2, 152, .337, 188)
Louisville = Team("Louisville",6, 17, 12.6, 1.171, 19, 0.998, 51, 12.8, 20, .357, 77)
SouthFlorida = Team("South Florida", 11, 45, 10.7, 1.128, 56, 0.990, 37, 4.1, 90, .331, 223)
MichiganState = Team("Michigan State",3, 11, 10.5, 1.148, 40, 0.995, 43, 13.9, 15, .359, 66)
NorthDakotaState = Team("North Dakota State", 14, 114, 8.3, 1.120, 63, 1.003, 58, -4.1, 254, .357, 73)
Ucla = Team("UCLA",7, 30, 6.7, 1.144, 44, 1.045, 139, 12.0, 24, .382, 16)
Ucf = Team("UCF", 10, 51, 2.5, 1.113, 74, 1.078, 229, 9.7, 47, .362, 47)
UConn = Team("UConn",2, 10, 12.4, 1.134, 50, 0.953, 14, 12.7, 22, .352, 105)
Furman = Team("Furman", 15, 186, 2.9, 1.091, 110, 1.049, 155, -3.8, 241, .333, 210)

#Midwest Teams
Michigan = Team("Michigan",1, 2, 17.6, 1.183, 8, 0.943, 7, 16.3, 1, .360, 59)
Howard = Team("Howard", 16, 203, 7.2, 1.045, 204, 0.945, 10, -8.3, 346, .352, 107)
Georgia = Team("Georgia",8, 33, 10.7, 1.173, 16, 1.034, 108, 11.3, 30, .341, 170)
SaintLouis = Team("Saint Louis", 9, 31, 15.8, 1.177, 15, 0.963, 19, 3.7, 94, .405, 2)
TexasTech = Team("Texas Tech",5, 19, 7.8, 1.154, 34, 1.043, 131, 14.3, 10, .393, 4)
Akron = Team("Akron", 12, 54, 12.4, 1.192, 5, 1.022, 89, -0.5, 136, .385, 14)
Alabama = Team("Alabama",4, 18, 8.3, 1.188, 6, 1.081, 234, 14.7, 6, .358, 70)
Hofstra = Team("Hofstra", 13, 88, 6.9, 1.099, 95, 0.997, 49, -0.3, 133, .368, 29)
Tennessee = Team("Tennessee",6, 20, 10.1, 1.137, 49, 0.992, 39, 14.2, 11, .334, 201)
MiamiOH = Team("Miami (OH)", 11, 64, 10.9, 1.178, 14, 1.031, 100, -2.7, 197, .375, 21)
Virginia = Team("Virginia",3, 12, 12.2, 1.159, 30, 0.983, 34, 11.1, 33, .359, 63)
WrightState = Team("Wright State", 14, 127, 4.6, 1.127, 57, 1.063, 186, -3.2, 216, .361, 49)
Kentucky = Team("Kentucky",7, 28, 6.9, 1.131, 53, 1.034, 106, 14.2, 12, .341, 167)
SantaClara = Team("Santa Clara", 10, 40, 9.8, 1.164, 24, 1.026, 93, 6.3, 79, .349, 130)
IowaState = Team("Iowa State",2, 6, 16.6, 1.173, 17, 0.934, 3, 14.1, 13, .387, 12)
TennesseeState = Team("Tennessee State", 15, 172, 4.1, 1.072, 144, 1.015, 72, -5.5, 289, .337, 189)

#West Teams
Arizona = Team("Arizona",1, 3, 17.4, 1.179, 12, 0.941, 6, 15.5, 2, .360, 57)
LongIsland = Team("Long Island", 16, 198, 3.0, 1.058, 175, 1.015, 74, -5.9, 296, .361, 50)
Villanova = Team("Villanova",8, 35, 6.4, 1.117, 69, 1.024, 90, 9.8, 46, .353, 101)
UtahState = Team("Utah State", 9, 26, 10.8, 1.160, 28, 1.006, 64, 6.3, 80, .351, 110)
Wisconsin = Team("Wisconsin",5, 25, 7.1, 1.163, 26, 1.063, 191, 13.1, 18, .361, 52)
HighPoint = Team("High Point", 12, 75, 14.6, 1.181, 9, 0.981, 33, -4.0, 247, .344, 156)
Arkansas = Team("Arkansas",4, 15, 9.9, 1.199, 29, 1.068, 202, 14.1, 14, .389, 8)
Hawaii = Team("Hawaii", 13, 101, 8.4, 1.057, 178, 0.944, 8, -3.0, 207, .316, 300)
Byu = Team("BYU",6, 23, 8.6, 1.178, 5, 1.036, 115, 13.0, 19, .349, 129)
Texas = Team("Texas", 11, 42, 5.8, 1.161, 26, 1.080, 232, 12.0, 25, .348, 132)
Gonzaga = Team("Gonzaga",3, 7, 19.1, 1.179, 13, 0.914, 1, 9.8, 45, .340, 177)
KennesawState = Team("Kennesaw State", 14, 155, 2.1, 1.076, 134, 1.047, 148, -1.8, 165, .337, 186)
MiamiFL = Team("Miami (FL)",7, 32, 10.8, 1.153, 36, 1.002, 56, 9.4, 50, .347, 138)
Missouri = Team("Missouri", 10, 58, 4.3, 1.125, 59, 1.064, 194, 10.6, 37, .350, 119)
Purdue = Team("Purdue",2, 9, 11.5, 1.224, 2, 1.051, 161, 15.1, 5, .379, 20)
Queens = Team("Queens", 15, 189, 1.7, 1.161, 27, 1.138, 339, -3.7, 234, .359, 67)

    
def create_south():
    s = []
    s.append(Florida)
    s.append(PrarieViewAM)
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
    mw.append(MiamiOH)
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
    w.append(Texas)
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
