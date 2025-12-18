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

    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    # length 1 substrings
    for i in range(n):
        dp[i][i] = True

    # check substrings of length >= 2
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j] and (length <= 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if length > max_len:
                    max_len = length
                    start = i

    return s[start:start + max_len]




# time O(n), space O(n)
def longestPalindrome_Manachers_algorithm(s):
    if not s:
        return ""

    # Transform string
    T = "^#" + "#".join(s) + "#$"
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
    print(f"Brute Force avg time: {dynamic_programming_time:.2f} μs")

    print(longestPalindrome_Manachers_algorithm(test))
    Manachers_algorithm_time = measure_time(longestPalindrome_expand_around_center, test)
    print(f"Brute Force avg time: {Manachers_algorithm_time:.2f} μs")