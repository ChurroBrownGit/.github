import json
l1 = []
l2 = []
with open('yourmom.json') as f:
    lisr = json.load(f)
for i in range(len(f)):
    if (i%2) == 2:
        l1.append(f[i])
    else:
        l2.append(f[i])
print(l1)