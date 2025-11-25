class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')

        for i in range(0,n-2):
            left = i+1
            right = n-1

            while left<right:
                total = nums[i]+nums[left]+nums[right]

                if total == target:
                    return target
                

                if abs(target-closest)>abs(target-total):
                    closest = total
                
                if total<target:
                    left+=1
                else:
                    right-=1
                
        return closest
        