class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = {}
        cols = {}
        boxes = {}
        mapping = { 0:0, 1:0, 2:0, 3:1, 4:1, 5:1, 6:2, 7:2, 8:2}
        n = len(board)
        m = len(board[0])
        for i in range(n):
            rows[i] = []
            for j in range(m):
                if board[i][j] == ".":
                    continue
                if j not in cols:
                    cols[j] = []
                box_mapping = str(mapping[i])+str(mapping[j])
                if box_mapping not in boxes:
                    boxes[box_mapping] = []

                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[box_mapping]:
                    return False
                else:
                    rows[i].append(board[i][j])
                    cols[j].append(board[i][j])
                    boxes[box_mapping].append(board[i][j])

        return True
