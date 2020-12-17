""" Reversing the given number using Euclidean Algorithm"""

def GCD(a, b):

   while(b):
       a, b = b, a % b
   return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print ("The GCD of", num1 ,"and", num2, "is ",end="")
print (GCD(num1,num2))