from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit

if __name__ == '__main__':
    prices = [7,1,2,5,4,2,6]
    solution = Solution()
    res = solution.maxProfit(prices)
    print(res)

