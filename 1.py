count = 1
output = str()
n = int(input ())
while count <= n+1 :
  for i in range(1,count):
    output +=str(i)
  print(output)
  output = ''
  count += 1
