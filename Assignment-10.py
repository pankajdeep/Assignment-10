#Q.1- Write a Python program to read n lines of a file
f=open('assq1.txt','r')
n=int(input("Enter Number of lines you want to read"))
for i in range(n):
    print(f.readline())
f.close()


#Q.2- Write a Python program to count the frequency of words in a file.
f=open('assq1.txt','r')
li=(f.read()).split()
size=len(li)
for i in range(size):
    count=1
    flag=0
    for j in range(i+1,size):
        if(li[i]==li[j]):
            count=count+1
    for k in range(i-1,0,-1):
        if(li[i]==li[k]):
            flag=1
            break
    if(flag==0):
        print(li[i],"has count of",count)
f.close()


#Q.3- Write a Python program to copy the contents of a file to another file
f=open('assq1.txt','r')
f2=open('assq3.txt','w')
data=f.read()
f2.write(data)
f.close()
f2.close()


#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
f1=open('assq1.txt','r')
f2=open('assq3.txt','r')
li=f1.readlines()
li2=f2.readlines()
l1=len(li)
l2=len(li2)
if(l1>l2):
    l=l2
else:
    l=l1
for i in range(l):
    print(li[i].strip('\n')+li2[i].strip('\n'))
f1.close()
f2.close()


#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
import random
f1=open('assq5.txt','r+')
for i in range(10):
    f1.write(str(random.random()))
    f1.write('\n')
ls1=f1.readlines()
ls1.sort()
f2=open('anotherfile.txt','w')
for i in ls1:
    f2.write(i)
f1.close()
f2.close()

    
