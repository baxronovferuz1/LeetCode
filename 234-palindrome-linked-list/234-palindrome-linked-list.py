# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        empty_list=[]
        while head:
            empty_list.append(head.val)
            head=head.next
        return empty_list==empty_list[::-1]
        
        
        
        
        
        

        