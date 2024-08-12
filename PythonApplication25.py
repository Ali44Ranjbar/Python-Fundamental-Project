print("\t\t-----welcome to my store-----")
print("\n")
name=input("please enter your name:")
familyname=input("please enter your family name:\n")
lesson1=input("Enter your course name:")
grade1=int(input("enter your grade:"))
lesson2=input("Enter your course name:")
grade2=int(input("enter your grade:"))
lesson3=input("Enter your course name:")
grade3=int(input("enter your grade:"))
lesson4=input("Enter your course name:")
grade4=int(input("enter your grade:"))
print("\n")
total=grade1+grade2+grade3+grade4
def new_func(total):
    ave=total/len(total)
    return ave
