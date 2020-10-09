class Building:
    Zoning = ""
    SqFt = 0
    Stories = 0
    YrBuilt = "yyyy"

class Residential(Building):
    roomCount = 0
    garage = False
    view = False

class Commercial(Building):
    parkingSpaces = 0
    elevator = True
    occupancy = 0



