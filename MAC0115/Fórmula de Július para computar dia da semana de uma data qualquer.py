d = int(input("dia:"))
m = int(input("mês:"))
a = int(input("ano:"))

s = (d+(13*(m+1))//5 + a + (a//4) - (a//100) + (a//400)) % 7

print(s)
