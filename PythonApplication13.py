Movies=["Mr.&Mrs.Smith","Inception","Tenet"]
Moviesscore=[0,0,0]
cond="yes"
score=0
while cond=="yes":
    print("please submit the score:(0 to 5)")
    index=0
    for x in Movies:
        score=int(input(f"please enter your rate {x}:"))
        if score<=5 and score>=0:
            Moviesscore[index]+=score
        else:
            print("this score is not save!")
            break
        index+=1
    print("thanks for your rate.")
    cond=input("do you want continue? yes/no")
    


print(Movies)
print(Moviesscore)
maxscore=max(Moviesscore)
maxscoreindex=Moviesscore.index(maxscore)
bestMovie=Movies[maxscoreindex]
print( "the final result of polling:\n",maxscore,"is maximum score.")
