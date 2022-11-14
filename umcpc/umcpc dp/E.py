#Zuma
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
    n = len(nums)
    if n == 1:
        return 1
    if nums == nums[::-1]:
        return 1
        
def main(): 
    n = int(input())
    nums = input().replace(" ", "")
    print(solve(nums))
if __name__ == "__main__":
    main()