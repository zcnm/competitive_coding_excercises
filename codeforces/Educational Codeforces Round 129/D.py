# Required Length
import heapq
def solve(n, x):
    m = len(str(x))
    if m == n:
        return 0
    if m > n:
        return -1
    
    q = [(n - m, 0, x)]
    while len(q) > 0:
        curr = heapq.heappop(q)
        h, f, x = curr 
        strX = str(x)
        s = len(strX)
        if s == n:
            return f 
        if s > n:
            continue
        
        newF = f + 1
        
        for digit in strX:
            if int(digit) < 2:
                continue
            newX = int(digit) * x 
            
            newH = n - len(str(newX)) + newF
            newNode = (newH, newF, newX)
            heapq.heappush(q, newNode)
            
    return -1
        


def main():
    n, x = map(int, input().split())
    y = solve(n, x)
    print(y)
        

if __name__ == "__main__":
    main()