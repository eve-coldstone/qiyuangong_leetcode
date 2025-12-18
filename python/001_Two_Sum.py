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


def twoSum_all_pairs_brute(nums, target):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                result.append([i, j])
    return result

from collections import defaultdict
def twoSum_all_pairs_hash(nums, target):
    num_map = defaultdict(list)  # value → list of indices
    result = []

    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            # add all pairs with previous occurrences of complement
            for comp_index in num_map[complement]:
                result.append([comp_index, index])
        num_map[num].append(index)
    return result

def twoSum_all_pairs_two_pointer(nums, target):
    nums_sorted = sorted(nums)
    l, r = 0, len(nums_sorted) - 1
    result = []

    while l < r:
        curr_sum = nums_sorted[l] + nums_sorted[r]
        if curr_sum == target:
            result.append([nums_sorted[l], nums_sorted[r]])
            # move pointers, skip duplicates
            left_val, right_val = nums_sorted[l], nums_sorted[r]
            while l < r and nums_sorted[l] == left_val:
                l += 1
            while l < r and nums_sorted[r] == right_val:
                r -= 1
        elif curr_sum < target:
            l += 1
        else:
            r -= 1

    return result

if __name__ == "__main__":
    # Example usage
    nums = [2, 9, 1, -1, 0, 11, 15, 7, 20, -2, -6]
    target = 9

    result = twoSum_brute_force(nums, target)
    print(f"-----Brute Force Alg-----")
    print(f"Indices of numbers that add up to {target}: {result}")
    brute_force_time = measure_time(twoSum_brute_force, nums, target)
    print(f"Brute Force avg time: {brute_force_time:.2f} μs")

    # start = time.time()
    result = twoSum_two_pointer(nums, target)
    # end = time.time()
    # elapsed_us = (end - start) *1000000
    print(f"-----Two Pointer Alg-----")
    print(f"Indices of numbers that add up to {target}: {result}")
    # print(f"Running time: {elapsed_us:.2f} micro seconds")
    two_pointer_time = measure_time(twoSum_two_pointer, nums, target)
    print(f"Two Pointer avg time: {two_pointer_time:.2f} μs")

    # start = time.time()
    result = twoSum_hash_map(nums, target)
    # end = time.time()
    # elapsed_us = (end - start) *1000000
    print(f"-----Hash Map Alg-----")
    print(f"Indices of numbers that add up to {target}: {result}")
    # print(f"Running time: {elapsed_us:.2f} micro seconds")
    hash_map_time = measure_time(twoSum_hash_map, nums, target)
    print(f"Hash Map avg time: {hash_map_time:.2f} μs")

    result = twoSum_all_pairs_brute(nums, target)
    print(f"-----Two Sum ALL pairs brute force Alg-----")
    print(f"Indices of numbers that add up to {target}: {result}")
    all_pairs_brute_force_time = measure_time(twoSum_all_pairs_hash, nums, target)
    print(f"All pairs brute force avg time: {all_pairs_brute_force_time:.2f} μs")

    result = twoSum_all_pairs_hash(nums, target)
    print(f"-----Two Sum ALL pairs hash map Alg-----")
    print(f"Indices of numbers that add up to {target}: {result}")
    all_pairs_hash_map_time = measure_time(twoSum_all_pairs_hash, nums, target)
    print(f"All pairs Hash Map avg time: {all_pairs_hash_map_time:.2f} μs")

    result = twoSum_all_pairs_two_pointer(nums, target)
    print(f"-----Two Sum ALL pairs two pointer Alg-----")
    print(f"Indices of numbers that add up to {target}: {result}")
    all_pairs_two_pointer_time = measure_time(twoSum_all_pairs_two_pointer, nums, target)
    print(f"All pairs two pointer avg time: {all_pairs_two_pointer_time:.2f} μs")