import datetime

now = datetime.datetime.now()
cur_year = now.year

user_name = input("What's your name? ")
user_age = int(input("How old are you? "))
print_loop = int(input("How many times do you wan to see this? "))

yrs_to_100 = 100-user_age

for p in range(0, print_loop):
    print("Hello {}.  You will turn 100 in {} years.".format(user_name, yrs_to_100))

