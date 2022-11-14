class Solution:
    def solve(self, s, k):
        ans = 0
        if k == 0:
            return 1
        
        if s == s[::-1]:
            return 1
        return 2
    
    
def main():
    solution = Solution()
    numInputs = int(input())
    for i in range(numInputs):
        n, k = map(int, input().split())
        s = input()
        output = solution.solve(s,k)
        print(output)
main()