def SelectionSort(nums):
    for i in range(len(nums)):
        min_index = i
        for o in range(i + 1, len(nums)):
            if nums[o] < nums[min_index]:
                min_index = o
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums