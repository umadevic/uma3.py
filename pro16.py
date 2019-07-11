app=int(input())
cad=list(map(int,input().split()))
xawt1=[1]*app
for pa in range(app):
    if pa==0:
        if cad[pa]>cad[pa+1]:
            xawt1[pa]=xawt1[pa]+xawt1[pa+1]
    elif pa>0:
        if cad[pa]>cad[pa-1]:
            xawt1[pa]=xawt1[pa]+xawt1[pa-1]
print(sum(xawt1))
