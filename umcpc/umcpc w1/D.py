# Puzzles
# ------------------------------------------------

def main():
    n, m = [int(num) for num in input().split()]
    puzzles = [int(num) for num in input().split()]
    puzzles.sort()
    ans = puzzles[m - 1] - puzzles[0]
    for i in range(m - n):
        ans = min(ans, puzzles[i + n - 1] - puzzles[i])        
    print(ans)
if __name__ == "__main__":
    main()