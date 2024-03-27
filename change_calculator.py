change = float(input("Enter the amount of change: "))
print(f"For {
      change} złoty, the change given as the smallest number of coins and notes is:")


change *= 100  # change amount in groszy

grozy_1 = 0
grozy_2 = 0
grozy_5 = 0
grozy_10 = 0
grozy_20 = 0
grozy_50 = 0
zloty_1 = 0
zloty_2 = 0
zloty_5 = 0

while change > 0:
    if change >= 500:
        zloty_5 += 1
        change -= 500
    elif change >= 200:
        zloty_2 += 1
        change -= 200
    elif change >= 100:
        zloty_1 += 1
        change -= 100
    elif change >= 50:
        grozy_50 += 1
        change -= 50
    elif change >= 20:
        grozy_20 += 1
        change -= 20
    elif change >= 10:
        grozy_10 += 1
        change -= 10
    elif change >= 5:
        grozy_5 += 1
        change -= 5
    elif change >= 2:
        grozy_2 += 1
        change -= 2
    else:  # This will only be for 1 grosz left
        grozy_1 += 1
        change -= 1

# Print out the results
print("5 złoty notes:", zloty_5)
print("2 złoty notes:", zloty_2)
print("1 złoty notes:", zloty_1)
print("grozy_50 notes:", grozy_50)
print("grozy_20 notes:", grozy_20)
print("grozy_10 notes:", grozy_10)
print("grozy_5 notes:", grozy_5)
print("grozy_2 notes:", grozy_2)
print("grozy_1 notes:", grozy_1)
