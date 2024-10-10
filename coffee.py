sweet = input("Do you like sweet coffee? (True/False): ")
frappe = input("Do you like cold frappe? (True/False): ")
# Only two parameters to avoid over complexity for user -Hayden W 10/10

if sweet == "True" and frappe == "True":
    print("Order a vanilla bean frappe with marshmellows on top!")

elif sweet == "True" and frappe == "False":
    print("Order a caramel hot latte!")

elif sweet == "False" and frappe == "True":
    print("Order an americano frappe!")
elif sweet == "False" and frappe == "False":
    print("Order a cappuccino!")
else:
    print("Invalid input. Please enter True or False. Otherwise order a caramel-vanilla frappe!")
