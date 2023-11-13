# 2785. Sort Vowels in a String

import unittest


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        pos, val = [], []
        for i in range(len(s)):
            if s[i] in vowels:
                pos.append(i)
                val.append(s[i])

        pos.sort()
        val.sort()
        pairs = dict(zip(pos, val))

        res = ""
        for i in range(len(s)):
            if i in pairs.keys():
                res += pairs[i]
            else:
                res += s[i]

        return res


class Tester(unittest.TestCase):
    def test_case1(self):
        sol = Solution().sortVowels(s="lEetcOde")
        self.assertEqual("lEOtcede", sol)

    def test_case2(self):
        sol = Solution().sortVowels(s="lYmpH")
        self.assertEqual("lYmpH", sol)


if __name__ == "__main__":
    unittest.main()
