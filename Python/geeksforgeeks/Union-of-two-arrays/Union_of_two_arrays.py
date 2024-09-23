class Solution:    
    def doUnion(self,arr1,arr2):
        return len(set(arr1 + arr2))


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.doUnion(a, b))
