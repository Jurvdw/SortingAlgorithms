def TwoPointSort(nums):
    for i in range(len(nums)):
        for o in range(len(nums)):
            if nums[i] < nums[o]:
                nums[i], nums[o] = nums[o], nums[i]
    return nums

def TwoPointSort_With_Steps(nums):
    steps = []
    nums = nums[:]
    for i in range(len(nums)):
        for o in range(len(nums)):
            steps.append((nums[:], i, o))
            if nums[i] < nums[o]:
                nums[i], nums[o] = nums[o], nums[i]
    return steps