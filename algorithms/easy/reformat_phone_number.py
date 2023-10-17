# 1694. Reformat Phone Number

class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "").replace("-", "")

        re_num, idx = "", 0
        for n in number:
            if n.isnumeric():
                re_num += n
                idx += 1
                if idx == 3:
                    re_num += "-"
                    idx = 0

        if idx == 0:
            return re_num[:-1]
        if idx == 1:
            return re_num[:-3] + "-" + re_num[-3] + re_num[-1]

        return re_num


sol = Solution().reformatNumber(number="123 4-56789012")
print(sol)
