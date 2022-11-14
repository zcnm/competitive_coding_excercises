#Flowers
# ------------------------------------------------
#helper functions
def printArray(array):
    output = ""
    for num in array:
        output += str(num) + " "
    print(output[:-1])
    return
# ------------------------------------------------
def solve(flowers, k, maxNum):
    MOD = 1000000007
    dp = []
    for i in range(k):
        dp.append(1)
    
    for n in range(k, maxNum + 1):
        total = dp[-1] + dp[-k]
        dp.append(total % MOD)
    
    prefArray = [0]
    for num in dp:
        prefArray.append(prefArray[-1] + num)
    for a, b in flowers:
        print((prefArray[b + 1] - prefArray[a]) % MOD)
    
    
def main(): 
    t, k = [int(num) for num in input().split()]
    flowers = []
    maxNum = 0
    for _ in range(t):
        a, b = [int(num) for num in input().split()]
        flowers.append((a, b))
        if b > maxNum:
            maxNum = b
    solve(flowers, k, maxNum)
if __name__ == "__main__":
    main()