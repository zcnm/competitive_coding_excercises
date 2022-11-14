class Solution:
    def solve(self, x, target, array):
        dp = {}
        def recurse(y, i):
            if i == len(array) - 1:
                if y ^ array[-1] == target or y + array[-1] == target:
                    return True
                dp[(y, i)] = 0
                return False
            if (y, i) in dp:
                return False
            return recurse(y + array[i], i + 1) or recurse(y ^ array[i], i + 1)
                
        if recurse(x, 0):
            return "Alice"
        return "Bob"
        
    
    
def main():
    solution = Solution()
    numInputs = int(input())
    for i in range(numInputs):
        n, x, y = map(int, input().split())
        array = list(map(int, input().split()))
        output = solution.solve(x, y, array)
        print(output)
main()