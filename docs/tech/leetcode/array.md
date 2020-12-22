# 01.Array类

## #0001 Two Sum

??? example "Steps"
    ```python hl_lines="5 7"
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            tmp = target - nums[i]
            if tmp in nums[i+1:]:
                return [i, nums[i+1:].index(tmp) + i + 1]
    ```

    ```python hl_lines="5 6 8"
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            tmp = target - nums[0]
            nums.pop(0)
            if tmp in nums:
                return [i, nums.index(tmp) + i + 1]
    ```

    ```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for i, num in enumerate(nums):
            last = target - num
            if last not in tmp:
                tmp[num] = i
            else:
                return [tmp[last], i]
    ```

    |编号|时间|内存|想法&结果
    |:-:|:-|:-|:-
    |01|76ms|14.5MB|问题实际是解构成寻找连续相邻元素加和的最大值
    |02|80ms|14.5MB|尝试加快速度，不过方法有问题，实际反而更慢了，本质还是暴力算法
    |03|48ms|14MB|

## #0053 Maximum Subarray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the `O(n)` solution, try coding another solution using the divide and conquer approach, which is more subtle.

```python
def maxSubArray(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    
    n = len(nums)
    
    s_nums = [0 for _ in range(n)]
    
    s_nums[0] = nums[0]
    for i in range(1, n):
        s_nums[i] = max(nums[i], s_nums[i-1] + nums[i])
    
    return max(s_nums)
```
