def min_time_to_build_engines(engines, split_cost):
    engines.sort()  # Sort engines in ascending order

    max_engines = len(engines)
    dp = [float('inf') - split_cost for _ in range(max_engines + 1)]  # Dynamic programming array

    # Base case: building one engine takes its own time
    dp[1] = engines[0]

    # Iterate through each engine
    for i in range(2, max_engines + 1):
        # Iterate from current number of engines down to 1 (representing splitting)
        for j in range(i, 0, -1):
            cost = max(engines[j - 1], dp[i - j] + split_cost)
            dp[i] = min(dp[i], cost)

    return dp[max_engines]

# Example usage:
engines = [4, 6, 8, 10]
split_cost = 3
print(min_time_to_build_engines(engines, split_cost))  # Output: 16