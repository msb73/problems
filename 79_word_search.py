from collections import Counter


class Solution:
    def __init__(self, board, word) -> None:
        self.board = board
        self.word = word
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        if len(word) > m*n:
            return False
        count = Counter(sum(board, []))
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False 
        if count[word[0]] > count[word[-1]]:
             word = word[::-1] 
        if board[m-1][n-1] == word:
            return True

        ls = [(i, j)   for i in range(m) for j in range(n) if board[i][j] == word[0]]
        # print(ls)
        def get_values(bol, innerls, i, j, l):
            # print(innerls)
            
            directions = (
                (i-1, j),
                (i, j+1),
                (i+1, j),
                (i, j-1)
            )
            for i, j in directions:
                if i < 0 or j < 0:
                    continue

                try:
                    # print(f'{board[i][j]}')
                    if board[i][j] == word[l] and not  (i, j) in innerls:
                        print(f'    {board[i][j]}    {(i, j)}    {l}')
                        innerls.add((i, j))
                        if l+1 == len(word):
                            print(l)
                            return True
                        bol = get_values(bol, innerls, i, j, l+1)
                        innerls.remove((i,j))
                except IndexError:
                    # print(f' except {(i, j)}')
                    continue
            return bol
              
        for i,j in ls:
            # print('\n\n')
            innerls = {(i, j)}
            if  get_values(False,  innerls, i, j, 1):
                return True
        return False
    

obj1 = Solution([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED')
op = obj1.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCEFSADEESE"
)
print(f'OP = 	{op}')