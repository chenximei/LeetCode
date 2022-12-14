from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        ans = [[] for _ in range(n)]
        for person in people:
            spaces = person[1] + 1
            for i in range(n):
                if not ans[i]:
                    spaces -= 1
                    if spaces == 0:
                        ans[i] = person
                        break
        return ans

    def reconstructQueue1(self, people):
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        res = []
        for s in people:
            res.insert(s[1], s)
        return res


if __name__ == '__main__':
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    solution = Solution()
    res = solution.reconstructQueue(people)
    print(res)
