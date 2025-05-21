def TwoPointSort(nums):
    for i in range(len(nums)):
        for o in range(len(nums)):
            if nums[i] < nums[o]:
                nums[i], nums[o] = nums[o], nums[i]
    return nums