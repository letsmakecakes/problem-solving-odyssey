from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Find the largest string that divides both str1 and str2.

        A string s divides a string t if t can be formed by concatenating
        s one or more times (e.g., "abc" divides "abcabc").

        Args:
            str1: First input string
            str2: Second input string
        
        Returns:
            The largest string that divides both inputs, or empty string if none exists
        """
        # If concatenations don't match, no common divisor exists
        # This works because if X divides both strings, then:
        # str1 = X * n and str2 = X * m for some integers n, m
        # Therefore: str1 + str2 = X * (n+m) = str2 + str
        if str1 + str2 != str2 + str1:
            return ""
        
        # The GCD of the lengths gives us the length of the largest divisor string
        gcd_length = gcd(len(str1), len(str2))

        return str1[:gcd_length]