class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        
        left = 0
        res = ""
        min_len = float('inf')

        hashmap = {}
        for char in t:
            hashmap[char] = 1 + hashmap.get(char, 0)

        need = len(hashmap)
        have = 0
        window = {} 

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)
            if char in hashmap and window[char] == hashmap[char]:
                have += 1
            
            while have == need:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    res = s[left:right + 1]
                char = s[left]
                window[char] -= 1
                if char in hashmap and window[char] < hashmap[char]:
                    have -= 1
                left += 1
        return res




