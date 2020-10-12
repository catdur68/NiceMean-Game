msg1 = "Please provide some info:"
print(msg1)
class Building_Main:

    City = input("City: ")
    SqFt = input("SqFt: ")
    Stories = input("Stories: ")
    YrBuilt = input("Year Built: ")
        
    def Message2(self):
        msg2 = input("Thanks!")
        print(msg2)                       

class A_Building(Building_Main):
    #User input for data
    def getBuildingInfo(Building_Main):
        print("If this is a residential building, please provide this info:")
        roomCount = input("Room Count:  ")
        bathroomCount = input("Bathroom Count: ")
        streetAddress = input("Street Address:  ")
    

class B_Building(Building_Main):
    #User input for data
    def getBuildingInfo(Building_Main):
        print("This section is specific to Commercial Buildings.")
        name = input("Enter name of Building: ")
        occupancy = input("Occupancy rate (%): ")
        parkingSpaces = input("Parking Spaces: ")
        leasingRevenues = float(Building_Main.SqFt) * 4.2 * (float(occupancy)/100)
        print("Leasing Revenues: :",leasingRevenues)
        

          

if __name__ == "__main__":
    Begin = Building_Main()
    Begin.Message2()
    A = A_Building()
    A.getBuildingInfo()
    B = B_Building()
    B.getBuildingInfo()
