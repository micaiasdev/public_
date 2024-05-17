
n = [94,1,3,4,88,14,33,71,5]

aux = 0
c = len(n)

for i in range(len(n)):
  for j in range(1, c):
    if n[j - 1] > n[j]:
      aux = n[j]
      n[j] = n[j - 1]
      n[j - 1] = aux
  c = c - 1
  
print(n)
  
    
     
  
  
    