
nu_dic = {}
list_keys = []
list_big = []
#cdef to chek number is prime
def is_prime(n):
   if n <= 1:
      return False
   else:
      for i in range(2, n):
         # checking for factor
         if n % i == 0:
            # return False
            return False
      # returning True
   return True
#for to give input for n number 
n = 4
for row in range(0,n):
    count = 0
    number = int(input())
    for item in range(1,number):
        if number % item ==0:
            if is_prime(item)==True:
                count+=1
    nu_dic[number] = count
    list_keys.append(count)
print(nu_dic)
list_keys.sort()
print(list_keys)
for item_2 in (nu_dic):
    if nu_dic[item_2] == list_keys[-1]:
        list_big.append(item_2)
list_big.sort(reverse=True)
print(list_big)
print(list_big[0],nu_dic[list_big[0]])

