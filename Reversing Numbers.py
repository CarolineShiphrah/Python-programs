""" Reversing the given number by using while loop"""

N = int(input("Enter any Number to reverse: "))
rev = 0
number = N

while (N > 0):
    rem = N % 10
    rev = (rev * 10) + rem
    N = N // 10

print("Reverse of number", number,"is", rev)