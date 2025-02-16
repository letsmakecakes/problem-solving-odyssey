#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List
import math


# } Driver Code Ends

#User function Template for python3

class Solution:
    def gcd(self, a: int, b: int) -> int:
        """
        Calculate the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.
        
        Args:
            a (int): First number
            b (int): Second number
        
        Returns:
            int: The GCD of the two numbers
        """
        while b:
            a, b = b, a % b
        return a
    
    def lcm(self, a: int, b: int) -> int:
        """
        Calculate the Least Common Multiple (LCM) of two numbers.
        Uses the formula: LCM(a,b) = |a * b| / GCD(a,b)
        
        Args:
            a (int): First number
            b (int): Second number
        
        Returns:
            int: The LCM of the two numbers
        """
        return abs(a * b) // self.gcd(a, b)
    
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        """
        Calculate both LCM and GCD of two numbers.
        
        Args:
            a (int): First number
            b (int): Second number
        
        Returns:
            List[int]: A list containing [GCD, LCM] of the two numbers
        """
        if a == 0 or b == 0:
            return [0, 0]
        
        gcd_result = self.gcd(abs(a), abs(b))
        lcm_result = self.lcm(abs(a), abs(b))
        
        return [lcm_result, gcd_result]

#{ 
 # Driver Code Starts.


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        a = int(input())
        b = int(input())
        obj = Solution()
        res = obj.lcmAndGcd(a, b)
        print(f"{res[0]} {res[1]}")
        print("~")

# } Driver Code Ends