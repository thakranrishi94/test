print()
print()
print()
a=int(input("Enter the number:- "))
b=a
sum=0
while a>0:
    rem=a%10
    sum=sum+(rem*rem*rem)
    a=a//10
if(sum==b):
    print("The number is armstrong")
else:
    print("The number is not armstrong")
print()
print()
print()
