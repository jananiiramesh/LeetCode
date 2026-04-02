class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        carry = 0

        while i >= 0 or k or carry:
            add = k % 10

            if i >= 0:
                total = num[i] + add + carry
                num[i] = total % 10
            else:
                total = add + carry
                num.insert(0, total % 10)

            carry = total // 10
            k //= 10
            i -= 1

        return num
