#Books
def solve(books, t):
    maxBooks = 0
    total = 0
    start = 0
    end = 0
    for i in range(len(books)):
        total += books[i]
        maxBooks = max(maxBooks, end - start)
        end += 1
        while total > t:
            total -= books[start]
            start += 1
    maxBooks = max(maxBooks, end - start)
    return maxBooks
    
# ------------------------------------------------

def main():
    n, t = [int(num) for num in input().split()]
    books = [int(num) for num in input().split()]
    print(solve(books, t))
if __name__ == "__main__":
    main()