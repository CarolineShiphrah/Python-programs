"""1.Write a function named check_fermat that takes four parameters a, b, c and n.
Checks to see if Fermat’s theorem holds. If n is greater than 2 and  a**n +b**n = c**n the program should
print, “Holy smokes, Fermat was wrong!”
Otherwise the program should print, “No, that doesn’t work.

2.Write a function that prompts the user to input values for a, b, c and n.
Converts them to integers, and uses check_fermat to check whether they violate Fermat’s theorem"""

def check_fermat(a,b,c,n):

    if n>2 and (a**n + b**n) == c**n:
        print("Holy smokes, Fermat was wrong!")

    else:
        print("No, that doesn't work.")

get_a = int(input("Enter the number(a):"))
get_b = int(input("Enter the number(b):"))
get_c = int(input("Enter the number(c):"))
get_n = int(input("Enter the number(n):"))

print(check_fermat(get_a, get_b, get_c, get_n))



