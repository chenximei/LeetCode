#这里  双指针方式，其实就类似是  快速排序中的方式，从前往后走【但是也跟快排中有很大不同】，我们需要的是0在前面，2在后面，1在中间。
#所以可以按位置进行交换调整。  可以看到核心是设置了 lo、hi、i三个指针，分别表示 0位置、2位置、1位置，当我们由前往后走时，遇到三种情况：
# 【1】遇到0，则跟 lo指标的进行交换
# 【2】遇到1，则不管了，直接往后走 i+1
# 【3】遇到2，则跟 hi的进行交换。
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1
        return nums

if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    solution = Solution()
    res = solution.sortColors(nums)
    print(res)

