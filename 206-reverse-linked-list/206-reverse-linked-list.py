# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        teskari_son=None
        while head:
            var=head.next
            head.next=teskari_son
            teskari_son=head
            head=var
        return teskari_son
    
            
            
            
            
            
            
