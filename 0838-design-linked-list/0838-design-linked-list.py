class Node:
    """A node in the linked list containing a value and reference to next node."""
    def __init__(self, value):
        self.val = value
        self.next = None

class MyLinkedList:
    """A singly linked list implementation with head and tail pointers."""

    def __init__(self, value=None):
        """Initialize an empty linked list or with a single value."""
        self.head = None
        self.tail = None
        self.length = 0
        
        if value is not None:
            self._initialize_with_value(value)
    
    def _initialize_with_value(self, value):
        """Helper method to initialize list with a single value."""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def _is_valid_index(self, index, allow_end=False):
        """Check if index is valid for the current list."""
        max_index = self.length if allow_end else self.length - 1
        return 0 <= index <= max_index
    
    def _get_node_at_index(self, index):
        """Get the node at the specified index."""
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def _handle_empty_list_insertion(self, new_node):
        """Handle insertion when list is empty."""
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def get(self, index: int) -> int:
        """ Get the value at the specified index. Returns -1 if index is invalid."""
        if not self._is_valid_index(index):
            return -1

        node = self._get_node_at_index(index)
        return node.val

    def addAtHead(self, val: int) -> None:
        """Add a new node with the given value at the head of the list."""
        new_node = Node(val)

        if self.length == 0:
            self._handle_empty_list_insertion(new_node)
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def addAtTail(self, val: int) -> None:
        """Add a new node with the given value at the tail of the list."""
        new_node = Node(val)

        if self.length == 0:
            self._handle_empty_list_insertion(new_node)
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """Add a new node with the given value at the specified index."""
        if not self._is_valid_index(index, allow_end=True):
            return
        
        # Delegate to specified methods for head and tail
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            self._insert_at_middle(index, val)
    
    def _insert_at_middle(self, index, val):
        """Insert a new node at the specified middle index."""
        new_node = Node(val)
        prev_node = self._get_node_at_index(index - 1)

        new_node.next = prev_node.next
        prev_node.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """Delete the node at the specified index."""
        if not self._is_valid_index(index):
            return
        
        if index == 0:
            self._delete_head()
        else:
            self._delete_at_middle_or_tail(index)
    
    def _delete_head(self):
        """Delete the head node."""
        old_head = self.head
        self.head = self.head.next
        old_head.next = None # Clean up reference
        self.length -= 1

        # Update tail if list becomes empty
        if self.length == 0:
            self.tail = None
    
    def _delete_at_middle_or_tail(self, index):
        """Delete a node at middle or tail position."""
        prev_node = self._get_node_at_index(index - 1)
        node_to_delete = prev_node.next

        prev_node.next = node_to_delete.next
        node_to_delete.next = None # Clean up reference
        self.length -= 1

        # Update tail if we deleted the last node
        if index == self.length:
            self.tail = prev_node



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)