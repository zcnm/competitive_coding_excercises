# Color with Occurrences
# ------------------------------------------------
#helper functions
def printArray(array):
    output = ""
    for num in array:
        output += str(num) + " "
    print(output[:-1])
    return
# ------------------------------------------------
def solve(text, covers):
    print(text)
    
        
        

def main():
    t = int(input())
    for _ in range(t):
        text = input()
        n = int(input())
        covers = []
        for _ in range(n):
            cover = input()
            covers.append(cover)
    
        solve(text, covers)
    return


if __name__ == "__main__":
    main()