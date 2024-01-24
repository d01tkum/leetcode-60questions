class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)

        chars = set()
        digits = list()
        for i in range(n):  # O(n)
            if ((s[i] == '+') or (s[i] == '-')) and (len(digits) == 0): # O(1)
                digits.append(s[i])
                continue
            
            if s[i].isalpha() or (s[i] == '.'): # O(1)
                chars.add(s[i])
                continue

            if s[i].isdigit():   # O(1)
                if (len(chars) != 0):   # O(1)
                    return 0
                digits.append(s[i])
                continue
        
        if (len(digits) == 0) or ((len(digits) == 1) and (digits[0] == '+' or digits[0] == '-')):    # O(1)
            return 0

        return int("".join(digits))
