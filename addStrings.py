class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == '0':
            return num2

        if num2 == '0':
            return num1

        ans = [0] * ((max(len(num1), len(num2)) + 1))

        num1, num2 = num1[::-1], num2[::-1]

        for i in range(min(len(num1), len(num2))):
            digit = int(num1[i]) + int(num2[i])
            ans[i] += digit
            ans[i + 1] += (ans[i] // 10)
            ans[i] = ans[i] % 10
        
        i += 1

        # leftover digits in num1
        while i < len(num1):
            ans[i] += int(num1[i])
            ans[i + 1] += ans[i] // 10
            ans[i] %= 10
            i += 1

        # leftover digits in num2
        while i < len(num2):
            ans[i] += int(num2[i])
            ans[i + 1] += ans[i] // 10
            ans[i] %= 10
            i += 1

        ans, beg = ans[::-1], 0
        while beg < len(ans) and ans[beg] == 0:
            beg += 1
        
        ans = map(str, ans[beg:])
        return "".join(ans)
