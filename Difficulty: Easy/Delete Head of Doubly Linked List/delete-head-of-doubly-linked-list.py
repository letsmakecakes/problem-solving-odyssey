# User function Template for python3
def deleteHead(head):
    # Empty list or single node - return None
    if not head or not head.next:
        return None
    
    # Move head to next node and update pointers
    new_head = head.next
    new_head.prev = None
    head.next = None  # Optional: clean up old head
    
    return new_head