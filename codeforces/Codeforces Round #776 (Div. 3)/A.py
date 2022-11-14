def main():
    numInputs = int(input())
    for i in range(numInputs):
        s = input()
        c = input()
        output = solve(s,c)
        if output:
            print("YES")
        else:
            print("NO")
        
def solve(s, c):
    for i in range(len(s)):
        if s[i] == c:
            if i % 2 == 0:
                return True 
    return False 
        
if __name__ == "__main__":
    main()