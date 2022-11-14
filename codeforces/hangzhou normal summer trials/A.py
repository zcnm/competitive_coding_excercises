# Game With Cards
def solve(s):
    target = "hznu"
    total = 0
    i = 0
    n = len(s)
    while i < n:
        if s[i] == 'h':
            
            if s[i: i + 4] == "hznu":
                total += 1
                i += 3
        i += 1
    return total
    
    

def main():

    s = input()
    print(solve(s))
        

if __name__ == "__main__":
    main()