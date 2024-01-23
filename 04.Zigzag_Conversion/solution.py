class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        分からなかったので、解説を読んでからやった。
        '''
        if numRows == 1:
            return s

        answer = list()
        n = len(s)
        skips_in_section = 2 * (numRows-1)    # 個人的に、文字の数よりも差の数の方が理解しやすい

        for curr_row in range(numRows):
            index = curr_row
            while index < n:
                answer.append(s[index])

                # 中間の行では、途中でも追加
                if ( curr_row != 0 ) and ( curr_row != numRows-1):
                    skips_in_between = skips_in_section - 2 * curr_row
                    second_index = index + skips_in_between

                    if second_index < n:
                        answer.append(s[second_index])

                index += skips_in_section

        return "".join(answer)
