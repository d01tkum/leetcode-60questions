# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(val=0)

        curr_node = dummy_head
        carry = 0
        while (l1 != None) or (l2 != None) or (carry != 0):
            # Current step
            l1_val = 0 if l1 == None else l1.val
            l2_val = 0 if l2 == None else l2.val

            sum_val = l1_val + l2_val + carry
            ones_place = sum_val % 10
            carry = sum_val // 10

            new_node = ListNode(val=ones_place)
            curr_node.next = new_node
            
            # Update to next step
            curr_node = new_node
            l1 = None if l1 == None else l1.next
            l2 = None if l2 == None else l2.next
            
        return dummy_head.next
