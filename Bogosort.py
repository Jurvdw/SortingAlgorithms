import random

def Bogosort(nums):
    sortednums = sorted(nums)
    while nums != sortednums:
        random.shuffle(nums)

    return nums