# for loop

# for i in range(0,100,5):
#     print(i)
    

# print("Over..............")

from time import sleep


mylist=["rice","wheat","ragi","biscuits","bread"]
name=input("Enter Your Name to Buy the Groceries:\n")

print("We are Shipped......")
sleep(5)
for grocery in mylist:    
    sleep(5)
    print(grocery)
sleep(3)
print("Delivered to ",name)