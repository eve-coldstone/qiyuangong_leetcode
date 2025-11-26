
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