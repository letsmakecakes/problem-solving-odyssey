class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []
        for char in s:
            # Convert uppercase ASCII (65-90) to lowercase (97-122)
            if 'A' <= char <= 'Z':
                result.append(chr(ord(char) + 32))
            else:
                result.append(char)
        return ''.join(result)