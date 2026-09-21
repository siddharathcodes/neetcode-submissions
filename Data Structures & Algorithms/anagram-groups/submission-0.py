class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}

        for s in strs:
            key = "".join(sorted(s))

            if key not in res:
                res[key] = []

            res[key].append(s)

        return list(res.values())