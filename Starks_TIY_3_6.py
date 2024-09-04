invites = ["bob", "rob", "phil", "bill"]
message = "You've been invited to my dinner,"

print(f"{message} {invites[0].title()}")
print(f"{message} {invites[1].title()}")
print(f"{message} {invites[2].title()}")
print(f"{message} {invites[3].title()}")

print(f"{invites[0].title()} couldn't make it")

invites[0] = "joe"

print(f"{message} {invites[0].title()}")
print(f"{message} {invites[1].title()}")
print(f"{message} {invites[2].title()}")
print(f"{message} {invites[3].title()}")

print("I have access to larger table, more people will be invited.")

invites.insert(0, "hank")
invites.insert(3,"frank")
invites.append("ross")

print(f"{message} {invites[0].title()}")
print(f"{message} {invites[1].title()}")
print(f"{message} {invites[2].title()}")
print(f"{message} {invites[3].title()}")
print(f"{message} {invites[4].title()}")
print(f"{message} {invites[5].title()}")
print(f"{message} {invites[6].title()}")


