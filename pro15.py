uma=input()
amu=map(int,input().split())
mom=[]
for g in amu:
    enum=bin(g)
    mom.append(enum)
fraud1=sorted(mom)
fraud1.reverse()
for h in fraud1:
    print(int(h,2))
