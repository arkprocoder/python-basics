# for loop & fstrings
'''1. Print the tables by taking input 
ex 4 X 1= 4

#functions

2.Take a input for to find an area of the rectangle
l*b

1.
def funcation_name(length & breadth):
    logic

take inputs(length & breadth)
funcation_name(length & breadth)
2.circle
3.square
4.triangle
'''

# 1
# num = int(input("Enter the Table Number:\n"))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i} ")

#2.



def rectangle(l,b):
    print(f"Area of the rectangle is {l*b}")

def square(a):
    print(f"Area of the Square is {a*a}")

def triangle():
    pass

def circle(r):
    print(f"Area of the Circle  is {3.14*r*r}")


print("Rectangle.....\n")
l=int(input("Enter the length:\n"))
b=int(input("Enter the Breadth:\n"))
rectangle(l,b)

print("\n")
print("Square.....\n")
a=int(input("Enter the sides:\n"))
square(a)

print("\n")
print("Circle.....\n")
r=int(input("Enter the radius:\n"))
circle(r)