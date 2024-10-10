rating = input("To calculate if you can see a movie, please enter your age ")
rating = int(rating)

if rating >= 18:
    print("You can see an R rated movie and:")
    print("PG-13 rated movies,")
    print("G rated movies and,")
    print("PG rated movies.")
elif rating >= 13:
    print("You can see PG-13 rated movies and:")
    print("G rated movies, as well as:")
    print("PG rated movies.")
elif rating >= 10:
    print("You can see G and PG rated movies only")
else:
    print("Sorry about that. You should check local laws and refer to theater policy")