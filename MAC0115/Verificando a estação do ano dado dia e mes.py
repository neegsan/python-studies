d = int(input("dia:"))
m = int(input("mes:"))

if  (( 22 <= d ) and ( 9 == m )) or (( 9 < m ) and ( m < 12 )) or (( d < 21 ) and ( m == 12 )) :
    print("1")

elif (( 21 <= d ) and ( m == 12)) or (( 1 <= m ) and ( m < 3 )) or (( d < 20 ) and ( m == 3 )) :
    print("2")

elif (( 20 <= d ) and ( m == 3)) or (( 3 < m) and ( m < 6 )) or (( d < 20 ) and ( m == 6 )) :
    print("3")
else :
    print("4")
