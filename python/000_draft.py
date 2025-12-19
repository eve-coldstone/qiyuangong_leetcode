
""" 
# 001
arr = [1,3,4,5,6]
num_index = [(index, val) for index, val in enumerate(arr)]
print(f"result is: {num_index}, type is: {type(num_index)}")
print(num_index[2])
"""

"""
# 001
nums = [2, 9, 1, -1, 0, 11, 15, 7, 20, -2, -6]
target = 9
num_map = {}
for index, num in enumerate(nums):
        print(f"---num is: {num}---")
        print(f"---index is: {index}---")
        complement = target - num
        if complement in num_map:
            print(f"num_map[complement] is: {complement}, and index is :{num_map[complement]}")
        num_map[num] = index
        print(f"final num_map is :{num_map}")
"""
"""
# 002
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedList(lst):
        dummy = ListNode()
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

def linkedList_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

lst = {1,4,6,7}
lkd_lst = list_to_linkedList(lst)
new_lst = linkedList_to_list(lkd_lst)
print(f"result is: {lkd_lst}, type is: {type(lkd_lst)}")
print(f"result is: {new_lst}, type is: {type(new_lst)}")
"""


"""
#004
print(f"float is : ", float("-inf"))
"""


"""
#005
s = "abcdef"
# res = bc, from index 1 to index 3-1
print(s[1:3])

# a*b*c*d*e*f
print("*".join(s))
for i in range(5, 9):
    # print 5,6,7,8
    print(i)
for j in range(3):
    # print 0,1,2
    print(j)
"""

#007
from collections import deque

d = deque()
d.append(1)
d.append(2)
print(len(d))
print(d.pop())