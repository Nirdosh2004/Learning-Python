def means 'defining function' okay!!!!!!!!!!!!

def calc_sum(a,b):
          val = a+b
          return val

print(calc_sum(4,6))



def div(a,b):
          valu = a*b
          return valu

print(div(5,3))


def one():
          print("Hello world! ")

def two():
        print("Whats Up brother")

print(one() + two())  #bad practice maybe!



calculate average of three numbers
a = int(input('Write first number : '))
b = int(input("Write second number : "))
c = int(input("Write third number please sir : "))

def avg(a,b,c):
          
          return  (a + b + c)/3

print(avg(a,b,c))



arr = [4.3,5,4,6,7,44]

for items in arr:
          print(items/33 )


calculate factorial

n = float(input("Enter value for n : "))

def factorial(n):
          if(n==0 or n == 1):
                  return 1
          else:
                  return n * factorial(n-1)

if(n<0):
        print("Factorial is not defined for negative numbers")
else:
        print('your answer is : ' , factorial(n))
