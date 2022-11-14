# Game With Cards
def solve(n, alice, m, bob):
    aliceMax = max(alice)
    bobMax = max(bob)
    if aliceMax > bobMax:
        print("Alice")
        print("Alice")
    elif bobMax > aliceMax:
        print("Bob")
        print("Bob")
    else:
        print("Alice")
        print("Bob")


def main():

    T = int(input())
    for i in range(T):
        n = int(input())
        alice = list(map(int, input().split()))
        m = int(input())
        bob = list(map(int, input().split()))
        solve(n, alice, m, bob)
        #print("Case #{}: {}".format(i + 1, y))
        

if __name__ == "__main__":
    main()