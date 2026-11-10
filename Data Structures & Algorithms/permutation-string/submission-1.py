
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        # If s1 is longer, permutation is not possible
        if n > m:
            return False

        # Frequency arrays for 26 lowercase letters
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        # Count characters of s1 and first window of s2
        for i, char in enumerate(s1):
            s1_freq[ord(char) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1

        # Count matching character frequencies
        matches = 0
        for i in range(26):
            if s1_freq[i] == s2_freq[i]:
                matches += 1

        # Check the first window
        if matches == 26:
            return True

        # Initialize sliding window pointers
        left = 0
        right = n

        # Slide the window through s2
        while right < m:

            # Add the new character from the right
            index = ord(s2[right]) - ord('a')
            s2_freq[index] += 1

            if s1_freq[index] == s2_freq[index]:
                matches += 1
            elif s1_freq[index] + 1 == s2_freq[index]:
                matches -= 1

            # Remove the old character from the left
            index = ord(s2[left]) - ord('a')
            s2_freq[index] -= 1

            if s1_freq[index] == s2_freq[index]:
                matches += 1
            elif s1_freq[index] - 1 == s2_freq[index]:
                matches -= 1

            # Move both pointers forward
            left += 1
            right += 1

            # If all 26 frequencies match, permutation exists
            if matches == 26:
                return True

        return False
