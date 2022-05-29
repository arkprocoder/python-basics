# # age=18

# # if(age>=18):
# #     print("No")
# # else:
# #     print("Yes")


# # print("Over")


# a=10
# b=5

# if(b<a):
#     print("Yes b is less than a")
#     a=12
#     b=12
#     print(a+b)
#     print("Hey how areyou")
# # print("aa")
# elif(b>a):
#     print("b is greater than a")


# elif(a>b):
#     print("Yes a is greater than b")


# else:
#     print("Nothing")
#     print("Nothing")
#     print("Nothing")
#     print("Nothing")
#     print("Nothing")

# print("aaa")

# Take a input as age from the User 
# "Enter Your Age"

# age<18:You cannot Vote
# age >=18:You can Vote if you have Voter ID
# age>70:You cannot  Vote pleas enjoy your rest of the life...
# age >100: Rest in Peace

age= int(input("Enter Your Age:\n"))
if(age<18):
    print("You cannot Vote...")
elif(age>=18 and age<=70):
    print("You can vote if you have voter Id")
elif(age>70 and age<100):
    print("You cannot  Vote pleas enjoy your rest of the life...")
else:
    print("Rest in Peace")
