import math


msg1 = "Please provide some info:"
print(msg1)
class Building_Main:
    def getBuildingInfo(self):
        self.City = input("City: ")
        self.SqFt = input("SqFt: ")
        self.Stories = input("Stories: ")
        self.YrBuilt = input("Year Built: ")

        SqFt = self.SqFt
        print("\nThanks! \n\nTo summarize: \nthis structure was built in {}, in {}. \nIt is a {} and is {} square feet."
              .format(self.YrBuilt, self.City, self.Stories, self.SqFt))
        print("\nthe Square Footage for Lease is:{}.\n".format(self.SqFt))

class A_Building(Building_Main):
    #User input for data
    def getBuildingInfo(self):
        print("\nOnly provide the following info if this is a residential building:")
        self.roomCount = input("Room Count:  ")
        self.bathroomCount = input("Bathroom Count: ")
        self.streetAddress = input("Street Address:  ")
    

class B_Building(Building_Main):
    #User input for data
    def getBuildingInfo(self):
        print("\nThis section is specific to Commercial Buildings.")
        self.name = input("Enter name of Building: ")
        self.occupancy = input("Occupancy rate (%): ")
        self.parkingSpaces = input("Parking Spaces: ")

        occupancy = self.occupancy
        print("Thanks for providing this information.")
        print("To summarize: \nthis Commercial building is known \nby the name of {}.\nIt has {} parking spaces, and is {}% occupied.".format(self.name, self.parkingSpaces, self.occupancy))
        


          

if __name__ == "__main__":
    Main = Building_Main()
    Main.getBuildingInfo()

    A = A_Building()
    A.getBuildingInfo()
    
    B = B_Building()
    B.getBuildingInfo()

    #leasingRevenues = float(SqFt) * 4.2 * (float(occupancy)/100)
    #print("Leasing Revenues: :",leasingRevenues)
