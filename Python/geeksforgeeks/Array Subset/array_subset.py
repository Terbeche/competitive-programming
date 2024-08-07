def isSubset( a1, a2, n, m):
    a1.sort()
    a2.sort()
    
    i = 0
    j = 0
    
    while i < n and j < m:
        if a1[i] == a2[j]:
            i += 1
            j += 1
        else:
            i += 1
        
        
    if j == m:
        return "Yes"
    else:
        return "No"
