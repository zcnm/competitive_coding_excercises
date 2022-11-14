# Card Trick
def solve(n, cards, m , moved):
    total = sum(moved)
    topindex = total % n
    return cards[topindex]


def main():

    T = int(input())
    for i in range(T):
        n = int(input())
        cards = list(map(int, input().split()))
        m = int(input())
        moved = list(map(int, input().split()))
        print(solve(n, cards, m, moved))
        #print("Case #{}: {}".format(i + 1, y))
        

if __name__ == "__main__":
    main()