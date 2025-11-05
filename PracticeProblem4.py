num=input("Enter a range: ")
num=int(num)

i=1

while(i<=num):
    if(i%2==0 and i%7==0):
        print(i)
    
    i+=1
