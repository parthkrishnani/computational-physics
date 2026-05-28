from myfunctions import binomial
n=int(input("Enter the number of rows for Pascal's Triangle: "))+1
for i in range(2, n+1):
    r=[]
    for j in range(0, i):
        r.append(binomial(i-1, j))
    print(r)