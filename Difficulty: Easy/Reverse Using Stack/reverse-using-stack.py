#{ 
 # Driver Code Starts

# } Driver Code Ends
def reverse(S):
    """
    Reverse a string using a stack.
    
    Args:
        string (str): Input string to be reversed
        
    Returns:
        str: Reversed string
    
    Example:
        >>> reverse("hello")
        'olleh'
    """
    # Early return for empty or single character strings
    if len(S) <= 1:
        return S
    
    stack = []
    # Push phase
    for char in S:
        stack.append(char)
    
    # Pop phase - using list comprehension and join
    return ''.join(stack.pop() for _ in range(len(stack)))

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
        print("~")
# } Driver Code Ends