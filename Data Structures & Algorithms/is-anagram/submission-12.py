class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = list(t)
        for i in s:
            if len(letters) == 0 or len(s) < len(letters):
                return False
            for j in range(len(letters)):
                if i == letters[j]:
                    letters.remove(i)
                    break
                if i != letters[j] and j == len(letters)-1:
                    return False
        return True