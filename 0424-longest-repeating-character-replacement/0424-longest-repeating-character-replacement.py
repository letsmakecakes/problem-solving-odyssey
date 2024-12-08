class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = dict()
        left = 0
        max_window = 0
        max_freq = 0

        for right, char in enumerate(s):
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
            
            max_freq = max(max_freq, char_freq[char])

            window_len = right - left + 1
            if (window_len - max_freq) > k:
                char_freq[s[left]] -= 1
                left += 1
            
            window_len = right - left + 1
            max_window = max(max_window, window_len)
        
        return max_window