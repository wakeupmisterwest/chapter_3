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

print("Bad news guys, I won't have access to the larger table in time for diner. I'll only have enough room for the two guests.")

uninvited = invites.pop()
print(f"I'm sorry {uninvited.title()}, but I can't invite you anymore.")
uninvited = invites.pop()
print(f"I'm sorry {uninvited.title()}, but I can't invite you anymore.")
uninvited = invites.pop()
print(f"I'm sorry {uninvited.title()}, but I can't invite you anymore.")
uninvited = invites.pop()
print(f"I'm sorry {uninvited.title()}, but I can't invite you anymore.")
uninvited = invites.pop()
print(f"I'm sorry {uninvited.title()}, but I can't invite you anymore.")

print(f"You're still invited {invites[0].title()}")
print(f"You're still invited {invites[1].title()}")
print(invites)

