class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        else:
            countS1 = {}
            countS2 = {}
            left = 0

            for i in range(len(s1)): #add all character of s1 to s1Count
                countS1[s1[i]] = 1 + countS1.get(s1[i], 0)

            for right in range(len(s2)):
                countS2[s2[right]] = 1 + countS2.get(s2[right], 0)

                while right - left + 1 > len(s1): #when length > s1, move left
                    countS2[s2[left]] -= 1 #remove count
                    if countS2[s2[left]] == 0: #remove when key = 0
                        countS2.pop(s2[left], None)
                    left += 1 #move left pointer

                if countS1 == countS2: #if permutation exist, immediately return true
                    return True
            
            return False
        