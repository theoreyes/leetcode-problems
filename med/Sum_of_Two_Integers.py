class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 1
        carry = 0
        res = 0

        for i in range(0, 32):
            a_bit = (mask & a) >> i
            b_bit = (mask & b) >> i
            
            if (carry):
                # XNOR is used for value of 'this' bit position
                res = res ^ (((a_bit ^ b_bit) ^ 1) << i)
                if (a_bit | b_bit):
                    carry = 1
                else:
                    carry = 0
            else:
                res = res ^ ((a_bit ^ b_bit) << i)
                carry = a_bit & b_bit

            mask = mask << 1
           
        if (res > (2 ** 31) - 1):
            res = ~(res ^ ((2 ** 32) - 1))

        return res
