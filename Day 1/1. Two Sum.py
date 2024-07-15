class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

#                   or

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_index = {}

        for i,num in enumerate(nums):
            complement = target-num

            if complement in nums_to_index:
                return [nums_to_index[complement], i]
        
            nums_to_index[num] = i
