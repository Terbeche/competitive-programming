from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        count1 = defaultdict(list)
        count2 = defaultdict(list)
        
        for i in range(len(s)):
            count1[s[i]].append(i)
        
        for i in range(len(t)):
            count2[t[i]].append(i)

        list_count1 = [freq for letter, freq in sorted(count1.items(), key=lambda x:x[1])]
        list_count2 = [freq for letter, freq in sorted(count2.items(), key=lambda x:x[1])]
        
        return list_count1 == list_count2
   