class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(nums)
        j = 1
        for i in nums:
            for k in range(j, len(nums)):
                if i == nums[k]:
                    return True
            j = j + 1
        return False