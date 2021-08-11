class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        cnt = 0
        status = True
        if len(arr) < 3:
            return False
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            elif arr[i] > arr[i+1]:
                if i == 0:
                    return False
                else:
                    status = False
            elif status == False and arr[i] < arr[i+1]:
                return False
        if status:
            return False
        return True