
u_number = int(input("Please give me a number... "))

if u_number % 4 == 0:
    print("{} is a multiple of 4".format(u_number))
elif u_number % 2 == 0:
    print("{} is even".format(u_number))
else:
    print("{} is odd".format(u_number))
