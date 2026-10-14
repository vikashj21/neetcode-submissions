class Solution:
    def climbStairs(self, n: int) -> int:
        var_1, var_2 = 1,1
        for i in range(n-1):
            temp = var_1
            var_1 = var_1+var_2
            var_2= temp
        return var_1
        