matrix1 = [[1,2],[5,6]]
matrix2 = [[3,4],[7,8]]
max1 = 0
max2 = 0
for i in range(2):
     for j in range(2):
          if matrix1[i][j]>0:
               max1 = matrix1[i][j]
          else:
               max1 = max1
for i in range(2):
     for j in range(2):
          if matrix2[i][j]>0:
               max2 = matrix2[i][j]
          else:
               max2 = max2
if max1>max2:
     print(max1)
else:
     print(max2)
