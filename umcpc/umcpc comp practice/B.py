#Changing Jewels     
def solve(N, X, Y):
    red = {1: 0, 2 : X * Y}
    blue = {1: 1, 2: Y}
    
    for i in range(3, N + 1):
        blue[i] = red[i - 1] + Y * blue[i - 1]
        red[i] = red[i - 1] + X * blue[i]

    return red[N]
    
# ------------------------------------------------
#helper functions
def printArray(array):
    output = ""
    for num in array:
        output += str(num) + " "
    print(output[:-1])
    return
# ------------------------------------------------

def main():
    N, X, Y = [int(num) for num in input().split()]
    print(solve(N, X, Y))

if __name__ == "__main__":
    main()