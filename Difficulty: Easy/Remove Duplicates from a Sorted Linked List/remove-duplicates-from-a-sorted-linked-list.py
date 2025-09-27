'''
	Your task is to remove duplicates from given 
	sorted linked list.
	
	Function Arguments: head (head of the given linked list) 
	Return Type: none, just remove the duplicates from the list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    """
    Remove duplicates from a sorted singly linked list.
    
    Args:
        head: Head node of the sorted linked list
    
    Returns:
        Node: Head of the modified linked list (same as input head)
    
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(1) - only uses constant extra space
    """
    if not head:
        return head
    
    current = head
    while current and current.next:
        if current.data == current.next.data:
            # Skip the duplicate node
            current.next = current.next.next
        else:
            # Move to next unique node
            current = current.next
    
    return head