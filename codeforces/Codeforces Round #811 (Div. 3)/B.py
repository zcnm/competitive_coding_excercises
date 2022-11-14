# Remove Prefix 
# ------------------------------------------------
#helper functions
def printArray(array):
    output = ""
    for num in array:
        output += str(num) + " "
    print(output[:-1])
    return
# ------------------------------------------------
def solve(n, nums):
    seen = {}
    count = 0
    for num in reversed(nums):
        if num in seen:
            return n - count 
        else:
            seen[num] = 1
            count += 1
    return 0

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = input().split()
        print(solve(n, nums))
    return

if __name__ == "__main__":
    main()