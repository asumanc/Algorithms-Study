def FindFactors(num):
    num_list = []
    i = 2
    while(i <= num):
        while(num % i == 0):
            num_list.append(i)
            num = num / i
        i = i + 1

     
    if (num > 1):
        num_list.append(num)
    return num_list

# valid = True
while True:
    answer = raw_input("Do you want to continue: (Y/N)")
    if answer == 'Y':
        number = int(raw_input("Enter a number to find it's factors: "))
        print(FindFactors(number))
    elif answer == 'N':
        break
    else:
        answer = raw_input("Invalid Answer, Do you want to continue: (Y/N)")


