# This is a Python class demo

# Create the class
class GwentCards:
    # Constructor to pass initial values into an object
    def __init__(self, name, power, provision, faction):
        self.name = name
        self.power = power
        self.provision = provision
        self.faction = faction
    # Function to print out values of the Objects
    def introduce(self):
        print("This card is " + self.name)
        print("This cards power is " + str(self.power) + " and its provision cost is " + str(self.provision))
        print("This card belongs to " + self.faction)

# Creating objects by calling the class and passing values into the constructor
g1 = GwentCards("Geralt of Rivia", 3, 10, "Neutral")
g2 = GwentCards("Yennefer of Vengerberg", 2, 10, "Neutral")
g3 = GwentCards("Dandelion", 6, 9, "Northern Realms")

# Run the function in the class to print out the values for the objects
g1.introduce()
g2.introduce()
g3.introduce()