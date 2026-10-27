# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         countS, countT = {}, {}

#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0)

#         for c in countS:
#             if countS[c] != countT.get(c, 0):
#                 return False

#         return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for char in s :
            if char in count_s:
                count_s[char]  += 1
            else:
                count_s[char] = 1
        for char in t:
            if char in count_t:
                count_t[char] = count_t[char] + 1
            else:
                count_t[char] = 1
        return count_s == count_t