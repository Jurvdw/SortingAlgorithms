def MergeSort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = MergeSort(nums[:mid])
    right = MergeSort(nums[mid:])

    return Merge(left, right)


def Merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
