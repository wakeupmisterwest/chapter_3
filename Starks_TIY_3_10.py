drinks = ["soda", "water", "juice", "milk"]
animals = ["wolf", "rabbit", "dog", "deer", "tiger", "bear", "sheep"]
food = ["burger", "hot dogs", "fries", "chicken"]
print(f"\nLabrador retrievers are loyal {animals[2]}s.")

animals[2] = "cat"
print(f"\n{animals}")

animals.append("dog")
print(f"\n{animals}")

animals.insert(0, "gazelle")
print(f"\n{animals}")

del animals[6]
print(f"\n{animals}")

popped_animal = animals.pop(6)
print(popped_animal)
print(f"\nThe {popped_animal} has soft wool.")

animals.remove('cat')
print(f"\n{animals}")
african_animal = "gazelle"
animals.remove(african_animal)
print(f"\n{animals}")
print(f"\n{african_animal.title()}'s can be found in Africa.")

print(f"\n{drinks}")

drinks.sort()
print(f"\n{drinks}")

drinks.sort(reverse=True)
print(f"\n{drinks}")

print(f"\n{sorted(drinks)}")

print(f"\n{drinks}")

food.reverse()
print(f"\n{food}")

print(f"\n{len(food)}")
