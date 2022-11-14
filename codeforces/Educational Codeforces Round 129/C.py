# Double Sort

def isSorted(array):
    if len(array) == 1:
        return True 
    prev = array[0]
    for num in array:
        if num < prev:
            return False
        prev = num 
    return True 


def solve(n, a, b):
    if isSorted(a) and isSorted(b):
        print(0)
        return
        
    swaps = []
    #bubble sort
    for i in reversed(range(n)):
        for j in range(0, i):
           
            if a[j] > a[j + 1]:
                if b[j] < b[j + 1]:
                   
                    print(-1)
                    return 
                else:
                    swaps.append((j + 1, j + 2))
                    a[j], a[j + 1] = a[j + 1], a[j]
                    b[j], b[j + 1] = b[j + 1], b[j]
                    continue 
            elif a[j] == a[j + 1]:
                if b[j] > b[j + 1]:
                    swaps.append((j + 1, j + 2))
                    a[j], a[j + 1] = a[j + 1], a[j]
                    b[j], b[j + 1] = b[j + 1], b[j]
                    continue 
            else:
                if b[j] > b[j + 1]:
                    
                    print(-1)
                    return 
                

    if isSorted(a) and isSorted(b):
        print(len(swaps))
        for swap in swaps:
            print(swap[0], swap[1])
    else:
        
        print(-1)
        return 



def main():

    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        solve(n, a, b)
        #print("Case #{}: {}".format(i + 1, y))
        

if __name__ == "__main__":
    main()