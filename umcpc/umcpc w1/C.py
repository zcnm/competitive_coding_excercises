# Bulbs 
# ------------------------------------------------

def main():
    n, m = [int(num) for num in input().split()]
    allBulbs = set()
    for _ in range(n):
        bulbs = [int(num) for num in input().split()]
        bulbs = bulbs[1:]
        allBulbs = allBulbs.union(bulbs)
    if len(allBulbs) == m:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()