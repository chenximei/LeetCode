from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0]
        highBit = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                highBit = i
            bits.append(bits[i - highBit] + 1)
        return bits

if __name__ == '__main__':
    n = 5
    solution = Solution()
    res = solution.countBits(n)
    print(res)