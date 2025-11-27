class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        last_seen_dict={}

        for index,key_value in enumerate(nums):
            if key_value in last_seen_dict and (index-last_seen_dict[key_value])<=k:
                return True
            last_seen_dict[key_value]=index

        return False