class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t is "":
            return ""
        
        count_t = {}
        window = {}
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)

        have = 0
        need = len(count_t)
        result = [-1, -1]
        result_len = float("infinity")
        left = 0

        for right, char in enumerate(s):
            window[char] = 1 + window.get(char, 0)

            if char in count_t and count_t[char] == window[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < result_len:
                    result = [left, right]
                    result_len = right - left + 1
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1 
        
        left, right = result

        return s[left:right+1] if result_len != float("infinity") else ""