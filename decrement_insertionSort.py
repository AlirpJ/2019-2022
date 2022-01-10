A=[2,6,7,4,7,22,2,5,4]

for j in range(1,len(A),1): 
    # Iterate through, comparing two elements
    k = A[j]
    i = j - 1
    while i>=0 and A[i]<k:
        # Swap if necessary
        A[i+1]=A[i]
        i=i-1
    A[i+1]=k


print(A)