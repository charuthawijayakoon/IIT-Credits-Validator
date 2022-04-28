p=input("Please enter your credits at pass: ")
while(p.isalpha()):
    print("Integer required")
    p=input("Please enter your credits at pass: ")
p=int(p)
while p % 20 != 0:
    print("Out of range")
    p=int(input("Please enter your credits at pass: "))
d=int(input("Please enter your credits at defer: "))
while d % 20 != 0:
    print("Out of range")
    d=int(input("Please enter your credits at defer: "))
f=int(input("Please enter your credits at fail: "))
while f % 20 != 0:
    print("Out of range")
    f=int(input("Please enter your credits at fail: "))
if (p==100) and ((d==20)or(f==20)):
    msg="Progress(module trailer)"
if (p==120):
    msg="Progress"
if(p+f+d)==120:
    if f>=80:
        msg="Exclude"
    elif p<100:
        msg="Do not progress-module retriver"
else:
    msg="Total Incorrect"

print(msg)    
    


           
    
