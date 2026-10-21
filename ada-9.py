
from typing import List


# 0/1 Knapsack using 2D Dynamic Programming
def knapsack_01_2d(
    weights: List[int],
    values: List[int],
    capacity: int
) -> int:
    if len(weights) != len(values):
        raise ValueError("Weights and values must have equal lengths")
    if capacity < 0 or any(w < 0 for w in weights):
        raise ValueError("Capacity and weights must be non-negative")

    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        for c in range(capacity + 1):
            # Do not include the current item
            dp[i][c] = dp[i - 1][c]

            # Include the item if it fits
            if weight <= c:
                dp[i][c] = max(
                    dp[i][c],
                    value + dp[i - 1][c - weight]
                )

    return dp[n][capacity]


# 0/1 Knapsack using 1D Dynamic Programming
def knapsack_01(
    weights: List[int],
    values: List[int],
    capacity: int
) -> int:
    if len(weights) != len(values):
        raise ValueError("Weights and values must have equal lengths")
    if capacity < 0 or any(w < 0 for w in weights):
        raise ValueError("Capacity and weights must be non-negative")

    dp = [0] * (capacity + 1)

    for weight, value in zip(weights, values):
        # Iterate backwards so each item is used at most once
        for c in range(capacity, weight - 1, -1):
            dp[c] = max(
                dp[c],
                value + dp[c - weight]
            )

    return dp[capacity]


# Main program
if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7

    print("Weights:", weights)
    print("Values:", values)
    print("Capacity:", capacity)

    print("\nMaximum value using 2D DP:",
          knapsack_01_2d(weights, values, capacity))

    print("Maximum value using 1D DP:",
          knapsack_01(weights, values, capacity))
