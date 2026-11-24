from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(count):
            if count >= n:
                return count == n
            return dfs(count + 1) + dfs(count + 2)

        return dfs(0)