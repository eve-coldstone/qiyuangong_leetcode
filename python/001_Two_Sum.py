# import time
# import timeit
from timer_utils import measure_time

# brute force
def twoSum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# two pointer
def twoSum_two_pointer(nums, target):
    nums_index = [(val, index) for index, val in enumerate(nums)]
    nums_index.sort()
    begin, end = 0, len(nums) - 1
    while begin < end:
        curr = nums_index[begin][0] + nums_index[end][0]
        if curr == target:
            return [nums_index[begin][1], nums_index[end][1]]
        elif curr < target:
            begin += 1
        else:
            end -= 1

# hash map
def twoSum_hash_map(nums, target):
    num_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index

if __name__ == "__main__":
    # Example usage
    nums = [2, 9, 1, -1, 0, 11, 15]
    target = 9

    # start = time.time()
    result = twoSum_two_pointer(nums, target)
    two_pointer_time = measure_time(twoSum_two_pointer, nums, target)
    # end = time.time()
    # elapsed_us = (end - start) *1000000
    print(f"-----Two Pointer Alg-----")
    print(f"Indices of numbers that add up to {target}: {result}")
    # print(f"Running time: {elapsed_us:.2f} micro seconds")
    print(f"Hash Map avg time: {two_pointer_time:.2f} μs")

    # start = time.time()
    result = twoSum_hash_map(nums, target)
    hash_map_time = measure_time(twoSum_hash_map, nums, target)
    # end = time.time()
    # elapsed_us = (end - start) *1000000
    print(f"-----Hash Map Alg-----")
    print(f"Indices of numbers that add up to {target}: {result}")
    # print(f"Running time: {elapsed_us:.2f} micro seconds")
    print(f"Hash Map avg time: {hash_map_time:.2f} μs")
