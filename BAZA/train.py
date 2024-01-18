from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        if size == 0:
            return ""

        if size == 1:
            return strs[0]

        # end

        # slice_dict = {}
        # t = 1
        # for index, i in enumerate(strs):
        #     s = i[:t]
        #     slice_dict[index] = s
        #
        # n = len(slice_dict.values())
        # while n > 0:
        #     if slice_dict.get(n) == slice_dict.get(n):
        #         n -= 1
        #
        # for i in slice_dict.values():
        #
        #
        # return len(slice_dict.values())

        # while slice_dict.get(t-1) == s:
        #     s = i[:t]
        #     slice_dict[index] = s
        #     t += 1
        #     break

        # for i in slice_dict:
        #     print("l")

        # return f'{slice_dict}'


a = Solution()
a1 = a.longestCommonPrefix(["flower", "flow", "flight"])
print(a1)
