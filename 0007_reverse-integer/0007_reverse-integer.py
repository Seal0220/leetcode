class Solution:
    def reverse(self, x: int) -> int:
        return n if -2147483648 <= (n := int(str(x)[::-1] if x>=0 else '-'+str(-x)[::-1])) <= 2147483647 else 0