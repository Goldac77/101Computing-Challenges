#The missing key - www.101computing.net/the-missing-key

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

#Continue the program here...
def mult(a,b):
  count = 1
  a1 = a
  while count < b:
    a1 = a1 + a
    count = count + 1
  return a1

print(mult(a,b))
