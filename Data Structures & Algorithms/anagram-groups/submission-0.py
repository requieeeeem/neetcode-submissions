class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            stringLetterCount = {}
            for letter in string:
                stringLetterCount[letter] = string.count(letter)
            print(tuple(stringLetterCount.items()))
            groups[tuple(sorted(stringLetterCount.items()))].append(string)

        return list(groups.values())