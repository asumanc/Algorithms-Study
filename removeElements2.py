def removeElements(numbers, target):
    if target not in set(numbers):
        return 0
    else:
        while (target in set(numbers)):
            numbers.remove(target)
    return

numbers = [int(i) for i in input().split()]
target = input()
print(removeElements(target, numbers))
