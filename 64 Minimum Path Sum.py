class Solution:
    def minPathSum(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)] #构建动态矩阵
        dp[0][0] = grid[0][0] #左上角与网格一样
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0] #上边从左到右依次相加，因为只能从左往右走
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j] #左侧边从上往下依次相加，因为只能从上往下走
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j] #从[1][1]位置开始计算上侧与左侧最小值并与当前值相加，一直算到右下角

        return dp[rows - 1][columns - 1]

grid = [[1,3,4,8],[3,2,2,4],[5,7,1,9],[2,3,2,3]]
solution = Solution()
min = solution.minPathSum(grid)
print(min)

