def pascal(row, column):
  if (column == 1):
    return 1
  if (row == column):
    return 1
  
  left = pascal(row-1, column-1)
  right = pascal(row-1, column)
  return left + right

#driver function
n = int(input())
for r in range(1,n+1):
  for col in range(1, r + 1):
    print(pascal(r, col), end='')
  print("")

