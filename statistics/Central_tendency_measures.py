# find mode
def mode(nums: []):
    return max(nums)


# find median
def median(nums: []):
    l = len(nums)
    nums.sort()
    if l % 2 == 0:
        return nums[l // 2]
    else:
        if l // 2 < 5:
            return (nums[(l // 2) - 1] + nums[(l // 2)]) / 2
        else:
            return (nums[(l // 2)] + nums[(l // 2) + 1]) / 2


# find average
def mx(nums: []):
    sum = 0
    for x in nums:
        sum += x
    return sum / len(nums)
