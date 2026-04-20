#HW4 Lists
#3.1
favorite_foods = ["Steak", "Eggs", "Hash Browns", "Toast", "Strawberry Milkshake"]
print(favorite_foods[1])
print(favorite_foods[-1])
favorite_foods.append("Mushrooms")
favorite_foods.insert(0, "apple")
favorite_foods.remove("Eggs")
print(len(favorite_foods))
for food in favorite_foods:
    upper = food.upper()
    print(upper)
first_last = [favorite_foods[0], favorite_foods[-1]]
if favorite_foods.index("potato") != -1:
    print("A potato!")
else:
    print("No potato!")

#3.2
