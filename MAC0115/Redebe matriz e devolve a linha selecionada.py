
# A basic code for matrix input from user
  
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
# Initialize matrix
matrix = []

print("Enter the entries rowwise:")
  
# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)
  
# For printing the matrix
#for i in range(R):
#    for j in range(C):
#        print(matrix[i][j], end = " ")
#    print()

#i = int(input("Digite uma linha:"))
linha = []
coluna = []
i = int(input("Digite a linha para ser impressa:"))

for j in range(len(matrix[1])):
    linha.append(matrix[i][j])

j = int(input("Digite a coluna para ser impressa:"))
for i in range(len(matrix)):
    coluna.append(matrix[i][j])

print(linha, '  ', matrix, '  ' ,coluna)
