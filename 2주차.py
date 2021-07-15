#수 정렬하기
n=int(input())
List=[]
for i in range(5):
    a=int(input())
    List.append(a)
List.sort()
for i in List:
    print(i)

#소트인사이드
n=input()
num=list(n)
num.sort()
for i in num:
    print(i,end="")
print()

#수 정렬하기2
n=int(input())
List=[]
for i in range(n):
    List.append(int(input()))
List.sort()
for i in List:
    print(i)

#좌표 정렬하기
def addList():
    cd=[]
    x,y=map(int,input().split())
    cd.append(x)
    cd.append(y)

    return cd

def makeList(n):
    List=[]
    for i in range(n):
        List.append(addList())
      
    return List

def listSort(x):
    for i in range(1,len(x)):
        j=i
        while j>0 and x[j-1][0]>=x[j][0]:
            x[j-1],x[j]=x[j],x[j-1]
            if x[j-1][0]==x[j][0]:
                if x[j-1][1]>x[j][1]:
                    x[j-1],x[j]=x[j],x[j-1]
                else:
                    x[j-1],x[j]=x[j-1],x[j]
            j-=1
            
    return x 

n=int(input())
x=makeList(n)
y=listSort(x)
for i in y:
    for j in i:
        print(j,end=" ")
    print()

#좌표 정렬하기2
def addList():
    cd=[]
    x,y=map(int,input().split())
    cd.append(x)
    cd.append(y)

    return cd
def makeList(n):
    List=[]
    for i in range(n):
        List.append(addList())
    
    
    return List

def listSort(x):
    for i in range(1,len(x)):
        j=i
        while j>0 and x[j-1][1]>=x[j][1]:
            x[j-1],x[j]=x[j],x[j-1]
            if x[j-1][1]==x[j][1]:
                if x[j-1][0]>x[j][0]:
                    x[j-1],x[j]=x[j],x[j-1]
                else:
                    x[j-1],x[j]=x[j-1],x[j]
            j-=1
            
    return x 

n=int(input())
x=makeList(n)
y=listSort(x)
for i in y:
    for j in i:
        print(j,end=" ")
    print()

#나이순 정렬
def addList():
    cd=[]
    x,y=input().split()
    x=int(x)
    cd.append(x)
    cd.append(y)

    return cd
def makeList(n):
    List=[]
    for i in range(n):
        List.append(addList())
    
    
    return List

def listSort(x):
    for i in range(1,len(x)):
        j=i
        while j>0 and x[j-1][0]>=x[j][0]:
            x[j-1],x[j]=x[j],x[j-1]
            if x[j-1][0]==x[j][0]:
                x[j-1],x[j]=x[j-1],x[j]
            j-=1
            
    return x 

n=int(input())
x=makeList(n)
y=listSort(x)
i=0
while i<len(y):
    print(y[i][0],end=" ")
    print(y[i][1])
    i+=1
print()

#국영수
def addList():
    cd=[]
    x,y,z,w=input().split()
    y,z,w=int(y),int(z),int(w)
    cd.append(x)
    cd.append(y)
    cd.append(z)
    cd.append(w)

    return cd

def makeList(n):
    List=[]
    for i in range(n):
        List.append(addList())
    
    return List

def listSort(x):
    List=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','w','y','z']
    for i in range(1,len(x)):
        j=i
        while j>0:
            if x[j-1][1]<x[j][1]:
                x[j-1],x[j]=x[j],x[j-1]
                
            elif x[j-1][1]==x[j][1]:
                if x[j-1][2]>x[j][2]: 
                    x[j-1],x[j]=x[j],x[j-1]
                    
                if x[j-1][2]<x[j][2]:
                    x[j-1],x[j]=x[j-1],x[j]
                    
                if x[j-1][2]==x[j][2]:
                    
                    if x[j-1][3]>x[j][3]:
                        x[j-1],x[j]=x[j-1],x[j]
                        
                    if x[j-1][3]<x[j][3]:
                        x[j-1],x[j]=x[j],x[j-1]
                        
                    if x[j-1][3]==x[j][3]:
                        a=islow(x[j-1][0])
                        b=islow(x[j][0])
                        for i in List:
                            if i==a[0]:
                                a=int(List.index(i))
                                break
                            if i==b[0]:
                                b=int(List.index(i))
                                break
                                
                            if a>b:
                                x[j-1],x[j]=x[j],x[j-1]
                                
                            else:
                                x[j-1],x[j]=x[j-1],x[j]
                else:
                    x[j-1],x[j]=x[j-1],x[j]
            j-=1
            
    return x 

