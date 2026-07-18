class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {} #keep track of all the letter counts
        length = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            while (right - left + 1) - max(count.values()) > k: #window length - max frequency
                count[s[left]] -= 1
                left += 1

            length = max(length, right - left + 1)

        return length