# Comparing Strings
# ------------------------------------------------
def solve(d1, d2):
    n = len(d1)
    if len(d2) != n:
        return "NO"
    if len(d1) == 1:
        return "NO"
    
    if d1 == d2:
        if len(set(d1)) < len(d1):
            return "YES"
        else:
            return "NO"
    
    first = None 
    for i in range(len(d1)):
       
        if d1[i] != d2[i]:
            
            if first is None:
                first = i 
            else:
                newString = list(d1)
                newString[i], newString[first] = newString[first], newString[i]
                if "".join(newString) == d2:
                    return "YES"
                else:
                    return "NO"
    return "NO"
def main():
    d1 = input()
    d2 = input()
    print(solve(d1, d2))
if __name__ == "__main__":
    main()