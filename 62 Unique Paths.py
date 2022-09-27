class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)] #构造动态矩阵，把上边和左侧边的值设为1，即边界值均为1
        # 注意，对于第一行
        # dp[0][j]，或者第一列
        # dp[i][0]，由于都是在边界，所以只能为1
        print(f)
        for i in range(1, m):
            for j in range(1, n): #从f[1][1]开始一边算一边走，一直算到最右下角的值
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]

m = 7
n = 3
solution = Solution()
paths = solution.uniquePaths(m,n)
print(paths)