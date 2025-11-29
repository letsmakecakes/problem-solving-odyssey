class Solution:
    def secondHighest(self, s: str) -> int:
        first = float('-inf')
        second = float('-inf')

        for ch in s:
            if ch.isdigit():
                num = int(ch)
                
                if num > first:
                    second = first
                    first = num
                elif num != first and num > second:
                    second = num
        
        return second if second != float('-inf') else -1