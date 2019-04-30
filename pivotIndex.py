def pivotIndex(self, nums):
    total = sum(nums)
    currentSum = 0
    for i in range(len(nums)):
        if (currentSumsum << 1) == total - nums[i]:
            return i
        currentSum += nums[i]
    return -1
