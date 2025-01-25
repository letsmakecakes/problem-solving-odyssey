#User function Template for python3

class TwoStacks:
    """A class that implements two separate stacks in one array."""
    def __init__(self):
        """Initialize two empty stacks in one array."""
        self.stack = [[], []]

    # Function to push an integer into stack 1
    def push1(self, x):
        self.stack[0].append(x)

    # Function to push an integer into stack 2
    def push2(self, x):
        self.stack[1].append(x)

    # Function to remove an element from top of stack 1
    def pop1(self):
        if len(self.stack[0]) == 0:
            return -1
        
        return self.stack[0].pop()

    # Function to remove an element from top of stack 2
    def pop2(self):
        if len(self.stack[1]) == 0:
            return -1
        
        return self.stack[1].pop()



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    while T > 0:
        sq = TwoStacks()
        Q = int(input())
        while Q > 0:
            query = list(map(int, input().split()))
            if query[1] == 1:
                if query[0] == 1:
                    sq.push1(query[2])
                elif query[0] == 2:
                    sq.push2(query[2])
            elif query[1] == 2:
                if query[0] == 1:
                    print(sq.pop1(), end=' ')
                elif query[0] == 2:
                    print(sq.pop2(), end=' ')
            Q -= 1
        print()
        T -= 1

        print("~")

# } Driver Code Ends