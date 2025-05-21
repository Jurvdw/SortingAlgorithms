def Bubblesort(nums):
    sorted = False   
    while (not sorted):
        sorted = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                sorted = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums
def Bubblesort_with_steps(nums):
    steps = []
    nums = nums[:]  # copy nums
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(nums) - 1):
            steps.append((nums[:], i, i + 1))
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                sorted = False
    return steps



