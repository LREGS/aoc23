nums = [1,2,3,44,65,76,87,4,5,5,6,7,4]

def median_followers(nums):
    sortedNums = sorted(nums)
    median = len(nums) / 2
    print(sortedNums[int(median)])

median_followers(nums)

print(2 ** 10)