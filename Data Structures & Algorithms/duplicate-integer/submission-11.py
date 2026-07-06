class Solution:
    def hasDuplicate(self,nums:list[int]) -> bool:
        seen = set()
        # seen = sorted([]) Tiem limit exceeded
        for i in nums:
          check = i not in seen
          if check:
            # seen.append(i)
            seen.add(i)

          else:
              return True

        return False      
        