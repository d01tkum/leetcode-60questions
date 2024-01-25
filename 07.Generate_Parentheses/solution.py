class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        answers = []
        def backtrack(curr_ans, open_count, close_conunt):
            # 制約 ------------------------- #
            if open_count < n:
                curr_ans.append('(')
                backtrack(curr_ans, open_count + 1, close_conunt)
                curr_ans.pop()  # 現在の curr_ans を後段で評価するために必要
             
            if close_conunt < open_count:
                curr_ans.append(')')
                backtrack(curr_ans, open_count, close_conunt + 1)
                curr_ans.pop()
            # ------------------------------ #

            # 終了条件 ---------------------- #
            if (open_count == n) and (close_conunt == n):
                answers.append("".join(curr_ans))    # 何故 return "".join(curr_ans) じゃダメ…？
                
            # ------------------------------ #
        backtrack([], 0, 0)
        #return backtrack([], 0, 0)
        return answers

