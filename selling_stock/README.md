# Selling Stock

Multiple questions related to finding the maximum profit attainable given a list of stock prices.

## Question Variations

1. You can only buy once and sell once.
2. You can buy and sell as often as you'd like but you can only ever own one stock unit at a time.
3. You can only complete two buy/sell transactions.
4. You can buy and sell at most `k` times.

## Examples by Variant

### Variant 1
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

### Variant 2
```
Input: prices = [7,1,5,3,6,4]
Output: 7

Input: prices = [1,2,3,4,5]
Output: 4
```

### Variant 3
```
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6

Input: prices = [1,2,3,4,5]
Output: 4
```

### Variant 4
```
Input: k = 2, prices = [2,4,1]
Output: 2

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
```
