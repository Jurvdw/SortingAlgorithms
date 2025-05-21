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



def MergeSort_WithSteps(nums):
    steps = []
    nums_copy = nums[:]
    _mergesort_with_steps(nums_copy, 0, len(nums_copy), steps)
    return steps

def _mergesort_with_steps(arr, start, end, steps):
    if end - start > 1:
        mid = (start + end) // 2
        _mergesort_with_steps(arr, start, mid, steps)
        _mergesort_with_steps(arr, mid, end, steps)
        _merge_with_steps(arr, start, mid, end, steps)

def _merge_with_steps(arr, start, mid, end, steps):
    left = arr[start:mid]
    right = arr[mid:end]
    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        # Save current array state and comparison indices
        steps.append((arr[:], k, mid + j if left[i] > right[j] else start + i))
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        steps.append((arr[:], k, start + i))
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        steps.append((arr[:], k, mid + j))
        j += 1
        k += 1