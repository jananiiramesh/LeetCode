##handle nines with a flag
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nines = False
        if digits[-1]!=9:
            digits[-1]+=1
        else:
            nines = True
            index = -2
            digits[-1] = 0
            while nines and index >= -len(digits):
                if digits[index] != 9:
                    digits[index]+=1
                    nines = False
                else:
                    digits[index]=0
                    index -= 1
            if nines:
                digits.insert(0, 1)
        return digits
