class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        n = len(chars)
        i = 0
        j = 0

        while j < n:
            char = chars[j]
            freq = 0

            while j < n and chars[j] == char:
                j += 1
                freq += 1

            chars[i] = char
            i += 1

            if freq > 1:
                for f in str(freq):
                    chars[i] = f
                    i += 1

        return i
        
