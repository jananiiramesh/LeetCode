
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend<0) ^ (divisor<0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            while dividend >= (temp_divisor << 1):
                temp_divisor = temp_divisor << 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple
        
        quotient *= sign

        MAX = 2**31-1
        MIN = -2**31

        if quotient>MAX:
            return MAX
        if quotient<MIN:
            return MIN
        return quotient
