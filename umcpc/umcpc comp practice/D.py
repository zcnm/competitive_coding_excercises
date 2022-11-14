#Bon Appetit
def solve(compartments):
    total = 0
    for compartment in compartments:
        people = compartments[compartment]
        people.sort(key = lambda x: x[1])
        prevFin = 0
        for person in people:
            start, finish = person
            if start >= prevFin:
                total += 1
                prevFin = finish 
    return total
    
# ------------------------------------------------

def main():
    T = int(input())
    
    for i in range(T):
        compartments = {}
        N, K = [int(num) for num in input().split()]
        for j in range(N):
            s, f, p = [int(num) for num in input().split()]
            if p not in compartments:
                compartments[p] = []
            compartments[p].append((s,f))

        print(solve(compartments))
if __name__ == "__main__":
    main()