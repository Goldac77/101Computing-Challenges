#Eureka! - Archimedes and King Hiero's Crown - www.101computing.net/eureka-and-king-hieros-crown/

mass = float(input("Input the mass of the crown in kg"))
volume = float(input("Input the volume of the crown in cubic meter"))

#Complete the code here to calculate the density and compare it with the density of a range of differen metals
density = int(mass / volume)      #round the density to whole numbers for better results
if density in range(2400, 2700):
  print("Crown is made of Aluminium")
elif density in range(8100, 8300):
  print("Crown is made of Bronze")
elif density in range(10400, 10600):
  print("Crown is made of Silver")
elif density in range(11200, 11400):
  print("Crown is made of Lead")
elif density in range(17100, 17500):
  print("Crown is made of Gold")
elif density in range(2100, 21500):
  print("Crown is made of Platinum")
