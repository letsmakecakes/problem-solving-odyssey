'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count