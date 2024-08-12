Programminglanguagelist=["python","java","c++","csharp"]
userlang=input("Enter the programming language you want:")

i=0
for x in Programminglanguagelist:
    if x==userlang:
        print("This Programminglanguage is taken by some body!")
        break
    elif i==len(Programminglanguagelist)-1 :
        print("submitted  in the program list:")
    i+=1
