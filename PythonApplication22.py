def getfilms():
   films=[]
   for x in range(5):
       films.append(input("Please enter your film:"))
   return films

def getratings(films):
    ratings={}
    for film in films:
        rating=float(input("Please enter your comment (0 to 5):"))
        ratings[film]=rating
    return ratings

def findbestfilm(ratings):
    bestfilm=max(ratings)
    return bestfilm

films=getfilms()
ratings=getratings(films)
bestfilm=findbestfilm(ratings)
print(f"The best movie based on user opinion:{bestfilm}")