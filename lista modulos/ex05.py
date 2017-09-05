def sum2(nums):
    n=0
    if len(nums) > 1:
        n = nums[0]+nums[1]
    elif len(nums) > 0:
        n = nums[0]
    return n