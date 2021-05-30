
list1 = [12, -7, -4, 5, 64, -14]
list2 = [12, 14, -95, 3]

posiNumL1 = [i for i in list1 if i >= 0]
posiNumL2 = [j for j in list2 if j >= 0]

print("Positive numbers in the list1: ", *posiNumL1)
print("Positive numbers in the list2: ", *posiNumL2)
