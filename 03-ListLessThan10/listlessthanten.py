#print all elements less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for aa in a: 
    if aa < 5: print(aa)


# make a new list of all elements less than 5 
# print that
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
bbb = []
for bb in b:
    if bb < 5:
        bbb.append(bb)

print(bbb)


# print all numbers that are less than user 
# inputed number

u_number = int(input("Please give me a number... "))
for aa in a:
    if aa < u_number: print(aa)
