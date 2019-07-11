uma,san = input().split()
san = int(san)
fake1 = False
cut = list(map(int,input().split()))
for i in range(len(cut)):
    for j in range(len(cut)):
        if cut[i]+cut[j] == san:
            fake1 = True
print("yes" if fake1 else "no") 
