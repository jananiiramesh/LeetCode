#create list, choose last element
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        return len(l[-1])
