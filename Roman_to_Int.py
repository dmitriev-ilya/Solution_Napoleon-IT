class Solution():
    """Solution for Napoleon.IT"""
    def romanToInt(self,s: str) -> int:
        """Convert roman numbers to arabic"""
        if len(s) > 15 or len(s) < 1:
            return 'Length must be greater than or equal to 1 and less than or equal to 15'
        else:
            s = s.upper()
            result = 0
            rtoa = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            }

            for i in range(len(s) - 1):
                if (rtoa[s[i]] < rtoa[s[i + 1]]):
                    result -= rtoa[s[i]]
                elif (rtoa[s[i]] >= rtoa[s[i + 1]]):
                    result += rtoa[s[i]]

            result += rtoa[s[len(s) - 1]]
            if result <= 3999:
                return result
            else:
                return 'Too big number'

if __name__ == "__main__":
    sol = Solution()
    s = input('Input: s = ')

    print('Output: {}'.format(sol.romanToInt(s)))


