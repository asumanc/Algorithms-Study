def targetSum(target, num):
    left, right = 0, len(num) -1

    while left < right:
        temp = num[left] + num[right]

        if temp > target :
            right -= 1

        elif temp < target:
            left += 1

        elif temp == target:
            return right, left


num = [int(i) for i in input().split()]
target = int(input())
print(targetSum(target, num))
