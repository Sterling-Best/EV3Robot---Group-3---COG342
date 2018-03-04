from src.Ev3Grid.Ev3Global import Ev3Global
from src.Ev3Grid.Ev3Region import Ev3Region
from src.Ev3Grid.Ev3Coordinates import Ev3Coordinates


aG = Ev3Global(100)
print(aG)
aC = Ev3Coordinates(2,4)
aG.addcoord(aC)
print(aG)
bC = Ev3Coordinates(12,8)
cC = Ev3Coordinates(-5,-7)
dC = Ev3Coordinates(0,0)
aG.addcoord(bC)
aG.addcoord(cC)
aG.addcoord(dC)
print (aG)
aG.addcoord(Ev3Coordinates(14,31))
aG.addcoord(Ev3Coordinates(8,12))
aG.addcoord(Ev3Coordinates(-10, -21))
aG.addcoord(Ev3Coordinates(27,53))
aG.addcoord(Ev3Coordinates(-49, 49))
print(aG)
aG.exportcsv()
