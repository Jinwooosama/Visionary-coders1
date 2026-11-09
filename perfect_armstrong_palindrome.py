n=int(input("Enter your number"))
a=0
for i in range(1,n):
    if n%i==0:
        a+=i
if a==n:
    print("perfect number")
else:
    print("Not perfect number")