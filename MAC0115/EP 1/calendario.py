n = 1
nosl = 0
pule = 2
branco = 1

print("  Dom  Seg  Ter  Qua  Qui  Sex  Sab")

p = 1
q = 32

pule = 1
branco = 1
while branco <= pule:
    print("     ", end='')
    branco = branco + 1

nosl = pule
num = p
while num < q:
    nosl = nosl + 1
    if nosl % 7 == 0:
        print(f"{num:5d}")
    else:
        print(f"{num:5d}", end='')
    num = num + 1
