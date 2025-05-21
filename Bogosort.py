import random

def Bogosort(nums):
    sortednums = sorted(nums)
    while nums != sortednums:
        random.shuffle(nums)

    return nums

def Bogosort_with_steps(nums):
    steps = []
    sortednums = sorted(nums)
    while nums != sortednums:
        steps.append((nums[:], 0, 8 + 1))
        random.shuffle(nums)

    return steps