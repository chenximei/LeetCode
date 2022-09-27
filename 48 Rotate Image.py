class Solution: #顺时针翻转90°，但不能借用其他数组帮忙，输出依然为原数组
    def rotate(self, matrix):
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j] #先左右翻
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] #再翻对角线
        print(matrix)

    def rotate1(self, A):
        x = A[::-1]
        A[:] = zip(*A[::-1])

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
solution = Solution()
solution.rotate1(matrix)
