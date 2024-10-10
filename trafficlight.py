traffic_light = input("What colour is the traffic light? ")

if traffic_light == "Red" or "red":
    print("Stop! Red means STOP!")
elif traffic_light == "Yellow" or "yellowre":
    print("Slow down! Yellow means SLOW DOWN!")
elif traffic_light == "Green" or "green":
    print("Go! Green means GO!")
else:
    print("That is not a valid traffic light colour.")

    # The lowercase version was added for each input value so that it will
    # print regardless of case for the first letter