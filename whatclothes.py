condition_cold = input("Is it cold? (True/False): ")
condition_rain = input("Is it raining? (True/False): ")
condition_wind40 = input("Is it windy? (True/False): ")
condition_hot = input("Is it hot? (True/False): ")

if condition_cold == "True":
    print("Take a jacket, it is cold outside")
elif condition_hot == "True":
    print("Wear light clothing due to the heat!")
elif condition_rain == "True":
    print("Take an umbrella, it is raining!")
elif condition_wind40 == "True":
    print("Wear a windbreaker, it is windy!")
else:
    print("Enjoy your day!")