class Solution:
    def maxArea2(self, height):
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans

    def maxArea(self, height):
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res

    def maxArea1(self, height):
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            res, l, r = max(res, h * (r - l)), l + (height[l] == h), r - (height[r] == h)
        return res

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    res = solution.maxArea(height)
    print(res)