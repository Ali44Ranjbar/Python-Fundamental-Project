usernamelist=[]
passwordlist=[]

print("\n\t---------------SingUp to panel and make your profile:---------------------")
cond="y"
while cond=="y": #for all users
        while True: #for user to make profile
           uname=input("please enter a new username:")
           if uname  not in usernamelist:
               print("this username approved! please set a password now:")
               usernamelist.append(uname)
               passwordlist.append(input("set a password:"))
               print("you have a profile here! cogrates")
               break # to stop making profile
           else:
               print("this username is reserved by someone!")
        cond=input("do you want continue? y/n")

print("\n\t-----------------Login Panel------------------")
cond="yes"
while True:
  print("dear member Login page guides you to your profile:")  
  u=input("please enter username:")
  p=input("please enter password:")

  if u in usernamelist and p==[usernamelist.index(u)]:
      print("\t\t---------wlecome to your profile----------.")
  else:
      print("incorrect username or password, try again!")
      for x in range(1,4):
          u=input("please enter username:")
          p=input("please enter password:")
          if u in usernamelist and p==[usernamelist.index(u)]:
              print("wlecome to your profile")
              break
          elif x==2:
              print("this the last chace!")
  if input('To stop login panel press s ')=='s':
      break








