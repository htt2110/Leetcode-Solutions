'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.You may assume the two numbers 
do not contain any leading zero, except the number 0 itself.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
        
        carry = 0
        result = ListNode(0)
        pointer = result
        
        while (l1 or l2 or carry):
            
            first_num = l1.val if l1 else 0
            second_num = l2.val if l2 else 0
            
            summation = first_num + second_num + carry
            
            num = summation % 10 #Remainder
            carry = summation // 10 #Int value at division
            
            pointer.next = ListNode(num)
            
            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result.next

