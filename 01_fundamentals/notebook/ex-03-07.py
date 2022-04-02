def total_spent(nums):
    nums = nums.split(' ')
    rSum = 0
    for el in nums:
        rSum = rSum + int(el)
    return rSum