# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def find_middle_element(left, right):
            slow = fast = left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            return slow

        def convert_list_to_bst(left, right):
            if left == right:
                return None
            
            mid = find_middle_element(left, right)
            root = TreeNode(mid.val)

            root.left = convert_list_to_bst(left, mid)
            root.right = convert_list_to_bst(mid.next, right)

            return root
        
        return convert_list_to_bst(head, None)