from timer_utils import measure_time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10
            curr.next = ListNode(total % 10)

            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next

    def list_to_linked(lst):
        dummy = ListNode()
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def linked_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    if __name__ == "__main__":
        # Example usage
        l1 = list_to_linked([2,4,3])
        l2 = list_to_linked([5,6,4])
        result = addTwoNumbers(l1, l2)
        print(linked_to_list(result))
        print(f"-----Brute Force Alg-----")
        print(f"sum using linked list is {linked_to_list(l1)} + {linked_to_list(l2)} = {linked_to_list(result)}")
        brute_force_time = measure_time(addTwoNumbers, l1, l2)
        print(f"Brute Force avg time: {brute_force_time:.2f} μs")
