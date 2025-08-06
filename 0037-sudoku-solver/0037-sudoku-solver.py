class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    num=int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)
                    box_id=(i//3)*3+(j//3)
                    boxes[box_id].add(num)
        
        solved=False

        def backtrack(i:int,j:int):
            nonlocal solved
            if solved:
                return 
            if i==9:
                solved=True
                return
            ni,nj=(i,j+1) if j<8 else(i+1,0)
            if board[i][j] != ".":
                backtrack(ni,nj)
            else:
                box_id=(i//3)*3+(j//3)
                for num in range(1,10):
                    if num not in rows[i] and num not in cols[j] and num not in boxes[box_id]:
                        board[i][j]=str(num)
                        rows[i].add(num)
                        cols[j].add(num)
                        boxes[box_id].add(num)
                        backtrack(ni,nj)
                        if solved:
                            return
                        board[i][j]="."
                        rows[i].remove(num)
                        cols[j].remove(num)
                        boxes[box_id].remove(num)
        backtrack(0,0)