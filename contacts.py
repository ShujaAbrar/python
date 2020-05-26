n=int(input())
l=[]
for i in range(n):
    x=list(map(str,input().split()))
    if x[0]=="add":
        l.append(x[1])
    if x[0]=="find":
        count=0
        for j in range(len(l)):
            if l[j].find(x[1])!=-1:
                count+=1
                l[j]="-1"
        print(count)
___________________________________________________
output:
sample input:
4
add mapit
add mapittech
find mapit
find teh
 sample output:
 2
 0
