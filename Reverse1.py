def reverseString(str):
    string = ""
    for i in str:
        string = i + string
    return string
str = input()
print (reverseString(str))
