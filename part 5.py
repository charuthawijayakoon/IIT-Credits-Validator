run_ok=True
pro=int()
tra=int()
ret=int()
exc=int()
Li=[]
while(run_ok):
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
    Li.append([p,d,f])

    print()
    
    print("Would you like to enter another set of data?")
    x=str(input("Enter \'y\' for yes or \'q\' to quit and view results: "))

    print()
    
    if (x=="y" or x=="Y"):
        run_ok=True
    else:
        run_ok=False
        
print()        

i=len(Li)
for i in range (0,i):
    x=Li[i]
    p=x[0]
    d=x[1]
    f=x[2]
    if (p==100) and ((d==20)or(f==20)):
        msg="Progress(module trailer)"
        tra+=1
    if (p==120):
        msg="Progress"
        pro+=1
    if(p+f+d)==120:
        if f>=80:
            msg="Exclude"
            exc+=1
        elif p<100:
            msg="Do not progress-module retriver"
            ret+=1
    else:
        msg="Total Incorrect"
    print(msg)
    
print()    

print('HoriZontal Histogram')
print("Progress 1   :",'*'*pro)
print("Trailing 2   :",'*'*tra)
print("Retriever 4  :",'*'*ret)
print("Excluded 3   :",'*'*exc)
    
    


           
    
