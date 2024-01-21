t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['janvier', 'fevrier', "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]
t3 = []
d = {e:t1[i] for i, e in enumerate(t2)}

for i, e in enumerate(t2):
    t3.append(e)
    t3.append(t1[i])

print(t3, d)