class Solution:
    def letterCombinations(self, digits: str): #回溯，更快
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations

    def letterCombinations1(self, digits):
        if not digits: return []
        digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                     '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = ['']
        for idx in range(len(digits)):
            result = [prev + l for prev in result for l in digit_map[digits[idx]]] #两个for递进，第一层result啥也没有，只有第一个数字的字母，
            # 第二层相当于接第一个数字的字母，去和下一个输入的数字排列组合，
        return result

if __name__ == '__main__':
    digits = "23"
    solution = Solution()
    res = solution.letterCombinations(digits)
    print(res)
