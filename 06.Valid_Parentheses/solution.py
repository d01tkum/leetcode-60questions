class Solution:
    def isValid(self, s: str) -> bool:
        hmap = { bk: 0 for bk in '()[]{}'}

        n = len(s)
        for i in range(n):  # O(n)
            if s[i] in ['(', '[', '{']:   # O(1)
                hmap[s[i]] += 1
            
            if s[i] == ')':               # O(1)
                hmap[')'] += 1
                if hmap['('] < hmap[')']: # O(1)
                    return False
            if s[i] == ']':               # O(1)
                hmap[']'] += 1
                if hmap['['] < hmap[']']: # O(1)
                    return False
            if s[i] == '}':               # O(1)
                hmap['}'] += 1
                if hmap['{'] < hmap['}']: # O(1)
                    return False
        
        if (hmap['('] == hmap[')']) and (hmap['['] == hmap[']']) and (hmap['{'] == hmap['}']):  # O(1)
            return True
        else:
            return False
