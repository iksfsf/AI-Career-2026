name = "   tabish ali   "
city = "lahore"
goal = "I am learning Python for AI"


name=name.strip()
name=name.upper()
city=city.title()

goal=goal.replace("Python","AI")

goal=goal.split()


print(name)
print(city)
print(goal)
print(len(goal))

print(name[0])
print(name[-1])
print(name[::-1])

print("AI" in goal)