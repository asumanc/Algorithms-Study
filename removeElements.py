def removeElements(target, numbers):

    for i in range(len(numbers)):
        if numbers[i] == target:
            numbers.remove(numbers[i])
        elif not numbers:
            return 0
    return removeElements

numbers = [int(i) for i in input().split()]
target = input()
print(removeElements(target, numbers))

'''
other way:

def removeElements(numbers, target);
    if target not in set(numbers):
        return 0
    elif:
        while (target in set(numbers)):
            numbers.remove(target)
    return
'''
