class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bk_map = {")": "(", "]": "[" , "}": "{"}
        
        for bk in s:
            if bk in bk_map.keys():
                top = stack.pop() if stack else 'hoge'
                
                if top != bk_map[bk]:
                    return False
            else:
                stack.append(bk)
        
        return not stack
