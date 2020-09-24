x=int(input("Enter the first interger"))
y=int(input("Enter the second integer:"))

if x!=0 & (y%x)==0:
    print(x, "is multiple of ",y)
else:
    print("its not")




x=int(input("Enter the grade: "))
if x>=90:
    print("Your grade is A")
elif x>= 80:
    print("Your grade is B")
elif x>=70:
    print("Your grade is C")
else:
    print("Your grade is F")
