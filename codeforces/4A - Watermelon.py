class Solution:
    def watermelon(self,weight):
        if weight > 2 and weight % 2 == 0:
            return "YES"
        return "NO"
    
def main():
    solution = Solution()
    weight = int(input())
    output = solution.watermelon(weight)
    print(output)

main()