class Solution:
    def countAndSay(self, n: int) -> str:

        def helper(string):
            temp_arr = []
            prev_char = ""
            for char in string:
                if char == prev_char:
                    temp_arr[-1][1] += 1
                else:
                    temp_arr.append([char,1])
                    prev_char = char
            print(temp_arr)
            return temp_arr

        def helper2(temp_arr):
            string = ""
            for chars in temp_arr:
                string = string + (str(chars[1]) + chars[0])

            return string

        i = 1
        s = ""
        while (i != n+1):
            if i == 1:
                s = "1"
            else:
                s = helper2(helper(s))
            i += 1
        return s
