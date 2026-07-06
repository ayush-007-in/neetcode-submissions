class Solution:
    def hasDuplicate(self,nums:list[int]) -> bool:
        seen = set()
        for i in nums:
          check = i not in seen
          if check:
            seen.add(i)

          else:
              return True

        return False      
        