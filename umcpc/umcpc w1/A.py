# In Search of an easy problem     
# ------------------------------------------------

def main():
    n = int(input())
    responses = [int(num) for num in input().split()]
    if sum(responses) == 0:
        print("EASY")
    else:
        print("HARD")

if __name__ == "__main__":
    main()