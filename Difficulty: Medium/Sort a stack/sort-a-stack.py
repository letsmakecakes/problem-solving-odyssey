class Solution:
    def sortStack(self, st):
        temp_stack = []
        
        while st:
            temp = st.pop()
            
            # Move elements that are smaller than temp
            while temp_stack and temp_stack[-1] < temp:
                st.append(temp_stack.pop())
            
            temp_stack.append(temp)
        
        # Copy back to original stack
        while temp_stack:
            st.append(temp_stack.pop())
