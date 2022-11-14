#Number of Ways   
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
    left = []
    right = []
    if len(nums) < 3:
        return 0
    if sum(nums) % 3 != 0:
        return 0
    third = sum(nums) // 3
    
    curr = 0
    for i in range(len(nums) - 2):
        curr += nums[i]
        if curr == third:
            left.append(i)
    curr = 0
    for i in reversed(range(1, len(nums))):
        curr += nums[i]
        if curr == third:
            right.append(i - 1)
    
    
    l = len(left)
    r = len(right)
    
    
    if l == 0 or r == 0:
        return 0
    
    right.sort()
    
    i = j = 0
    total = 0
    while i <l and j < r:
        if left[i] < right[j]:
            total += r - j 
            i += 1
        else: 
            j += 1
    return total
    
def main():
    n = int(input())
    nums = [int(num) for num in input().split()]
    
    
    print(solve(nums))
if __name__ == "__main__":
    main()