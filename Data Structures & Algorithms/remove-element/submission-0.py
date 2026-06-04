class Solution:
    def deleteElement(self, nums, i):
        for j in range(i, len(nums)-1):
            nums[j] = nums[j+1]
        nums[len(nums) - 1] = None

    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            while nums[i] == val:
                self.deleteElement(nums, i)
            if nums[i] == None:
                print(nums)
                return i
        return len(nums)