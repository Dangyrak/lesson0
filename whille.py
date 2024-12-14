my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_number=[]
index=0
while index<len(my_list):
    if my_list[index]<0:
        break
    if my_list[index]>0:
        positive_number.append((my_list[index]))

    index+=1
for my_list in positive_number:

    print(my_list)