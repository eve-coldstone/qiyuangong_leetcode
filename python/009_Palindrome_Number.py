from collections import deque
class Solution(object):
    def isPalindrome_brute_force(self, x):
        temp = x
        if temp < 0:
            return False

        y = 0
        while (x != 0):
            y = y * 10 + x % 10
            x //= 10
        
        if temp == y:
            return True
        else:
            return False
    
    def isPalindrome_deque(self, x):
        if x < 0:
            return False
        d = deque()
        while (x != 0):
            d.append(x % 10)
            x //= 10

        # as long as my deque is NOT empty !d
        # better yet, as long as we got more than 1 left; 
        while (len(d) >1):
            if d.pop() != d.popleft():
                return False
            
        return True
    
    def isPalindrome_string_based(self, x):
        s = str(x)
        return s == s[::-1] 
    
    def isPalindrome_half_reverse(self, x):
        # Negative numbers and numbers ending in 0 (except 0 itself) can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even digits: x == reversed_half
        # For odd digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10



if __name__ == '__main__':
    # begin
    s = Solution()
    print (s.isPalindrome_brute_force(1001))
    print (s.isPalindrome_deque(1001))
    print (s.isPalindrome_string_based(1001))
    print (s.isPalindrome_half_reverse(1001))
    
