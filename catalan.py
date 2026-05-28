n=int(input("Enter the value of n for Catalan number: "))
def catalan(n):
    if n==0:
        return 1
    else:
        return ((4*n-2)*catalan(n-1))//(n+1)
print("The", n, "th Catalan number is:", catalan(n))