#Program Seson4 % T-1 Day-9 % 99-01-06
import math
list_1 =[]
no_1 = int(input())
for i in range (0,no_1):
    list_1.append(int(input()))
# print (list_1)
for t in range(0 ,no_1):
    # print ("%.4f" % (math.sqrt(lt_1[t])))
    no_2 = (math.sqrt(list_1[t]))
    no_2 = str(no_2)
    no_2 = no_2 + "0000"
    print (no_2)
    text=str()
    for item in range(len(no_2)):
        print (no_2[item])
        text = text + no_2[item]
        if no_2[item] == ".":
            text_2 = (no_2[(item+1):])
            break
    print(text + text_2[:4])