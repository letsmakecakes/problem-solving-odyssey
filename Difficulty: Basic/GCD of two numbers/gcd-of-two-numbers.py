class Solution:
    def gcd(self, a, b):
        # Euclidean algorithm
        while b:
            a, b = b, a % b
        return a