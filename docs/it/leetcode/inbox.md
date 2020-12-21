# inbox

## #0121 Best Time to Buy and Sell Stock

??? example "Steps"
    ```python hl_lines="0"
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        cum_sum = [0 for _ in prices]
        cum_sum[0] = 0
        
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i-1]
            if (cum_sum[i-1] + tmp) >= tmp:
                cum_sum[i] = cum_sum[i-1] + tmp
            else:
                cum_sum[i] = tmp
            
        return max(cum_sum)
    ```

    ```python hl_lines="10"
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        cum_sum = [0 for _ in prices]
        cum_sum[0] = 0
        
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i-1]
            cum_sum[i] = max(0, cum_sum[i-1]) + tmp
            
        return max(cum_sum)
    ```

    ```python hl_lines="8"
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        cum_sum = [0 for _ in prices]
        
        for i in range(1, len(prices)):
            cum_sum[i] = max(0, cum_sum[i-1]) + (prices[i] - prices[i-1])
            
        return max(cum_sum)
    ```

    ```python
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        maxProfit = 0
        maxCurProfit = 0
        
        for i in range(1, len(prices)):
            maxCurProfit = max(0, maxCurProfit + prices[i] - prices[i-1])
            maxProfit = max(maxProfit, maxCurProfit)
        
        return maxProfit
    ```

    |编号|时间|内存|想法&结果
    |:-:|:-|:-|:-
    |01|68ms|15.3MB|初步解决
    |02|64ms|15.3MB|精简运算逻辑
    |03|60ms|15.3MB|进一步精简

## #0167 Two Sum II - Input array is sorted

??? example "Steps"
    ```python
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i, j = 0, len(numbers) - 1
        
        while i < j:
            tmp = numbers[i] + numbers[j]
            if tmp > target:
                j -= 1
            elif tmp < target:
                i += 1
            else:
                return [i+1, j+1]
    ```

## #0078 Subsets

```python
def subsets(self, nums: List[int]) -> List[List[int]]:
    subsets = [[]]
    
    for num in nums:
        subsets += [ subset + [num] for subset in subsets]
    
    return subsets
```

## #0763 Partition Labels

```python
def partitionLabels(self, S: str) -> List[int]:
    if len(S) == 1:
        return [1]
    
    subsets = []
    positions = []
    
    for i, s in enumerate(S[1:]):
        if i == 0:
            positions.append(S.rindex(s))
            subsets.append(s)
            continue
        
        if i <= positions[-1]:
            if (S.rindex(s) >= positions[-1]):
                positions[-1] = S.rindex(s)
                subsets[-1] += s
            else:
                subsets[-1] += s
        else:
            positions.append(S.rindex(s))
            subsets.append(s)
            
    return [len(subset) for subset in subsets]
```

## #0338 Counting Bits

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.



??? example "Steps"

    ```python
    def countBits(self, num: int) -> List[int]:
        return [ f'{n:b}'.count('1') for n in range(num+1)]
    ```

    ```python
    def countBits(self, num: int) -> List[int]:
        iniArr = [0]
        
        if num > 0:
            amountToAdd = 1
            while len(iniArr) < num + 1:
                iniArr.extend([x+1 for x in iniArr])
        
        return iniArr[0:num+1]
    ```

    ```python
    def countBits(self, num):
        setBits = [0] * (num+1)
        for i in range(1 ,num+1):
            # (i & (i -1)) is actually Brian Kernighan’s Algorithm
            setBits[i] = setBits[i & (i-1)] + 1
        return setBits
    ```


## #