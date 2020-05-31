points = [9,3,2,4,7,3,5]

def partition(i,j)->int:
  pivot = points[j]
  l = i - 1
  for r in range(i,j):
    rv = points[r]
    print(r, points)
    if rv < pivot:
      l += 1
      points[l], points[r] = points[r], points[l]
  points[j], points[l+1] = points[l+1], points[j]
  return l+1

print(partition(0, len(points)-1))
print(points)