class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        seen = set()
        maxL = 0
        length = 0
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                length += 1
                if length > maxL:
                    maxL = length
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                    length -= 1
        
        return maxL