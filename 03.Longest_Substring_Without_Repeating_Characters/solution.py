class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        # Sliding Window
        1. index 0 から既出の文字が出るまで走査する
        2. index を 1 つ進める度に、ans を更新 max(ans, j - i + 1)
        3. もし既出の文字が無ければ、ans が答え
        4. もし既出の文字が有れば、
            1. それまでの箇所は確認済みなので、既出文字までを腐り落とし、既出文字の次を新たな始点とする
        '''
        length = len(s)
        hashmap = dict()
        ans = 0

        i = 0
        for j in range(length):
            if s[j] in hashmap.keys():
                i = max(hashmap[s[j]], i)   # 現在の始点よりも前に登場している場合は影響しない為スキップ
                
            ans = max(ans, j - i + 1)
            hashmap[s[j]] = j + 1
        return ans