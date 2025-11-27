#User function Template for python3

class Solution:
    def print_divisors(self, N):
        # Print divisors up to sqrt(N)
        for i in range(1, int(N**0.5) + 1):
            if N % i == 0:
                print(i, end=" ")
        
        # Print divisors from sqrt(N) down (in reverse to maintain order)
        for i in range(int(N**0.5), 0, -1):
            if N % i == 0 and i != N // i:
                print(N // i, end=" ")
        