class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        window = {}
        countT = {}
        
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)

        charNeed = len(countT) #
        charHave = 0 #how many characters count have been satisfied
        left = 0
        resLen = float('inf')
        res = [-1, -1] #default value, to store left and right indisces

        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right], 0)
            #if character is in T and the count is correct
            if s[right] in countT and window[s[right]] == countT[s[right]]:
                charHave += 1 #character requirement satisfied
            while charHave == charNeed:
                if right - left + 1 < resLen: #if current window length is shorter than resLen, update
                    resLen = right - left + 1 #result length, to keep comparing
                    res = [left, right] #indisces, to return result later
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    charHave -= 1
                left += 1
        
        left, right = res #update left, right to the correct result
        return s[left:right + 1]


            