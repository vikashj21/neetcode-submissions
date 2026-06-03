class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones, cont_ones = 0,0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                cont_ones += 1
                if i == len(nums) - 1 and cont_ones > max_ones:
                    max_ones = cont_ones 
            else:
                if cont_ones > max_ones:
                    max_ones = cont_ones
                cont_ones = 0
            
            print(i, cont_ones)
        return max_ones