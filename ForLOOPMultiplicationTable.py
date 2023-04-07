#Multiplication Tables

"""
num=int(input("Which multiplication table need to print: "))

t=int(input("Till to be printed"))

for i in range(t):
    print(num*i)

"""

t=input("What tables to display")
t=int(t)
for i in range(11):
    print(t,"X",i,"=",t*i)