qwer1,qser1=map(int,input().split())
law1=list(map(int,input().split()))
qwer1=[]
law1.insert(0,0)
for p in range(chet1):
     vim1=[]
     cat=0
     but1,zee1=map(int,input().split())
     for i in range(but1,zee1+1):         
         cat^=law1[i]     
     qwer1.append(cat)
for p in qwer1:
     print(p)
