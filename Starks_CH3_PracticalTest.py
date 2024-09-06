candy = ["brady's favorite candy is reeses", "chris's favorite candy is chocalate switzerland", "jack's favorite candy is twizzlers", "yaseen's favorite candy is snickers", "mig's favorite candy is reeses", "nicoles favorite candy is hersheys", "michael's favorite candy is hersheys"]
print(candy)

print(candy[0])
print(candy[1])
print(candy[2])
print(candy[3])
print(candy[4])
print(candy[5])
print(candy[6])


candy.sort()
print(f"\n{candy}")

print(f"\n{candy[0]}")
print(f"\n{candy[1]}")
print(f"\n{candy[2]}")
print(f"\n{candy[3]}")
print(f"\n{candy[4]}")
print(f"\n{candy[5]}")
print(f"\n{candy[6]}")

candy.append("mr.mckinstry's favorite candy is almond joy")
print(f"\n{candy}")

candy.reverse()
print(f"\n{candy}")

print(f"\n{len(candy)}")