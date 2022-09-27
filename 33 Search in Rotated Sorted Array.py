#数组本来按从小到大排列，然后在某点旋转
#将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。此时有序部分用二分法查找。
#无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环.
# 对应在实现时。
#（1）先用二分查找找到旋转的分界点，比如[4,5,6,7,0,1,2]的7， 特点是这一位比后一位大。
#（2）找到之后数组就分成了两段单调递增的区间，将target跟nums[0]比较之后可以判断出target落在哪段区间上，
#然后就是普通的二分查找。
#思路贼简单，就是进行了两次的二分查找。 第一次二分方式找到旋转位置。
#第二次二分查找是 在旋转划分后找到的空间中进行目标的二分搜索。

#永远是用有序的半边判断在哪边进行二分搜索，就算分到无序的那边，也总会二分之后，有一边是有序的

class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]: # 如果左半边是有序的，判断条件一定是<=，
                # 因为如果只有两个元素，low和mid是同一个，必须有＝的条件来cover这个situation
                if nums[l] <= target < nums[mid]: # 如果target在有序的那边
                    r = mid - 1
                else:
                    l = mid + 1 #如果target在无序的那边
            else: #如果右半边是有序的，
                if nums[mid] < target <= nums[r]: # target在有序的那边
                    l = mid + 1
                else:
                    r = mid - 1 #target在无序的那边
        return -1

nums = [3,1]
target = 1
solution = Solution()
index = solution.search(nums,target)
print(index)
