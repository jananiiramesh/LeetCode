class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        sols = []
        cols = set()
        pos_diagonal = set()
        neg_diagonal = set()

        def generate_string(index):
            string = ""
            for i in range(n):
                if i == index:
                    string += 'Q'
                else:
                    string += '.'
            return string

        def queens(row,possibility):
            if row == n:
                #reached a solution
                sols.append(possibility[:])
                return

            for i in range(n):
                if (i in cols or 
                (i+row) in pos_diagonal or 
                (i-row) in neg_diagonal):
                    continue
                else:
                    cols.add(i)
                    pos_diagonal.add(i+row)
                    neg_diagonal.add(i-row)

                    string = generate_string(i)
                    possibility.append(string)

                    queens(row + 1, possibility)

                    possibility.pop()
                    cols.remove(i)
                    pos_diagonal.remove(i+row)
                    neg_diagonal.remove(i-row)

        queens(0,[])
        return sols
