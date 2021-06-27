#Jack and the beanstalk - www.101computing.net/jack-and-the-beanstalk-python-challenge/

print("The Magic Beanstalk")
height = 100
hours = int(input("Enter a number of hours: eg. 1.2"))
print("After one hour, the beanstalk was 100cm tall.")
for i in range(2, hours):
  height = int(height * 1.5 + 30)
  print("After " + str(i) + " hours, the beanstalk was " + str(height) + "cm tall!") 
print("And it's still growing!!!")
