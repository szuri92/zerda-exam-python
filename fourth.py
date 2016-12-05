# Create a Rocket class.
# It should take 3 parameters in its constructor
# 1st parameter: the type of the rocket as a string, "falcon1" or "falcon9".
# 2nd parameter: the starting fuel level as a number, defaults to 0.
# 3rd parameter: number of launches as a number, defaults to 0.
#
# It should have 3 methods:
#
# launch()
# it should use 1 fuel if it's a falcon1 and 9 fuels if it's a falcon9.
# it should increment the launches by one if it had enough fuel for the launch.
#
# refill()
# it should refill the rocket's fuel level to 5 if falcon1 and to 20 if falcon9.
# it should return the amount of fuel used for the refill.
# example: if the rocket is a falcon1 and has fuel level 3, then it should return 2.
#
# getStats()
# it should return its stats as a string like: "name: falcon9, fuel: 11, launches: 1"

################################################

# The following code should work with the class:

class Rocket:


    def __init__(self, rocket_type, fuel = 0, launches = 0):
        self.rocket_type = rocket_type
        self.fuel = fuel
        self.launches = launches

    def launch(self):
        if self.rocket_type == 'falcon1':
            self.fuel -= 1
            if self.fuel >= 0:
                self.launches += 1
        elif self.rocket_type == 'falcon9':
            self.fuel -= 9
            if self.fuel >= 0:
                self.launches += 1

    def getStats(self):
        return "name: {}, fuel: {}, launches: {}".format(self.rocket_type, self.fuel, self.launches)

    def refill(self):
        falcon1_fill = 5
        falcon9_fill = 20
        fill_count = 0
        if self.rocket_type == 'falcon1' and self.fuel < 5:
            fill_count = falcon1_fill - self.fuel
            self.fuel = falcon1_fill
        elif self.rocket_type == 'falcon9' and self.fuel < 20:
            fill_count = falcon9_fill - self.fuel
            self.fuel = falcon9_fill
        return fill_count

falcon1 = Rocket('falcon1')
returned_falcon9 = Rocket('falcon9', 11, 1)

falcon1.refill() # 5
falcon1.launch()

print(falcon1.getStats()) # name: falcon1, fuel: 4, launches: 1
print(returned_falcon9.getStats()) # name: falcon9, fuel: 11, launches: 1
