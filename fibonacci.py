number_of_terms = 20
num_1, num_2 = 0, 1
count = 0
print("Fibonacci sequence:")
while count < nterms:
    print(num_1)
    nth = num_1 + num_2
    num_1 = num_2
    num_2 = nth
    count += 1
