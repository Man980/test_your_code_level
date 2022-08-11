# display duplicate numbers
def duplicateNumbers(nums):
	nums.sort()
	for i in range(1, len(nums)):
		if nums[i]==nums[i-1]:
			return nums[i]
print(duplicateNumbers([1, 4, 3, 5, 3]))