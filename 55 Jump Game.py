from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost: #看当前位置能不能跳到
                rightmost = max(rightmost, i + nums[i]) #能跳到的话，检查当前位置最远跳到哪，如果更远就替换，如果没有更远就保持原来的
                if rightmost >= n - 1: #只要出现最远跳到的位置超过最后一个，就代表能跳到，返回
                    return True
        return False

if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    #nums = [3, 2, 1, 0, 4]
    solution = Solution()
    res = solution.canJump(nums)
    print(res)
