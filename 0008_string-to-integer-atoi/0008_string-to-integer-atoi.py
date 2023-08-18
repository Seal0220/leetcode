class Solution:
    def myAtoi(self, s: str) -> int:
        MIN, MAX = -2147483648, 2147483647
        try:
            s, result, i = s.strip(), '', 0

            if s[0] in ('-','+'):
                result+=s[0]
                s=s[1:]

            while i<len(s) and (c := s[i]).isnumeric():
                result += c
                i += 1
        
            return (lambda x: MIN if MIN > x else MAX if x > MAX else x)(int(result))
        except:
            return 0