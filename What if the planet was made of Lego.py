#How many lego bricks would be needed to build planet Earth - www.101computing/what-if-planet-earth-was-made-of-lego/

radius = 6371 #km
width = 16 #mm
length = 16 #mm
height = 10 #mm

#Convert Earth radius from km to mm
#...radius * 1000000
radius = radius * 1000000

#"\n" is just meant to space out the outputs for a cleaner presentation
#Calculate and output the volume of planet Earth in mm3
#...
planetEarth = int(4*3.14 * (radius**3)/3)
print("Volume of Planet Earth: " + str(planetEarth) + "mm3\n")

#Calculate and output the volume of a lego brick in mm3
#...
legoBrick = int(width * length * height)
print("Volume of a Lego brick: " + str(legoBrick) + "mm3\n")

#Calculate and output the number of lego bricks needed to build planet Earth
#...
numberOfBricks = int(planetEarth / legoBrick)
print("To build planet Earth of lego, you will need " + str(numberOfBricks) + " bricks!")
