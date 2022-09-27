class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 == 1:
            return False
        if len(s) == 0:
            return True

        Pairs = {')': '(', ']': '[', '}': '{'}
        stack = list() #初始化空集合

        for ch in s:
            if ch in Pairs:
                if stack == [] or ch != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return stack == []

    def isValid1(self, s: str) -> bool:
        stack = []

        for item in s:
            if item == '(':
                stack.append(')')   # 添加想反的，为了之后和配对来的右括号作比较
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or stack[-1] != item:    # 先判断stack是否已经为空，再判断当前stack的top位是否和来配对的相等
                return False
            else:
                stack.pop() # 如果配对成功，就弹出

        return True if not stack else False # 如果最后stack不是空的，则结果是False

    def isValid2(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()
        return True if not stack else False

if __name__ == '__main__':
    s = '()'
    solution = Solution()
    res = solution.isValid(s)
    print(res)
