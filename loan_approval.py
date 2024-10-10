trust_score = input("What is your trust score? ")
trust_score = int(trust_score)
MAX_LIMIT = 500
MIN_LIMIT = 1

if trust_score >= 350 and trust_score <= 500:
    print("You have been deemed to be credit-worthy! Continue with a certified APR of just 6%!")
elif trust_score >= 280 and trust_score <= 349:
    print("You have been deemed to be credit-worthy! Continue with an APR of 10%!")
elif trust_score >= 200 and trust_score<= 279:
    print("You have been deemed to be credit-worthy! Continue with an APR of 12%!")
elif trust_score >= 199 and trust_score <= 50:
    print("You might be credit-worthy! Continue application, note APR will be 18+%")
elif trust_score < 1 or trust_score > 500:
    print("Trust score must be between 1 and 500!")
else:
    print("Sorry, you must call 555-555-5555 to continue with the application process.")

# Was kind of thinking about CHEX systems while doing this, note this is purely meant for practing with python - Hayden White 10/10
