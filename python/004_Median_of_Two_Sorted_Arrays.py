def findMedianSortedArrays(nums1, nums2):
    # binary search fulfills the goal of log(m+n)
    # always have shorter array as nums1
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    # m always <= n
    m, n = len(nums1), len(nums2)
    total = m + n
    half = total // 2

    left, right = 0, m

    while True:
        print(f"---in the while loop---")
        i = (left + right) // 2
        print(f"left is: ", left)
        print(f"right is: ", right)
        print(f"i is: ", i)
        j = half - i
        print(f"j is: ", j)

        nums1_left  = nums1[i - 1] if i > 0 else float("-inf")
        print(f"nums1_left is: ", nums1_left)
        nums1_right = nums1[i]     if i < m else float("inf")
        print(f"nums1_right is: ", nums1_right)
        nums2_left  = nums2[j - 1] if j > 0 else float("-inf")
        print(f"nums2_left is: ", nums2_left)
        nums2_right = nums2[j]     if j < n else float("inf")
        print(f"nums2_right is: ", nums2_right)

        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            if total % 2:
                return float(min(nums1_right, nums2_right))  # force float
            return (max(nums1_left, nums2_left) +
                    min(nums1_right, nums2_right)) / 2.0     # explicit float
        # nums1_left > nums2_right and nums2_left <= nums1_right:
        elif nums1_left > nums2_right:
            right = i - 1
        # nums1_left <= nums2_right and nums2_left > nums1_right
        else:
            left = i + 1


if __name__ == '__main__':
    # begin
    print(findMedianSortedArrays([1, 4, 7],[2, 5, 6, 8]))
