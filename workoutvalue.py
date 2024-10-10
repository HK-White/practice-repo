feedback = input("How many minutes do do you workout daily? Be honest, no judgement!")
feedback = int(feedback)

if feedback >= 60:
    print("That is amazing that you work out at least one hour daily! KEEP IT UP!")
elif feedback >= 30:
    print("You are right in the sweet-spot! If possible, try adding 10 minutes daily until you get to 60")
elif feedback >= 10:
    print("Any time you can fit in is excellent, but you and I are going to work on making more time for excercise. Good job being health-aware!")
else:
    print("Life is busy, I understand. But excercise is so important and I would love to see you fit in time to do a COMPLETE workout or two to start out!")


comfort = input("On a scale of 1-10, how comfortable do you feel working out? ")
comfort = int(comfort)

if comfort == 10:
    print("That is awesome that you feel this comfortable with fitness. Keep it at a 10, you sexy beast")
elif comfort >= 8:
    print("Great job, lets get you up to a 10")
elif comfort >= 5:
    print("Halfway to being a 10 at working out, we can get there champ, keep trying! You rock")
else:
    print("That is a good start, lets focus on adding more focus on your excercise")