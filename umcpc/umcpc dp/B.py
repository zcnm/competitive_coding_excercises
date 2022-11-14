#Basketball Exercise    
# ------------------------------------------------
#helper functions
def printArray(array):
    output = ""
    for num in array:
        output += str(num) + " "
    print(output[:-1])
    return
# ------------------------------------------------
def solve(xs, ys):
    n = len(xs)
    if n <= 1:
        return max(xs[0], ys[0])
    
    dpX = {n-1: xs[-1]}
    dpY = {n-1: ys[-1]}
    
    dpX[n - 2] = xs[-2] + ys[-1]
    dpY[n - 2] = ys[-2] + xs[-1]
    
    for i in reversed(range(n - 2)):
        dpX[i] = xs[i] + max(dpY[i + 1], dpX[i + 2], dpY[i + 2])
        dpY[i] = ys[i] + max(dpX[i + 1], dpY[i + 2], dpX[i + 2])
        
        
    return max(dpX[0], dpY[0])
    
    
def main():
    n = int(input())
    heights1 = [int(num) for num in input().split()]
    heights2 = [int(num) for num in input().split()]
    
    print(solve(heights1, heights2))
if __name__ == "__main__":
    main()