class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        n = len(cardPoints)
        if k == n:
            return total

        window = n - k
        curr = sum(cardPoints[:window])
        min_sum = curr

        for i in range(window, n):
            curr += cardPoints[i] - cardPoints[i - window]
            min_sum = min(min_sum, curr)

        return total - min_sum
