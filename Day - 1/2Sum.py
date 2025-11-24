class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n-1

        a = []

        for num in nums:
            a.append(num)

        nums.sort()

        v = []

        while left<right:
            summ = nums[left]+nums[right]
            if summ == target:
                break
            elif summ < target:
                left+=1
            else:
                right-=1
        
        for i in range(n):
            if nums[left] == a[i]:
                v.append(i)
            elif nums[right] == a[i]:
                v.append(i)


        return v
