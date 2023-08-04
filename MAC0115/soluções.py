a = float(input("Determine um número não nulo"))
b = float(input("Determine um número qualquer"))
c = float(input("Determine mais um número qualquer"))
delta = b * b - 4 * a * c 
      
    if delta > 0: 
        print(" real and different roots ")
        print(-b + sqrt(delta)/(2 * a))
        print(-b - sqrt(delta)/(2 * a))
      
    elif delta == 0: 
        print(" real and same roots") 
        print(-b / (2 * a)) 
      
    else:
        print("Complex Roots") 
        print(- b / (2 * a), " + i", sqrt(delta)) 
        print(- b / (2 * a), " - i", sqrt(delta))