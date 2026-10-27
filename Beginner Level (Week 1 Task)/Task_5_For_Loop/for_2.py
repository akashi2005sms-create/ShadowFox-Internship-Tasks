totaljj = 100
completedjj = 0

for i in range(10):
    print("Please perform 10 jumping jacks...")
    print("You are doing 10 jumping jacks...")
    print("1..2..3..4..5..6..7..8..9 and 10. Done :)")
    completedjj += 10
    remainingjj = totaljj - completedjj

    if completedjj == 100:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()

    if tired in ["yes","y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()

        if skip in ["yes","y"]:
            print(f"You completed a total of {completedjj} jumping jacks.")
            break

    elif tired in ["no","n"]:
        print(f"{remainingjj} jumping jacks are remaining")