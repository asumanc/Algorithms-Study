def subsetSum(target, nums):
        #two pointers left and right for tracking every subarray
        left = 0
        right = 0

        count = 0
        n = len(nums)

        length = n
        while right < n:
            # While count is less than target,
            # we increment the size of the array
            while count < target and right < n:
                count += nums[right]
                right += 1

            if right > n:
                break
            # While sum of current subarray is greater then target,
            # decrease the the size of the array
            # move the pointer to next index.
            while left < right and count >= target:
                length = min(length, right - left)
                count -= nums[left]
                left += 1

        if (length != n+1):
            return length
        else:
            0

target = int(input())
nums = [int(i) for i in input().split()]
print (subsetSum(target, nums))
