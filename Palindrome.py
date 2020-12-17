""" Finding palindrome of the number given by the user """

num = int(input("Enter the number:"))
n = num
pal = 0

while num > 0:
    dig = num % 10
    pal = pal * 10 + dig
    num = num // 10

if (n == pal):
    print("Yes, it's a palindrome")
else:
    print("Oops,the number is not a palindrome!!")

