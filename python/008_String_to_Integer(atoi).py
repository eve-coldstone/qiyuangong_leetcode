from timer_utils import measure_time

class Solution(object):
    def myAtoi_Dict(self, s):
        """
        :type str: str
        :rtype: int
        """
        
        res = 0
        sign = 1
        started = False   # have we started reading sign/digits?

        my_dict = {
            "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
            "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
        }

        for c in s:
            # Skip leading spaces
            if not started and c == " ":
                continue

            # Handle sign (only once, before digits)
            if not started and (c == "+" or c == "-"):
                sign = -1 if c == "-" else 1
                started = True
                continue

            # Read digits using dictionary
            if c in my_dict:
                started = True
                res = res * 10 + my_dict[c]
                continue

            # Stop at first invalid character
            break

        res *= sign

        # Clamp to 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX

        return res

    def myAtoi_NO_Dict(self, s):
        i = 0
        n = len(s)
        sign = 1
        res = 0

        # 1. Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # 2. Handle optional sign
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        # 3. Convert digits
        # ord(char) returns the Unicode (ASCII) number for a character.
        # substracting to convert a digit character into its integer value.
        while i < n and s[i].isdigit():
            res = res * 10 + (ord(s[i]) - ord("0"))
            i += 1

        res *= sign

        # 4. Clamp to 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX

        return res



if __name__ == '__main__':
    # begin
    s = Solution()
    string = "-11234567851264896c55"
    print(s.myAtoi_Dict(string))
    print(f"-----Using Dictionary Alg-----")
    dict_time = measure_time(s.myAtoi_Dict, string)
    print(f"avg time: {dict_time:.2f} μs")

    print(s.myAtoi_NO_Dict(string))
    print(f"-----NOT Using Dictionary Alg-----")
    no_dict_time = measure_time(s.myAtoi_NO_Dict, string)
    print(f"avg time: {no_dict_time:.2f} μs")