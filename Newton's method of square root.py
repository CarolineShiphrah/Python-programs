def get_sqt(number):
    sqt = number

    while abs(number - sqt * sqt ) > precision:
        sqt = (sqt + number/sqt) / 2
    return sqt

number = int(input("Enter the number :"))
precision = float(input('Enter the precision :'))

print(get_sqt(number))