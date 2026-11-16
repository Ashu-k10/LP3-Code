# N-Queens using Backtracking
n = int(input("Enter N (1 to 15): "))

if n < 1 or n > 15:
    print("Enter a value from 1 to 15.")
else:
    queens = [-1] * n
    solution_count = 0

    def is_safe(row, col):
        for previous_row in range(row):
            previous_col = queens[previous_row]
            if previous_col == col:
                return False
            if abs(previous_col - col) == abs(previous_row - row):
                return False
        return True

    def solve(row):
        global solution_count
        if row == n:
            solution_count += 1
            print(f"\nSolution {solution_count}:")
            for r in range(n):
                for c in range(n):
                    print("Q" if queens[r] == c else ".", end=" ")
                print()
            return

        for col in range(n):
            if is_safe(row, col):
                queens[row] = col
                solve(row + 1)
                queens[row] = -1

    solve(0)
    print("\nTotal solutions =", solution_count)

