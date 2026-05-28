import numpy as np
prime=[2]
n=int(input("Enter the maximum number you want: "))
for i in range(3, n+1, 2):
    for j in range (3, int(np.sqrt(i))+1):
        if i%j == 0:
            break
    else:
        prime.append(i)
print("The prime numbers up to", n, "are:", prime)