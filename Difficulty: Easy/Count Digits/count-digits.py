#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        """
        Counts how many digits of a number evenly divide the number itself.
        
        Args:
            n (int): The number to check. Must be a positive integer.
        
        Returns:
            int: Count of digits that evenly divide n.
        
        Raises:
            ValueError: If n is not a positive integer.
            ZeroDivisionError: If n contains zero as a digit.
        """
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Input must be a positive integer")
        
        def count_evenly_dividing_digits(num: int) -> int:
            count = 0
            temp = num
            
            while temp > 0:
                digit = temp % 10
                if digit == 0:
                    temp //= 10
                    continue
                
                if num % digit == 0:
                    count += 1
                temp //= 10
        
            return count
        
        return count_evenly_dividing_digits(n)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.evenlyDivides(N))
        print("~")

# } Driver Code Ends