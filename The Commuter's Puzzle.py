#The commuter's puzzle - www.101computing.net/to-the-moon-and-back
dailyCommute = 60 * 2
weeklyCommute = 5 * dailyCommute
yearlyCommute = weeklyCommute * 52
yearlyDistance = yearlyCommute * 1.609
moonTrip = 384400 * 2
years = moonTrip / yearlyDistance

print("Yuri would have travelled the equivalent of going to the Moon and back in " + str(int(years)) + "years!")
