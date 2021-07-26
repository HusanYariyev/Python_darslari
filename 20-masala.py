matrix1 = [[1,2],[5,6]]
matrix2 = [[3,4],[7,8]]
a = [[0,0],[0,0]]

for i in range(2):
     for j in range(2):
          a[i][j] = matrix1[i][j] + matrix2[i][j]
print(a)
