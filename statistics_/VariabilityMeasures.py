from statistics_ import CentralTendencyMeasures as ctm


# find standard deviation
def sd(nums: []):
    var = 0
    mx_ = ctm.mean(nums)
    for x in nums:
        var += (x - mx_) ** 2
    return (var / (len(nums) - 1)) ** 0.5


# find variance
def variance(nums: []):
    var = 0
    mx_ = ctm.mean(nums)
    for x in nums:
        var += (x - mx_) ** 2
    return var / (len(nums) - 1)


# find range
def range(nums: []):
    return max(nums) - min(nums)
