class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        for i, _ in enumerate(range(m - n + 1)):
            substr = s2[i:i + n]

            if sorted(substr) == sorted(s1):
                return True

        return False