def islow(s):
    s=s.lower()
    ans=''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            ans+=c
    return ans
    
n=int(input())
x=makeList(n)
y=listSort(x)
for i in range(len(y)):
    print(y[i][0])

#수 정렬하기3
def addList(n):
    List=[]
    for i in range(n):
        a=int(input())
        List.append(a)
        
    return List

def listSort(x):
    for i in range(1,len(x)):
        j=i
        while j>0 and x[j-1]>x[j]:
            x[j-1],x[j]=x[j],x[j-1]
            j-=1   
    return x

n=int(input())
x=addList(n)
y=listSort(x)
for i in y:
    print(i)

#카드
n=int(input())
List=[]
for i in range(n):
    a=int(input())
    List.append(a)

count={}
for i in List:
    try:
        count[i]+=1
    except:
        count[i]=1

def my_max():
    i=0
    a=count[List[0]]
    num=List[0]
    while i<len(List):
        if a<count[List[i]]:
            a=count[List[i]]
            num=List[i]
        i+=1
    return num

print(my_max())

#k번째 수
n,k=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
print(nums[k-1])

#최소,최대
def my_max(num):
    a=num[0]
    for i in num:
        if i>a:
            a=i
    return a

def my_min(num):
    a=num[0]
    for i in num:
        if i<a:
            a=i
    return a

n=int(input())
num=list(map(int,input().split()))
print(my_min(num),end=" ")
print(my_max(num))

#최댓값
def my_max(num):
    a=num[0]
    for i in num:
        if i>a:
            a=i
    return a

def maxIndex(num):
    Index=0
    for i in num:
        if i==a:
            Index=num.index(i)+1
    return Index

num=[]
for i in range(9):
    a=int(input())
    num.append(a)
a=my_max(num)   
print(a)
print(maxIndex(num))

#숫자의 개수
def checknum(k):
    check=0
    for i in result:
        if i==k:
            check+=1
        else:
            pass
    return check
        
A=int(input())
B=int(input())
C=int(input())
result=str(A*B*C)
for k in range(10):
    k=str(k)
    print(checknum(k))

#나머지
def remainder(i):
    result=i%42
    return result

def checknum(resultList):
    new_list=[]
    for i in resultList:
        if i not in new_list:
            new_list.append(i)
        else:
            pass
    length=len(new_list)
    return length


num=[]
for i in range(10):
    a=int(input())
    num.append(a)
    
resultList=[]
for i in num:
    resultList.append(remainder(i))

print(checknum(resultList))

#평균
def my_max(grade):
    a=grade[0]
    for i in grade:
        if i>a:
            a=i
    return a

def my_grade(grade):
    Max=my_max(grade)
    new_grade=[]
    for i in grade:
        new=i/Max*100
        new_grade.append(new)
    
    return new_grade

def my_avg():
    avg_grade=my_grade(grade)
    Sum=0
    for i in avg_grade:
        Sum+=i
    result=Sum/len(avg_grade)
        
    return result

n=int(input())
grade=list(map(int,input().split()))
print(my_avg())

#OX퀴즈
def grade(i):
    result=1
    new_sum=0
    for k in range(len(i)):
        if i[k]=='O':
            if k+1==len(i):
                if i[k-1]=='O':
                    new_sum+=result
                    break
                else:
                    break
            else:
                if i[k+1]=='O':
                    new_sum+=result
                    result+=1
    
                else:
                    if result==1:
                        new_sum+=result
                    else:
                        new_sum+=result
                        result=1
        else:
            result=1
            
    return new_sum

n=int(input())
List=[]
for i in range(n):
    a=input()
    List.append(a)
    
for i in List:
    print(grade(i))

#평균은 넘겠지
n=int(input())
for i in range(n):
    num=list(map(int,input().split()))
    avg=sum(num[1:])/num[0]
    cnt=0
    for i in num[1:]:
        if i>avg:
            cnt+=1
            
    result=cnt/(len(num)-1)*100
    
    print(f"{result:.3f}%")
    
#정수 N개의 합
def solve(a):
    ans = 0
    for i in a:
        ans+=i
    return ans

#셀프넘버
def d(n):
    result=0
    for i in list(str(n)):
        result+=int(i)
        
    return result+int(n)

List=[]
for i in range(1,10001):
    a=d(i)
    List.append(a)

for i in range(1,10001):
    if i not in List:
        print(i)
    else:
        pass

#한수
def han(n):
    result=0
    if n<100:
        return n
    else:
        for i in range(100,n+1):
            A=i//100
            B=(i%100)//10
            C=i%10

            if (A-B)==(B-c):
                result+=1
        return result+99
        if 
n=int(input())
print(han(n))