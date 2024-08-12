usernamelist=[]
passwordlist=[]

print("\n\t----------------SingUp to system or panel and make your profile:----------------")
while True:
    uname=input("please enter new username:")
    i=0
    if len(usernamelist)!=0:
        for x in usernamelist:
            if x==uname:
                print(" this username is taken by some body!")
                break
            elif i==len(usernamelist)-1 :
                print(" this user submitted for you:")
                usernamelist.append(uname)
                password=input("please set the password:")
                passwordlist.append(password)
                print("your profile is ready now,enjoy it!")
                break
            i+=1
    else:
        usernamelist.append(uname)
        passwordlist.append(input("please set the password:"))
    if input("<press ENTER for next membership SingUp>")!="":
        break
