#Make Product Equal One        
# ------------------------------------------------
#helper functions
def printArray(array):
    output = ""
    for num in array:
        output += str(num) + " "
    print(output[:-1])
    return
# ------------------------------------------------
def solve(nums):
    zeros = 0
    negs = 0
    total = 0
    for num in nums:
        if num == 0:
            zeros += 1
        elif num < 0:
            negs += 1
            total += (-1 - num)
        else:
            total += (num - 1)
    
    total += zeros 
    if negs % 2 == 1:
        if zeros == 0:
            return total + 2
    return total
    
def main():
    n = int(input())
    nums = [int(num) for num in input().split()]
    print(solve(nums))
if __name__ == "__main__":
    main()