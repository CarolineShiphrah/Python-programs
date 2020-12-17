""" Finding the sum of the digits of the given number using while loop """

num = int(input("Enter a Number: "))
sum = 0
digit = num

while num > 0:
    rem = num % 10
    sum = sum + rem
    num = num//10

print("Sum of the digit", digit, "is:", sum)