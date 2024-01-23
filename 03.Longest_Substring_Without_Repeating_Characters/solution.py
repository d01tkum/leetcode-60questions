class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        ・substring の長さが s の長さの半分を超えたら、その時点でその substring が最大
        '''
        length = len(s)
        
        maximum = 0
        for start in range(length):     #O(n)
            for end in range(start, length):   #O(n)
                sub_s = s[start:end+1]

                if len(sub_s) != len(set(sub_s)):
                    break
            if end - start + 1 > maximum:
                maximum = end - start + 1
        return maximum

