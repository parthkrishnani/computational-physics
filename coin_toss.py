from myfunctions import binomial
n=int(input("Enter the number of coin tosses: "))
k=int(input("Enter the number of heads: "))
print("The probability of getting exactly", k, "heads in", n, "tosses is", binomial(n, k) * (0.5**n))
p = 0
for i in range(k, n+1):
    p += binomial(n, i) * (0.5**n)
print("The probability of getting at least", k, "heads in", n, "tosses is", p)