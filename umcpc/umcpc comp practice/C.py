#Unique Nicknames 
def solve(people, names):

    for person in people:
        first, last = person
        if names[first] > 1:
            if names[last] > 1:
                return "No" 
    return "Yes"
    
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
    N = int(input())
    people = []
    names = {}
    for i in range(N):
        first, last = input().split()
        people.append((first, last))
        
        if first not in names:
            names[first] = 0
        if last not in names:
            names[last] = 0
        
        names[first] += 1
        if first != last:
            names[last] += 1

    
    print(solve(people, names))

if __name__ == "__main__":
    main()