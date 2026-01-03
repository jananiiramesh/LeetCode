from functools import lru_cache

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        cols = [0, 1, 2]

        patterns = []
        for a in cols:
            for b in cols:
                for c in cols:
                    if a != b and b != c:
                        patterns.append((a, b, c)) 

        def nomismatch(p1, p2):
            for i in range(3):
                if p1[i] == p2[i]:
                    return False
            return True

        @lru_cache(None)
        def recursion(row, prev_pattern_idx):
            if row == n:
                return 1

            ways = 0
            for i, pattern in enumerate(patterns):
                if prev_pattern_idx == -1 or nomismatch(pattern, patterns[prev_pattern_idx]):
                    ways = (ways + recursion(row + 1, i)) % MOD

            return ways

        return recursion(0, -1)
