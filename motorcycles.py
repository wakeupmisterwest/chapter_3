motorcycles = ['honda', 'yahma', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yahma')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yahama', 'suzuki']

motorcycles.insert(0,'ducatio')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

first_owned = motorcycles.pop(0)
print(f"The first motorcycleI owned was a {first_owned.title()}")

motorcycles = ['honda', 'yahma', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yahma', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me." )