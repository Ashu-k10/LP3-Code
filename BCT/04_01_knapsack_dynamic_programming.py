n = int(input("Enter number of items :"))
w = int(input("Enter Capacity :"))

wt = []
val = []

for i in range(n):
    w ,v = map(int, input("Enter weight and value: ").split())
    wt.append(w)
    val.append(v)

dp = [[0] * (w+ 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for w in range(w + 1):

        dp[i][w] = dp[i-1][w]

        if wt[i-1] <= w:
            dp[i][w] = max(dp[i][w],
                           val[i-1] + dp[i-1][w-wt[i-1]])

print("Maximum value =", dp[n][w])