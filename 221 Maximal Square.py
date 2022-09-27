class Solution:
    def maximalSquare(self, matrix) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:  #检测行列是否为0
            return 0

        maxSide = 0 #设置初始最大边长为0
        rows, columns = len(matrix), len(matrix[0]) #矩阵行列数
        dp = [[0] * columns for _ in range(rows)] #简历动态规划矩阵，为输入矩阵同样维度的全0矩阵
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1': #第一个条件，假如输入矩阵当前数是1
                    if i == 0 or j == 0: #第二个条件，假如是在四边
                        dp[i][j] = 1 #在四边则边长只能为1，因为是当前数作为正方形右下角
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 #否则不在四边的话，算上，左，斜上三个的最小值再加1
                    maxSide = max(maxSide, dp[i][j]) #替换当前最大边长

        maxSquare = maxSide * maxSide #平方算面积
        return maxSquare

matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

solution = Solution()
max = solution.maximalSquare(matrix=matrix)
print(max)



