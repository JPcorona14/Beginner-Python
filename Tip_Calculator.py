print("Welcome to the tip calculator!")

bill = float(input("How much is the bill? $"))
people = int(input("How many people will it be split through?"))
tip = float(input("How much will the tip be? 10, 12, or 15?")) * 0.01

print(f"Each person should pay ${str(round(((bill * tip) + bill) / people ,2))}")
