class Solution:
    def exist(self, board, word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] #四个方向，右，左，下，上

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]: #先判断当前位置和单词字母相不相同，不相同就结束
                return False
            if k == len(word) - 1: #如果相同，判断这是不是单词的最后一个字母，如果是则包含单词
                return True

            visited.add((i, j)) #添加当前位置作为走过的标记
            result = False
            for di, dj in directions: #循环检索四个方向的下个字母
                newi, newj = i + di, j + dj #跳到要检索的新的位置
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]): #检索新的位置是否有效，超没超出网格范围
                    if (newi, newj) not in visited: #检索新的位置是否是已经走过的位置
                        if check(newi, newj, k + 1): #检索新的位置是不是要找的下一个字母并继续进行深度检索
                            result = True
                            break

            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCEE"
solution = Solution()
exist = solution.exist(board,word)
print(exist)
