uma,san = input().split()
san = int(san)
fake1 = False
bent = list(map(int,input().split()))
for i in range(len(bent)):
    for j in range(len(bent)):
        if bent[i]+bent[j] == san:
            fake1 = True
print("yes" if fake1 else "no") 
