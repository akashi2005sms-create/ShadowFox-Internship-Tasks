import random

count_6 = 0
count_1 = 0
count_two_6 = 0
previous_roll = 0

for i in range(20):
    roll = random.randint(1,6)
    print(f"{i+1}: {roll}")

    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            count_two_6 += 1
        
    if roll == 1:
        count_1 += 1

    previous_roll = roll

print(f"Total 6s rolled: {count_6}")
print(f"Total 1s rolled: {count_1}")
print(f"Two 6s rolled in row: {count_two_6}")
