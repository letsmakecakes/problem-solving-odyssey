#User function Template for python3

class MyStack:
    """A simple stack implementation using a list as the underlying data structure.
    
    This class implements basic stack operations including push and pop, following the Last-In-First-Out (LIFO) principle.
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self._items=[]
    
    def push(self,data):
        """Push an integer onto the top of the stack.
        
        Args:
            item: The integer to be pushed onto the stack.
        """
        self._items.append(data)
    
    def pop(self):
        """Remove and return the top item from the stack.
        
        Returns:
            int: The top item from the stack if it exists, -1 if the stack is empty.
        """
        return self._items.pop() if self._items else -1
        


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    idx = 1
    for _ in range(T):
        sq = MyStack()
        line = data[idx].strip()
        nums = list(map(int, line.split()))
        idx += 1
        n = len(nums)
        i = 0
        while i < n:
            QueryType = nums[i]
            i += 1
            if QueryType == 1:
                a = nums[i]
                i += 1
                sq.push(a)
            elif QueryType == 2:
                print(sq.pop(), end=" ")
        print()
        print("~")

# } Driver Code Ends