class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n): #只是对第一个和第二个指针做循环，第三个通过条件判断增减
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue #继续下个循环的意思，如果现在的和上一个值一样就不用再算一遍了，继续前进
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first] #给出target然后寻找两数之和
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue #继续下个循环的意思，如果现在的和上一个值一样就不用再算一遍了，继续前进
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1 #第三个指针左移，如果需要第二个指针右移则通过循环实现
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third: #从上面循环中产生两种结果，一种是2，3指针汇合，没有合适的，一种是合适的，存起来
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans

    def threeSum1(self, nums): #更快

        res = set()

        # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        # 2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))

        # 3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0, 0, 0))

        # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        return res

    def threeSum2(self, nums):
        ans = []
        n = len(nums)
        nums.sort() # 很重要，之后去重的逻辑关键，譬如说nums[i]，如果排序了，就只需要看nums[i]和nums[i-1]是否相等，
        # 不会出现乱序的话有可能nums[i]和再之前的相等
        for i in range(n):
            left = i + 1
            right = n - 1
            if nums[i] > 0: # 如果排好序，第一个就大于0，那之后就没可能，跳出循环，返回空ans
                break
            if i >= 1 and nums[i] == nums[i - 1]:   # 这个一定写在判断left right之前，如果i和i-1是一样的，就走下个循环。
                # 如果写在下面while里，会死循环，因为if成立，left又小于right，出不来
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left + 1]: left += 1 # 和之前去重i的逻辑一样
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
        return ans

if __name__ == '__main__':
    nums = [-2, 10, -2, 10, 10, 0, 2]
    solution = Solution()
    res = solution.threeSum2(nums)
    print(res)

