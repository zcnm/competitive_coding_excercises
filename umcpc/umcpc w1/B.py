# Patrick and Shopping    
# ------------------------------------------------

def main():
    d1, d2, d3 = [int(num) for num in input().split()]
    print(min(d1 + d2 + d3, d1 + d1 + d2 + d2, d1 + d3 + d3 + d1, d2 + d3 + d3 + d2))

if __name__ == "__main__":
    main()