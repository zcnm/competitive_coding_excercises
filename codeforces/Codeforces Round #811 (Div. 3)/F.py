#TEMPLATE  
# ------------------------------------------------
#helper functions
def printArray(array):
    output = ""
    for num in array:
        output += str(num) + " "
    print(output[:-1])
    return
# ------------------------------------------------
def solve(args):
    pass 

def main():
    singleNum = int(input())
    lineToNum = [int(num) for num in input().split()]
    print(solve(singleNum))
    return

if __name__ == "__main__":
    main()