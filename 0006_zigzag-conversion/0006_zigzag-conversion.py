class Solution:
    def convert(self, s: str, n: int) -> str:
        string = ['']*n
        
        for i, c in enumerate(s):
            string[0 if n == 1 else _i if (_i := i%(_n := (n-1)*2)) < n else _n - _i ] += c

        return ''.join(string)