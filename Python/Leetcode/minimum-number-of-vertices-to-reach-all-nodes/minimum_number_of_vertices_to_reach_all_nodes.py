class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        verses = set()
        answer = []

        for i in range(len(edges)):
            verses.add(edges[i][1])
        
        for number in range(n):
            if number not in verses:
                answer.append(number)

        return answer