class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]  # start with last row
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                # pick smaller of the two children
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]