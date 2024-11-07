while True:

    weight = float(input("Enter your weight: "))
    unit = input("Is this in kilograms or pounds (K/L)? ")

    if unit.lower() == "k":
        weight = weight * 2.205
        unit = "Lbs"
    elif unit.lower() == "l":
        weight = weight / 2.205
        unit = "Kgs"
    else:
        print(f"{unit} was not a valid choice")
        continue

    print(f"Your newly converted weight is: {round(weight, 1)} {unit}")

    play_again = input("Would you like to still play: (Y/N) ")

    if play_again.lower() == "y":
        continue
    elif play_again.lower() == "n":
        print("Thank you for converting!")
        break
    else:
        print(f"{play_again} was not a valid choice, exiting program.")
        break
