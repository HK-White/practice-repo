overdue_count = int(input("How many days is your book overdue? Be honest, we will check to verify! "))

min_fee = 1 * overdue_count
mid_fee = 2 * overdue_count
max_fee = 5 * overdue_count

if overdue_count <= 5:
    print(f"Your fee is ${min_fee}")
elif overdue_count <= 10:
    print(f"Your fee is ${mid_fee}")
elif overdue_count > 10:
    print(f"Your fee is ${max_fee}")
if overdue_count <= 5:
    print(f"Your fee is ${min_fee}")
elif overdue_count <= 10:
    print(f"Your fee is ${mid_fee}")
else:
    print(f"Your fee is ${max_fee}")

# Had to read documentation to figure this one out, sorry if not completely following PEP8
