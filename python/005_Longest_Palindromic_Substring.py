from timer_utils import measure_time
# time O(n^2), space O(1)
def longestPalindrome_expand_around_center(s):
    if len(s) <= 1:
        return s

    res = ""

    for i in range(len(s)):
        # odd length
        p1 = expand(s, i, i)
        # even length
        p2 = expand(s, i, i + 1)

        if len(p1) > len(res):
            res = p1
        if len(p2) > len(res):
            res = p2

    return res

def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


# time O(n^2), space O(n^2)
def longestPalindrome_dynamic_programming(s):
    n = len(s)
    if n <= 1:
        return s

    # dp[i][j] == True if s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n)]

    start = 0       # starting index of longest palindrome
    max_len = 1     # length of longest palindrome

    # Base case: single characters
    for i in range(n):
        dp[i][i] = True

    # Check substrings of increasing length
    # length = j - i + 1 (end - start + 1)
    # length possible val 2,3,4,...,n

    """
    You must compute smaller substrings first, so that dp[i+1][j-1] is already known.
    That’s why we iterate by substring length, not by indices:
    """
    # for length possible values...
    for length in range(2, n + 1):
        # for start point possible values...
        for i in range(n - length + 1):
            # for length = end - start + 1
            # so end = start + length - 1
            j = i + length - 1
            # length range from 2, so min is 2;
            # if length is 2, s[i] = s[j] is good enough
            # if length is more, we check the inner layer
            if s[i] == s[j] and (length == 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if length > max_len:
                    max_len = length
                    start = i

    # length = end - start + 1
    # end = start + len - 1
    # but string[start, end + 1]
    # aka string[start, start + len]
    return s[start:start + max_len]




# time O(n), space O(n)
def longestPalindrome_Manachers_algorithm(s):
    if not s:
        return ""

    # Transform string
    T = "^#" + "#".join(s) + "#$"
    print(f"T is: ", T)
    n = len(T)
    P = [0] * n
    center = right = 0

    for i in range(1, n - 1):
        mirror = 2 * center - i

        if i < right:
            P[i] = min(right - i, P[mirror])

        # expand around center i
        while T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1

        # update center and right boundary
        if i + P[i] > right:
            center = i
            right = i + P[i]

    # find max palindrome
    max_len = 0
    center_index = 0
    for i in range(1, n - 1):
        if P[i] > max_len:
            max_len = P[i]
            center_index = i

    # extract result
    start = (center_index - max_len) // 2
    return s[start:start + max_len]


if __name__ == '__main__':
    # begin
    test = "abacdcabbaabacdcabbaabacdcabbaabacdcabbaabacdcabbaabacdcabbaabacdcabbaabacdcabbaabacdcabbaabacdcabba"
    
    print(longestPalindrome_expand_around_center(test))
    expand_around_center_time = measure_time(longestPalindrome_expand_around_center, test)
    print(f"expand_around_center_time: {expand_around_center_time:.2f} μs")
    
    print(longestPalindrome_dynamic_programming(test))
    dynamic_programming_time = measure_time(longestPalindrome_dynamic_programming, test)
    print(f"dynamic_programming_time: {dynamic_programming_time:.2f} μs")

    print(longestPalindrome_Manachers_algorithm(test))
    Manachers_algorithm_time = measure_time(longestPalindrome_expand_around_center, test)
    print(f"Manachers_algorithm_time: {Manachers_algorithm_time:.2f} μs")