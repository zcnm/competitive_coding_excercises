#Everyone Loves to Sleep
# ------------------------------------------------
#helper functions
def printArray(array):
    output = ""
    for num in array:
        output += str(num) + " "
    print(output[:-1])
    return
# ------------------------------------------------
def solve(H, M, alarms):
    minTime = 24 * 60 
    currTime = H * 60 + M 
    for h, m in alarms:
        alarmTime = h * 60 + m 
        if alarmTime < currTime:
            alarmTime += 24 * 60 
        diff = alarmTime - currTime 
        minTime =  min(minTime, diff)
    print(minTime // 60, minTime % 60)

def main():
    t = int(input())
    for _ in range(t):
        n, H, M = [int(num) for num in input().split()]
        alarms = []
        for _ in range(n):
            h, m = [int(num) for num in input().split()]
            alarms.append((h, m))
        solve(H, M, alarms)
    return

if __name__ == "__main__":
    main()