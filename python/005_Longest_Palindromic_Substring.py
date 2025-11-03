class Solution(object):
    def longestPalindrome(self, s):
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        res = ""
        for i in range(len(s)):
            # Odd length
            tmp1 = expand(i, i)
            # Even length
            tmp2 = expand(i, i+1)
            # Keep the longer palindrome
            res = max(res, tmp1, tmp2, key=len)
        return res
    
    def longestPalindromeListAll(self, s):
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        longest = 0
        result = set()  # use set to avoid duplicates

        for i in range(len(s)):
            # Odd-length palindrome
            p1 = expand(i, i)
            # Even-length palindrome
            p2 = expand(i, i + 1)

            for p in (p1, p2):
                if len(p) > longest:
                    longest = len(p)
                    result = {p}
                elif len(p) == longest:
                    result.add(p)

        return list(result)
    
    def longestPalindromesListAllWithIndices(self, s):
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # returns (substring, left_index, right_index)
            return s[l+1:r], l+1, r-1

        longest = 0
        result = []  # list of (substring, start, end)

        for i in range(len(s)):
            # Expand for odd-length palindrome
            p1, l1, r1 = expand(i, i)
            # Expand for even-length palindrome
            p2, l2, r2 = expand(i, i + 1)

            for p, l, r in [(p1, l1, r1), (p2, l2, r2)]:
                length = r - l + 1
                if length > longest:
                    longest = length
                    result = [(p, l, r)]
                elif length == longest:
                    # avoid duplicates
                    if (p, l, r) not in result:
                        result.append((p, l, r))

        return result


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.longestPalindrome("abababcb"))
    print(s.longestPalindromeListAll("abababcb"))
    print(s.longestPalindromesListAllWithIndices("abababcb"))
