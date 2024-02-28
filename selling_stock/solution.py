class Variant1:
    def brute_force_max_profit(self, prices: List[int]) -> int:
        """
        Compare every possible buy/sell pair
        """
        profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return profit
    
    def recursive_max_profit(self, prices: List[int]) -> int:
        """
        Divide and Conquer Algorithm
        """
        if len(prices) == 1:
            return 0

        if len(prices) == 2:
            return max(0, prices[1] - prices[0])

        midpoint = (len(prices) // 2) + 1

        l = prices[:midpoint]
        r = prices[midpoint:]

        left = self.recursive_max_profit(l)
        right = self.recursive_max_profit(r)
        cross = max(r) - min(l)

        return max(0, left, right, cross)

    def linear_time_max_profit(self, prices: List[int]) -> int:
        """
        O(n) runtime max profit
        """
        profit = 0
        buy_minimum = prices[0]
        for p in prices:
            buy_minimum = min(buy_minimum, p)
            profit = max(profit, p - buy_minimum)
        return profit


class Variant1:
    def max_profit(self, prices: List[int]) -> int:
        pass


class Variant1:
    def max_profit(self, prices: List[int]) -> int:
        pass


class Variant1:
    def max_profit(self, k: int, prices: List[int]) -> int:
        pass