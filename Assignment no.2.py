# Python Assignment no.2

# QUESTION NO.1

var1="Python is a case sensitive language"
# (a) Length of the input string.
print(len(var1))
# (b)Reversed order of the string in one line code.
print(var1[::-1])
# (c) “a case sensitive” stored in new string.
var2=(var1[10:27])
print(var2)
# (d) “a case sensitive” replaced by “object oriented”.
print(var1.replace("a case sensitive","object oriented"))
# (e) index of substring “a”
print(var1.index("a"))
# (f)white spaces removed from the given input string.
print(var1.replace(" ",""))

# QUESTION NO.2

print("Enter your good name")
v1=input()
print("Hey",v1," Here!")
print("Enter your SID")
v2=int(input())
print("My SID is ",v2)
print("Enter your Branch")
v3=input()
print("Enter your CGPA")
v4=int(input())
print("I am from ",v3,"department and my CGPA is",v4)

# QUESTION NO.3

a=56
b=10
print("The value of","a&b = ",a&b)
print("The value of","a|b = ",a|b)
print("The value of","a^b = ",a^b)
print("The value of","a<<2 = ",a<<2,"\nThe value of","b<<2 = ",b<<2)
print("The value of","a>>2 = ",a>>2,"\nThe value of","b>>4 = ",b>>4)


# QUESTION NO.4

print("Enter any sentence of your choice:-")
Var1=input()
if "name" in Var1:
    print("Yes")
else:
    print("No")

# QUESTION NO.5

print("This program determine if,the three sides entered by the use can form a triangle or not ?")
print("Enter first side of triangle:-")
side1=int(input())
print("Enter second side of triangle:-")
side2=int(input())
print("Enter third side of triangle:-")
side3=int(input())

A=side1<side2+side3
B=side2<side1+side3
C=side3<side2+side1

Result=str(A&B&C)
print("The sides entered by the use can form a triangle?")
Result=Result.replace("True","YES")
Result=Result.replace("False","NO")
print("The Answer is ",Result)

# QUESTION NO.6

a=int(input("Enter the value of a:-"))
b=int(input("Enter the value of b:-"))
c=(a^b)
d=bin(c)
count=0
for i in d[2:]:
    if i=="1":
        count+=1
    print(count)
