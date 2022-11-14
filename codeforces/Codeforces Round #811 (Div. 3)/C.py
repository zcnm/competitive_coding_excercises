# Minimum Varied Number
# ------------------------------------------------
#helper functions
def printArray(array):
    output = ""
    for num in array:
        output += str(num) + " "
    print(output[:-1])
    return
# ------------------------------------------------
def solve(s):
    ans = ""
    remaining = s
    for i in reversed(range(1, 10)):
        if remaining > i:
            remaining -= i 
            ans += str(i)
        elif remaining == i:
            ans += str(i)
            return ans[::-1]
        else:
            ans += str(remaining)
            return ans[::-1]
    return ans[::-1]

def main():
    t = int(input())
    for _ in range(t):
        s = int(input())
        print(solve(s))
    return

if __name__ == "__main__":
    main()