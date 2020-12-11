
products = ['appel', 'aap', 'opa', 'bompa', 5, True, True] 


seen = {}
dupes = []

for x in products:
    if x not in seen:
        seen[x] = 1
    else:
        if seen[x] == 1:
            dupes.append(x)
        seen[x] += 1

print(seen)

