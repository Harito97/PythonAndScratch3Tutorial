def max_score_with_constraints(n, grid):
    # Initialize dp table with three dimensions
    dp = [[[0] * 3 for _ in range(2)] for _ in range(n)]
    print(dp)
    # Base case: The first row values
    dp[0][0][1] = grid[0][0]
    dp[0][1][1] = grid[0][1]
    
    # Fill the dp table using the state transition equations
    for i in range(1, n):
        # Moving to column 0
        dp[i][0][1] = max(dp[i-1][1][1], dp[i-1][1][2]) + grid[i][0]    # move to diff col
        dp[i][0][2] = dp[i-1][0][1] + grid[i][0]    # stay in col
        
        # Moving to column 1
        dp[i][1][1] = max(dp[i-1][0][1], dp[i-1][0][2]) + grid[i][1]    # move to diff col
        dp[i][1][2] = dp[i-1][1][1] + grid[i][1]    # stay in col
    
    # The result is the maximum value in the last row considering all states
    return max(dp[n-1][0][1], dp[n-1][0][2], dp[n-1][1][1], dp[n-1][1][2])

# Read input
with open('PLAYHOPS.INP', 'r') as infile:
    n = int(infile.readline().strip())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, infile.readline().strip().split())))

# Calculate the result
result = max_score_with_constraints(n, grid)

# Write output
with open('PLAYHOPS.OUT', 'w') as outfile:
    outfile.write(str(result) + '\n')
