
# Question 1(a)
#  You are a planner working on organizing a series of events in a row of n venues.
# Each venue can be decorated with one of the k available themes. However, adjacent venues should not have the same theme. The cost of decorating each venue with a certain theme varies. The costs of decorating each venue with a specific theme are represented by an n x k cost matrix. For example, costs [0][0] represents the cost of decorating venue 0 with theme 0, and costs[1][2] represents the cost of decorating venue 1 with theme 2. Your task is to find the minimum cost to decorate all the venues while adhering to the adjacency constraint.
#  For example, given the input costs = [[1, 5, 3], [2, 9, 4]], the minimum cost to decorate all the venues is 5.
# One possible arrangement is decorating venue 0 with theme 0 and venue 1 with theme 2, resulting in a minimum cost of 1 + 4 = 5. Alternatively, decorating venue 0 with theme 2 and venue 1 with theme 0 also yields a minimum cost of 3 + 2 = 5. Write a function that takes the cost matrix as input and returns the minimum cost to decorate all the venues while satisfying the adjacency constraint. Please note that the costs are positive integers. Example: Input: [[1, 3, 2], [4, 6, 8], [3, 1, 5]] Output: 7 Explanation: Decorate venue 0 with theme 0, venue 1 with theme 1, and venue 2 with theme 0. Minimum cost: 1 + 6 + 1 = 7 

def min_cost(costs):
    if not costs:
        return 0

    n = len(costs)  # Number of venues
    k = len(costs[0])  # Number of themes

    # Initialize the DP table
    dp = [[0] * k for _ in range(n)]
    dp[0] = costs[0]  # Base case: first row

    # Fill the DP table
    for i in range(1, n):
        for j in range(k):
            min_cost = float('inf')   # Find the minimum cost of decorating the (i-1)-th venue with a different theme
            for l in range(k):
                if l != j:
                    min_cost = min(min_cost, dp[i - 1][l])
            dp[i][j] = costs[i][j] + min_cost

    # Find the minimum cost to decorate all venues
    return min(dp[-1])


# Example usage
costs = [[1, 3, 2], [4, 6, 8], [3, 1, 5]]
print(min_cost(costs))