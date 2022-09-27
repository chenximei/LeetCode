class Solution(object):
    def searchRange(self, nums, target):
        lo, hi = 0, len(nums) - 1
        # 第一步 找到目标数字所在的位置 midtarget，但是这个位置不一定是边界，但是可以作为进行边界查找时的依据
        while (lo <= hi):
            mid = (lo + hi) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        if lo > hi:  # 不存在
            return [-1, -1]
        midtarget = mid

        #第二步，进行 左边目标  数字位置 leftpos的查找。在（0，mid）范围内找左边界
        lo, hi = 0, mid
        leftpos = 0
        while (lo <= hi):
            # print lo, hi
            if (hi >= 1 and nums[hi - 1] != target) or hi == 0:  # 找到左边界或者找到头了
                leftpos = hi
                break
            mid = (lo + hi) // 2

            #下面的挪动细节，树主要体现左边界查找和右边界查找区分的核心。
            if nums[mid] == target:
                hi = mid
            elif nums[mid] < target:
                lo = mid + 1

        #第三步，在左边目标数字的基础上进行rightpos的查找，在（mid，len(nums)）范围内找右边界
        rightpos = 0
        lo, hi = midtarget, len(nums) - 1
        while (lo <= hi):
            if (lo <= len(nums) - 2 and nums[lo + 1] != target) or lo == len(nums) - 1:  # 找到右边界或者找到头了
                rightpos = lo
                break

            mid = (lo + hi + 1) // 2
            if nums[mid] == target:
                lo = mid
            elif nums[mid] > target:
                hi = mid - 1

        return [leftpos, rightpos]

    def searchRange1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] == target and nums[r] == target:
                return [l, r]
            if nums[l] < target:
                l += 1
            if nums[r] > target:
                r -= 1

        return [-1, -1]

nums = [5,7,7,8,8,10]
target = 8
solution = Solution()
position = solution.searchRange(nums,target)
print(position)