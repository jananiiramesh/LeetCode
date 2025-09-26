class Solution:
    def firstUniqChar(self, s: str) -> int:
        indices = {}
        duplicates = set()

        for i, char in enumerate(s):
            if char not in indices and char not in duplicates:
                indices[char] = i
            elif char in indices:
                duplicates.add(char)
                indices.pop(char)

        if indices:
            return min(indices.values())
        else:
            return -1        
