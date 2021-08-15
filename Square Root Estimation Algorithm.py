#Square Root Estimation Algorithm Using the Babylonian Approach - www.101computing.net/square-root-estimation-algorithms

#Complete the code here...
def square_root(number):
  x = 1
  for i in range(100):
    x = (x + (number/x))/2
  return x

number = int(input("Type a number: "))
sqrt = square_root(number)
print(sqrt)
