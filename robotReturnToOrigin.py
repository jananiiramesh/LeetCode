class Solution:
    def judgeCircle(self, moves: str) -> bool:
        hori = 0
        vert = 0
        # we see up, hori ++, down means hori --
        # same thing for vert
        for d in moves:
            if d == 'U':
                hori += 1
            elif d == 'D':
                hori -= 1
            elif d == 'L':
                vert += 1
            else:
                vert -= 1

        return hori == 0 and vert == 0
