#Complementary Colours Algorithm - www.101computing.net/complementary-colours-algorithm

#Complete the code here...
red = int(input("Red Value:"))
green = int(input("Green Value:"))
blue = int(input("Blue Value:"))

complementaryRed = 255 - red
complementaryGreen = 255 - green
complementaryBlue = 255 - blue

print("Colour: (" + str(red)+ "," + str(green) + "," + str(blue) + ")")
print("Complementary Colour: (" + str(complementaryRed) + "," + str(complementaryGreen) + "," + str(complementaryBlue) + ")")
