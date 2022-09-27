class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]

    def isMatch1(self, s, p):
        prev = [False, True]
        for j in range(len(p)):
            prev.append(p[j]=='*' and prev[j])

        for i in range(len(s)):
            curr = [False, False]
            for j in range(len(p)):
                if p[j]=='*':
                    curr.append(curr[j] or curr[j+1] or (prev[j+2] and p[j-1] in (s[i], '.')))
                else:
                    curr.append(prev[j+1] and p[j] in (s[i], '.'))
            prev = curr
        return prev[-1]

if __name__ == '__main__':
    s = "ab"
    p = ".*"
    solution = Solution()
    res = solution.isMatch1(s,p)
    print(res)