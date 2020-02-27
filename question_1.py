def prime(low,high,array):
        for i in range(low,high):
                flag=0
                for j in range(2,i):
                        if(i%j==0):
                                flag=1
                                break
                if (flag==0):
                   array.append(i) 
                       
array=[]
low = int(input())
high= int(input())

prime(low,high,array)

print("Prime numbers :: ")
for i in array:
        if i!=1:
                print(i)
