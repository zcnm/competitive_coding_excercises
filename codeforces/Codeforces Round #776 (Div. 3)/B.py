def solve(l, r, a):
    if r // a > a - 1:
        return r // a + r % a 
    else:
        best = r - (r % a) - 1
        
        if best < l:
            return r // a + r % a
        return best // a + best % a
       
def main():
    numInputs = int(input())
    for i in range(numInputs):
        line = input()
        l, r, a = list(map(int, line.split()))
        output = solve(l, r, a)
        print(output)
        
         
if __name__ == "__main__":
    main()