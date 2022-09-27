class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = "0" #将遍历过的1变成0
        nr, nc = len(grid), len(grid[0]) #行列数
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]: #上，下，左，右去找1
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y) #如果是1就进入当前这个1的深度遍历，即将其变成0再搜索上下左右，直到上下左右都是0的时候跳出

    def numIslands(self, grid) -> int:
        nr = len(grid) #行数
        if nr == 0:
            return 0
        nc = len(grid[0]) #列数

        num_islands = 0
        for r in range(nr):
            for c in range(nc): #遍历整个网格
                if grid[r][c] == "1": #注意是str
                    num_islands += 1 #碰到一个1就增加一个数量
                    self.dfs(grid, r, c) #开始深度遍历
        print(num_islands)
        return num_islands

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]


solution = Solution()
solution.numIslands(grid=grid)



