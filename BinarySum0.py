#gets input from user
num1 = input()
num2 = input()

# built-in functions bin() and int() used to sum up
# int() converts the inpur to interger with base 2
# bin() converts numbers to binary 

sum = bin(int(num1, 2) + int(num2, 2))
print(sum)
