class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            maxi = arr[i+1]
            for j in range(i+2, len(arr)):
                maxi = max(maxi,arr[j])
            arr[i] = maxi
        arr[len(arr)-1] = -1
        return arr